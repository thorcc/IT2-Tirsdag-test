# Et program som fortsetter helt til bruker har skrevet riktig input

år = 2024

while True:
    try:
        alder = int(input("Hvor gammel blir du i år? "))
        break
    except:
        print("Ugyldig input. Input må være et tall")

fødselsår = år - alder
print(f"Du er født i {fødselsår}")



# Tips til 3.14
navn = "Thor Christian Coward"
splittet_navn = navn.split(" ") # -> ["Thor", "Christian", "Coward"]
antall_navn = len(splittet_navn) # -> 3

# Oppgave 3.14
"""
Lag et program som genrerer mailadresser fra fornavn og etternavn. 
Mailen skal bestå av hele det første fornavnet og første bokstav i 
etternavnet etterfulgt av @afk.no. For eksempel skal Thor Christian Coward 
bli thorc@afk.no. Som input til programmet må brukeren skrive inn 
minst to navn (fornavn og etternavn), hvis ikke skal brukeren få 
en feilmelding og få lov til å skrive input på nytt.
"""
while True:
    navn = input("Hva heter du? ")   # -> Thor Christian Coward
    splittet_navn = navn.split(" ")  # -> ["Thor", "Christian", "Coward"]
    antall_navn = len(splittet_navn) # -> 3
    if antall_navn < 2:
        print("Ugyldig input. Input må bestå av minst to navn.")
    else:
        break # Bryter ut av løkka
fornavn = splittet_navn[0] # -> Thor
første_bokstav_etternavn = splittet_navn[-1][0] # -> C
mail = fornavn + første_bokstav_etternavn + "@viken.no" # -> ThorC@viken.no
mail = mail.lower() # -> thorc@viken.no
print(mail)
