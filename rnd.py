import blocksmith 
import random
import time
import sys
from colorama import Fore, Style

S = 0
S1 = 0

prefix = input("Введите префикс:")
M = len(prefix)
V = 34 - M
H = str(prefix[:V])
with open("Bal.txt", "a") as f:
    while True:
        
        F = random.randint(36893488147419103232,73786976294838206463)
        U = '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so'
        T = '00000000000000000000000000000000000000000000000' + format(F, '016x')
        AD = blocksmith.BitcoinWallet.generate_compressed_address(T)
        S += 1
        print("\033c", end="")
        print(Fore.RED + "AD: " + AD)
        print(Fore.YELLOW + "HEX: " + T)
        print(Fore.MAGENTA + "Просканировано: " + str(S) + " Адресов")
        
        
        if H in AD:
            S1 += 1
            
            with open("prefix.txt", "a") as f:
                f.write("prefix: " + str(H) + " addres: " + str(AD) + " decimal: " + str(F) + "\n")
                
                
        if AD == U:
            print(Fore.RED + "ВНИМАНИЕ НАЙДЕН PRIVATE KEY")
            f.write(AD + "\n")
            f.write(str(F) + "\n")
            break

        print("Префикс",str(H),"найдено таких",S1,"шт.")                
                
        