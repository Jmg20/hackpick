#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------

#|_|<Fuck/ON>_____________|_|
#| .----------------------. |
#| |  .----------------.  | |
#| |  |                |  | |
#| |()|                |  | |
#| |""|           tm   |  | |
#| |  |   MALWARELAB   |  | |
#| |  |   Alpha 0.1    |  | |
#| |  |                |  | |
#| |  |                |  | |
#| |  '----------------'  | |
#| |__HACKPICK____________/ |
#|          __________      |
#|    .    (Malwarelab)     |
#|  _| |_   """""""""" .-.  |
#|<[_ o _]>       .-. (   ) |
#|   |_|         (   ) '-'  |
#|    '           '-'   A   |
#|                 B        |
#|          ___   ___       |
#|         (___) (___)  \\\\|
#|        select start \\\\\|
#|                    \\\\\ /
#|        (phones)   \\\\'.'
#`-----------------------`
#------------------------------------------------------------



import RPi.GPIO as gpio
import time
import os
import locale
from dialog import Dialog

locale.setlocale(locale.LC_ALL, '')
gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(17, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(18, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(27, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(22, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(23, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(24, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(25, gpio.IN, pull_up_down = gpio.PUD_UP)

#-----------------------------------------
#Funções

def menu():
        menu = Dialog(dialog="dialog")
        menu.set_background_title("HackPIck")
        op, tag = menu.menu("Tools:",
                choices=[("DuckyPi", "Ataque via USB1."),
                         ("Fake", "Fake game."),
                         ("System", "Opções do systema."),
                         ("Update", "Atualização via git.")])
        #print ("OP: ", op)
        #print ("TAG: ", tag)
        if tag == 'DuckyPi':
                duckypi()
        elif tag == 'Dev':
                menu.msgbox("Em desenvolvimento. =(")
        elif tag == 'Update':
                update()
        elif tag == 'System':
                system()

def check_modules():
        alert = Dialog(dialog="dialog")
        if os.path.exists('/sys/kernel/config/usb_gadget/g1/UDC'):
                return True
        else:
                alert.msgbox("Iniciando o modulo usb")
                #os.system('sudo /home/pi/hackpick/tools/DuckyPi/hid.sh')
                os.system('sudo /home/pi/hackpick/tools/DuckyPi/gf.sh')
                if os.path.exists('/sys/kernel/config/usb_gadget/g1/UDC'):
                        alert.msgbox("Iniciando com sucesso!")
def update():
        os.system('git -C /home/pi/hackpick/ pull origin master')

def system():
        menu = Dialog(dialog="dialog")
        menu.set_background_title("HackPIck")
        op, tag = menu.menu("System:",
                choices=[("Reboot", "Reiniciar o hackpick."),
                         ("Shutdown", "Desligar o hackpick.")])
        if tag == 'Reboot':
                menu.msgbox("Reiniciando o Hackpick!")
                os.system('sudo reboot')
        elif tag == 'Shutdown':
            menu.msgbox("Desligando o Hackpick!")
            os.system('sudo shutdown -h now')

def duckypi():
        itens = os.listdir('/home/pi/hackpick/tools/DuckyPi/payloads/')
        
        itens_list = []
        for i in itens:
                itens_list.append(i)
                itens_list.append('payload')
        
        duckypi_screen = Dialog(dialog="dialog")
        duckypi_screen.set_background_title("HackPIck")
        op, tag = duckypi_screen.menu("Payloads:",
                                        choices=[itens_list])
        duckypi_screen.msgbox("Payload escolhido:\n"+tag)
        check_modules()
        os.system('sudo /home/pi/hackpick/tools/DuckyPi/duckpi.sh /home/pi/hackpick/tools/DuckyPi/payloads/'+tag)

        
        
#-----------------------------------------
#Main
main_screen = Dialog(dialog="dialog")
main_screen.set_background_title("HackPIck")
main_screen.msgbox("Bem vindo ao HackPIck!!")

while True:
        menu()
        if gpio.input(25) == gpio.LOW and gpio.input(24) == gpio.LOW :
                print("Botão pressionado: START e SELECT")
                print("Desligando HackPIcK")
                os.system("sudo shutdown -h now")
