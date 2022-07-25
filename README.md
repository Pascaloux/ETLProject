# ETLProject

# EXECUTION DU PROGRAMME
Il y a trois fichiers pour la création de la base de données et quatre fichiers pour l'ETL.

# Première partie : création de la base de données
Premièrement il faut exécuter le fichier createtable.py pour créer la base de données ainsi que les tables.
Le fichier createtable.py fera appel aux fichiers base.py et table.py.
Il faudra renseigner les paramètres de connexions a MySQL.

# Deuxième partie : remplissage de la base de données avec une méthode Extract-Transform-Load
Deuxièmement il faut exécuter le fichier execute.py qui fera successivement appel aux fonctions du fichiers extract.py, transform.py et load.py.
Il faudra renseigner les paramètres de connexions a MySQL.

# Sous-Dossiers
- DonneesBrutes : contient les 3 fichiers csv de base créés avec le fichier extract.py
- DonneesPropres : contient les 3 fichiers csv transformés avec le fichier transform.py
(Dans chaque sous-dossier des données, les fichiers csv des valeurs foncieres n'ont pas pu être charger sur github à cause de leur taille trop importante )



# ANALYSE DES DONNNEES

# extract des valeurs foncières

colonnes pertinentes : 
    . No disposition            = de 1 à 198                                                                                       - Pas de null
    . Date mutation             = dates de 2021                                                                                    - Pas de null
    . Nature mutation    = Adjudication, Echange, Expropriation, Vente, Vente en l'état futur d'achèvement, Vente terrain à bâtir  - Pas de null
    . Valeur fonciere           = de 0,15 à 620 000 000                                                                       - Beaucoup de null
    . No voie                   = de 0 à 9999                                                                                 - Beaucoup de null
    . B/T/Q                     = de 0 à 9, de A à Z, -, .                                                                    - Beaucoup de null
    . Type de voie              = raccourcis de 2, 3 ou 4 lettres                                                             - Beaucoup de null
    . Code voie                 = de 1 à 9992, de A000 à X993                                                                 - Beaucoup de mail
    . Voie                      = zone texte                                                                                  - Beaucoup de null
    . Code postal               = de 01000 à 97490                                                                            - Beaucoup de null
    . Commune                   = zone texte                                                                                       - Pas de null
    . Code departement          = de 1 à 95, 2A et 2B, de 971 à 974                                                                - Pas de null
    . Code commune              = de 1 à 909                                                                                       - Pas de null
    . Prefixe de section        = de 1 à 950                                                                                  - Beaucoup de null
    . Section                   = de A à Z, de AA à ZZ                                                                             - Pas de null
    . No plan                   = de 1 à 9844                                                                                      - Pas de null
    . No Volume                 = de 1 à 211 402, A, B, D, 1B, 3B, P419004, UN, DEUX, TROIS, ET                               - Beaucoup de null
    . 1er lot                   = numérique ou alphanumérique jusqu'à 10 caractères                                           - Beaucoup de null
    . Surface Carrez du 1er lot = de 0,01 à 9614                                                                              - Beaucoup de null
    . 2eme lot                  = numérique ou alphanumérique jusqu'à 10 caractères                                           - Beaucoup de null
    . Surface Carrez du 2eme lot= de 0,5 à 7392                                                                               - Beaucoup de null
    . 3eme lot                  = numérique ou alphanumérique jusqu'à 10 caractères                                           - Beaucoup de null
    . Surface Carrez du 3eme lot= de 0,2 à 2550                                                                               - Beaucoup de null
    . 4eme lot                  = numérique ou alphanumérique jusqu'à 10 caractères                                           - Beaucoup de null
    . Surface Carrez du 4eme lot= de 1,1 à 6881                                                                               - Beaucoup de null
    . 5eme lot                  = numérique ou alphanumérique jusqu'à 10 caractères                                           - Beaucoup de null
    . Surface Carrez du 5eme lot= de 0,4 à 1451,59                                                                            - Beaucoup de null
    . Nombre de lots            = de 0 à 138                                                                                       - Pas de null
    . Code type local           = de 1 à 4                                                                                    - Beaucoup de null
    . Type local                = Maison(1), Appartement(2), Dépendance(3), Local industriel, commercial ou assimilé(4)       - Beaucoup de null
    . Surface reelle bati       = de 0 à 237 500                                                                              - Beaucoup de null
    . Nombre pieces principales = de 0 à 89                                                                                   - Beaucoup de null
    . Nature culture            = 1 ou 2 lettres                                                                              - Beaucoup de null
    . Nature culture speciale   = 4 ou 5 lettres                                                                              - Beaucoup de null
    . Surface terrain           = de 0 à 2 967 329                                                                            - Beaucoup de null

colonnes inutiles :
- colonne vides :
    . Code service CH
    . Reference document
    . 1 Articles CGI
    . 2 Articles CGI
    . 3 Articles CGI
    . 4 Articles CGI
    . 5 Articles CGI
    . Identifiant local


# extract "market capitalization of largest banks"

colonnes pertinentes : 
    . Name                         = Nom de la banque                                                                              - Pas de null
    . Market Cap (US$ Billion)     = Capitalisation boursière en milliards de dollars                                              - Pas de null
   

# transform des valeurs foncières

colonnes transformées en string: 
    . Nature mutation'
    . B/T/Q
    . Type de voie
    . Code voie
    . Voie
    . Commune
    . Code departement
    . Section
    . No Volume
    . 1er lot
    . 2eme lot
    . 3eme lot
    . 4eme lot
    . 5eme lot
    . Type local
    . Nature culture
    . Nature culture speciale
    . Surface Carrez du 1er lot

colonnes tranformées en int :
    . No voie
    . Code postal
    . Prefixe de section
    . No plan


colonnes transformées en float :
    . Valeur fonciere
    . Surface Carrez du 1er lot
    . Surface Carrez du 2eme lot
    . Surface Carrez du 3eme lot
    . Surface Carrez du 4eme lot
    . Surface Carrez du 5eme lot


# transform # extract "market capitalization of largest banks"

colonnes transformées en float: 
    . Market Cap (US$ Billion)

colonnes transformées du Dollar à l'Euro:
    . Market Cap (US$ Billion) ---->  Market_Cap(Eur_Billion)
    
 