# Generated by Django 4.1 on 2022-08-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('categorieid', models.AutoField(db_column='CategorieId', primary_key=True, serialize=False)),
                ('nomcategorie', models.CharField(db_collation='French_CI_AS', db_column='NomCategorie', max_length=15)),
                ('description', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Description', max_length=2000, null=True)),
            ],
            options={
                'db_table': 'Categorie',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('clientid', models.CharField(db_collation='French_CI_AS', db_column='ClientId', max_length=5, primary_key=True, serialize=False)),
                ('nomsociete', models.CharField(db_collation='French_CI_AS', db_column='NomSociete', max_length=40)),
                ('contactnom', models.CharField(blank=True, db_collation='French_CI_AS', db_column='ContactNom', max_length=30, null=True)),
                ('contacttitre', models.CharField(blank=True, db_collation='French_CI_AS', db_column='ContactTitre', max_length=30, null=True)),
                ('adresse', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Adresse', max_length=60, null=True)),
                ('ville', models.CharField(db_collation='French_CI_AS', db_column='Ville', max_length=15)),
                ('region', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Region', max_length=15, null=True)),
                ('codepostal', models.CharField(blank=True, db_collation='French_CI_AS', db_column='CodePostal', max_length=10, null=True)),
                ('pays', models.CharField(db_collation='French_CI_AS', db_column='Pays', max_length=15)),
                ('telephone', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Telephone', max_length=24, null=True)),
                ('fax', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Fax', max_length=24, null=True)),
            ],
            options={
                'db_table': 'Client',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Collation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.CharField(db_collation='French_CI_AS', max_length=30)),
            ],
            options={
                'db_table': 'Collation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('commandeid', models.AutoField(db_column='CommandeId', primary_key=True, serialize=False)),
                ('clientid', models.CharField(db_collation='French_CI_AS', db_column='ClientId', max_length=5)),
                ('employeid', models.IntegerField(db_column='EmployeId')),
                ('datecommande', models.DateTimeField(db_column='DateCommande')),
                ('datedemandee', models.DateTimeField(blank=True, db_column='DateDemandee', null=True)),
                ('dateexpedition', models.DateTimeField(blank=True, db_column='DateExpedition', null=True)),
                ('transporteurid', models.IntegerField(blank=True, db_column='TransporteurId', null=True)),
                ('transport', models.DecimalField(blank=True, db_column='Transport', decimal_places=4, max_digits=19, null=True)),
            ],
            options={
                'db_table': 'Commande',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('divisionid', models.SmallIntegerField(db_column='DivisionId', primary_key=True, serialize=False)),
                ('nomdivision', models.CharField(db_collation='French_CI_AS', db_column='NomDivision', max_length=40)),
            ],
            options={
                'db_table': 'Division',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('employeid', models.AutoField(db_column='EmployeId', primary_key=True, serialize=False)),
                ('nom', models.CharField(db_collation='French_CI_AS', db_column='Nom', max_length=20)),
                ('prenom', models.CharField(db_collation='French_CI_AS', db_column='Prenom', max_length=10)),
                ('titre', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Titre', max_length=30, null=True)),
                ('civilite', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Civilite', max_length=25, null=True)),
                ('sexe', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Sexe', max_length=1, null=True)),
                ('datenaissance', models.DateTimeField(blank=True, db_column='DateNaissance', null=True)),
                ('dateembauche', models.DateTimeField(blank=True, db_column='DateEmbauche', null=True)),
                ('adresse', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Adresse', max_length=60, null=True)),
                ('ville', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Ville', max_length=15, null=True)),
                ('region', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Region', max_length=15, null=True)),
                ('codepostal', models.CharField(blank=True, db_collation='French_CI_AS', db_column='CodePostal', max_length=10, null=True)),
                ('pays', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Pays', max_length=15, null=True)),
                ('telephonepersonnel', models.CharField(blank=True, db_collation='French_CI_AS', db_column='TelephonePersonnel', max_length=24, null=True)),
                ('extension', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Extension', max_length=4, null=True)),
                ('dependde', models.IntegerField(blank=True, db_column='DependDe', null=True)),
                ('salaireactuel', models.DecimalField(db_column='SalaireActuel', decimal_places=4, max_digits=19)),
                ('prime', models.DecimalField(blank=True, db_column='Prime', decimal_places=4, max_digits=19, null=True)),
                ('divisionid', models.SmallIntegerField(blank=True, db_column='DivisionId', null=True)),
                ('serviceid', models.SmallIntegerField(blank=True, db_column='ServiceId', null=True)),
            ],
            options={
                'db_table': 'Employe',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('fournisseurid', models.AutoField(db_column='FournisseurId', primary_key=True, serialize=False)),
                ('nomsociete', models.CharField(db_collation='French_CI_AS', db_column='NomSociete', max_length=40)),
                ('contactnom', models.CharField(blank=True, db_collation='French_CI_AS', db_column='ContactNom', max_length=30, null=True)),
                ('contacttitre', models.CharField(blank=True, db_collation='French_CI_AS', db_column='ContactTitre', max_length=30, null=True)),
                ('adresse', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Adresse', max_length=60, null=True)),
                ('ville', models.CharField(db_collation='French_CI_AS', db_column='Ville', max_length=15)),
                ('region', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Region', max_length=15, null=True)),
                ('codepostal', models.CharField(blank=True, db_collation='French_CI_AS', db_column='CodePostal', max_length=10, null=True)),
                ('pays', models.CharField(db_collation='French_CI_AS', db_column='Pays', max_length=15)),
                ('telephone', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Telephone', max_length=24, null=True)),
                ('fax', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Fax', max_length=24, null=True)),
                ('siteweb', models.CharField(blank=True, db_collation='French_CI_AS', db_column='SiteWeb', max_length=100, null=True)),
            ],
            options={
                'db_table': 'Fournisseur',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('produitid', models.AutoField(db_column='ProduitId', primary_key=True, serialize=False)),
                ('nomproduit', models.CharField(db_collation='French_CI_AS', db_column='NomProduit', max_length=40)),
                ('fournisseurid', models.IntegerField(blank=True, db_column='FournisseurId', null=True)),
                ('categorieid', models.IntegerField(db_column='CategorieId')),
                ('unitecontionnement', models.CharField(blank=True, db_collation='French_CI_AS', db_column='UniteContionnement', max_length=20, null=True)),
                ('prixunitaire', models.DecimalField(blank=True, db_column='PrixUnitaire', decimal_places=4, max_digits=19, null=True)),
                ('quantiteenstock', models.SmallIntegerField(blank=True, db_column='QuantiteEnStock', null=True)),
                ('quantiteencommande', models.SmallIntegerField(blank=True, db_column='QuantiteEnCommande', null=True)),
                ('niveaureappro', models.SmallIntegerField(blank=True, db_column='NiveauReappro', null=True)),
                ('enrupture', models.BooleanField(db_column='EnRupture')),
            ],
            options={
                'db_table': 'Produit',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Transporteur',
            fields=[
                ('transporteurid', models.AutoField(db_column='TransporteurId', primary_key=True, serialize=False)),
                ('nomsociete', models.CharField(db_collation='French_CI_AS', db_column='NomSociete', max_length=40)),
                ('telephone', models.CharField(blank=True, db_collation='French_CI_AS', db_column='Telephone', max_length=24, null=True)),
            ],
            options={
                'db_table': 'Transporteur',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('divisionid', models.SmallIntegerField(db_column='DivisionId', primary_key=True, serialize=False)),
                ('serviceid', models.SmallIntegerField(db_column='ServiceId')),
                ('nomservice', models.CharField(db_collation='French_CI_AS', db_column='NomService', max_length=40)),
            ],
            options={
                'db_table': 'Service',
                'managed': True,
                'unique_together': {('divisionid', 'serviceid')},
            },
        ),
        migrations.CreateModel(
            name='Lignecommandes',
            fields=[
                ('commandeid', models.IntegerField(db_column='CommandeId', primary_key=True, serialize=False)),
                ('produitid', models.IntegerField(db_column='ProduitId')),
                ('prixunitaire', models.DecimalField(db_column='PrixUnitaire', decimal_places=4, max_digits=19)),
                ('quantite', models.SmallIntegerField(db_column='Quantite')),
                ('remise', models.DecimalField(db_column='Remise', decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'LigneCommandes',
                'managed': True,
                'unique_together': {('commandeid', 'produitid')},
            },
        ),
        migrations.CreateModel(
            name='Historiquesalaires',
            fields=[
                ('employeid', models.IntegerField(db_column='EmployeId', primary_key=True, serialize=False)),
                ('datedebut', models.DateTimeField(db_column='DateDebut')),
                ('salaire', models.DecimalField(db_column='Salaire', decimal_places=4, max_digits=19)),
                ('datefin', models.DateTimeField(blank=True, db_column='DateFin', null=True)),
            ],
            options={
                'db_table': 'HistoriqueSalaires',
                'managed': True,
                'unique_together': {('employeid', 'datedebut')},
            },
        ),
    ]