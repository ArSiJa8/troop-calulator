Fahrzeugtyp = input("Für welchen Fahrzeugtyp möchtest du die Supplies berechenen?:")
Amount = int(input(f"Wieviele des Fahrzeugtyps {Fahrzeugtyp} brauchst du?:"))
Troops = int(input(f"Wieviel besatzung benötigt 1 {Fahrzeugtyp}?:"))
TroopsTotal = Troops * Amount

print(f"Für {Amount} {Fahrzeugtyp} welcher je {Troops} Läute Besatzung benötigt brauchst du {TroopsTotal} truppen.")