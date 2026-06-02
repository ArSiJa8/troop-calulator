# General
Fahrzeugtyp = input("Fahrzeugtyp für Logistikberechnung eingeben (z.B. SPz Marder): ")
Amount = int(input(f"Anzahl der Einheiten vom Typ [{Fahrzeugtyp}] im Verband: "))

# Troops
Troops = int(input(f"Soll-Stärke der Besatzung pro {Fahrzeugtyp} (Anzahl Soldaten): "))
TroopsTotal = int(Troops * Amount)

# Supplies
Fuil = int(input(f"Treibstoffverbrauch pro {Fahrzeugtyp} (in Litern, nur Zahl): "))
Food = int(input(f"Verpflegungssatz pro Soldat/Tag (in kg, nur Zahl): "))

Food1 = int(Troops * Food)

FuilTotal = int(Amount * Fuil)
FoodTotal = int(Amount * Food1)


# Output
print("\n" + "="*50)
print("LOGISTISCHER LAGEBERICHT / BEDARFSBERECHNUNG")
print("="*50)
print(f"Einsatzverband: {Amount}x {Fahrzeugtyp}")
print(f"Gesamt-Personalsollstärke: {TroopsTotal} Soldaten (Besatzung: {Troops} Mann pro System).")
print("-"*50)
print(f"Tagesverbrauch Einzelsystem [{Fahrzeugtyp}]:")
print(f" -> Betriebsstoffe (POL): {Fuil}l")
print(f" -> Verpflegung (Vpf): {Food1}kg")
print("-"*50)
print(f"Gesamtbedarf des Verbandes (pro 24 Stunden):")
print(f" -> POL-Gesamt: {FuilTotal}l Treibstoff")
print(f" -> Vpf-Gesamt: {FoodTotal}kg Verpflegung")
print("="*50)