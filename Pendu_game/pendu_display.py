RED_COLOR = "\33[31m"
GREEN_COLOR = "\33[32m"
YELLOW_COLOR = "\33[33m"
BLUE_COLOR = "\33[34m"
PURPLE_COLOR = "\33[35m"
LIGHT_BLUE_COLOR = "\33[36m"
WHITE_COLOR = "\33[37m"
EMOJI_DIFFICULTY = "📊"
EMOJI_WARNING = "⚠️"


header_display = f"""
 {LIGHT_BLUE_COLOR}
██████╗ ███████╗███╗   ██╗██████╗ ██╗   ██╗     ██████╗  █████╗ ███╗   ███╗███████╗
██╔══██╗██╔════╝████╗  ██║██╔══██╗██║   ██║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██████╔╝█████╗  ██╔██╗ ██║██║  ██║██║   ██║    ██║  ███╗███████║██╔████╔██║█████╗  
██╔═══╝ ██╔══╝  ██║╚██╗██║██║  ██║██║   ██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
██║     ███████╗██║ ╚████║██████╔╝╚██████╔╝    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═╝     ╚══════╝╚═╝  ╚═══╝╚═════╝  ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                                                                       
                                                             {WHITE_COLOR}by jean-xavierr"""      

header_display_old_version = f"""
 {LIGHT_BLUE_COLOR} _____               _          _____          __  __ ______ 
 |  __ \             | |        / ____|   /\   |  \/  |  ____|
 | |__) |__ _ __   __| |_   _  | |  __   /  \  | \  / | |__   
 |  ___/ _ \ '_ \ / _` | | | | | | |_ | / /\ \ | |\/| |  __|  
 | |  |  __/ | | | (_| | |_| | | |__| |/ ____ \| |  | | |____ 
 |_|   \___|_| |_|\__,_|\__,_|  \_____/_/    \_\_|  |_|______|
                                                              
                                                             {WHITE_COLOR}by jean-xavierr"""
                                                     

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
   ||/        O    {RED_COLOR}Aie !{WHITE_COLOR}
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
   ||/        O/   {RED_COLOR}Qu'est-ce-que vous regardez comme ça !{WHITE_COLOR}
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
   ||/        O    {LIGHT_BLUE_COLOR}Lisez plutôt les règles du jeu{WHITE_COLOR}
   ||        /|\\       {LIGHT_BLUE_COLOR}Et détacher moi !{WHITE_COLOR}
   ||        /|
   ||
  /||
 //||
===========
"""]

rules_display = f"""
Le but du {LIGHT_BLUE_COLOR}jeu Pendu {WHITE_COLOR}est de deviner un mot en proposant des lettres.
Mais vous avez droit à un nombre limité d'erreur !
Si vous atteignez la limite des erreurs, vous avez {RED_COLOR}perdu{WHITE_COLOR}.
Si vous trouvez le mot avant d'atteindre la limite vous avez {GREEN_COLOR}gagné !{WHITE_COLOR} 
"""

difficulty_level_display = f"""



    ||    Choissisez votre Niveau de difficulté  {EMOJI_DIFFICULTY}  ||

    {GREEN_COLOR}niveau 1{WHITE_COLOR}: Débutant vous avez le droit à la première et la dernière lettre du mot à deviner pour vous aider.
    {BLUE_COLOR}niveau 2{WHITE_COLOR}: Intermédiaire vous n'avez plus aucune lettre pour vous aider.
    {RED_COLOR}niveau 3{WHITE_COLOR}: Expert vous n'avez plus aucune lettre pour vous aider et vous devez trouver le mot en moins de 3min !
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
   ||/        O  {WHITE_COLOR}Arrrrf{WHITE_COLOR}
   ||        /|\\
   ||        /|
   ||
  /||
 //||
===========""",f"""

   ,==========Y===
   ||  /      |
   || /       |
   ||/       \O/  {RED_COLOR}C'était pas dur pourtant{WHITE_COLOR}
   ||         |
   ||        /|
   ||
  /||
 //||
===========""", f"""

   ,==========Y===
   ||  /      |
   || /       |
   ||/       _O__  {RED_COLOR}Peut-être que tu auras plus de chance la prochaine fois{WHITE_COLOR}
   ||        \|
   ||        /|
   ||
  /||
 //||
==========="""]

game_over_display = f"""{RED_COLOR}


   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                      {WHITE_COLOR}"""


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
  /||                                \O  {GREEN_COLOR}Bien joué tu as trouvé le mot !{WHITE_COLOR}
 //||                                 |\\
============_________________________/ \\""",]

win_display = f"""{GREEN_COLOR}


 __          ___                         _ 
 \ \        / (_)                       | |
  \ \  /\  / / _ _ __  _ __   ___ _ __  | |
   \ \/  \/ / | | '_ \| '_ \ / _ \ '__| | |
    \  /\  /  | | | | | | | |  __/ |    |_|
     \/  \/   |_|_| |_|_| |_|\___|_|    (_)
                                                {WHITE_COLOR}"""


end_display = f"""
  {LIGHT_BLUE_COLOR} /= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =\\
  /= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =\\
 ||                                                               ||
 || {WHITE_COLOR} _____               _          _____          __  __ ______  {LIGHT_BLUE_COLOR}||
 || {WHITE_COLOR}|  __ \             | |        / ____|   /\   |  \/  |  ____| {LIGHT_BLUE_COLOR}||
 || {WHITE_COLOR}|  __) |__ _ __   __| |_   _  | |  __   /  \  | \  / | |__    {LIGHT_BLUE_COLOR}||
 || {WHITE_COLOR}|  ___/ _ \ '_ \ / _` | | | | | | |_ | / /\ \ | |\/| |  __|   {LIGHT_BLUE_COLOR}||
 || {WHITE_COLOR}| |  |  __/ | | | (_| | |_| | | |__| |/ ____ \| |  | | |____  {LIGHT_BLUE_COLOR}||
 || {WHITE_COLOR}|_|   \___|_| |_|\__,_|\__,_|  \_____/_/    \_\_|  |_|______| {LIGHT_BLUE_COLOR}||
 ||                                                               ||
 ||                                                               ||
 ||                                                               ||
 ||                  {WHITE_COLOR}Merci d'avoir jouer au Pendu                 {LIGHT_BLUE_COLOR}||
 ||               {WHITE_COLOR}N'hésitez pas à me faire votre retour           {LIGHT_BLUE_COLOR}||
 ||                                                               ||
 ||                                                               ||
 ||                                                               ||
 ||       {WHITE_COLOR},==========Y===                                         {LIGHT_BLUE_COLOR}||
 ||       {WHITE_COLOR}||  /      |                                            {LIGHT_BLUE_COLOR}||
 ||       {WHITE_COLOR}|| /       |                                            {LIGHT_BLUE_COLOR}||
 ||       {WHITE_COLOR}||/        O                                            {LIGHT_BLUE_COLOR}||
 ||       {WHITE_COLOR}||        /|\\                                           {LIGHT_BLUE_COLOR}||
 ||       {WHITE_COLOR}||        /|                                            {LIGHT_BLUE_COLOR}||
 ||       {WHITE_COLOR}||                                                      {LIGHT_BLUE_COLOR}||
 ||      {WHITE_COLOR}/||                                                      {LIGHT_BLUE_COLOR}||
 ||     {WHITE_COLOR}//||                                                      {LIGHT_BLUE_COLOR}||  
 ||    {WHITE_COLOR}===========                                                {LIGHT_BLUE_COLOR}||
 ||          {YELLOW_COLOR}github: {WHITE_COLOR}https://github.com/Jean-xavierr              {LIGHT_BLUE_COLOR}||
 ||                                                               {LIGHT_BLUE_COLOR}||
 ||                       {WHITE_COLOR}A bientôt                               {LIGHT_BLUE_COLOR}||
  \= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =/
   \= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =/
"""