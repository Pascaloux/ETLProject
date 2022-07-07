# ETLProject

# extract des valeurs foncières

colonnes pertinentes : 
    . No disposition            = de 1 à 198                                                                                       - Pas de null
    . Date mutation             = dates de 2021                                                                                    - Pas de null
    . Nature mutation    = Adjudication, Echange, Expropriation, Vente, Vente en l'état futur d'achèvement, Vente terrain à bâtir  - Pas de null
    . Valeur fonciere           = de 0,6 à 50 000 000                                                                         - Beaucoup de null
    . No voie                   = de 1 à 9999                                                                                 - Beaucoup de null
    . B/T/Q                     = de 0 à 9, de A à Z, -, .                                                                    - Beaucoup de null
    . Type de voie              = raccourcis de 2, 3 ou 4 lettres                                                             - Beaucoup de null
    . Code voie                 = de 1 à 9810, de A001 à X991                                                                 - Beaucoup de mail
    . Voie                      = zone texte                                                                                  - Beaucoup de null
    . Code postal               = nombre à 5 chiffres                                                                         - Beaucoup de null
    . Commune                   = zone texte                                                                                       - Pas de null
    . Code departement          = de 1 à 99, 2A et 2B                                                                              - Pas de null
    . Code commune              = de 1 à 834                                                                                       - Pas de null
    . Prefixe de section        = de 2 à 950                                                                                  - Beaucoup de null
    . Section                   = 1 ou 2 lettres                                                                                   - Pas de null
    . No plan                   = de 1 à 8494                                                                                      - Pas de null
    . No Volume                 = de 1 à 130000, 1B, 3B DEUX, P419004, TROIS, UN                                              - Beaucoup de null
    . 1er lot                   = numérique ou alphanumérique                                                                 - Beaucoup de null
    . Surface Carrez du 1er lot = de 1 à 9614                                                                                 - Beaucoup de null
    . 2eme lot                  = numérique ou alphanumérique                                                                 - Beaucoup de null
    . Surface Carrez du 2eme lot = de 0,7 à 4950                                                                              - Beaucoup de null
    . 3eme lot                  = numérique ou alphanumérique                                                                 - Beaucoup de null
    . Surface Carrez du 2eme lot = de 0,2 à 1764,67                                                                           - Beaucoup de null
    . 4eme lot                  = numérique ou alphanumérique                                                                 - Beaucoup de null
    . Surface Carrez du 2eme lot = de 3,3 à 675,91                                                                            - Beaucoup de null
    . 5eme lot                  = numérique ou alphanumérique                                                                 - Beaucoup de null
    . Surface Carrez du 2eme lot = de 1,07 à 859,11                                                                           - Beaucoup de null
    . Nombre de lots            = de 0 à 75                                                                                        - Pas de null
    . Code type local           = de 1 à 4                                                                                    - Beaucoup de null
    . Type local                = Maison(1), Appartement(2), Dépendance(3), Local industriel, commercial ou assimilé(4)       - Beaucoup de null
    . Surface réelle bati       = de 0 à 125 530                                                                              - Beaucoup de null
    . Nombre pieces principales = de 0 à 55                                                                                   - Beaucoup de null
    . Nature culture            = 1 ou 2 lettres                                                                              - Beaucoup de null
    . Nature culture speciale   = 4 ou 5 lettres                                                                              - Beaucoup de null
    . Surface terrain           = de 0 à 592 047                                                                              - Beaucoup de null

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
    . Name                         = Nom de la banque                                                                                 - Pas de null
    . Market Cap (US$ Billion)     = Capitalisation boursière en milliards de dollars                                                 - Pas de null
   

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

colonnes transformée en float: 
    . Market Cap (US$ Billion)

colonnes transformée du Dollar à l'Euro:
    . Market Cap (US$ Billion) ---->  Market_Cap(Eur_Billion)
    