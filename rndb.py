
import blocksmith 
import random
import time
import sys
from colorama import Fore, Style
import requests
import hashlib
import binascii
import random

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
        address = AD
        url = f"https://blockchain.info/balance?active={address}"
        
        response = requests.get(url)
  
        data = response.json()
        balance = data[address]['final_balance']
        balances = data[address]['total_received']
        
        
        print("\033c", end="")
        print(f"{balance} Баланс" + "\r")
        print(f"{balances} Всего txn." + "\r")
        
        if balance > 0:
            print(Fore.RED + "Money Нашел")
            f.write("AD:" + AD + " HEX:" + T + " BAL:" + f"{balance}" + "\n")
            break
        if balances > 0:
            print(Fore.RED + "txn Найден")
            f.write("AD:" + AD + " HEX:" + T + " TXN:" + f"{balances}" + "\n")
        print(Fore.RED + "AD: " + AD)
        
        print(Fore.GREEN + "DEC: " + str(F))
        
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
                
        