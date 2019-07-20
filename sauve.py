#Sauve 1.0
import os
import filecmp
import shutil

if filecmp.cmp('/etc/network/interfaces' ,'/bac/backup' ):
    print('Fichier non modifier donc aucune sauvegarde')
else:
    shutil.copyfile('/etc/network/interfaces', '/bac/backup')
    print('Fichier sauvegarder')
