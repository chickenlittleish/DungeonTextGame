import sys

if __name__ == "__main__":
    print("You wake up in a barely lit room. There is a small chill in the room.")
    print("As you stand up you see that to your left, there were 2 huge pure white doors that shined golden that felt somewhat heavenly and divine. To the left of the doors was a tall statue of an angel, her eyes covered in a bandage. It's wings made it seem like it was flying as it held scale in it's right hand up and high and in its left hand, a sword held near her chest.")
    print("To your right, there were 2 huge pure black doors that shined red that felt ominous and demonic, the opposite of the last one. To the left of the doors was a statue of an angel on her knees. Her eyes were bleeding blood as she held the hilt of a sword pierced through her chest.")
    print("A message appears infront of you hovering that says: What is thy name, one who dares to try to escape their eternal prison?")
    Winners = ["Deez Nuts","Your Mom","Why Should I Tell You?","I Gotta Piss","Saif","Piss Master 14 the 5th Lord of Bathania"]
    Losers = ["Matthew","Zola","Brett","Declan","David","Sasha","Leen","Saif Sucks","Saif is Cringe","Not Sasha","Saif is Rubbish","Declan Lynch"]
    name = input()
    if name in Winners:
        print("Victory!!! Now leave I gotta greet the next tortured soul.")
        sys.exit()
    if name in Losers:
        print("You have been killed it seems like you were meant to be sent to the execution realm to be killed but were sent here instead, you're soul shall be put in a jar and kept in the bathroom for the rest of eternity.")
        sys.exit()
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




