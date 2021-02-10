from django.db import models
import uuid
from django.contrib.auth.models import User


#class MyManager(models.Manager):
 #   def custom_filter(self, **kwargs):
  #      return super().get_queryset.filter(**kwargs)


class MedicalStaff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=100)
    doctor = 'doctor'
    nurse = 'nurse'
    labAssist = 'laboratory assistant'
    medAssist = 'medical assistant'
    positionChoices = ((doctor, 'doctor'), (nurse, 'nurse'),
                       (labAssist, 'laboratory assistant'), (medAssist, 'medical assistant'))
    position = models.CharField(max_length=22, choices=positionChoices)
    specialization = models.CharField(max_length=100)
    startWork = models.DateField()
    phone = models.CharField(max_length=30)

    class Meta:
        unique_together = ['name', 'surname', 'specialization']

    def __str__(self):
        return self.surname



class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    cityVillage = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    houseDetails = models.CharField(max_length=40)


class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=100)
    dateBirth = models.DateField(help_text="YYYY-MM-DD")
    m = 'man'
    w = 'woman'
    genderChoices = ((m, 'man'), (w, 'woman'))
    gender = models.CharField(max_length=7, choices=genderChoices)
    Ip = 'O(I) Rh-'
    Im = 'O(I) Rh+'
    IIp = 'A(II) Rh+'
    IIm = 'A(II) Rh-'
    IIIp = 'B(III) Rh+'
    IIIm = 'B(III) Rh-'
    IVp = 'AB(IV) Rh+'
    IVm = 'AB(IV) Rh-'
    bloodChoices = ((Ip, 'O(I) Rh-'), (Im, 'O(I) Rh+'), (IIp, 'A(II) Rh+'), (IIm, 'A(II) Rh-'),
                    (IIIp, 'B(III) Rh+'), (IVp, 'AB(IV) Rh+'), (IVm, 'AB(IV) Rh-'))
    bloodType = models.CharField(max_length=12, choices=bloodChoices)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    idAddress = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    socialStatus = models.CharField(max_length=80)
    maritalStatus = models.CharField(max_length=50)

   # objects = models.Manager()


class NationCl025(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codeIll = models.CharField(max_length=30)
    nameIll = models.CharField(max_length=70)

    def __str__(self):
        return self.nameIll


class TreatmentSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idPatient = models.ForeignKey(Patient, related_name='treatment_session', on_delete=models.CASCADE)
    idMainIll = models.ForeignKey(NationCl025, null=True, on_delete=models.SET_NULL)
    startSession = models.DateTimeField()
    endSession = models.DateTimeField(blank=True)
    idDoctor = models.ForeignKey(MedicalStaff, related_name='treatment_session', null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ['startSession', 'endSession']


class Comorbidity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idSession = models.ForeignKey(TreatmentSession, related_name='comorbidity', on_delete=models.CASCADE, null=True)
    idNameIll = models.ForeignKey(NationCl025, null=True, on_delete=models.SET_NULL)


class StageOfTreatment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idSession = models.ForeignKey(TreatmentSession, related_name='stage_of_treatment', on_delete=models.CASCADE)
    stageName = models.CharField(max_length=100)
    startStage = models.DateTimeField()
    endStage = models.DateTimeField(blank=True)

    class Meta:
        unique_together = ['stageName', 'startStage', 'endStage']

class NationCl026(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codeIntervention = models.CharField(max_length=30)
    nameIntervention = models.CharField(max_length=70)

    def __str__(self):
        return self.nameIntervention


class Surgery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idStage = models.ForeignKey(StageOfTreatment, related_name='surgery', on_delete=models.CASCADE)
    idNameIntervention = models.ForeignKey(NationCl026, null=True, on_delete=models.SET_NULL)
    DateIntervention = models.DateTimeField()
    idMedStaff = models.ManyToManyField(MedicalStaff, through='SurgeryMedicalStaff',
                                        through_fields=('surgery', 'medicalStaff'))

    class Meta:
        unique_together = ['DateIntervention']


class SurgeryMedicalStaff (models.Model):
    surgery = models.ForeignKey(Surgery, related_name='sur_med_staff', null=True, on_delete=models.SET_NULL)
    medicalStaff = models.ForeignKey(MedicalStaff, null=True, on_delete=models.SET_NULL)


class NationClPill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codePill = models.CharField(max_length=100)
    namePill = models.CharField(max_length=100)

    def __str__(self):
        return self.namePill


class Pharmacotherapy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idStage = models.ForeignKey(StageOfTreatment, related_name='pharmacotherapy', on_delete=models.CASCADE)
    idNamePill = models.ForeignKey(NationClPill, null=True, on_delete=models.SET_NULL)
    dosePill = models.FloatField()
    unitPill = models.CharField(max_length=20)
    datePill = models.DateTimeField()
    #idMedStaff = models.ForeignKey(MedicalStaff, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ['dosePill', 'unitPill', 'datePill']


class Physiotherapy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idStage = models.ForeignKey(StageOfTreatment, related_name='physiotherapy', on_delete=models.CASCADE)
    namePhysiotherapy = models.CharField(max_length=60)
    valuePhysiotherapy = models.FloatField()
    unitPhysiotherapy = models.CharField(max_length=20)
    datePhysiotherapy = models.DateTimeField()
    idMedStaff = models.ManyToManyField(MedicalStaff, through='PhysiotherapyMedicalStaff',
                                        through_fields=('physiotherapy', 'medicalStaff'))

    class Meta:
        unique_together = ['namePhysiotherapy', 'valuePhysiotherapy', 'unitPhysiotherapy', 'datePhysiotherapy']


class PhysiotherapyMedicalStaff (models.Model):
    physiotherapy = models.ForeignKey(Physiotherapy, null=True, related_name='physiotherapy_med_staff', on_delete=models.SET_NULL)
    medicalStaff = models.ForeignKey(MedicalStaff, null=True, on_delete=models.SET_NULL)


class ElectroUltrasoundTherapy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idStage = models.ForeignKey(StageOfTreatment, related_name='electro_ultrasound_therapy', on_delete=models.CASCADE)
    nameEus = models.CharField(max_length=60)
    valueEus = models.FloatField()
    unitEus = models.CharField(max_length=20)
    dateEus = models.DateTimeField()
    idMedStaff = models.ManyToManyField(MedicalStaff, through='EusMedicalStaff',
                                        through_fields=('eus', 'medicalStaff'))

    class Meta:
        unique_together = ['nameEus', 'valueEus', 'unitEus', 'dateEus']


class EusMedicalStaff (models.Model):
    eus = models.ForeignKey(ElectroUltrasoundTherapy, related_name='eus_med_staff', null=True, on_delete=models.SET_NULL)
    medicalStaff = models.ForeignKey(MedicalStaff, null=True, on_delete=models.SET_NULL)


class State(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idStage = models.ForeignKey(StageOfTreatment, related_name='state', on_delete=models.CASCADE)


class NationCl027(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codeTest = models.CharField(max_length=30)
    nameTest = models.CharField(max_length=70)

    def __str__(self):
        return self.nameTest


class LaboratoryTest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idState = models.ForeignKey(State, related_name='laboratory_test', on_delete=models.CASCADE)
    nameTest = models.ForeignKey(NationCl027, null=True, on_delete=models.SET_NULL)
    valueTest = models.FloatField()
    unitTest = models.CharField(max_length=20)
    dateTest = models.DateTimeField()
    laboratoryName = models.CharField(max_length=150)
    idMedStaff = models.ManyToManyField(MedicalStaff, through='LabMedicalStaff',
                                        through_fields=('laboratoryTest', 'medicalStaff'))

    class Meta:
        unique_together = ['valueTest', 'unitTest', 'dateTest', 'laboratoryName']


class LabMedicalStaff (models.Model):
    laboratoryTest = models.ForeignKey(LaboratoryTest, related_name='lab_staff', null=True, on_delete=models.SET_NULL)
    medicalStaff = models.ForeignKey(MedicalStaff, null=True, on_delete=models.SET_NULL)


class CatalogMeasurement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nameMeasurement = models.CharField(max_length=100)
    unitMeasurement = models.CharField(max_length=20)

    def __str__(self):
        return self.nameMeasurement


class Measurement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idState = models.ForeignKey(State, related_name='measurement', on_delete=models.CASCADE)
    idCatalogMeasurement = models.ForeignKey(CatalogMeasurement, null=True, on_delete=models.SET_NULL)
    valueMeasurement = models.FloatField()
    dateMeasurement = models.DateTimeField()
    idMedStaff = models.ForeignKey(MedicalStaff, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ['valueMeasurement', 'dateMeasurement']


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idState = models.ForeignKey(State, null=True, related_name='image', on_delete=models.CASCADE)
    nameImage = models.CharField(max_length=80)
    hostImage = models.FilePathField()
    dateImage = models.DateTimeField()

    class Meta:
        unique_together = ['nameImage', 'hostImage', 'dateImage']
