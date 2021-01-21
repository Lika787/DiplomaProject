from django.contrib import admin

# Register your models here.

from .models import MedicalStaff, Address, Patient, NationCl025, TreatmentSession, Comorbidity, StageOfTreatment, \
    NationCl026, Surgery, SurgeryMedicalStaff, NationClPill, Pharmacotherapy, Physiotherapy, \
    PhysiotherapyMedicalStaff, ElectroUltrasoundTherapy, EusMedicalStaff, State, NationCl027, LaboratoryTest, \
    LabMedicalStaff, CatalogMeasurement, Measurement, Image


admin.site.register(MedicalStaff)
admin.site.register(Address)
admin.site.register(Patient)
admin.site.register(NationCl025)
admin.site.register(TreatmentSession)
admin.site.register(Comorbidity)
admin.site.register(StageOfTreatment)
admin.site.register(NationCl026)
admin.site.register(Surgery)
admin.site.register(SurgeryMedicalStaff)
admin.site.register(NationClPill)
admin.site.register(Pharmacotherapy)
admin.site.register(Physiotherapy)
admin.site.register(PhysiotherapyMedicalStaff)
admin.site.register(ElectroUltrasoundTherapy)
admin.site.register(EusMedicalStaff)
admin.site.register(State)
admin.site.register(NationCl027)
admin.site.register(LaboratoryTest)
admin.site.register(LabMedicalStaff)
admin.site.register(CatalogMeasurement)
admin.site.register(Measurement)
admin.site.register(Image)
