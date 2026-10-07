# Domain To IP Converter Script
# Just for Learn and fun

import socket
import pyfiglet
from termcolor import colored
import time

print(colored("\n***************** Domain to IP Address *****************", 'blue'))

banner = colored(pyfiglet.figlet_format("DP Converter"), 'red')
print(banner)

print(colored("***************** Created By Dare_Devil *****************\n", 'blue'))

domain_name = input(" Enter Target Domain Name :>>>>> ")

for loop in range(15):
    def print_slow(text, delay=0.1):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()


    print_slow(" IP Recognizing ............ ", 0.002)

print_slow("\n IP Detected ", 0.002)

IP = socket.gethostbyname(domain_name)
print(" IP ADDRESS of {0} :>>>>> ".format(domain_name), IP)
