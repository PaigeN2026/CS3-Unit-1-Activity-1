#  DEFINE YOUR FUNCTIONS HERE

# PART A: Functions with no argument + no return
bread = "ciabatta"
cheese = "mozzarella"

def welc_msg():
    print(f"welcome to cooking with paige! ₍^. .^₎⟆")
    print(f"today we will be making a sandwhich")
    print(f"⋆｡‧˚ 🥪 ˚‧｡⋆")

# PART B: Functions with arguments + no return 
def store_bread(choosen_bread):
    print(f"you're in a bakery!")
    print(f"you have to choose which bread you want for for your sandwhich.")
    print(f"as you walk through, you see baguettes, rolls, and so much more.")
    print(f"you spend a lot of time pondering, but ultimately pick {choosen_bread}.") 
    print(f"⋆｡‧˚ 🥖 ˚‧｡⋆")
    

def toast_bread():
    print(f"you're back home now.")
    print(f"take your {bread} and cut it in half.")
    print(f"butter both sides, and place it on a warm skillet.")
    print(f"let it toast until golden brown.")
    print(f"⋆｡‧˚ 🧈 ˚‧｡⋆")

# PART D: Functions with optional arguments
def add_pesto(toasted_bread, pesto_typed="basil"):
    print(f"once your {toasted_bread} is toasted, take it off the skillet")
    print(f"now, spread your {pesto_typed} pesto along each slice") 
    print(f"and place the bread back on the skillet.")
    print(f"⋆｡‧˚ 🌿 ˚‧｡⋆")

def put_sandwhich_together():
    print(f"while the {bread} is on skillet, get your last two ingredients: cheese and tomato.")
    print(f"you look in your fridge, and all you have is {cheese}.")
    print(f"you cut the tomato and {cheese} into slices, and then put it on the bread.")
    print(f"now form the sandwhich, and leave it on the skillet until the cheese is melted.")
    print(f"ta-da! your sandwhich is done and ready to be eatnen.")
    print(f"⋆｡‧˚ 🍽️ ˚‧｡⋆")

# PART C: Functions with arguments + return
def sandwhich_name(bread_type, pesto_type, cheese_type):
    return f"{bread_type} + tomato + {pesto_type} + {cheese_type} equals a... caprese sandwhich! \nenjoy your meal ૮₍ ´ ꒳ `₎ა \n⋆｡‧˚ 🥗 ˚‧｡⋆"

# PART E: Review challenge
def make_sandwhich():
    welc_msg()
    store_bread(bread)
    toast_bread()
    add_pesto(bread)
    put_sandwhich_together()
    print(sandwhich_name(bread, "basil", cheese))


def main():
    make_sandwhich()
    
    # CAL YOUR FUNCTIONS in the main

if __name__ == "__main__":
    main()
