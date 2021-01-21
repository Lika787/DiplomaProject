from rest_framework import serializers
#from .models import Patient
from .models import MedicalStaff, Address, Patient, NationCl025, TreatmentSession, Comorbidity, StageOfTreatment, \
    NationCl026, Surgery, SurgeryMedicalStaff, NationClPill, Pharmacotherapy, Physiotherapy, \
    PhysiotherapyMedicalStaff, ElectroUltrasoundTherapy, EusMedicalStaff, State, NationCl027, LaboratoryTest, \
    LabMedicalStaff, CatalogMeasurement, Measurement, Image


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'


class CatalogMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogMeasurement
        fields = '__all__'


class LabMedicalStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabMedicalStaff
        fields = '__all__'


class NationCl027Serializer(serializers.ModelSerializer):
    class Meta:
        model = NationCl027
        fields = '__all__'


class EusMedicalStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = EusMedicalStaff
        fields = '__all__'


class ElectroUltrasoundTherapySerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectroUltrasoundTherapy
        fields = '__all__'


class PhysiotherapyMedicalStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysiotherapyMedicalStaff
        fields = '__all__'


class PhysiotherapySerializer(serializers.ModelSerializer):
    class Meta:
        model = Physiotherapy
        fields = '__all__'


class NationClPillSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationClPill
        fields = '__all__'


class SurgeryMedicalStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurgeryMedicalStaff
        fields = '__all__'


class SurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Surgery
        fields = '__all__'


class NationCl026Serializer(serializers.ModelSerializer):
    class Meta:
        model = NationCl026
        fields = '__all__'


class ComorbiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comorbidity
        fields = '__all__'


class NationCl025Serializer(serializers.ModelSerializer):
    class Meta:
        model = NationCl025
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class MedicalStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalStaff
        fields = '__all__'


class TreatmentSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentSession
        fields = '__all__'


class StageOfTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageOfTreatment
        fields = '__all__'


class PharmacotherapySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacotherapy
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class LaboratoryTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoryTest
        fields = '__all__'