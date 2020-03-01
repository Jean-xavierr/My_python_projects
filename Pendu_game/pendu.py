import json
import os
import sys
import time
import random
import logging
from pendu_display import * 

list_word = "agneau aigle albatros alligator alpaga anaconda ane antilope araignee autruche babouin baleine belette beluga biche bison blaireau boa boeuf bonobo brebis buffle cachalot campagnol canard capucin capybara caribou carpe castor cerf chacal chameau chamois chat chaus cheval chevre chevreuil chien chimpanze chinchilla chouette cigogne cobaye coccinelle cochon coq coyote crabe crocodile cygne daim dauphin dinde dindon dingo drill dromadaire ecureuil elan elephant emeu epaulard escargot espadon eyra faisan faon faucon fennec fouine fourmilier furet gaufre gaur gazelle gelada genette gerbille gerboise gibbon girafe glouton gnou gorille grenouille grizzly grue guanaco guepard guigna hamster herisson hermine heron hibou hippocampe hippopotame hirondelle hyene ibis iguane impala isard isatis jaguar kangourou kiwi koala kodiak koudou lamantin lama lapin lemming lemurien leopard lerot lezard lievre lion loir lophophore lori loup loutre lycaon lynx manchot mandrill mangouste manul mara marmotte marsouin martre mesange morse mouette moufette mouflon mouton mulet mulot musaraigne muscardin naja nandou narval nasique nason noctule notou numbat ocelot octodon oie okapi once opossum oran ornithorynque orque orycterope oryx otarie ouistiti ours panda pangolin panthere paon paresseux pecaris pekan pelican perroquet phacochere phoque pie pika pingouin pipistrelle pogona poisson polatouche poney poule poulpe poussin puma putois python quetzal quiscale quokka ragondin rat ratufa renard requin rhesus rhinoceros roussette salamandre sanglier serpent serval singe souris suricate tamandua tamanoir tamarin tamia tapir tarsier tatou taupe taureau tigre tortue toucan trigonocephale unau urubu vache varan vautour veau vipere vison wallabi wapiti watussi wombat xerus yack zebre zebrule zebu zibeline zorille".split()

def ft_clear_terminal_sleep(duration):
    time.sleep(duration)
    os.system('clear')

def ft_start_display():
    ft_clear_terminal_sleep(0)
    print(header_display + start_display[0])
    ft_clear_terminal_sleep(1)
    print(header_display + start_display[1])
    ft_clear_terminal_sleep(1.5)
    print(header_display + start_display[2])
    ft_clear_terminal_sleep(2.8)
    print(header_display + start_display[3])
    ft_clear_terminal_sleep(2.6)
    print(header_display + start_display[0] + rules_display)
    time.sleep(2)
    input("Appuyer sur enter pour commencer le jeu : ")

def ft_difficulty_level():
    ft_clear_terminal_sleep(0)
    print(header_display + difficulty_level_display)
    return (input("Entrer votre niveau de difficulté (1, 2, 3) : "))

def ft_letters_tried(i, all_letters_try):
    if i != 0:
        print("Lettre essayé : ", end="")
        n = len(all_letters_try)
        for word in all_letters_try:
            print(word, end="")
            if n > 1:
                print(', ', end="")
            n -= 1

def ft_game_display(i, word_to_find, number_tries, all_letters_try):
    ft_clear_terminal_sleep(0)
    print(header_display + pendu_display[i], end="")
    print("\tMot à trouver : " + " ".join(word_to_find), end="")
    print(f"\t\tnombre d'essaie restant {number_tries - i}")
    ft_letters_tried(i, all_letters_try)

def ft_game_over(word, all_letters_try):
    i = 0
    while i != 3:
        ft_clear_terminal_sleep(0)
        print(header_display + pendu_game_over_display[i], end="")
        print(f"\tLe mot à trouver été : {light_blue_color}" + word + f"{white_color}")
        ft_letters_tried(1, all_letters_try)
        sys.stdout.flush()
        time.sleep(2)
        i += 1
    print(game_over_display)

def ft_win_game(i, word, all_letters_try):
    i = 0
    while i != 2:
        ft_clear_terminal_sleep(0)
        print(header_display + pendu_win_display[i], end="")
        print(f"\tLe mot à trouver été : {light_blue_color}" + word + f"{white_color}")
        ft_letters_tried(1, all_letters_try)
        sys.stdout.flush()
        time.sleep(1)
        i += 1
    print(win_display)

def ft_retry():
    retry = input("\n\tVoulez-vous rejouer ? (oui/non) :")
    if retry == "oui" or retry == 'o':
        ft_start_game(ft_difficulty_level())
    else:
        ft_clear_terminal_sleep(0)
        print(end_display)

def ft_start_game(difficulty_level):
    ft_clear_terminal_sleep(0)
    #word = list_word[random.randint(0,243)]
    word = "rat"
    word_to_find = []
    letter_try = None
    all_letters_try = []
    for letter in word:
        word_to_find.append('_')
    word_found = False
    valid_letter = False
    find_letter = False
    number_tries = 8
    i = 0
    while not word_found:
        ft_game_display(i, word_to_find, number_tries, all_letters_try)
        print(word)
        while not valid_letter:
            letter_try = input("\nEntrer une lettre : ")
            if letter_try in all_letters_try:
                ft_game_display(i, word_to_find, number_tries, all_letters_try)
                print(f"\n\n{emoji_warning}{yellow_color}   Lettre déjà essayé, veuillez en choisir une autre{white_color}")
            elif not letter_try.isalpha() or len(letter_try) != 1:
                ft_game_display(i, word_to_find, number_tries, all_letters_try)
                print(f"\n\n{emoji_warning}{yellow_color}   Entrer seulement une lettre{white_color}")
            else:
                valid_letter = True
        valid_letter = False
        all_letters_try.append(letter_try)
        i += 1
        for index, letter in enumerate(word):
            if letter == letter_try:
                word_to_find[index] = letter_try
                find_letter = True
        if find_letter:
            i -= 1
            find_letter = False
        if "".join(word_to_find) == word:
            ft_win_game(i, word, all_letters_try)
            word_found = True
        if number_tries - i == 0:
            ft_game_over(word, all_letters_try)
            break
    
#ft_start_display()
difficulty_level = ft_difficulty_level()
ft_start_game(difficulty_level)
ft_retry()