Projet - Sauve

Ce programme consiste à effectuer une sauvegarde quotidiennement. La sauvegarde ne s'effectue que lorsque le contenu du fichier 
de configuration, est diffèrent à celui du fichier d'origine déjà sauvegarder dans un répertoire de sauvegarde diffèrent à celui 
du programme du fichier en question. 
L'opération de sauvegarde se déroule comme suit :
1.	Le programme vérifie d'abord si les deux fichiers sont différents :
•	Si tel est le cas, le programme sauvegarde le fichier de configuration.
•	Crée un fichier ZIP et place l'ancien fichier dans le zip dont le nom sera précédé par un nombre qui va s'accroitre au fil des 
    sauvegardes
•	Envoie un message à l'administrateur pour l'informer qu'une nouvelle sauvegarde vient de s'effectuer.

2.	Dans le cas contraire, le programme envoi tout de même un email à l'administrateur pour lui informer qu'aucune sauvegarde 
    n'a été effectué car aucune modification du contenu du fichier n'a été constaté
    
Le programme existe en plusieurs version :
•	Le premier qui porte le nom de « sauve 1.0 » consiste seulement à effectuer une sauvegarde si le fichier source est différent
    à celui de destination déjà sauvegardée.
•	Le deuxième « sauve 1.1 » consiste à effectuer une sauvegarde si le fichier source est différent à celui de destination déjà 
    sauvegardé et place l’ancien fichier sauvegardé dans un fichier zip qui portera comme nom le nom de la date de création du zip
    plus le suffixe « _backup ».
•	Le troisième « sauve 1.2 » fait ce que les deux précédentes versions font et envoi un email si une sauvegarde a été effectuer
    ou non.
