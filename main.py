#General
Fahrzeugtyp = input("Für welchen Fahrzeugtyp möchtest du die Supplies berechenen?:")
Amount = int(input(f"Wieviele des Fahrzeugtyps {Fahrzeugtyp} brauchst du?:"))

#Troops
Troops = int(input(f"Wieviel besatzung benötigt 1 {Fahrzeugtyp}?:"))
TroopsTotal = int(Troops * Amount)

#Supplies
Fuil = int(input(f"Wieviele Liter Treibstoff benötigt EIN {Fahrzeugtyp} (nur Nummer):"))
Food = int(input(f"Wieviel Essen benötigt EIN Mann täglich (In Kilogramm, nur Zahl):"))
Medicine = float(input(f"Wieviel Kilogramm Medizin benötigt ein Mann der besatzung des {Fahrzeugtyp} täglich (Auch Dezimalzahlen möglich, z.B. 0.3)"))

Food1 = int(Troops * Food)
Medicine1 = float(Troops * Medicine)

FuilTotal = int(Amount * Fuil)
FoodTotal = int(Amount * Food1)
MedicineTotal = float(Amount * Medicine1)




#Output
print(f"Für {Amount} {Fahrzeugtyp} welcher je {Troops} Läute Besatzung benötigt brauchst du {TroopsTotal} truppen.")
print(f"Ein {Fahrzeugtyp} mit Besatzung benötigt also täglich {Fuil}l Treibstoff, {Food1}kg Essen und {Medicine1}kg Medizin.")
print(f"Das sind also für alle {Amount} {Fahrzeugtyp} zusammen {FuilTotal}l Treibstoff, {FoodTotal}kg Essen und {MedicineTotal}kg Medizin Täglich.")