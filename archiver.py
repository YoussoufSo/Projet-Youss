#Import du module os dédié à la gestion des fichiers et des dossiers
import os
#Import du module shutil dédié à copie et à la copie et à l'archivage des fichiers et dossiers
import shutil
#Import du module shutil dédié au temps (date et heure)
import datetime

#Déclaration du variable de la date du jour
t = datetime.date.today()

""" Création de la fonction au non de make_archive qui consistera à archiver un fichier 
    un fichier à partir d'un repertoire vers un autre"""

def make_archive(source, destination):
    base = os.path.basename(destination)
    name = base.split('.')[0]
    format = base.split('.')[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    shutil.make_archive(name, format, archive_from, archive_to)
    shutil.move('%s.%s'%(name,format), destination)

"""appele du fonction ci-dessous appliquer le variable 't' qui consistera 
  à intégrer la date du jour au nom du fichier archiver
  par exemple YYYY/MM/DD_backup.zip"""
  
make_archive('/bac/backup', '/bac/%s_backup.zip' % t)
