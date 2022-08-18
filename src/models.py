# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categorie(models.Model):
    categorieid = models.AutoField(db_column='CategorieId', primary_key=True)  # Field name made lowercase.
    nomcategorie = models.CharField(db_column='NomCategorie', max_length=15, db_collation='French_CI_AS')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=2000, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Categorie'


class Client(models.Model):
    clientid = models.CharField(db_column='ClientId', primary_key=True, max_length=5, db_collation='French_CI_AS')  # Field name made lowercase.
    nomsociete = models.CharField(db_column='NomSociete', max_length=40, db_collation='French_CI_AS')  # Field name made lowercase.
    contactnom = models.CharField(db_column='ContactNom', max_length=30, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contacttitre = models.CharField(db_column='ContactTitre', max_length=30, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=60, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ville = models.CharField(db_column='Ville', max_length=15, db_collation='French_CI_AS')  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=15, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    codepostal = models.CharField(db_column='CodePostal', max_length=10, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pays = models.CharField(db_column='Pays', max_length=15, db_collation='French_CI_AS')  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=24, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=24, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Client'


class Collation(models.Model):
    texte = models.CharField(max_length=30, db_collation='French_CI_AS')

    class Meta:
        managed = True
        db_table = 'Collation'


class Commande(models.Model):
    commandeid = models.AutoField(db_column='CommandeId', primary_key=True)  # Field name made lowercase.
    clientid = models.CharField(db_column='ClientId', max_length=5, db_collation='French_CI_AS')  # Field name made lowercase.
    employeid = models.IntegerField(db_column='EmployeId')  # Field name made lowercase.
    datecommande = models.DateTimeField(db_column='DateCommande')  # Field name made lowercase.
    datedemandee = models.DateTimeField(db_column='DateDemandee', blank=True, null=True)  # Field name made lowercase.
    dateexpedition = models.DateTimeField(db_column='DateExpedition', blank=True, null=True)  # Field name made lowercase.
    transporteurid = models.IntegerField(db_column='TransporteurId', blank=True, null=True)  # Field name made lowercase.
    transport = models.DecimalField(db_column='Transport', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Commande'


class Division(models.Model):
    divisionid = models.SmallIntegerField(db_column='DivisionId', primary_key=True)  # Field name made lowercase.
    nomdivision = models.CharField(db_column='NomDivision', max_length=40, db_collation='French_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Division'


class Employe(models.Model):
    employeid = models.AutoField(db_column='EmployeId', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=20, db_collation='French_CI_AS')  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=10, db_collation='French_CI_AS')  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=30, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    civilite = models.CharField(db_column='Civilite', max_length=25, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=1, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datenaissance = models.DateTimeField(db_column='DateNaissance', blank=True, null=True)  # Field name made lowercase.
    dateembauche = models.DateTimeField(db_column='DateEmbauche', blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=60, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ville = models.CharField(db_column='Ville', max_length=15, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=15, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    codepostal = models.CharField(db_column='CodePostal', max_length=10, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pays = models.CharField(db_column='Pays', max_length=15, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telephonepersonnel = models.CharField(db_column='TelephonePersonnel', max_length=24, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    extension = models.CharField(db_column='Extension', max_length=4, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dependde = models.IntegerField(db_column='DependDe', blank=True, null=True)  # Field name made lowercase.
    salaireactuel = models.DecimalField(db_column='SalaireActuel', max_digits=19, decimal_places=4)  # Field name made lowercase.
    prime = models.DecimalField(db_column='Prime', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    divisionid = models.SmallIntegerField(db_column='DivisionId', blank=True, null=True)  # Field name made lowercase.
    serviceid = models.SmallIntegerField(db_column='ServiceId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Employe'


class Fournisseur(models.Model):
    fournisseurid = models.AutoField(db_column='FournisseurId', primary_key=True)  # Field name made lowercase.
    nomsociete = models.CharField(db_column='NomSociete', max_length=40, db_collation='French_CI_AS')  # Field name made lowercase.
    contactnom = models.CharField(db_column='ContactNom', max_length=30, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contacttitre = models.CharField(db_column='ContactTitre', max_length=30, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=60, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ville = models.CharField(db_column='Ville', max_length=15, db_collation='French_CI_AS')  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=15, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    codepostal = models.CharField(db_column='CodePostal', max_length=10, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pays = models.CharField(db_column='Pays', max_length=15, db_collation='French_CI_AS')  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=24, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=24, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    siteweb = models.CharField(db_column='SiteWeb', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Fournisseur'


class Historiquesalaires(models.Model):
    employeid = models.IntegerField(db_column='EmployeId', primary_key=True)  # Field name made lowercase.
    datedebut = models.DateTimeField(db_column='DateDebut')  # Field name made lowercase.
    salaire = models.DecimalField(db_column='Salaire', max_digits=19, decimal_places=4)  # Field name made lowercase.
    datefin = models.DateTimeField(db_column='DateFin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'HistoriqueSalaires'
        unique_together = (('employeid', 'datedebut'),)


class Lignecommandes(models.Model):
    commandeid = models.IntegerField(db_column='CommandeId', primary_key=True)  # Field name made lowercase.
    produitid = models.IntegerField(db_column='ProduitId')  # Field name made lowercase.
    prixunitaire = models.DecimalField(db_column='PrixUnitaire', max_digits=19, decimal_places=4)  # Field name made lowercase.
    quantite = models.SmallIntegerField(db_column='Quantite')  # Field name made lowercase.
    remise = models.DecimalField(db_column='Remise', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LigneCommandes'
        unique_together = (('commandeid', 'produitid'),)


class Produit(models.Model):
    produitid = models.AutoField(db_column='ProduitId', primary_key=True)  # Field name made lowercase.
    nomproduit = models.CharField(db_column='NomProduit', max_length=40, db_collation='French_CI_AS')  # Field name made lowercase.
    fournisseurid = models.IntegerField(db_column='FournisseurId', blank=True, null=True)  # Field name made lowercase.
    categorieid = models.IntegerField(db_column='CategorieId')  # Field name made lowercase.
    unitecontionnement = models.CharField(db_column='UniteContionnement', max_length=20, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prixunitaire = models.DecimalField(db_column='PrixUnitaire', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quantiteenstock = models.SmallIntegerField(db_column='QuantiteEnStock', blank=True, null=True)  # Field name made lowercase.
    quantiteencommande = models.SmallIntegerField(db_column='QuantiteEnCommande', blank=True, null=True)  # Field name made lowercase.
    niveaureappro = models.SmallIntegerField(db_column='NiveauReappro', blank=True, null=True)  # Field name made lowercase.
    enrupture = models.BooleanField(db_column='EnRupture')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Produit'


class Service(models.Model):
    divisionid = models.SmallIntegerField(db_column='DivisionId', primary_key=True)  # Field name made lowercase.
    serviceid = models.SmallIntegerField(db_column='ServiceId')  # Field name made lowercase.
    nomservice = models.CharField(db_column='NomService', max_length=40, db_collation='French_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Service'
        unique_together = (('divisionid', 'serviceid'),)


class Transporteur(models.Model):
    transporteurid = models.AutoField(db_column='TransporteurId', primary_key=True)  # Field name made lowercase.
    nomsociete = models.CharField(db_column='NomSociete', max_length=40, db_collation='French_CI_AS')  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=24, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Transporteur'