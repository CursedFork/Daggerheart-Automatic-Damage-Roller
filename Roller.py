import random

# Utility to roll dice and optionally reroll 1s and 2s
def roll_dice(num, sides, reroll_low=False):
    rolls = []
    for _ in range(num):
        roll = random.randint(1, sides)
        while reroll_low and roll in (1, 2):
            roll = random.randint(1, sides)
        rolls.append(roll)
    return rolls

def attack(weapon, persona=False, bloody=False, brutal=False):
    # ----- Base modifiers -----
    strength = 4
    brutal_bonus = 3 if brutal else 0
    persona_prof = 3 if persona else 0
    bloody_bonus = 3 if bloody else 0

    # ---- Attack Roll (Hope/Fear system) ----
    hope = random.randint(1, 12)
    fear = random.randint(1, 12)
    total_bonus = strength + persona_prof + bloody_bonus + brutal_bonus
    total_roll = hope + fear + total_bonus

    print(f"\n=== {weapon.upper()} ATTACK ===")
    print(f"Hope: {hope} | Fear: {fear} | Modifiers: +{total_bonus}")
    print(f"Total To-Hit Roll: {total_roll} -> {'HIT!' if total_roll >= 12 else 'MISS!'}")

    # ---- Damage Roll ----
    if weapon == "sword":
        base_rolls = roll_dice(3, 10, reroll_low=True)
        damage_bonus = 15
        range_ft = 20 if persona else 10

        # Persona adds extra d10s, Bloody Charge adds one more d10
        persona_damage = roll_dice(persona_prof, 10) if persona else []
        bloody_damage = [random.randint(1, 10)] if bloody else []

        all_rolls = base_rolls + persona_damage + bloody_damage

        # "Massive": roll an extra die and drop lowest
        extra_roll = random.randint(1, 10)
        all_rolls.append(extra_roll)
        all_rolls.remove(min(all_rolls))

        total_damage = sum(all_rolls) + damage_bonus

        print(f"Damage Dice (d10s): {all_rolls} + {damage_bonus} = {total_damage}")
        print(f"Range: {range_ft} ft")

    elif weapon == "shield":
        base_rolls = roll_dice(3, 6, reroll_low=True)
        damage_bonus = 10
        range_ft = 15 if persona else 5

        # Persona adds extra d6s (not d10s), Bloody Charge adds one more d6
        persona_damage = roll_dice(persona_prof, 6) if persona else []
        bloody_damage = [random.randint(1, 6)] if bloody else []

        all_rolls = base_rolls + persona_damage + bloody_damage

        # "Massive": roll an extra die and drop lowest
        extra_roll = random.randint(1, 6)
        all_rolls.append(extra_roll)
        all_rolls.remove(min(all_rolls))

        total_damage = sum(all_rolls) + damage_bonus

        print(f"Damage Dice (d6s): {all_rolls} + {damage_bonus} = {total_damage}")
        print(f"Range: {range_ft} ft")

# ---- Menu System ----
def menu():
    persona = False
    bloody = False

    while True:
        print("\n--- Daggerheart Attack Menu ---")
        print("1. Sword Attack")
        print("2. Shield Attack")
        print(f"3. Toggle Persona Mode (Currently {'ON' if persona else 'OFF'})")
        print(f"4. Toggle Bloody Charge (Currently {'ON' if bloody else 'OFF'})")
        print("5. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            attack("sword", persona=persona, bloody=bloody)
        elif choice == "2":
            attack("shield", persona=persona, bloody=bloody)
        elif choice == "3":
            persona = not persona
            print(f"Persona {'enabled' if persona else 'disabled'}.")
        elif choice == "4":
            bloody = not bloody
            print(f"Bloody Charge {'enabled' if bloody else 'disabled'}.")
        elif choice == "5":
            print("Exiting roller. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
