# Generated by Django 2.2.4 on 2020-02-20 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Energy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=3, default=0, max_digits=21, null=True)),
                ('primary', models.BooleanField(default='True')),
                ('final', models.BooleanField(default='False')),
                ('energy_density', models.DecimalField(decimal_places=10, default=0, max_digits=21, null=True)),
                ('specific_energy', models.DecimalField(decimal_places=15, default=0, max_digits=30, null=True)),
            ],
            options={
                'ordering': ['resource'],
            },
        ),
        migrations.CreateModel(
            name='EnergyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy_type', models.CharField(default='thermal', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physical_quantity', models.CharField(default='DEFAULT', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(default='solid', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, null=True)),
                ('book', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(default='DEFAULT', max_length=100)),
                ('symbol', models.CharField(default='DEFAULT', max_length=100)),
                ('comment', models.TextField(blank=True, null=True)),
                ('physical_quantity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.PhysicalQuantity')),
            ],
            options={
                'ordering': ['symbol'],
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='resource', max_length=100)),
                ('weight', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('volume', models.DecimalField(decimal_places=10, default=0, max_digits=19, null=True)),
                ('density', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('price', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('density_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='density_ref', to='tools.Reference')),
                ('density_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Resource_density_unit', to='tools.Unit')),
                ('price_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='price_ref', to='tools.Reference')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.PhysicalState')),
                ('volume_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Resource_volume_unit', to='tools.Unit')),
                ('weight_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Resource_weight_unit', to='tools.Unit')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PhysicalConstant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('value', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('efficiency', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('price', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('power', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('consumption', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('consumption_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tools.Unit')),
                ('energy_input', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Machine_energy_input', to='tools.Energy')),
                ('energy_output', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Machine_energy_output', to='tools.Energy')),
                ('power_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tools.Unit')),
                ('resource_input', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Machine_resource_input', to='tools.Resource')),
                ('resource_output', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Machine_resource_output', to='tools.Resource')),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arms_power', models.DecimalField(decimal_places=0, max_digits=4, null=True)),
                ('legs_power', models.DecimalField(decimal_places=0, max_digits=4, null=True)),
                ('weight', models.DecimalField(decimal_places=0, max_digits=4, null=True)),
                ('arms_power_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Human_arms_power_unit', to='tools.Unit')),
                ('legs_power_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Human_legs_power_unit', to='tools.Unit')),
                ('weight_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Human_weight_unit', to='tools.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='HeightScale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('height', models.DecimalField(decimal_places=0, max_digits=4, null=True)),
                ('height_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HeightScale_height_unit', to='tools.Unit')),
            ],
        ),
        migrations.AddField(
            model_name='energy',
            name='energy_density_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='energy_density_ref', to='tools.Reference'),
        ),
        migrations.AddField(
            model_name='energy',
            name='energy_density_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='energy_density_unit', to='tools.Unit'),
        ),
        migrations.AddField(
            model_name='energy',
            name='energy_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.EnergyType'),
        ),
        migrations.AddField(
            model_name='energy',
            name='resource',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tools.Resource'),
        ),
        migrations.AddField(
            model_name='energy',
            name='specific_energy_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specific_energy_ref', to='tools.Reference'),
        ),
        migrations.AddField(
            model_name='energy',
            name='specific_energy_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specific_energy_unit', to='tools.Unit'),
        ),
        migrations.AddField(
            model_name='energy',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Unit'),
        ),
        migrations.CreateModel(
            name='ConversionCoefficient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=3, default=0, max_digits=21, null=True)),
                ('unit_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tools.Unit')),
                ('unit_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tools.Unit')),
            ],
        ),
    ]
