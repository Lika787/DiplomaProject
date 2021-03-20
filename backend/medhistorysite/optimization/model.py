import itertools
import os

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor as Regression


class OptimizationModel:
    input_features = ['X1', 'X2', 'X3',
                      'X4', 'X5', 'X6']
    healing_features = ['U1', 'U2']
    features = input_features + healing_features

    output_labels = ['X7', 'X8', 'X9']
    optimization_label = 'X10'
    labels = output_labels + [optimization_label]

    constraints = {
        'U1': (0, 20), 'U2': (14, 32),

        'X7': (42, 80), 'X8': (3, 14),
        'X9': (0.4, 1.4), 'X10': (56, 78)
    }

    def __init__(self):
        df = self.read_database_file()
        features_df = df[self.features]
        self.models = dict()
        for label in self.labels:
            X, y = features_df, df[label].values
            self.models[label] = Regression().fit(X, y)

    def predict(self, input_df):
        input_df = input_df.copy()
        if missed_columns := set(self.features) - set(input_df.columns):
            raise ValueError(f'Missed input columns: {", ".join(sorted(missed_columns))}')

        X = input_df[self.features]
        for label in self.labels:
            model = self.models[label]
            input_df[label] = model.predict(X)

        return input_df

    def optimize(self, input_df, k_best=5):
        input_df = input_df.copy()
        if missed_columns := set(self.input_features) - set(input_df.columns):
            raise ValueError(f'Missed input columns: {", ".join(sorted(missed_columns))}')

        return input_df.apply(lambda x: self.optimize_row(x, k_best), axis=1).values

    def optimize_row(self, row, k_best):
        results = dict()
        for field in self.healing_field():
            row_dict = dict(row)
            row_dict.update(dict(zip(self.healing_features, field)))
            row_df = pd.DataFrame(pd.Series(row_dict)).transpose()
            row_df = self.predict(row_df)
            if self.constraints_score(row_df):
                score = self.optimization_score(
                    row_df[self.optimization_label].values[0])
                results[score] = row_df

        scores = sorted(results.keys())[:k_best]
        return [{'score': s, 'parameters': results[s].to_dict(orient='records')[0]}
                for s in scores]

    @staticmethod
    def read_database_file():
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.xlsx')
        df = pd.read_excel(file_path)
        df.columns = [column.split()[0] for column in df.columns]
        return df[df['X9'] < df['X9'].quantile(0.95)]

    @classmethod
    def optimization_score(cls, value):
        min_val, max_val = cls.constraints[cls.optimization_label]
        return np.abs(value - np.mean([min_val, max_val]))

    @classmethod
    def healing_field(cls):
        step = 3
        prod = itertools.product(*[np.arange(*cls.constraints[feature], step)
                                   for feature in cls.healing_features])
        return list(map(tuple, prod))

    @classmethod
    def constraints_score(cls, row_df):
        for label, (min_val, max_val) in cls.constraints.items():
            if not (min_val <= row_df[label].values[0] <= max_val):
                return False
        return True
