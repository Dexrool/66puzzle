
import blocksmith 
import random
import sys
from colorama import Fore, Style
import requests
import hashlib
import binascii
import random
S = 0
with open("Bal.txt", "a") as f:
    while True:
        with open('seed.txt', 'r') as file:
            seed_phrase = file.read().strip()
            word = seed_phrase.split()
            random_word = random.sample(word, 12)
            new_seed_phrase = " ".join(random_word)
            new_seed_hash = hashlib.sha256(new_seed_phrase.encode('utf-8')).digest()
            seed = new_seed_hash.hex()
        print("Seed phrase:", new_seed_phrase)
        U = '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so'
        AD = blocksmith.BitcoinWallet.generate_address(seed)
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
            f.write("AD:" + AD + " HEX:" + seed + " BAL:" + f"{balance}" + "\n")
            break
        if balances > 0:
            print(Fore.RED + "txn Найден")
            f.write("AD:" + AD + " HEX:" + seed + " TXN:" + f"{balances}" + "\n")
            break
        print(Fore.RED + "AD: " + AD)
        print(Fore.YELLOW + "HEX: " + seed)
        print(Fore.MAGENTA + "Просканировано: " + str(S) + " Адресов")
        print(Fore.GREEN + "Hex seed:", seed)
        if AD == U:
            print(Fore.RED + "ВНИМАНИЕ НАЙДЕН PRIVATE KEY")
            f.write(AD + "\n")
            f.write(str(F) + "\n")
            break

        