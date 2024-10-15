# Generated by Django 4.2.10 on 2024-08-20 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("claim_sampling", "0005_alter_claimsamplingbatchassignment_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="claimsamplingbatchassignment",
            name="claim",
            field=models.ForeignKey(
                db_column="ClaimID",
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="assignments",
                to="claim.claim",
            ),
        ),
        migrations.AlterField(
            model_name="claimsamplingbatchassignment",
            name="claim_batch",
            field=models.ForeignKey(
                db_column="ClaimSamplingBatchID",
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="assignments",
                to="claim_sampling.claimsamplingbatch",
            ),
        ),
    ]