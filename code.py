import colorama, ctypes
from colorama import Fore, init
from random import choice, randint
from os import system, name
import os, datetime, random, string
from os.path import exists, isfile
colorama.init()

os.system("cls")
if __name__ == "__main__":
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("Nitro generator by vlc#1769")
    colorama.init()

logo = '''                                                                                   
#    # # ##### #####   ####      ####  ###### #    # ###### #####    ##   #####  ####  #####  
##   # #   #   #    # #    #    #    # #      ##   # #      #    #  #  #    #   #    # #    # 
# #  # #   #   #    # #    #    #      #####  # #  # #####  #    # #    #   #   #    # #    # 
#  # # #   #   #####  #    #    #  ### #      #  # # #      #####  ######   #   #    # #####  
#   ## #   #   #   #  #    #    #    # #      #   ## #      #   #  #    #   #   #    # #   #  
#    # #   #   #    #  ####      ####  ###### #    # ###### #    # #    #   #    ####  #    # 

Made by vlc#1769
'''

print(Fore.BLUE + logo)

num = ('').join(random.choices(string.ascii_letters + string.digits, k=10))

amount = int(input('Amount of codes: '))
value = 1
print(f"\n{Fore.LIGHTGREEN_EX}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Started generating codes...(it will take about {amount/100} seconds)")
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open(f'{amount}_codes_{num}.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    value += 1
f = open(f'{amount}_codes_{num}.txt', "a+")
f.write(f'Generator made by vlc#1769\n')
f.close()
print(f"\n{Fore.LIGHTGREEN_EX}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Generated {amount} codes and saved it in {amount}_codes_{num}.txt")
nextCode = input('\nPress Enter to close generator')  
