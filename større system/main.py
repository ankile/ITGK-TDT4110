# Importer moduler
from bruker import *
from fil import *

# Opprette variabler og initiér
db = {}  # tom dictionary
dbid = 0  # Dictionariens id

# Gi en varm velkomst til bruker
velkomstbeskjed()

# Vis en valgmeny til bruker
valg = skriv_meny()

end = False

while not end:
    if valg == 'utgift' or valg == 'inntekt':
        dbid += 1
        # Registrere inntekt/utgift (bruker.py)
        db = registrer(db, dbid, valg)

    elif valg == 'vis':
        vis(db)

    elif valg == 'fjern':
        db = fjern(db)

    elif valg == 'save':
        filnavn = velg_filnavn()
        save(db, filnavn)

    elif valg == 'load':
        filnavn = velg_filnavn()
        db = load(filnavn)
        dbid = max(db)
        melding(filnavn + ' er lastet inn')

    elif valg == 'avslutt':
        break

    else:
        melding('Feil kommando')

    valg = skriv_meny()