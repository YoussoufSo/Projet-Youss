# Sauve 1.2
#Import du module os dédié à la gestion des fichiers et des dossiers
import os
#Import du module filecmp dédié à la comparaison des fichiers et des dossiers
import filecmp
#Import du module shutil dédié à copie et à la copie et à l'archivage des fichiers et dossiers
import shutil

#Comparaison des deux fichiers interfaces et backup

if filecmp.cmp('/etc/network/interfaces' ,'/bac/backup'):
    """Si le contenu des deux fichiers est le même on appele le fichier notsavemessage.py 
    avec la commande import notsavemessage
    qui envoi un message à un adresse pour l'informe qu'aucune sauvegarde n'a été effectue"""
    import notsavemessage

#Sinon si les contenus des deux fichiers sont différents
    
else:
    
    #On fait appele au fichier archiver.py pour archiver la sauvegarde presente avant d'effectuer une atre autre
    import archiver
    #Ensuite on remplace le fichier 'backup' par le fichier 'interfaces'
    shutil.copyfile('/etc/network/interfaces', '/bac/backup')
    
    """Et on envoi un message à une adresse pour l'informer qu'une sauvegarde 
    vient d'être effectué en incluant le fichier savemessage.py"""
    
    import savemessage
