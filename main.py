#  DEFINE YOUR FUNCTIONS HERE

# PART A: Functions with no argument + no return
def welc_msg():
    print("Welcome to cooking with Paige!")
    print("Today we will be making a caprese sandwhich 🥪")

# PART B: Functions with arguments + no return 
def store_bread(choosen_bread):
    print(f"You're in a bakery! 🥖")
    print(f"You have to choose which bread you want for for your sandwhich.")
    print(f"As you walk through, you see baguettes, rolls, and so much more.")
    print(f"You spend a lot of time pondering, but ultimately pick {choosen_bread}.")
    

def toast_bread():
    print(f"Take your bread and cut it in half")

def main():
    print("hello world")
    
    bread = "ciabatta"
    store_bread(bread)
    # CAL YOUR FUNCTIONS in the main

if __name__ == "__main__":
    main()
