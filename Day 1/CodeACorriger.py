#6 erreurs à trouver!
#####################

#Combien de jours reste-t'il avant le 1er juillet ?
#Donner date actuelle ci-dessous
var_jour = 30    #N° du jour
var_mois = 6   #N° du mois

#Nombre de jours de chaque mois
jours_mars = 31
jours_avril = 30
jours_mai = 31
jours_juin = 30

#Cas selon le mois traité
if var_mois == 3 : #Mars
    jours_restant_mars = jours_mars - var_jour
    jours_totaux = jours_restant_mars + jours_avril + jours_mai + jours_juin + 1
    print("Il reste " + str(jours_totaux) + " jours avant le 1er juillet.")
if var_mois == 4 : #Avril
    jours_restants_avril = jours_avril - var_jour
    jours_totaux = jours_restants_avril + jours_mai + jours_juin + 1
    print("Il reste " + str(jours_totaux) + " jours avant le 1er juillet.")
if var_mois == 5 : #Mai
    jours_restants_mai = jours_mai - var_jour
    jours_totaux = jours_restants_mai + jours_juin + 1
    print("Il reste " + str(jours_totaux) + " jours avant le 1er juillet.")
if var_mois == 6 : #Juin
    jours_restants_juin = jours_juin - var_jour
    jours_totaux = jours_restants_juin + 1
    print("Il reste " + str(jours_totaux) + " jours avant le 1er juillet.")
