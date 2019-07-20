#Sauve 1.1
import os
import filecmp
import shutil
import datetime

t = datetime.date.today()

def make_archive(source, destination):
    base = os.path.basename(destination)
    name = base.split('.')[0]
    format = base.split('.')[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    shutil.make_archive(name, format, archive_from, archive_to)
    shutil.move('%s.%s'%(name,format), destination)

if filecmp.cmp('/etc/network/interfaces' ,'/bac/backup' ):
    print('Fichier non modifier donc aucune sauvegarde')

else:
    make_archive('/bac/backup', '/bac/%s_backup.zip' % t)
    shutil.copyfile('/etc/network/interfaces', '/bac/backup')
    print('Fichier sauvegarder et ancienne sauvegarde archiver')
