#Import du module smtplib dédié à l'envoi et à la reception des email
import smtplib

#Connéction au compte expéditeur
mail_user = 'compte@site.fr'  

#Mot de passe compte expéditeur
mail_password = '$$$$$$$$'

#Variable expéditeur
sent_from = mail_user  

#adresse du destinataire
to = ['compte@site.com']  

#Sujet du message
subject = 'Aucune sauvegarde effectuer'  

#Contenu du message
body = 'Bonjour,\nAucune saugarde effectuer.\nCordialement'

email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)

#Fonction et paramétres de connéction et d'envoi de l'email
server = smtplib.SMTP_SSL('smtp.site.fr', 465)
server.ehlo()

#Connéxion au serveur de messagerie
server.login(mail_user, mail_password)

#envoi de l'email
server.sendmail(sent_from, to, email_text)

#Déconnexion au serveur
server.close()
