from functools import wraps

from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
import pandas as pd

from .model import OptimizationModel


class OptimizationViewset(viewsets.GenericViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = OptimizationModel()

    @action(detail=False, methods=['get'])
    def optimization(self, request, *args, **kwargs):
        try:
            params = {key: float(val[0]) for key, val in dict(request.query_params).items()}
            k_best = params.pop('k_best', 5)
            input_df = pd.DataFrame(pd.Series(params)).transpose()
            result = self.model.optimize(input_df, k_best)[0]
            return JsonResponse({'strategies': result})
        except Exception as e:
            return JsonResponse({
                'error_type': e.__class__.__name__,
                'error_message': str(e),
            })

    @action(detail=False, methods=['get'])
    def prediction(self, request, *args, **kwargs):
        try:
            params = {key: float(val[0]) for key, val in dict(request.query_params).items()}
            input_df = pd.DataFrame(pd.Series(params)).transpose()
            result = self.model.predict(input_df).to_dict(orient='records')[0]
            return JsonResponse(result)
        except Exception as e:
            return JsonResponse({
                'error_type': e.__class__.__name__,
                'error_message': str(e),
            })