import os
import json
import inspect
import time


blue_color = "\033[34m"
white_color = "\33[37m"
yellow_color = "\33[33m"
green_color = "\33[32m"
valid_emote = '\U00002705'
refuse_emote = '\U0000274C'

affichage_start = f"""
{blue_color} ---------------------------------
|                                 |
|   {white_color}Bienvenue dans le programme   {blue_color}|
|  {white_color}de gestion de liste de course  {blue_color}|         
|                                 |
 ---------------------------------{white_color}
"""

affichage_end = f"""
{blue_color} ----------------------------------------------
|                                              |
|          {white_color}Merci d'avoir utilisé ce            {blue_color}|
|  {white_color}programme pour gérer votre liste de course  {blue_color}|         
|                                              |
|                                              |
|                  {white_color}A bientôt                   {blue_color}|
 ----------------------------------------------{white_color}
"""

affichage = f"""


{blue_color} ---------------------------------
|                                 |
| {white_color}Choisissez une option:          {blue_color}|
|                                 |
|\t{white_color}1: Ajouter un élément     {blue_color}|
|\t{white_color}2: Enlever un élément     {blue_color}|
|\t{white_color}3: Afficher la liste      {blue_color}|
|\t{white_color}4: Vider la liste         {blue_color}|
|\t{white_color}5: Terminer               {blue_color}|
|                                 |
 ---------------------------------{white_color}
"""

affichage_add_item = f"""
 {blue_color}--------------------------------------------
|                                            |
| {white_color}Écrivez l'élément que vous voulez rajouter {blue_color}|
|                                            |
|  {white_color}Si vous voulez entrer plusieurs éléments  {blue_color}|
|      {white_color}séparer les d'une virgule ','         {blue_color}|
|                                            |
|                                            |
|                                            |
|     Pour revenir au menu taper "menu"      |
 --------------------------------------------{white_color}
"""

affichage_remove_item = f"""
 {yellow_color}--------------------------------------------
|                                            |
| {white_color}Écrivez l'élément que vous voulez enlever  {yellow_color}|
|                                            |
|  {white_color}Si vous voulez enlever plusieurs éléments {yellow_color}|
|      {white_color}séparer les d'une virgule ','         {yellow_color}|
|                                            |
|                                            |
|                                            |
|     Pour revenir au menu taper "menu"      |
 --------------------------------------------{white_color}
"""

folder_path = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(folder_path, "liste.json")
# print(folder_path)
# print(json_file_path)

if os.path.exists(json_file_path):
    fd = open(json_file_path, "r")
    # liste_de_courses = fd.read().splitlines
    liste_de_courses = json.load(fd)
    fd.close()
else:
    liste_de_courses = []

print(affichage_start)
option = "0"
while option != "5":
    option = input(affichage + "Entrer votre option: ")
    if ' ' in option:
            option = option.replace(' ', "")
    if not option.isdigit():
        print("Option no correcte, merci de rentrer une option valide")
        continue
    else:
        if option == "1":
            os.system('clear')
            print(affichage_add_item)
            if liste_de_courses:
                print(inspect.cleandoc(f"""{blue_color}|   {white_color}Vos éléments actuels dans votre liste :  {blue_color}|
                {blue_color}|                                            |{white_color}"""))
                for i in range(len(liste_de_courses)):
                    len_word = len(liste_de_courses[i])
                    print(f"{blue_color}|       {white_color}- {liste_de_courses[i]}", end='')
                    while len_word < 35:
                        print(" ", end='')
                        len_word += 1
                    print(f"{blue_color}|")
                print(inspect.cleandoc(f"""{blue_color}|                                            |
                --------------------------------------------{white_color}"""))
            else:
                print(inspect.cleandoc(f"""{blue_color}|                                            |
                |     {white_color}La liste ne contien aucun élément      {blue_color}|
                |               {white_color}pour le moment               {blue_color}|
                |                                            |
                |                                            |
                 --------------------------------------------{white_color}"""))
            item_add = input(": ")
            if item_add == "menu":
                os.system('clear')
                continue
            if ',' in item_add:
                item_add =  item_add.split(',')
                print(inspect.cleandoc(f"""{blue_color} --------------------------------------------
                |                                            |"""))
                for i in range(len(item_add)):
                    if ' ' in item_add[i]:
                        item_add[i] = item_add[i].replace(' ', "")
                    liste_de_courses.append(item_add[i])
                    print(inspect.cleandoc(f"""| {valid_emote}  {white_color}Élément rajouté: {item_add[i]}{blue_color}"""), end='')
                    len_word = len(item_add[i]) + 21
                    while len_word < 44:
                        print(" ", end='')
                        len_word += 1
                    print("|")
                print(inspect.cleandoc(f"""|                                            |
                 --------------------------------------------{white_color}"""))
            else:
                liste_de_courses.append(item_add)
                print(inspect.cleandoc(f"""{blue_color} --------------------------------------------
                |                                            |
                | {valid_emote}  {white_color}Élément rajouté: {item_add}{blue_color}"""), end='')
                len_word = len(item_add) + 21
                while len_word < 44:
                    print(" ", end='')
                    len_word += 1
                print("|")
                print(inspect.cleandoc(f"""{blue_color}|                                            |
                 --------------------------------------------{white_color}"""))   
            time.sleep(10)
            os.system('clear')
            continue
        elif option == "2":
            os.system('clear')
            print(affichage_remove_item)
            if liste_de_courses:
                print(inspect.cleandoc(f"""{yellow_color}|   {white_color}Vos éléments actuels dans votre liste :  {yellow_color}|
                {yellow_color}|                                            |{white_color}"""))
                for i in range(len(liste_de_courses)):
                    len_word = len(liste_de_courses[i])
                    print(f"{yellow_color}|       {white_color}- {liste_de_courses[i]}", end='')
                    while len_word != 35:
                        print(" ", end='')
                        len_word += 1
                    print(f"{yellow_color}|")
                print(inspect.cleandoc(f"""{yellow_color}|                                            |
                --------------------------------------------{white_color}"""))
            else:
                print(inspect.cleandoc(f"""{yellow_color}|                                            |
                |     {white_color}La liste ne contien aucun élément      {yellow_color}|
                |               {white_color}pour le moment               {yellow_color}|
                |                                            |
                |                                            |
                 --------------------------------------------{white_color}"""))
            item_remove = input(": ")
            if item_remove == "menu":
                os.system('clear')
                continue
            if ',' in item_remove:
                item_remove =  item_remove.split(',')
                for i in range(len(item_remove)):
                    if ' ' in item_remove[i]:
                        item_remove[i] = item_remove[i].replace(' ', "")
                    if item_remove[i] in liste_de_courses:
                        liste_de_courses.remove(item_remove[i])
            else:
                if item_remove in liste_de_courses:
                    liste_de_courses.remove(item_remove)
            time.sleep(1)
            os.system('clear')
        elif option == "3":
            os.system('clear')
            if liste_de_courses:
                print(inspect.cleandoc(f""" {green_color} --------------------------------------------
                {green_color}|   {white_color}Vos éléments actuels dans votre liste :  {green_color}|
                {green_color}|                                            |{white_color}"""))
                for i in range(len(liste_de_courses)):
                    len_word = len(liste_de_courses[i])
                    print(f"{green_color}|       {white_color}- {liste_de_courses[i]}", end='')
                    while len_word != 35:
                        print(" ", end='')
                        len_word += 1
                    print(f"{green_color}|")
                print(inspect.cleandoc(f"""{green_color}|                                            |
                |                                            |
                |                                            |
                |     {white_color}Pour revenir au menu taper "menu"      {green_color}|
                --------------------------------------------{white_color}"""))
            else:
                print(inspect.cleandoc(f""" {green_color} --------------------------------------------
                |                                            |
                |     {white_color}La liste ne contien aucun élément.     {green_color}|
                |                                            |
                |     {white_color}Pour revenir au menu taper "menu"      {green_color}|
                 --------------------------------------------{white_color}"""))
            view_elem = input(": ")
            if view_elem == "menu":
                os.system('clear')
                continue
            time.sleep(1)
            os.system('clear')
        elif option == "4":
            os.system('clear')
            liste_de_courses.clear()
            print(inspect.cleandoc(f"""{blue_color} --------------------------------------------
                |                                            |
                |           {white_color}La liste a été supprimé.         {blue_color}|
                |                                            |
                |    {white_color}Retour au menu dans quelque instant     {blue_color}|
                 --------------------------------------------"""))
            time.sleep(2)
            os.system('clear')
os.system('clear')
print(affichage_end)
fd = open(json_file_path, "w")
json.dump(liste_de_courses, fd, indent=4)
fd.close()
        