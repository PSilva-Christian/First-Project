import os

class Contact:

    def __init__(self, name: str, number: str, nickname: str):
        self.name = name
        self.number = number
        self.nickname = nickname

    def print_contact(self):
        print(f"\n\tContact name: {self.name}\nContact number: {self.number}\nContact nickname: {self.nickname}")

    def conta(self ):
        return f"Name: {self.name}\nNumber: {self.number}\nNickname: {self.nickname}\n"

def menu() -> None:
    print("\n\n\t========================\n"
              "\t======= Contacts =======\n"
              "\t========================")
    while True:
        choose = str(input("\n\tChoose what to do: \n\t\t  I: Add - add a new Contact.\n\t\t"
                           " II: Remove - remove a Contact .\n\t\t""III: List - list all Contacts.\n\t\t"
                           " IV: Exit - Exit program\n\t R: "))

        if choose.lower() == "exit":
            print("Exiting program...")
            return
        elif choose.lower() == "add":
            add_new_contact()
        elif choose.lower() == "remove":
            remove_contact()
        elif choose.lower() == "list":
            list_all()
        else:
            print("\nWrong answer, try again!")

def add_new_contact() -> None:
    print("\n== Add Contact ==\n")
    with open("Contacts.txt", "a") as file:
        new_contact_name = str(input("\nWhat's the name of the Contact: "))
        new_contact_number = str(input("\nWhat's the number of the Contact: "))
        new_contact_nickname = str(input("\nWhat's the nickname of the Contact: "))

        new_contact = Contact(new_contact_name, new_contact_number, new_contact_nickname)
        file.write(Contact.conta(new_contact))
        print("Added Contact!")
        Contact.print_contact(new_contact)
    return

def remove_contact() -> None:
    print("\n== REMOVE CONTACT ==\n")
    list_all()
    removed_contact = []
    try:
        removed_contact[0] = int(input("Which line should be removed: "))
        removed_contact[1] = removed_contact[0] + 1
        removed_contact[2] = removed_contact[1] + 1

    except ValueError:
        print("\nEntrada inválida. Por favor, digite o número da linha.")
    i = 1
    with open("aux.txt", "w") as aux:
        with open("Contacts.txt", "r") as file:
            for linha in file:

                if i in removed_contact:
                    continue
                else:
                    aux.write(linha)

                i += 1

    os.remove("Contacts.txt")
    os.rename("aux.txt", "Contacts.txt")

def list_all() -> None:
    print("\n== LIST CONTACT'S ==\n")
 # Arrumar #
    with open("Contacts.txt", "r") as file:
        i = 1
        cont = 0
        for linha in file:
            if cont % 3 == 0:
                print(f"{i} Contact:\n")
                i += 1
            print(f"\t{linha}")
            cont += 1

        i += 1

menu()
