#General
Fahrzeugtyp = input("Für welchen Fahrzeugtyp möchtest du die Supplies berechenen?:")
Amount = int(input(f"Wieviele des Fahrzeugtyps {Fahrzeugtyp} brauchst du?:"))

#Troops
Troops = int(input(f"Wieviel besatzung benötigt 1 {Fahrzeugtyp}?:"))
TroopsTotal = int(Troops * Amount)

#Supplies
Fuil = int(input(f"Wieviel Treibstoff benötigt EIN {Fahrzeugtyp} (nur Nummer):"))
Food = int(f"Wieviel Essen benötigt EIN Mann täglich (In Kilogramm, nur Zahl):")
Medicine = float(input(f"Wieviel Kilogramm Medizin benötigt ein Mann der besatzung des {Fahrzeugtyp} täglich (Auch Dezimalzahlen möglich, z.B. 0.3)"))



#Output
print(f"Für {Amount} {Fahrzeugtyp} welcher je {Troops} Läute Besatzung benötigt brauchst du {TroopsTotal} truppen.")