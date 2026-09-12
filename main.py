def addieren():
    return

def main():
    print("Taschenrechner")
    print("1 fuer Addition")
    print("2 fuer Subtraktion")
    print("3 fuer Multiplikation")
    print("4 fuer Division")

    wahl = input("Wahl eingeben: ")

    match wahl:
        case "1":
            print("Resultat: {}".format(addieren()))
            # Hier Funktion für Addition einfügen
        case "2":
            print("Subtraktion")
            # Hier Funktion für die Subtraktion einfügen
        case "3":
            print("Multiplikation")
            # Hier die Funktion für die Multiplikation einfügen
        case "4":
            print("Division")
            # Hier die Funktion für die Division einfügen
        case _:
            print("Falsche Auswahl, das Programm wird beendet.")

if __name__ == "__main__":
    main()