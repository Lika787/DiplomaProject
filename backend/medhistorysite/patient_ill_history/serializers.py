from rest_framework import serializers
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


class ImageDetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['nameImage', 'hostImage', 'dateImage']


class MeasurementDetSerializer(serializers.ModelSerializer):
    nameMeasurement = serializers.CharField(source='idCatalogMeasurement.nameMeasurement')
    unitMeasurement = serializers.CharField(source='idCatalogMeasurement.unitMeasurement')
    medStaff = serializers.CharField(source='idMedStaff.surname')

    class Meta:
        model = Measurement
        fields = ['nameMeasurement','valueMeasurement', 'unitMeasurement', 'dateMeasurement', 'medStaff']


class LabMedicalStaffDetSerializer(serializers.ModelSerializer):
    medStaff = serializers.CharField(source='medicalStaff.surname')

    class Meta:
        model = LabMedicalStaff
        fields = ['medStaff']


class LaboratoryTestDetSerializer(serializers.ModelSerializer):
    nameTest = serializers.CharField(source='nameTest.nameTest')
    lab_staff = LabMedicalStaffDetSerializer(many=True, read_only=True)

    class Meta:
        model = LaboratoryTest
        fields = ['nameTest', 'valueTest', 'unitTest', 'dateTest', 'laboratoryName', 'lab_staff']


class StateDetSerializer(serializers.ModelSerializer):
    state_on = serializers.CharField(source='idStage.stageName')
    laboratory_test = LaboratoryTestDetSerializer(many=True, read_only=True)
    measurement = MeasurementDetSerializer(many=True, read_only=True)
    image = ImageDetSerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['state_on', 'laboratory_test', 'measurement', 'image']


class EusMedicalStaffDetSerializer(serializers.ModelSerializer):
    medStaff = serializers.CharField(source='medicalStaff.surname')

    class Meta:
        model = EusMedicalStaff
        fields = ['medStaff']


class ElectroUltrasoundTherapyDetSerializer(serializers.ModelSerializer):
    eus_med_staff = EusMedicalStaffDetSerializer(many=True, read_only=True)

    class Meta:
        model = ElectroUltrasoundTherapy
        fields = ['nameEus', 'valueEus', 'unitEus', 'dateEus', 'eus_med_staff']


class PhysiotherapyMedicalStaffDetSerializer(serializers.ModelSerializer):
    medStaff = serializers.CharField(source='medicalStaff.surname')

    class Meta:
        model = PhysiotherapyMedicalStaff
        fields = ['medStaff']


class PhysiotherapyDetSerializer(serializers.ModelSerializer):
    physiotherapy_med_staff = PhysiotherapyMedicalStaffDetSerializer(many=True, read_only=True)

    class Meta:
        model = Physiotherapy
        fields = ['namePhysiotherapy', 'valuePhysiotherapy', 'unitPhysiotherapy', 'datePhysiotherapy',\
                  'physiotherapy_med_staff']


class PharmacotherapyDetSerializer(serializers.ModelSerializer):
    namePill = serializers.CharField(source='idNamePill.namePill')
    #medStaff = serializers.CharField(source='idMedStaff.surname')

    class Meta:
        model = Pharmacotherapy
        fields = ['namePill', 'dosePill', 'unitPill', 'datePill'] #'medStaff']


class SurgeryMedicalStaffDetSerializer(serializers.ModelSerializer):
    medStaff = serializers.CharField(source='medicalStaff.surname')

    class Meta:
        model = SurgeryMedicalStaff
        fields = ['medStaff']


class SurgeryDetSerializer(serializers.ModelSerializer):
    sur_med_staff = SurgeryMedicalStaffDetSerializer(many=True, read_only=True)
    nameInterven = serializers.CharField(source='idNameIntervention.nameIntervention')

    class Meta:
        model = Surgery
        fields = ['DateIntervention', 'nameInterven', 'sur_med_staff']


class StageOfTreatmentDetSerializer(serializers.ModelSerializer):
    surgery = SurgeryDetSerializer(many=True, read_only=True)
    pharmacotherapy = PharmacotherapyDetSerializer(many=True, read_only=True)
    physiotherapy = PhysiotherapyDetSerializer(many=True, read_only=True)
    electro_ultrasound_therapy = ElectroUltrasoundTherapyDetSerializer(many=True, read_only=True)
    state = StateDetSerializer(many=True, read_only=True)

    class Meta:
        model = StageOfTreatment
        fields = ['stageName', 'startStage', 'surgery', 'pharmacotherapy', 'physiotherapy', 'electro_ultrasound_therapy',\
                  'state', 'endStage']


class ComorbidityDetSerializer(serializers.ModelSerializer):
    nameIll = serializers.CharField(source='idNameIll.nameIll')

    class Meta:
        model = Comorbidity
        fields = ['nameIll']


class TreatmentDetSerializer(serializers.ModelSerializer):
    comorbidity = ComorbidityDetSerializer(many=True, read_only=True)
    stage_of_treatment = StageOfTreatmentDetSerializer(many=True, read_only=True)
    doctor = serializers.CharField(source='idDoctor.surname')
    mainIll = serializers.CharField(source='idMainIll.nameIll')
    class Meta:
        model = TreatmentSession
        fields = ['startSession', 'mainIll', 'doctor', 'comorbidity', 'stage_of_treatment', 'endSession']


class MedicalStaffAtTreatmentSession(serializers.ModelSerializer):
    treatment_session = TreatmentDetSerializer(many=True, read_only=True)
    class Meta:
        model = MedicalStaff
        fields = ['name', 'surname', 'specialization', 'treatment_session']


class PatientAllSerializer(serializers.ModelSerializer):
    treatment_session = TreatmentDetSerializer(many=True, read_only=True)
    class Meta:
        model = Patient
        fields = ['name', 'surname', 'treatment_session']


class TreatmentSessionTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentSession
        fields = ['startSession', 'endSession']


class TestSerializer(serializers.ModelSerializer):
    treatment_session = TreatmentSessionTestSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ['name', 'surname', 'treatment_session']

