import sys

invalid_input = True
invalid_inputCHOICE = True
invalid_inputCHOICE2 = True

def debut():
    print("\033[34m\033[1mDiscord Python Bot Editor V.1 created by ALEXDIEU !\033[0m")
    print("\033[41m\033[22mPlease choose an option : \033[0m")
    print("\033[33m\033[2m1.create a new bot\033[0m ")
    print("\033[33m\033[2m2.edit a bot(soon)\033[0m ")
    print("\033[33m\033[2m3.exit\033[0m ")


def pick_one():
    global f
    invalid_input = False
    namefile = input("okay , what should be the main file bot title ? \n")
    PREFIX = input("Before starting , what should be the bot prefix ? \n")
    token = input('What is the bot token ? \n')
    start = f"import discord\nfrom io import BytesIO\nfrom discord.ext import commands\nimport asyncio\nimport aiohttp\nfrom discord.ext.commands import Bot\nimport os\nimport platform\nfrom platform import python_version\n\n\nbot = commands.Bot(command_prefix='{PREFIX}')\nBLACKLIST = []\nTOKEN = '{token}'"
    with open(namefile + ".py", 'w') as f:
        f.write('{}'.format(start))
        print('Bot succesfully created ! Now let\'s do the starting events !')
        startEvent()
        choice2()

def startEvent():
    global f
    invalid_inputCHOICE = False
    personnal = input('Now , would you like to print a personnal message when the bot is ready ?(That will print it in your python console , it\'s recommended you keep the default(say no to keep the default) wich is : \nregistred as (bot name)\nDiscord.py version = (version)\nPython Version (version) \nRunning on (OS)\nSo ?  ')
    if personnal == 'yes':
        print('The bot name is metionned at the end of your message !')
        OnreadyMsgP = input(
            f'Please enter your new message wich the bot will display in the console when it is ready (if you want to write this carcter : \' please do \ then \' thanks (if not your bot will not working  thanks !) :')
        OnreadyMsg = (f'\n@bot.event\nasync def on_ready():\n    print(\'{OnreadyMsgP}\'+ bot.user.name )\n')
        f.write('{}'.format(OnreadyMsg))
    if personnal == 'no':
        print('On ready message set as default !')
        OnreadyMsg = ('\n@bot.event\nasync def on_ready():\n    print(\'Registred as \' + bot.user.name)\n    print(\"API version of discord.py :\"), discord.__version__\n    print(\"Python version :\", platform.python_version())\n    print(\"Running on :\", platform.system(), platform.release(), \"(\" + os.name + \")\")\n    print(\'-------------------\')')
        f.write('{}'.format(OnreadyMsg))
    else:
        print('Please answer by yes or no !')
        invalid_inputCHOICE = False
        startEvent()


def start() :
    debut()

    in_pick = input("\033[31m\033[1mYour choice : \033[0m")

    if in_pick == '1':
       pick_one()
    else:
        print('Answer by yes or no please !')

    if in_pick == '2':
        print("soon , if you want it now , come help us on my github !")

    if in_pick == '3':
        print('Created by Alexdieu')
        invalid_input = False
        sys.exit()
    else:
        print('This Option doesn\'t exist (may be yet) sorry')

def choice2():
    global f
    invalid_inputCHOICE2 = False
    choice1 = input('Now what do you want see next ? events , commands ,plugins or exit ?(commands written by community or Alexdieu(Credits of the plugin at the end)\nPLEASE ANSWER by the choices proposed : events , commands ,exit(finish the file and compile it) or plugins(integred functiinalities or Precommands) !\nYour answer :')
    if choice1 == 'event':
        print('events')
        choiceEV = input('What event do you want ?\n1.On member join \n2.On reaction add\n3.')

    if choice1 == 'commands':
        print('commands')
        f.write('WORKING')
    if choice1 == 'plugins':
        print('plugins')
        f.write('WORKING')
    if choice1 == ('exit'):
        print('credits: Alexdieu . Maybe Others with the time ;)')
        END = '\n\nbot.run(TOKEN)'
        f.write('{}'.format(END))
        invalid_input = True
    else:
        print('PLEASE ANSWER by the choices proposed : events , commands , exit or plugins !')
        invalid_inputCHOICE2 = True




while invalid_input :
    start()
while invalid_inputCHOICE :
    startEvent()
while invalid_inputCHOICE2:
    choice2()
