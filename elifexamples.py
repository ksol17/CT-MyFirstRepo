# example 1
 weather = "rainy"

if weather == "sunny":
    print("It's a bright and beautiful day!")
elif weather == "rainy":
    print("Carry an umbrella!")
elif weather == "snowy":
    print("Time to build a snowman!")

# example 2
sword_material = "silver"
if sword_material == "gold":
    print("The sword shines brightly!")
elif sword_material == "silver":
    print("The sword has a mystical glimmer!")
elif sword_material == "bronze":
    print("The sword looks ancient and valuable!")

# Example 3

player_level = 12
if player_level < 5:
    print("Access the beginner dungeon!")
elif 5 <= player_level < 10:
    print("Enter the intermediate dungeon!")
elif player_level >= 10:
    print("Challenge the advanced dungeon!")

# Example 4 
is_dragon_present = True
has_treasure = False

if is_dragon_present and not has_treasure:
    print("Enter with caution! Dragon ahead, but no treasure in sight!")
elif not is_dragon_present and has_treasure:
    print("No dragon around! Quick, grab the treasure!")
elif is_dragon_present and has_treasure:
    print("A mighty dragon guards the treasure! Tread carefully.")
else:
    print("Empty lair. Safe to explore, but no treasures here.")

# Potion Mixing Consequences
red_potion = True
blue_potion = False

if red_potion and not blue_potion:
    print("You get a potion of strength!")
elif not red_potion and blue_potion:
    print("You get a potion of speed!")
elif red_potion and blue_potion:
    print("Oops! Mixing red and blue makes it explode!")
else:
    print("No potion was mixed.")