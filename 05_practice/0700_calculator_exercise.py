""" Øvelse: "Calculator"

Som altid, læs hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

-------

Opret et program, der fungerer som en simpel lommeregner. Programmet skal fungere som følger:
    1. Forklar brugeren hvordan man betjener programmet.
    2. Præsenter en menu med følgende muligheder:
        - Addition
        - Subtraktion
        - Multiplikation
        - Division
        - Afslut
    3. Bed brugeren om at vælge en mulighed fra menuen.
    4. Hvis brugeren vælger en aritmetisk operation, bed om to tal.
    5. Udfør den valgte operation og vis resultatet.
    6. Gentag processen, indtil brugeren vælger at afslutte.

-------

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""


def vis_menu():
    print("\n=== Simpel Lommeregner ===")
    print("Vælg en af følgende muligheder:")
    print("1. Addition (+)")
    print("2. Subtraktion (-)")
    print("3. Multiplikation (*)")
    print("4. Division (/)")
    print("5. Afslut")


def hent_tal():
    while True:
        try:
            tal1 = float(input("Indtast første tal: "))
            tal2 = float(input("Indtast andet tal: "))
            return tal1, tal2
        except ValueError:
            print("Ugyldigt input. Prøv igen med tal.")


def main():
    print("Velkommen til lommeregneren!")
    print("vælge en matematisk operation,")
    print("og derefter indtaste to tal for at få resultatet.")

    while True:
        vis_menu()
        valg = input("Vælge operation(1-5): ")

        if valg == "1":
            tal1, tal2 = hent_tal()
            print(f"Resultat: {tal1} + {tal2} = {tal1 + tal2}")
        elif valg == "2":
            tal1, tal2 = hent_tal()
            print(f"Resultat: {tal1} - {tal2} = {tal1 - tal2}")
        elif valg == "3":
            tal1, tal2 = hent_tal()
            print(f"Resultat: {tal1} * {tal2} = {tal1 * tal2}")
        elif valg == "4":
            tal1, tal2 = hent_tal()
            if tal2 == 0:
                print("Fejl: Division med nul er ikke tilladt.")
            else:
                print(f"Resultat: {tal1} / {tal2} = {tal1 / tal2}")
        elif valg == "5":
            print("Programmet afsluttes. Tak for brugen!")
            break
        else:
            print("Ugyldigt valg. Prøv igen.")


if __name__ == "__main__":
    main()
