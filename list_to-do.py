# Functions
import os

def menu() -> None:
    print("\n\n\t===================================\n"
    "\t=== That's the menu of the list ===\n"
    "\t===================================")
    while True:
        choose = str(input("\n\tChoose what to do: \n\t\t  I: Add - add a new thing to-do.\n\t\t II: Remove - remove a thing to-do.\n\t\t"
              "III: List - list all.\n\t\t IV: Exit - Exit program\n\t R: ")).strip()
        if choose.lower() == "exit":
            print("Exiting program...")
            return
        elif choose.lower() == "add" or "i":
            addnew()
        elif choose.lower() == "remove" or "ii":
            removenew()
        elif choose.lower() == "list" or "iii":
            list_all()
        else:
            print("\nWrong answer, try again!")

def addnew() -> None:
    with open("lista_arquivo.txt", "a") as lista:
        inserido = str(input("What's gonna be inserted: "))
        lista.write(inserido + "\n")

def removenew() -> None:
    list_all()
    try:
        removed_line = int(input("Which line should be removed: "))
    except ValueError:
        print("\nEntrada inválida. Por favor, digite o número da linha.")
        return

    i = int(1)
    with open("lista_arquivo.txt", "r") as lista:
        with open("aux.txt", "w") as aux:
            for linha in lista:
                if i != removed_line:
                    aux.write(linha)

                i += 1

    os.remove("lista_arquivo.txt")
    os.rename("aux.txt","lista_arquivo.txt")

def list_all() -> None:
    i = int(1)
    print("\n\nContent in the list: \n")
    with open("lista_arquivo.txt", "r") as lista:
        for linha in lista:
            print(f"{i} - {linha.strip()}")
            i += 1

# Main

menu()