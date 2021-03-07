from datetime import date
from uuid import UUID

import pandas
from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer


from .models import MedicalStaff, Address, Patient, NationCl025, TreatmentSession, Comorbidity, StageOfTreatment, \
    NationCl026, Surgery, SurgeryMedicalStaff, NationClPill, Pharmacotherapy, Physiotherapy, \
    PhysiotherapyMedicalStaff, ElectroUltrasoundTherapy, EusMedicalStaff, State, NationCl027, LaboratoryTest, \
    LabMedicalStaff, CatalogMeasurement, Measurement, Image
from .serializers import PatientSerializer, TreatmentSessionSerializer, StageOfTreatmentSerializer, \
    PharmacotherapySerializer, StateSerializer, LaboratoryTestSerializer, ImageSerializer, MeasurementSerializer, \
    CatalogMeasurementSerializer, LabMedicalStaffSerializer, NationCl027Serializer, \
    EusMedicalStaffSerializer, ElectroUltrasoundTherapySerializer, PhysiotherapyMedicalStaffSerializer, \
    PhysiotherapySerializer, NationClPillSerializer, SurgeryMedicalStaffSerializer, SurgerySerializer,\
    NationCl026Serializer, ComorbiditySerializer, NationCl025Serializer, AddressSerializer, MedicalStaffSerializer,\
    PatientAllSerializer, MedicalStaffAtTreatmentSession, TestSerializer

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()


class CatalogMeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = CatalogMeasurementSerializer
    queryset = CatalogMeasurement.objects.all()


class LabMedicalStaffViewSet(viewsets.ModelViewSet):
    serializer_class = LabMedicalStaffSerializer
    queryset = LabMedicalStaff.objects.all()


class LaboratoryTestViewSet(viewsets.ModelViewSet):
    serializer_class = LaboratoryTestSerializer
    queryset = LaboratoryTest.objects.all()


class NationCl027ViewSet(viewsets.ModelViewSet):
    serializer_class = NationCl027Serializer
    queryset = NationCl027.objects.all()


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()


class EusMedicalStaffViewSet(viewsets.ModelViewSet):
    serializer_class = EusMedicalStaffSerializer
    queryset = EusMedicalStaff.objects.all()


class ElectroUltrasoundTherapyViewSet(viewsets.ModelViewSet):
    serializer_class = ElectroUltrasoundTherapySerializer
    queryset = ElectroUltrasoundTherapy.objects.all()


class PhysiotherapyMedicalStaffViewSet(viewsets.ModelViewSet):
    serializer_class = PhysiotherapyMedicalStaffSerializer
    queryset = PhysiotherapyMedicalStaff.objects.all()


class PhysiotherapyViewSet(viewsets.ModelViewSet):
    serializer_class = PhysiotherapySerializer
    queryset = Physiotherapy.objects.all()


class PharmacotherapyViewSet(viewsets.ModelViewSet):
    serializer_class = PharmacotherapySerializer
    queryset = Pharmacotherapy.objects.all()


class NationClPillViewSet(viewsets.ModelViewSet):
    serializer_class = NationClPillSerializer
    queryset = NationClPill.objects.all()


class SurgeryMedicalStaffViewSet(viewsets.ModelViewSet):
    serializer_class = SurgeryMedicalStaffSerializer
    queryset = SurgeryMedicalStaff.objects.all()


class SurgeryViewSet(viewsets.ModelViewSet):
    serializer_class = SurgerySerializer
    queryset = Surgery.objects.all()


class NationCl026ViewSet(viewsets.ModelViewSet):
    serializer_class = NationCl026Serializer
    queryset = NationCl026.objects.all()


class StageOfTreatmentViewSet(viewsets.ModelViewSet):
    serializer_class = StageOfTreatmentSerializer
    queryset = StageOfTreatment.objects.all()


class ComorbidityViewSet(viewsets.ModelViewSet):
    serializer_class = ComorbiditySerializer
    queryset = Comorbidity.objects.all()


class TreatmentSessionViewSet(viewsets.ModelViewSet):
    serializer_class = TreatmentSessionSerializer
    queryset = TreatmentSession.objects.all()


class NationCl025ViewSet(viewsets.ModelViewSet):
    serializer_class = NationCl025Serializer
    queryset = NationCl025.objects.all()


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class MedicalStaffViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalStaffSerializer
    queryset = MedicalStaff.objects.all()


class PatientListView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.order_by('-surname')


class PatientDateBirth(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.filter(dateBirth__lte='1998-01-01')


class PatientAll(viewsets.ModelViewSet):
    serializer_class = PatientAllSerializer
    queryset = Patient.objects.filter(id=1)


class MedicalStaffAtTreatmentSession(viewsets.ModelViewSet):
    serializer_class = MedicalStaffAtTreatmentSession
    queryset = MedicalStaff.objects.all()


class MyExampleViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Patient.objects.filter(id=1)
    serializer_class = PatientAllSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'my_export.xlsx'

from pandas.io.json import json_normalize
from django.http import HttpResponse
from json import dumps
from rest_framework.views import APIView


class Test(APIView):
    def get(self, request):
        queryset = Measurement.objects.select_related().all()
        normalized = json_normalize([p.__dict__ for p in queryset])
        result = normalized.to_dict(orient='record')
        for res in result:
            for k, v in res.items():
                if isinstance(v, UUID) or isinstance(v, date):
                    res[k] = str(v)
            res['_state'] = None
        return HttpResponse(dumps(result))


class MyTestViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Patient.objects.filter(id=1)
    #json_normalize(queryset)
    serializer_class = TestSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'my_export_test.xlsx'


