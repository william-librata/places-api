# Generated by Django 3.0.6 on 2020-05-19 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20200519_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressalias',
            name='alias_pid',
            field=models.ForeignKey(db_column='alias_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='address_alias_pid', to='places.AddressDetail'),
        ),
        migrations.AddField(
            model_name='addressalias',
            name='alias_type_code',
            field=models.ForeignKey(db_column='alias_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.AddressAliasTypeAut'),
        ),
        migrations.AddField(
            model_name='addressalias',
            name='principal_pid',
            field=models.ForeignKey(db_column='principal_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='address_alias_principal_pid', to='places.AddressDetail'),
        ),
        migrations.AddField(
            model_name='addressdefaultgeocode',
            name='address_detail_pid',
            field=models.ForeignKey(db_column='address_detail_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.AddressDetail'),
        ),
        migrations.AddField(
            model_name='addressdefaultgeocode',
            name='geocode_type_code',
            field=models.ForeignKey(db_column='geocode_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.GeocodeTypeAut'),
        ),
        migrations.AddField(
            model_name='addressdetail',
            name='address_site_pid',
            field=models.ForeignKey(db_column='address_site_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.AddressSite'),
        ),
        migrations.AddField(
            model_name='addressdetail',
            name='flat_type_code',
            field=models.ForeignKey(blank=True, db_column='flat_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.FlatTypeAut'),
        ),
        migrations.AddField(
            model_name='addressdetail',
            name='level_geocoded_code',
            field=models.ForeignKey(db_column='level_geocoded_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.GeocodedLevelTypeAut'),
        ),
        migrations.AddField(
            model_name='addressdetail',
            name='level_type_code',
            field=models.ForeignKey(blank=True, db_column='level_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.LevelTypeAut'),
        ),
        migrations.AddField(
            model_name='addressdetail',
            name='locality_pid',
            field=models.ForeignKey(db_column='locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.Locality'),
        ),
        migrations.AddField(
            model_name='addressdetail',
            name='street_locality_pid',
            field=models.ForeignKey(blank=True, db_column='street_locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetLocality'),
        ),
        migrations.AddField(
            model_name='addressmeshblock2011',
            name='address_detail_pid',
            field=models.ForeignKey(db_column='address_detail_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.AddressDetail'),
        ),
        migrations.AddField(
            model_name='addressmeshblock2011',
            name='mb_2011_pid',
            field=models.ForeignKey(db_column='mb_2011_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.Mb2011'),
        ),
        migrations.AddField(
            model_name='addressmeshblock2011',
            name='mb_match_code',
            field=models.ForeignKey(db_column='mb_match_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.MbMatchCodeAut'),
        ),
        migrations.AddField(
            model_name='addressmeshblock2016',
            name='address_detail_pid',
            field=models.ForeignKey(db_column='address_detail_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.AddressDetail'),
        ),
        migrations.AddField(
            model_name='addressmeshblock2016',
            name='mb_2016_pid',
            field=models.ForeignKey(db_column='mb_2016_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.Mb2016'),
        ),
        migrations.AddField(
            model_name='addressmeshblock2016',
            name='mb_match_code',
            field=models.ForeignKey(db_column='mb_match_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.MbMatchCodeAut'),
        ),
        migrations.AddField(
            model_name='addresssite',
            name='address_type',
            field=models.ForeignKey(blank=True, db_column='address_type', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.AddressTypeAut'),
        ),
        migrations.AddField(
            model_name='addresssitegeocode',
            name='address_site_pid',
            field=models.ForeignKey(blank=True, db_column='address_site_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.AddressSite'),
        ),
        migrations.AddField(
            model_name='addresssitegeocode',
            name='geocode_type_code',
            field=models.ForeignKey(blank=True, db_column='geocode_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.GeocodeTypeAut'),
        ),
        migrations.AddField(
            model_name='addresssitegeocode',
            name='reliability_code',
            field=models.ForeignKey(db_column='reliability_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.GeocodeReliabilityAut'),
        ),
        migrations.AddField(
            model_name='locality',
            name='gnaf_reliability_code',
            field=models.ForeignKey(db_column='gnaf_reliability_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.GeocodeReliabilityAut'),
        ),
        migrations.AddField(
            model_name='locality',
            name='locality_class_code',
            field=models.ForeignKey(db_column='locality_class_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.LocalityClassAut'),
        ),
        migrations.AddField(
            model_name='locality',
            name='state_pid',
            field=models.ForeignKey(db_column='state_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.State'),
        ),
        migrations.AddField(
            model_name='localityalias',
            name='alias_type_code',
            field=models.ForeignKey(db_column='alias_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.LocalityAliasTypeAut'),
        ),
        migrations.AddField(
            model_name='localityalias',
            name='locality_pid',
            field=models.ForeignKey(db_column='locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.Locality'),
        ),
        migrations.AddField(
            model_name='localityneighbour',
            name='locality_pid',
            field=models.ForeignKey(db_column='locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='locality_neighbour_locality_pid', to='places.Locality'),
        ),
        migrations.AddField(
            model_name='localityneighbour',
            name='neighbour_locality_pid',
            field=models.ForeignKey(db_column='neighbour_locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='locality_neighbour_neighbour_locality_pid', to='places.Locality'),
        ),
        migrations.AddField(
            model_name='localitypoint',
            name='locality_pid',
            field=models.ForeignKey(db_column='locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.Locality'),
        ),
        migrations.AddField(
            model_name='primarysecondary',
            name='primary_pid',
            field=models.ForeignKey(db_column='primary_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='primary_secondary_primary_pid', to='places.AddressDetail'),
        ),
        migrations.AddField(
            model_name='primarysecondary',
            name='ps_join_type_code',
            field=models.ForeignKey(db_column='ps_join_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.PsJoinTypeAut'),
        ),
        migrations.AddField(
            model_name='primarysecondary',
            name='secondary_pid',
            field=models.ForeignKey(db_column='secondary_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='primary_secondary_secondary_pid', to='places.AddressDetail'),
        ),
        migrations.AddField(
            model_name='streetlocality',
            name='gnaf_reliability_code',
            field=models.ForeignKey(db_column='gnaf_reliability_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.GeocodeReliabilityAut'),
        ),
        migrations.AddField(
            model_name='streetlocality',
            name='locality_pid',
            field=models.ForeignKey(db_column='locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.Locality'),
        ),
        migrations.AddField(
            model_name='streetlocality',
            name='street_class_code',
            field=models.ForeignKey(db_column='street_class_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetClassAut'),
        ),
        migrations.AddField(
            model_name='streetlocality',
            name='street_suffix_code',
            field=models.ForeignKey(blank=True, db_column='street_suffix_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetSuffixAut'),
        ),
        migrations.AddField(
            model_name='streetlocality',
            name='street_type_code',
            field=models.ForeignKey(blank=True, db_column='street_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetTypeAut'),
        ),
        migrations.AddField(
            model_name='streetlocalityalias',
            name='alias_type_code',
            field=models.ForeignKey(db_column='alias_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetLocalityAliasTypeAut'),
        ),
        migrations.AddField(
            model_name='streetlocalityalias',
            name='street_locality_pid',
            field=models.ForeignKey(db_column='street_locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetLocality'),
        ),
        migrations.AddField(
            model_name='streetlocalityalias',
            name='street_suffix_code',
            field=models.ForeignKey(blank=True, db_column='street_suffix_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetSuffixAut'),
        ),
        migrations.AddField(
            model_name='streetlocalityalias',
            name='street_type_code',
            field=models.ForeignKey(blank=True, db_column='street_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetTypeAut'),
        ),
        migrations.AddField(
            model_name='streetlocalitypoint',
            name='street_locality_pid',
            field=models.ForeignKey(db_column='street_locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetLocality'),
        ),
    ]
