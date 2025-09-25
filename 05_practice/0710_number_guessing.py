""" Opgave "Number guessing"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Opret et program, der spiller et gættespil med brugeren. Programmet fungerer på følgende måde:
    Forklar reglerne for brugeren.
    Generer tilfældigt et 4-cifret heltal.
    Bed brugeren om at gætte et 4-cifret tal.
    Hvert ciffer, som brugeren gætter korrekt i den rigtige position, tæller som en sort mønt.
    Hvert ciffer, som brugeren gætter korrekt, men i den forkerte position, tæller som en hvid mønt.
    Når brugeren har gættet, udskrives det, hvor mange sorte og hvide mønter gættet er værd.
    Lad brugeren gætte, indtil gættet er korrekt.
    Hold styr på antallet af gæt, som brugeren gætter i løbet af spillet, og print det ud til sidst.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
import random

def forklar_regler():
    print("=== Gættespillet ===")
    print("Regler:")
    print("- Et 4-cifret tal er blevet genereret.")
    print("- Du skal gætte tallet.")
    print("- Sort mønt: Et ciffer er korrekt og på rigtig plads.")
    print("- Hvid mønt: Et ciffer er korrekt, men på forkert plads.")
    print("- gæt indtil du rammer det rigtige tal.")
    print("Held og lykke!\n")

def generer_tal():
    return [int(c) for c in str(random.randint(1000, 9999))]

def hent_bruger_gaet():
    while True:
        gaet = input("Indtast dit gæt (4-cifret tal): ")
        if gaet.isdigit() and len(gaet) == 4:
            return [int(c) for c in gaet]
        else:
            print("Ugyldigt input. Indtast præcis 4 cifre (f.eks. 1234).")

def vurder_gaet(hemmeligt_tal, gaet):
    sort = 0
    hvid = 0

    brugt_i_hemmeligt = [False] * 4
    brugt_i_gaet = [False] * 4

    for i in range(4):
        if gaet[i] == hemmeligt_tal[i]:
            sort += 1
            brugt_i_hemmeligt[i] = True
            brugt_i_gaet[i] = True

    for i in range(4):
        if not brugt_i_gaet[i]:
            for j in range(4):
                if not brugt_i_hemmeligt[j] and gaet[i] == hemmeligt_tal[j]:
                    hvid += 1
                    brugt_i_hemmeligt[j] = True
                    break

    return sort, hvid

def main():
    forklar_regler()
    hemmeligt_tal = generer_tal()
    forsøg = 0

    while True:
        gaet = hent_bruger_gaet()
        forsøg += 1
        sort, hvid = vurder_gaet(hemmeligt_tal, gaet)

        print(f"Resultat: {sort} sort(e) mønt(er), {hvid} hvid(e) mønt(er)\n")

        if sort == 4:
            print(f"Tillykke! Du gættede det rigtige tal: {''.join(str(c) for c in hemmeligt_tal)}")
            print(f"Du brugte {forsøg} forsøg.")
            break

if __name__ == "__main__":
    main()