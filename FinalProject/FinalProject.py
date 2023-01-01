import sys

if __name__ == "__main__":
    #Introduction to the world and where you currently are and where you can go
    print("You wake up in a barely lit room. There is a small chill in the room.")
    print("As you stand up you see that to your left, there were 2 huge pure white doors that shined golden that felt somewhat heavenly and divine. To the left of the doors was a tall statue of an angel, her eyes covered in a bandage. It's wings made it seem like it was flying as it held scale in it's right hand up and high and in its left hand, a sword held near her chest.")
    print("To your right, there were 2 huge pure black doors that shined red that felt ominous and demonic, the opposite of the last one. To the left of the doors was a statue of an angel on her knees. Her eyes were bleeding blood as she held the hilt of a sword pierced through her chest.")
    #Choosing your name and the special names that gain certain privliges and unlock certain interactions
    Winners = ["Deez Nuts","Your Mom","Why Should I Tell You?"]
    Losers = ["Matthew","Zola","Brett","Declan","David","Sasha","Leen","Saif Sucks","Saif is Cringe","Not Sasha","Saif is Rubbish","Declan Lynch"]
    Saif = ["Saif","saif","Lord of the Void, the Abyssal Monarch, Saif","Lord of the Void, Saif"]
    print("A message appears infront of you hovering that says: What is thy name, one who dares to try to escape their eternal prison?")
    name = input()
    if name in Winners:
        print("Victory!!! Now leave, I gotta greet the next tortured soul.")
        sys.exit()
    if name == "Piss Master 14, the 5th Lord of Bathania":
        print("Oh my god, it's you your holiness. This humble god greets the 5th Lord of Bathania, one who rules over the great toilet water lakes of the east and the never ending sewers of the west, Piss Master 14, the divin lord of Piss. It seems you were sent here by mistake. I will make sure to fire whoever put you here. Here, I'll send your holiness back to Bathania.")
        sys.exit()
    if name in Saif:
        print("Wait? Why the hell are you here? You made this damn world, so you shouldn't even be here. Get out, just because you made us all doesn't mean you can make my job even harder for me so please leave.")
        sys.exit()
    if name in Losers:
        print("You have been killed it seems like you were meant to be sent to the execution realm to be killed but were sent here instead, you're soul shall be put in a jar and kept in the janitors bathroom for the rest of eternity.")
        sys.exit()
    print("Welcome, " +name+ " to your eternal prison. May luck be with you, one who dares try to escape from their eternal resting place but do remember, they all will try to stop you!")
    #Choosing your weapon
    print("But before you go you might consider choosing a weapon it might assist you in your adventure")
    print("Choose a Weapon: Spear, Staff, Sword, Bow and Arrow, Dagger","Fists","Gun")
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


