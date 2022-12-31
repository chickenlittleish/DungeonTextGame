import sys


if __name__ == "__main__":
    print("what's your name?")
    name = input()
    print("You wake up in a dark room. You feel cold and out of a sudden, torches around the room light up.")
    print("You see a pure white door to your left with an angel holding a scale in its left arm high above its head and its other hand holding a sword.")
    print("To your right, you see a pure black door with a pure black angel with blood coming out of its eyes with its hands holding a sword going through its chest.")
    print("Choose a Weapon: Spear, Staff, Sword, Bow and Arrow, Dagger")
    weapon_choice = ["Spear","Staff","Sword","Bow and Arrow","Dagger"]
    weapon_user_choice = input()
    print("(" + name + " you must choose a path to go through)")
    list_choices_1 = ["left","right","break"]
    choice_1 = input()
    if choice_1 == "left":
        print("You stand up and walk through the pure white door.")
    if choice_1 == "right":
        print("You stand up and walk through the pure black door.")
    if choice_1 == "break":
        print("Which statue would you like to break? The left one or the right one?")
        statue_choice_list = ["left","right"]
        statue_choice = input()
        if statue_choice == "left":
            print("You walk over to the left statue.")
        if statue_choice == "right":
            print("You walk over to the right statue.")
    sys.exit()