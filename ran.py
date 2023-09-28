from colorama import Fore, Style
import blocksmith 
import random
import time
import sys
import requests
import hashlib
import binascii
import random
import secrets
import os



S = 1
prefix = input("Введите число до 64:")
number = int(input("1.Uncompressed" + "\n" + "2.Compressed:"))
while number == 1 or 2:
    if number == 1:
        print("Выбран режим Uncompresses!")
        break
    elif number == 2:
        print("Выбран режим Compresses!")
        break    
    
    else:
        print("Неправильный ввод!")
        number = int(input("1.Uncompressed" + "\n" + "2.Compressed:"))
        




with open("Bal.txt", "a") as f:
    while True:
        
        OUT = ''.join(secrets.choice("123456789abcdef") for _ in range(int(prefix)))
        
        Q = 64
        L = 64 - int(prefix)
        BUT = "0" * L + str(OUT)
       
        
  
        
        if number == 2:
            AD = blocksmith.BitcoinWallet.generate_compressed_address(BUT)
        elif number == 1:
            AD = blocksmith.BitcoinWallet.generate_address(BUT)
            
        else:
            print("Неправильный ввод!")
                
        
        
        U = '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so'
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
            f.write("AD:" + AD + " HEX:" + OUT + " BAL:" + f"{balance}" + "\n")
            break
        if balances > 0:
            print(Fore.RED + "txn Найден")
            f.write("AD:" + AD + " HEX:" + OUT + " TXN:" + f"{balances}" + "\n")
            
         
    
        
        print(Fore.RED + "AD: " + AD + "\r")
        print(Fore.YELLOW + "HEX: " + OUT + "\r")
        print(Fore.MAGENTA + "Просканировано: " + str(S) + " Адресов" + "\r")
        
        
        
        

                
                
        if AD == U:
            print(Fore.RED + "ВНИМАНИЕ НАЙДЕН PRIVATE KEY")
            f.write(AD + "\n")
            f.write(str(F) + "\n")
            break
