import sys

invalid_input = True
invalid_inputCHOICE = True
invalid_inputCHOICE2 = True


def debut():
    print("Discord Python Bot Editor V.1.3 created by ALEXDIEU !")
    print("Please choose an option : ")
    print("1.create a new bot")
    print("2.edit a bot(soon)")
    print("3.exit")

def status():
    global f
    print('Here I ask you to define the tasks of the bot (Task is playing with ...)')
    TASK = input('Please enter the first task of the bot(Task = playing with ...):\n')
    TASK1 = input('Please enter the second task of the bot :\n')
    TASK2 = input('Please enter the third task of the bot :\n')
    TASK3 = input('Please enter the fourth(last) task of the bot :\n')
    TASKS = (f'\nasync def status_task():\n    while True:\n        await bot.change_presence(activity=discord.Game(\"{TASK}\"))\n        await asyncio.sleep(10)\n        await bot.change_presence(activity=discord.Game(\"{TASK1}\"))\n        await asyncio.sleep(10)\n        await bot.change_presence(activity=discord.Game(\"{TASK2}\"))\n        await asyncio.sleep(10)\n        await bot.change_presence(activity=discord.Game(\"{TASK3}\"))\n        await asyncio.sleep(10)')
    f.write('{}'.format(TASKS))
    print('succes !')
    startEvent()

def pick_one():
    global f
    global ID
    invalid_input = False
    ID = input('Before all , can you tell me your profil ID(NOT THE BOT!) please ?\n')
    namefile = input("okay , what should be the main file bot title ? \n")
    PREFIX = input("Before starting , what should be the bot prefix ? \n")
    token = input('What is the bot token ? \n')
    start = f'import discord\nfrom io import BytesIO\nfrom discord.ext import commands\nimport asyncio\nimport aiohttp\nfrom discord.ext.commands import Bot\nimport os\nimport platform\nfrom platform import python_version\n\n\nbot = commands.Bot(command_prefix=\'{PREFIX}\')\nOWNER = [{ID}]\nBLACKLIST = []\nTOKEN = \'{token}\''
    with open(namefile + ".py", 'w') as f:
        f.write('{}'.format(start))
        print('Bot succesfully created ! Now let\'s do the starting events !')
        status()


def startEvent():
    global f
    invalid_inputCHOICE = False
    personnal = input('Now , would you like to print a personnal message when the bot is ready ?(That will print it in your python console , it\'s recommended you keep the default(say no to keep the default) wich is : \nregistred as (bot name)\nDiscord.py version = (version)\nPython Version (version) \nRunning on (OS)\nSo ?  ')
    if personnal == 'yes':
        print('The bot name is metionned at the end of your message !')
        OnreadyMsgP = input(f'Please enter your new message wich the bot will display in the console when it is ready (if you want to write this caracter : \' please do \ then \' thanks (if not your bot will not working  thanks !) :')
        OnreadyMsg = (f'\n\n@bot.event\nasync def on_ready():\n    print(\'{OnreadyMsgP}\'+ bot.user.name )\n    print(\'Created by DISCORDBOTMAKER(by alexdieu)\')\n')
        f.write('{}'.format(OnreadyMsg))
        choice2()
    if personnal == 'no':
        print('On ready message set as default !')
        OnreadyMsg = ('\n\n@bot.event\nasync def on_ready():\n    bot.loop.create_task(status_task())\n    print(\'Registred as \' + bot.user.name)\n    print(\'Created by DISCORDBOTMAKER(by alexdieu)\')\n    print(\"API version of discord.py :\"), discord.__version__\n    print(\"Python version :\", platform.python_version())\n    print(\"Running on :\", platform.system(), platform.release(), \"(\" + os.name + \")\")\n    print(\'-------------------\')')
        f.write('{}'.format(OnreadyMsg))
        choice2()
    else:
        print('Please answer by yes or no !')
        invalid_inputCHOICE = False
        startEvent()



def start() :
    debut()

    in_pick = input("Your choice : ")

    if in_pick == '1':
       pick_one()
    else:
        print('Answer by yes or no please !')

    if in_pick == '2':
        print("soon , if you want it now , come help us on my github !")

    if in_pick == '3':
        print('Created by Alexdieu')
        sys.exit()

    else:
        print('This Option doesn\'t exist (may be yet) sorry')

def choice2():
    global f
    invalid_inputCHOICE2 = False
    choice1 = input('Now what do you want see next ? events , commands ,plugins(soon!) or exit(compile the file) ?(commands written by community or Alexdieu(Credits of the plugins at the end)\nPLEASE ANSWER by the choices proposed : events , commands ,exit(finish the file and compile it) or plugins(integred functiinalities or Precommands) !\nYour answer :')
    if choice1 == 'events':
        print('events')
        choiceEV = input('What event do you want ?\n1.On member join \n2.On reaction add\n3.On member leave\nChoice :')
        if choiceEV == '1':
            onmemberjoin()
        if choiceEV == '2':
            print('soon(some bugs still not fixed with this function !)')
            choice2()
        if choiceEV == '3':
            onmemberleft()

    if choice1 == 'commands':
        commands()

    if choice1 == 'plugins' :
        print('plugins(soon!I am working on it :))')
        choice2()
    if choice1 == ('exit'):
        print('credits: Alexdieu . Maybe Others with the time ;)')
        print('Plugins credits : \n -Google for Google translate api !')
        END = '\n\nbot.run(TOKEN)'
        f.write('{}'.format(END))
        f.close()
        start()
    else:
        print('PLEASE ANSWER by the choices proposed : events , commands , exit or plugins !')
        invalid_inputCHOICE2 = True
        choice2()

def commands():
    print('availaibles commands categorys :')
    print('1.personalised commands')
    print('2.moderations commands')
    print('3.Back')
    print('For community commands , it\'s in plugins !')
    commands_choice = input('Your choice : ')

    if commands_choice == '1':
        perso_com()
    if commands_choice == '2':
        print('SOON')
        commands()
    if commands_choice == '3':
        choice2()

def onmemberleft():
    LEFTCHANNEL = input('What is the leaving channel ?(channel ID)\n')
    MSGLEFT = input('What is the leaving message ?(Watch the tutorial on github for  mentions , and server name !)\n')
    Leftmessage = (f'\n@bot.event\nasync def on_member_remove(member):\n    ID = f\'<@{{member.id}}>\'\n    SERVERNAME = member.guild.name\n    print(f\'{{member.id}}, {{member}} left the server!\')\n    channel = bot.get_channel(date[\'leave_channel\'])\n    await channel.send(f\'{MSGLEFT}\')')
    f.write('{}'.format(Leftmessage))

def perso_com():
    global f
    print('personnalised commands !')
    print('Options :')
    print('1.Create a personnalised answer to a personnal command for the bot !')
    print('2.Create an Embed(EMBED CREATOR NOW OUT IN STABLE VERSIONS SINCE V1.3)!')
    print('3.Back')
    CHOICEPERSO = input('Okay , what do you want to do ? \n')

    if CHOICEPERSO == '1':
        NAMECOM = input('What will b the command name ?\n')
        ANSWER1 = input('What will the bot answer \n(see github wiki for https://github.com/alexdieu/DiscordPythonBotMaker/wiki/tutorial syntax) ?\n')
        COMPERSO = (f"\n@bot.command()\nasync def {NAMECOM}(context):\n    AUTHOR = \f'<@{message.author.id}>'\n    SERVERNAME = member.guild.name\n    await context.message.channel.send(\"{ANSWER1}\")")
        f.write('{}'.format(COMPERSO))
        print('succes !')
        perso_com()
    if CHOICEPERSO == '2':
        print('Redirecting ... ')
        Embed()

    if CHOICEPERSO == '3':
        choice2()
    else:
        print('please answer by 1,2 or 3!')
        perso_com()


def onmemberjoin():
    global f
    print('event on member join choosed !')
    print('Did the bot say your message in DM or in the same channel as the person send the message ?(To answer , \nPlease say 1 for DM , \n2.In a specific channel(need the channel ID), \n3.DM and specific channel\n4.back ')
    answer2 = input('Your choice : ')
    if answer2 == '1':
        DMsg = input('\n Use Tutorial : \nTo type \' do \\\' \nYou have to write or copy/paste :\n{ID} to mention member who just joined\n{SERVERNAME} to mention the server !\nAnd **To write in bold** or \ and \' to write \' !\nWhat should be the DM message ?\n')
        DMNEW = (f'\n@bot.event\nasync def on_member_join(member):\n    ID = f\'<@{{member.id}}>\'\n    SERVERNAME = member.guild.name\n    await member.create_dm()\n    await member.dm_channel.send(f\'{DMsg}\')')
        f.write('{}'.format(DMNEW))
        print('succes')
        choice2()
    if answer2 == '2':
        print('Specific channel')
        CHANNELID = input('What is the welcome channel ID ?\n')
        MMSSGG = input('What is the welcome message ?\nTo type \' do \\\' \nTo mention user , please copy/paste {ID} in your message, and to mention server it\'s {SERVERNAME} \n')
        SpecificCHAN = (f'\n@bot.event\nasync def on_member_join(member):\n    print(f\'{{member.id}}, {{member}}Join the server!\')\n    ID = \'<@{{member.id}}>\'\n    SERVERNAME = member.guild.name\n    channel = bot.get_channel(date[\'{CHANNELID}\'])\n    await channel.send(f\'{MMSSGG}\')')
        f.write('{}'.format(SpecificCHAN))
        print('succes')
        choice2()
    if answer2 == '3':
        print('You requested DM + Specific channel')
        CHANELID1 = input('What is the channel ID ?\n')
        CHANNELMSG = input('What is the welcome message ?\nTo type \' do \\\' \nTo mention user , please copy/paste {ID} in your message, and to mention server it\'s {SERVERNAME} \n')
        DNEWM = input('What will be your welcome Dm message ?\nTo type \' do \\\' \nTo mention user , please copy/paste {ID} in your message, and to mention server it\'s {SERVERNAME}\n')
        ALLINONE = (f'\n@bot.event\nasync def on_member_join(member):\n    ID = f\'<@{{member.id}}>\'\n    SERVERNAME = member.guild.name\'\n    await member.create_dm()\n    await member.dm_channel.send(f\'{DNEWM}\')\n    channel = bot.get_channel(date[\'{CHANELID1}\'])\n    await channel.send(f\'{CHANNELMSG}\')')
        f.write('{}'.format(ALLINONE))
        print('succes')
        choice2()
    if answer2 == '4':
        choice2()
    else:
        print('Please choose 1 , 2 ,3 or 4 !')
        onmemberjoin()

def Embed():
    global f
    import datetime
    n = True
    title_try = 1
    thumb_try = 1
    author_try = 1
    footer_try = 1
    now = datetime.datetime.now()
    real_time = now.strftime("%Y-%m-%d %H:%M")
    NAMEEMB = input('What is the command name ?(the bot will answer it with an embed !)')
    EMBEDSTART = (f"\n@bot.command\nasync def {NAMEEMB}():\n")
    f.write('{}'.format(SpecificCHAN))

    while n == True:
        print("\n1.title\n2.thumbnail_url\n3.author\n4.footer\n5.set_image\n6.add_field\n7.quit\nANSWER WITH A NUMBER OTHER WAYS THE PROGRAM WILL CRASH !\n")
        value = int(input())
        if value == 7:
            n = False

        elif value == 6:
            ask = input("if want in inline reply with 'y' else 'n' --\n")
            if ask == 'y' or ask == 'Y':
                print("Its in inline now ")
                name = input("Enter name --\n")
                value = input("Enter value --\n")
                test = f"embed.add_field( name = '{name}' , value = '{value}' , inline = {True} )"
                f.write(test + '\n')
                f.close
                print(test)
            elif ask == 'n' or ask == 'N':
                print("It is not in inline now ")
                name = input("Enter name --\n")
                value = input("Enter value --\n")
                test = f"embed.add_field( name = '{name}' , value = '{value}' , inline = {False} )"
                f.write(test + '\n')
                f.close
                print(test)

        elif value == 4:
            if footer_try == 1:
                name = input("enter text --\n")
                icon = input("Enter icon url for author ==\n")
                test = f"embed.set_author(text = '{name}' , icon_url = '{icon}')"
                f.write(test + '\n')
                f.close
                print(test)
                footer_try = 0
            elif footer_try == 0:
                print("Sorry cant add more than once. ")


        elif value == 3:
            if author_try == 1:
                name = input("enter author name --\n")
                icon = input("Enter icon url for author ==\n")
                test = f"embed.set_author(name = '{name}' , icon_url = '{icon}')"
                f.write(test + '\n')
                f.close
                print(test)

                author_try = 0
            elif author_try == 0:
                print("Author can be added only once. ")

        elif value == 5:
            img = input("Enter image url you want to set --\n")
            test = f'embed.set_image( url = "{img}")'
            f.write(test + '\n')
            f.close
            print(test)

        elif value == 1:
            if title_try == 1:
                print("Enter your embed title --")
                data = input()
                print("Enter your embed description --")
                discrip = input()
                print("Enter your embed colour --")
                clr = input()
                test = f"embed = discord.Embed(title = '{data}',description = '{discrip}',color = {clr})"
                f.write(test + '\n')
                f.close
                print(test)
                title_try = 0
            elif title_try == 0:
                print("sorry title can be added only once")

        elif value == 2:
            if thumb_try == 1:
                print("Enter your thubnail url --")
                url = input()
                test = f"embed.set_thumbnail(url = '{url}')"
                f.write(test + '\n')
                f.close
                print(test)
                thumb_try = 0
            elif thumb_try == 0:
                print("Thubnail cann be added only once")



while invalid_input :
    start()

