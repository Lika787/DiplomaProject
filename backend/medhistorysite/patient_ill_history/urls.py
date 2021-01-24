from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MedicalStaffViewSet, PatientDateBirth, PatientListView, ImageViewSet, MeasurementViewSet,\
    CatalogMeasurementViewSet, LabMedicalStaffViewSet, LaboratoryTestViewSet, NationCl027ViewSet, StateViewSet,\
    EusMedicalStaffViewSet, ElectroUltrasoundTherapyViewSet, PhysiotherapyMedicalStaffViewSet, PhysiotherapyViewSet, \
    PharmacotherapyViewSet, NationClPillViewSet, SurgeryMedicalStaffViewSet, SurgeryViewSet, NationCl026ViewSet,\
    StageOfTreatmentViewSet, ComorbidityViewSet, TreatmentSessionViewSet, NationCl025ViewSet, PatientViewSet, \
    AddressViewSet, PatientAll, Doctor

router = DefaultRouter()

router.register(r'MedicalStaff', MedicalStaffViewSet, basename='user')
router.register(r'Address', AddressViewSet, basename='user')
router.register(r'Patient', PatientViewSet, basename='user')
router.register(r'NationCl025', NationCl025ViewSet, basename='user')
router.register(r'TreatmentSession', TreatmentSessionViewSet, basename='user')
router.register(r'Comorbidity', ComorbidityViewSet, basename='user')
router.register(r'StageOfTreatment', StageOfTreatmentViewSet, basename='user')
router.register(r'NationCl026', NationCl026ViewSet, basename='user')
router.register(r'Surgery', SurgeryViewSet, basename='user')
router.register(r'SurgeryMedicalStaff', SurgeryMedicalStaffViewSet, basename='user')
router.register(r'NationClPill', NationClPillViewSet, basename='user')
router.register(r'Pharmacotherapy', PharmacotherapyViewSet, basename='user')
router.register(r'Physiotherapy', PhysiotherapyViewSet, basename='user')
router.register(r'PhysiotherapyMedicalStaff', PhysiotherapyMedicalStaffViewSet, basename='user')
router.register(r'ElectroUltrasoundTherapy', ElectroUltrasoundTherapyViewSet, basename='user')
router.register(r'EusMedicalStaff', EusMedicalStaffViewSet, basename='user')
router.register(r'State', StateViewSet, basename='user')
router.register(r'NationCl027', NationCl027ViewSet, basename='user')
router.register(r'LaboratoryTest', LaboratoryTestViewSet, basename='user')
router.register(r'LabMedicalStaff', LabMedicalStaffViewSet, basename='user')
router.register(r'CatalogMeasurement', CatalogMeasurementViewSet, basename='user')
router.register(r'Measurement', MeasurementViewSet, basename='user')
router.register(r'Image', ImageViewSet, basename='user')

router.register(r'PatientDateBirth', PatientDateBirth, basename='user')
router.register(r'PatientListView', PatientListView, basename='user')
router.register(r'PatientAll', PatientAll, basename='user')
router.register(r'Doctor', Doctor, basename='user')

urlpatterns = router.urls