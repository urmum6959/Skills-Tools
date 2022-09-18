import sys
from time import sleep
import os
import time
from turtle import clear
import requests
import marshal
import zlib
from os import system





def fuckskids():
    sleep(0.5)

    print('made by skill issue#1457')
    sleep(0.5)
    print('fuck skids')

    sleep(1)

def spamhook():
    system("title " + "Skills Spammer")
    print('''

        ░██████╗██╗░░██╗██╗██╗░░░░░██╗░░░░░░██████╗  ░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
        ██╔════╝██║░██╔╝██║██║░░░░░██║░░░░░██╔════╝  ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
        ╚█████╗░█████═╝░██║██║░░░░░██║░░░░░╚█████╗░  ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
        ░╚═══██╗██╔═██╗░██║██║░░░░░██║░░░░░░╚═══██╗  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
        ██████╔╝██║░╚██╗██║███████╗███████╗██████╔╝  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
        ╚═════╝░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚═════╝░  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
        ''')
    fuckskids()
    webhook = input('Please Insert Webhook URL: ')
    msg = input('Please Insert Message To Spam: ')
    spamamnt = int(input('Please Insert Amount Of Messages To Send: '))

    def spam(msg, webhook):
            counter = 0
            while True:
                counter = counter+1
                data = requests.post(webhook, json={'content': msg})
                print(data.text)
                print(data.status_code)
                if data.status_code == 204:
                    print(f"Sent MSG {msg}")
                if data.status_code == 404:
                    print(f"Sent MSG {msg}")
                    break
                if counter == spamamnt:
                    time.sleep(3)
                    requests.delete(webhook)
                    sleep(0.5)
                else:
                    try:
                        time.sleep(data.json()["retry_after"]/1000)
                    except:
                            pass

    spam(msg, webhook)





def delhook():
    system("title " + "Skills Deleter")
    print('''

    ░██████╗██╗░░██╗██╗██╗░░░░░██╗░░░░░░██████╗  ██████╗░███████╗██╗░░░░░███████╗████████╗███████╗██████╗░
    ██╔════╝██║░██╔╝██║██║░░░░░██║░░░░░██╔════╝  ██╔══██╗██╔════╝██║░░░░░██╔════╝╚══██╔══╝██╔════╝██╔══██╗
    ╚█████╗░█████═╝░██║██║░░░░░██║░░░░░╚█████╗░  ██║░░██║█████╗░░██║░░░░░█████╗░░░░░██║░░░█████╗░░██████╔╝
    ░╚═══██╗██╔═██╗░██║██║░░░░░██║░░░░░░╚═══██╗  ██║░░██║██╔══╝░░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗
    ██████╔╝██║░╚██╗██║███████╗███████╗██████╔╝  ██████╔╝███████╗███████╗███████╗░░░██║░░░███████╗██║░░██║
    ╚═════╝░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚═════╝░  ╚═════╝░╚══════╝╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
    ''')
    fuckskids()
    webhook = input('Please Insert Webhook URL: ')

    def delt(webhook):
        requests.delete(webhook)
    delt(webhook)
    sleep(0.5)
    print("deleted webhook!")
    sleep(0.5)




def zlb():
    system("title " + "AntiZLib")
    print('''

    ░█████╗░███╗░░██╗████████╗██╗███████╗██╗░░░░░██╗██████╗░
    ██╔══██╗████╗░██║╚══██╔══╝██║╚════██║██║░░░░░██║██╔══██╗
    ███████║██╔██╗██║░░░██║░░░██║░░███╔═╝██║░░░░░██║██████╦╝
    ██╔══██║██║╚████║░░░██║░░░██║██╔══╝░░██║░░░░░██║██╔══██╗
    ██║░░██║██║░╚███║░░░██║░░░██║███████╗███████╗██║██████╦╝
    ╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝╚══════╝╚══════╝╚═╝╚═════╝░
    ''')

    fuckskids()
    encodedstring = eval(input('Encoded string: '))
    output = marshal.loads(zlib.decompress(encodedstring))

    decoded = open('decoded.txt','w')
    decoded.write(output)
    decoded.close()

    print(output)

    print("Source code in decoded.txt, enjoy!")
    sleep(0.5)





#console clearing
def clearConsole():
    os.system("cls")




exit = 4 #defines the exit int




#option select
def select():
    system("title " + "Skills Tools")
    clearConsole()
    sleep(0.1)
    print('''
█─▄▄▄▄█▄─█─▄█▄─▄█▄─▄███▄─▄███─▄▄▄▄███─▄─▄─█─▄▄─█─▄▄─█▄─▄███─▄▄▄▄█
█▄▄▄▄─██─▄▀███─███─██▀██─██▀█▄▄▄▄─█████─███─██─█─██─██─██▀█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
    ''')
    sleep(0.5)
    fuckskids()
    print("[1] Webhook Spammer")
    print("[2] Webhook Deleter")
    print("[3] ZLib Decoder")
    print("[4] Exit")




select()
option = int(input("what u pickin: "))



#execute commands
while option != exit:
    if option == 1:
        clearConsole()
        sleep(0.5)
        spamhook()
        pass



    elif option == 2:
        clearConsole()
        sleep(0.5)
        delhook()



    elif option == 3:
        clearConsole()
        sleep(0.5)
        zlb()



    else:
        print("pick one dumbass")
        

    clearConsole()
    select()
    option = int(input("what u pickin: "))
    