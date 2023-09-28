import subprocess
selection = input("Выберите Режим 66 puzzle:" + "\n" + "1 — Рандом Обычный" + "\n" + "2 — Рандом с проверкой на баланс" + "\n"  + "3 — SEED с проверкой на баланс" + "\n" + "4 — Режим рандом HEX(читайте инструкцию)")

if selection == '1':
    subprocess.run(['python', 'rnd.py'])
elif selection == '2':
    subprocess.run(['python', 'rndb.py'])
elif selection == '3':
    subprocess.run(['python', 'seed.py'])
elif selection == '4':
    subprocess.run(['python', 'ran.py'])
else:
    print("Неправильный выбор.")