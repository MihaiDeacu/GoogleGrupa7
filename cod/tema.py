categorii = input("Introduceți categoriile de task-uri: ")
categorii = [cat.strip() for cat in categorii.split(",")]

with open("categorii.txt", "w") as file:
    for cat in categorii:
        file.write(cat + "\n")

def afisare_categorii():
    try:
        with open("categorii.txt", "r") as file:
            categorii = file.read().splitlines()
            print("Categoriile de task-uri disponibile sunt:")
            for cat in categorii:
                print(cat)
    except FileNotFoundError:
        print("Nu există categorii de task-uri disponibile.")

def afisare_taskuri():
    try:
        with open("taskuri.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Nu există task-uri disponibile.")


def adaugare_task():
    task = input("Introduceți un task: ")
    deadline = input("Introduceți data limită: ")
    responsabil = input("Introduceți persoana responsabilă: ")
    categoria = input("Introduceți categoria: ")

    try:
        with open("taskuri.txt", "a") as file:
            file.write(f"{task} - {deadline} - {responsabil} - {categoria}\n")
        print("Task-ul a fost adăugat!")
    except:
        print("Eroare. Task-ul nu a fost salvat.")



while True:
    print("\nMeniu:")
    print("1. Adăugare task")
    print("2. Lista de task-uri")
    print("3. Lista de categorii")
    print("4. Ieșire")
    optiune = input("Selectați o opțiune: ")
    if optiune == "1":
         adaugare_task()
    elif optiune == "2":
         afisare_taskuri()
    elif optiune == "3":
         afisare_categorii()
    elif optiune == "4":
        break
    else:
        print("Opțiunea nu exista. Încercați din nou.")