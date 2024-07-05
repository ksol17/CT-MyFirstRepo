is_daytime = False
is_raining = False

if is_daytime:
    print("Take the sunny path throught the meadow!")
elif is_raining:
    print("Take the raining path throught the marsh!")
else:
    print("Neither path is suitable right now. Use your compass and head back home!")


# Weather Wardrobe Guide
is_raining = True
is_cold = False

if is_raining and is_cold:
    print("Wear a waterproof jacked and a scarf!")
elif is_raining:
    print("Don't forget your umbrella!")
else:
    print("Looks like a clear day, dress as you wish!")

# Monthly Savings Calculator
income = 5000
expenses = 4500

savings = income - expenses

if savings > 1000:
    print("Great job! You saved a lot this month.")
elif savings <= 0:
    print("Looks like you've spent all or more than you earned!")
else:
    print("Every little bit counts! Keep saving.")

# Example 3: Museum Entry Discounts
is_student = True
is_senior = False

if is_student:
    print("You get a 50% student discount!")
elif is_senior:
    print("Seniors enjoy a 40% discount!")
else:
    print("Regular entry fee applies.")

# Example 4: Weekend Activity Planner
is_sunny = True
have_money = False

if is_sunny and not have_money:
    print("Great day for a walk in the park!")
else:
    print("Maybe consider indoor activities or saving for a sunny day outing.")

# Example 5  Game Character Interaction
is_friendly = False 
has_quest = True

if not is_friendly:
    print("Be cautious! This character might not be helpful.")
elif has_quest:
    print("This character has a quest for you!")
else:
    print ("Just a regular villager passing by.")

# Example 6 Drive-Thru Order Suggestion
wants_veggie = True
likes_spice = False

if wants_veggie and likes_spice:
    print("How about a spicy veggie wrap?")
elif wants_veggie:
    print("Try our classic veggie burger!")
else:
    print("Check out our grill menu!")