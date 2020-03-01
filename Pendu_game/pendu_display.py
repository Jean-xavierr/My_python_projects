red_color = "\33[31m"
green_color = "\33[32m"
yellow_color = "\33[33m"
blue_color = "\33[34m"
purple_color = "\33[35m"
light_blue_color = "\33[36m"
white_color = "\33[37m"
emoji_difficulty = "📊"
emoji_warning = "⚠️"


header_display = f"""
 {light_blue_color} _____               _          _____          __  __ ______ 
 |  __ \             | |        / ____|   /\   |  \/  |  ____|
 | |__) |__ _ __   __| |_   _  | |  __   /  \  | \  / | |__   
 |  ___/ _ \ '_ \ / _` | | | | | | |_ | / /\ \ | |\/| |  __|  
 | |  |  __/ | | | (_| | |_| | | |__| |/ ____ \| |  | | |____ 
 |_|   \___|_| |_|\__,_|\__,_|  \_____/_/    \_\_|  |_|______|
                                                              
                                                             {white_color}by jean-xavierr"""

start_display = [f"""          

   ,==========Y===
   ||  /      |
   || /       |
   ||/        O 
   ||        /|\\
   ||        /|
   ||
  /||
 //||
===========
""", f"""          

   ,==========Y===
   ||  /      |
   || /       |
   ||/        O    {red_color}Aie !{white_color}
   ||        /|\\
   ||        /|
   ||
  /||
 //||
===========
""", f"""          

   ,==========Y===
   ||  /      |
   || /       |
   ||/        O/   {red_color}Qu'est-ce-que vous regardez comme ça !{white_color}
   ||        /|
   ||        / \\
   ||
  /||
 //||
===========
""", f"""          

   ,==========Y===
   ||  /      |
   || /       |
   ||/        O    {light_blue_color}Lisez plutôt les règles du jeu{white_color}
   ||        /|\\       {light_blue_color}Et détacher moi !{white_color}
   ||        /|
   ||
  /||
 //||
===========
"""]

rules_display = f"""
Le but du {light_blue_color}jeu Pendu {white_color}est de deviner un mot en proposant des lettres.
Mais vous avez droit à un nombre limité d'erreur !
Si vous atteignez la limite des erreurs, vous avez {red_color}perdu{white_color}.
Si vous trouvez le mot avant d'atteindre la limite vous avez {green_color}gagné !{white_color} 
"""

difficulty_level_display = f"""



    ||    Choissisez votre Niveau de difficulté  {emoji_difficulty}  ||

    {green_color}niveau 1{white_color}: Débutant vous avez le droit à la première et la dernière lettre du mot à deviner pour vous aider.
    {blue_color}niveau 2{white_color}: Intermédiaire vous n'avez plus aucune lettre pour vous aider.
    {red_color}niveau 3{white_color}: Expert vous n'avez plus aucune lettre pour vous aider et vous devez trouver le mot en moins de 3min !
"""

pendu_display = [f"""

   ,==========Y===
   ||  /      
   || /       
   ||/         
   ||        
   ||        
   ||
  /||
 //||
===========""", f"""

   ,==========Y===
   ||  /      |
   || /       
   ||/        
   ||        
   ||        
   ||
  /||
 //||
===========""", f"""

   ,==========Y===
   ||  /      |
   || /       |
   ||/         
   ||        
   ||        
   ||
  /||
 //||
===========""", f"""

   ,==========Y===
   ||  /      |
   || /       |
   ||/        O 
   ||        
   ||        
   ||
  /||
 //||
===========""", f"""

   ,==========Y===
   ||  /      |
   || /       |
   ||/        O 
   ||         |
   ||        
   ||
  /||
 //||
===========""", f"""

   ,==========Y===
   ||  /      |
   || /       |
   ||/        O 
   ||        /|
   ||        
   ||
  /||
 //||
===========""", f"""

   ,==========Y===
   ||  /      |
   || /       |
   ||/        O 
   ||        /|\\
   ||        
   ||
  /||
 //||
===========""", f"""

   ,==========Y===
   ||  /      |
   || /       |
   ||/        O 
   ||        /|\\
   ||        /
   ||
  /||
 //||
===========""", f"""

   ,==========Y===
   ||  /      |
   || /       |
   ||/        O 
   ||        /|\\
   ||        /|
   ||
  /||
 //||
==========="""]

pendu_game_over_display = [f"""

   ,==========Y===
   ||  /      |
   || /       |
   ||/        O  {white_color}Arrrrf{white_color}
   ||        /|\\
   ||        /|
   ||
  /||
 //||
===========""",f"""

   ,==========Y===
   ||  /      |
   || /       |
   ||/       \O/  {red_color}C'était pas dur pourtant{white_color}
   ||         |
   ||        /|
   ||
  /||
 //||
===========""", f"""

   ,==========Y===
   ||  /      |
   || /       |
   ||/       _O__  {red_color}Peut-être que tu auras plus de chance la prochaine fois{white_color}
   ||        \|
   ||        /|
   ||
  /||
 //||
==========="""]

game_over_display = f"""{red_color}


   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                      {white_color}"""


pendu_win_display = [f"""
   ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        
   ||        
   ||
  /||                                 O
 //||                                /|\\
============_________________________/ \\""", f"""
   ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        
   ||        
   ||
  /||                                \O  {green_color}Bien joué tu as trouvé le mot !{white_color}
 //||                                 |\\
============_________________________/ \\""",]

win_display = f"""{green_color}


 __          ___                         _ 
 \ \        / (_)                       | |
  \ \  /\  / / _ _ __  _ __   ___ _ __  | |
   \ \/  \/ / | | '_ \| '_ \ / _ \ '__| | |
    \  /\  /  | | | | | | | |  __/ |    |_|
     \/  \/   |_|_| |_|_| |_|\___|_|    (_)
                                                {white_color}"""


end_display = f"""
  {light_blue_color} /= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =\\
  /= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =\\
 ||                                                               ||
 || {white_color} _____               _          _____          __  __ ______  {light_blue_color}||
 || {white_color}|  __ \             | |        / ____|   /\   |  \/  |  ____| {light_blue_color}||
 || {white_color}|  __) |__ _ __   __| |_   _  | |  __   /  \  | \  / | |__    {light_blue_color}||
 || {white_color}|  ___/ _ \ '_ \ / _` | | | | | | |_ | / /\ \ | |\/| |  __|   {light_blue_color}||
 || {white_color}| |  |  __/ | | | (_| | |_| | | |__| |/ ____ \| |  | | |____  {light_blue_color}||
 || {white_color}|_|   \___|_| |_|\__,_|\__,_|  \_____/_/    \_\_|  |_|______| {light_blue_color}||
 ||                                                               ||
 ||                                                               ||
 ||                                                               ||
 ||                  {white_color}Merci d'avoir jouer au Pendu                 {light_blue_color}||
 ||               {white_color}N'hésitez pas à me faire votre retour           {light_blue_color}||
 ||                                                               ||
 ||                                                               ||
 ||                                                               ||
 ||       {white_color},==========Y===                                         {light_blue_color}||
 ||       {white_color}||  /      |                                            {light_blue_color}||
 ||       {white_color}|| /       |                                            {light_blue_color}||
 ||       {white_color}||/        O                                            {light_blue_color}||
 ||       {white_color}||        /|\\                                           {light_blue_color}||
 ||       {white_color}||        /|                                            {light_blue_color}||
 ||       {white_color}||                                                      {light_blue_color}||
 ||      {white_color}/||                                                      {light_blue_color}||
 ||     {white_color}//||                                                      {light_blue_color}||  
 ||    {white_color}===========                                                {light_blue_color}||
 ||          {yellow_color}github: {white_color}https://github.com/Jean-xavierr              {light_blue_color}||
 ||                                                               {light_blue_color}||
 ||                       {white_color}A bientôt                               {light_blue_color}||
  \= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =/
   \= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =/
"""