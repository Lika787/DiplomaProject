# Generated by Django 3.1.2 on 2020-11-11 12:25

import uuid
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('cityVillage', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('houseDetails', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogMeasurement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nameMeasurement', models.CharField(max_length=100)),
                ('unitMeasurement', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ElectroUltrasoundTherapy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nameEus', models.CharField(max_length=60)),
                ('valueEus', models.FloatField()),
                ('unitEus', models.CharField(max_length=20)),
                ('dateEus', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LabMedicalStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalStaff',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('patronymic', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('doctor', 'doctor'), ('nurse', 'nurse'), ('laboratory assistant', 'laboratory assistant'), ('medical assistant', 'medical assistant')], max_length=22)),
                ('specialization', models.CharField(max_length=100)),
                ('startWork', models.DateField()),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NationCl025',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codeIll', models.CharField(max_length=30)),
                ('nameIll', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='NationCl026',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codeIntervention', models.CharField(max_length=30)),
                ('nameIntervention', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='NationCl027',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codeTest', models.CharField(max_length=30)),
                ('nameTest', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='NationClPill',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codePill', models.CharField(max_length=30)),
                ('namePill', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('patronymic', models.CharField(max_length=100)),
                ('dateBirth', models.DateField(help_text='DD.MM.YYYY')),
                ('gender', models.CharField(choices=[('man', 'man'), ('woman', 'woman')], max_length=7)),
                ('bloodType', models.CharField(choices=[('O(I) Rh-', 'O(I) Rh-'), ('O(I) Rh+', 'O(I) Rh+'), ('A(II) Rh+', 'A(II) Rh+'), ('A(II) Rh-', 'A(II) Rh-'), ('B(III) Rh+', 'B(III) Rh+'), ('AB(IV) Rh+', 'AB(IV) Rh+'), ('AB(IV) Rh-', 'AB(IV) Rh-')], max_length=12)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('socialStatus', models.CharField(max_length=80)),
                ('maritalStatus', models.CharField(max_length=50)),
                ('idAddress', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.address')),
            ],
        ),
        migrations.CreateModel(
            name='Physiotherapy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('namePhysiotherapy', models.CharField(max_length=60)),
                ('valuePhysiotherapy', models.FloatField()),
                ('unitPhysiotherapy', models.CharField(max_length=20)),
                ('datePhysiotherapy', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='StageOfTreatment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('stageName', models.CharField(max_length=100)),
                ('startStage', models.DateTimeField()),
                ('endStage', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('DateIntervention', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentSession',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('startSession', models.DateTimeField()),
                ('endSession', models.DateTimeField(blank=True)),
                ('IdMainIll', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.nationcl025')),
                ('idDoctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.medicalstaff')),
                ('idPatient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_ill_history.patient')),
            ],
        ),
        migrations.CreateModel(
            name='SurgeryMedicalStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicalStaff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.medicalstaff')),
                ('surgery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.surgery')),
            ],
        ),
        migrations.AddField(
            model_name='surgery',
            name='idMedStaff',
            field=models.ManyToManyField(through='patient_ill_history.SurgeryMedicalStaff', to='patient_ill_history.MedicalStaff'),
        ),
        migrations.AddField(
            model_name='surgery',
            name='idNameIntervention',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.nationcl026'),
        ),
        migrations.AddField(
            model_name='surgery',
            name='idStage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_ill_history.stageoftreatment'),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('idStage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_ill_history.stageoftreatment')),
            ],
        ),
        migrations.AddField(
            model_name='stageoftreatment',
            name='idSession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_ill_history.treatmentsession'),
        ),
        migrations.CreateModel(
            name='PhysiotherapyMedicalStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicalStaff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.medicalstaff')),
                ('physiotherapy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.physiotherapy')),
            ],
        ),
        migrations.AddField(
            model_name='physiotherapy',
            name='idMedStaff',
            field=models.ManyToManyField(through='patient_ill_history.PhysiotherapyMedicalStaff', to='patient_ill_history.MedicalStaff'),
        ),
        migrations.AddField(
            model_name='physiotherapy',
            name='idStage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_ill_history.stageoftreatment'),
        ),
        migrations.CreateModel(
            name='Pharmacotherapy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dosePill', models.FloatField()),
                ('unitPill', models.CharField(max_length=20)),
                ('datePill', models.DateTimeField()),
                ('idMedStaff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.medicalstaff')),
                ('idNamePill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.nationclpill')),
                ('idStage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_ill_history.stageoftreatment')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('valueMeasurement', models.FloatField()),
                ('unitMeasurement', models.CharField(max_length=20)),
                ('dateMeasurement', models.DateTimeField()),
                ('idCatalogMeasurement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.catalogmeasurement')),
                ('idMedStaff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.medicalstaff')),
                ('idState', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_ill_history.state')),
            ],
        ),
        migrations.CreateModel(
            name='LaboratoryTest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nameTest', models.CharField(max_length=60)),
                ('valueTest', models.FloatField()),
                ('unitTest', models.CharField(max_length=20)),
                ('dateTest', models.DateTimeField()),
                ('laboratoryName', models.CharField(max_length=150)),
                ('idMedStaff', models.ManyToManyField(through='patient_ill_history.LabMedicalStaff', to='patient_ill_history.MedicalStaff')),
                ('idState', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_ill_history.state')),
            ],
        ),
        migrations.AddField(
            model_name='labmedicalstaff',
            name='laboratoryTest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.laboratorytest'),
        ),
        migrations.AddField(
            model_name='labmedicalstaff',
            name='medicalStaff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.medicalstaff'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nameImage', models.CharField(max_length=80)),
                ('hostImage', models.FilePathField()),
                ('dateImage', models.DateTimeField()),
                ('idState', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_ill_history.state')),
            ],
        ),
        migrations.CreateModel(
            name='EusMedicalStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.electroultrasoundtherapy')),
                ('medicalStaff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.medicalstaff')),
            ],
        ),
        migrations.AddField(
            model_name='electroultrasoundtherapy',
            name='idMedStaff',
            field=models.ManyToManyField(through='patient_ill_history.EusMedicalStaff', to='patient_ill_history.MedicalStaff'),
        ),
        migrations.AddField(
            model_name='electroultrasoundtherapy',
            name='idStage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_ill_history.stageoftreatment'),
        ),
        migrations.CreateModel(
            name='Comorbidity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('IdNameIll', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_ill_history.nationcl025')),
                ('idSession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_ill_history.treatmentsession')),
            ],
        ),
    ]
