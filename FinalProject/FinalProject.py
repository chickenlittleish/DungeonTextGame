import sys
import time


class Challenger():
    def __init__(self):
            self.name = name
            self.equipped_weapon = None
            self.alive = True
            self.weapon_choices = weapon_list
            self.health = 100
            self.divine_treasure = None

    def damage(self, amount):
            self.health -= amount
            print(f"{self.name} received {amount} damage")
            if self.health <=0:
                self.kill()
        
    def kill(self):
            print(f"{self.name} has died and entered the 6 channels of reincarnation.")

    def __str__(self):
            return self.name  

    def weapon(self):
        weapon_chosen = input("Choose a weapon to assist you in your feeble adventure: " + str(weapon_list))
        if weapon_chosen in weapon_list:
                self.equipped_weapon = weapon_chosen
        else:
            print("Hey I already provided you with a list. choose from it genius")

   #def divine_gift(self): 

if __name__ == "__main__":
    #Introduction to the world and where you currently are and where you can go
    print("You wake up in a barely lit room. There is a small chill in the room.")
    print(" ")
    time.sleep(3)
    print("As you stand up you see that to your left, there were 2 huge pure white doors that shined golden that felt somewhat heavenly and divine. To the left of the doors was a tall statue of an angel, her eyes covered in a bandage. It's wings made it seem like it was flying as it held scale in it's right hand up and high and in its left hand, a sword held near her chest.")
    print(" ")
    time.sleep(8)
    print("To your right, there were 2 huge pure black doors that shined red that felt ominous and demonic, the opposite of the last one. To the left of the doors was a statue of an angel on her knees. Her eyes were bleeding blood as she held the hilt of a sword pierced through her chest.")
    print(" ")
    time.sleep(8)
    #Choosing your name and the special names that gain certain privliges and unlock certain interactions
    Winners = ["mr. bowman", "phil","bowman","phil bowman"]
    Losers = ["matthew","zola","brett","declan","david","sasha","leen","saif sucks","saif is cringe","not sasha","saif is rubbish","declan lynch"]
    Saif = ["saif"]
    print("A message appears infront of you hovering that says: What is thy name, one who dares to try to escape their eternal prison?(Use capital for every word)")
    name = input()
    #These are names that just win automatically. It also causes some annoyance to a certain person
    if name.lower() in Winners:
        print("Victory!!! Through favoritism and bribing you have been allowed to leave the prison, now leave, I gotta greet the next tortured soul. God, why did Jerry have to quit there's only like 5 gods in charge of torturing souls and now I have to finish his weekly quota. Screw you Jerry.")
        sys.exit()
    #He just wins. No questions asked.
    if name == "Piss Master 14, the 5th Lord of Bathania":
        print("Oh my god, it's you your holiness. This humble god greets the 5th Lord of Bathania, one who rules over the great toilet water lakes of the east and the never ending sewers of the west, Piss Master 14, the divin lord of Piss. It seems you were sent here by mistake. I will make sure to fire whoever put you here. Here, I'll send your holiness back to Bathania.")
        sys.exit()
    #These are names that lose automatically because it was funny.
    if name.lower() in Losers:
        print("You have been killed it seems like you were meant to be sent to the execution realm to be killed but were sent here instead, you're soul shall be put in a jar and kept in the janitors bathroom for the rest of eternity.")
        sys.exit()
    #This is a fun easter egg if you put my name in that involves some problems
    if name.lower() in Saif:
        print("Administrator Detected")
        time.sleep(2)
        print("Administrator 0: Saif")
        time.sleep(2)
        print("Booting up administrator system")
        time.sleep(10)
        print("Transfering from purgatory system ver 1.03.24 to administrator system")
        time.sleep(6)
        print("Activating administrator assisstant Kiser")
        time.sleep(7)
        print("Verification required, please enter the system key")
        system_key = input()
        if system_key == "residentofthefinalgate":
            print("How may I assisst you, administrator " + name + "?")
            administrator_privileges = input()
            print(" ")
            if administrator_privileges == "activate: reset of purgatory system ver 1.03.24":
                print("Command received, purgatory system ver 1.03.24 reseting has been initiated")
                time.sleep(15)
                print(" ")
                print("reset completed")
                print("Purgatory System: Removed")
                sys.exit()
                #find out how to reset the code
            if administrator_privileges == "activate: erasure process ver 1.2":
                print("Error, command outside of administrator privileges, erasure not granted")
                code = input()
                print(" ")
                if code == "activate: oblivion override of purgatory system ver 1.03.24 use key: Final Order of King Noebius":
                    print("Override activated, privilige granted to administrator " + name + " by order of King Noebius. Erasure of system has been activated.")
                    time.sleep(10)
                    sys.exit()
                else:
                    print("Command not applicable. Administrator system defense protocol activated: shutting down program.")
                    sys.exit()
        else:
            #fix it as it doesn't it prints the code after as well and this is for alls the elses
            print("Command not applicable. Administrator system defense protocol activated: shutting down program.")
            sys.exit()
    print("Welcome, " + name + " to your eternal prison. May luck be with you, one who dares try to escape from their eternal resting place but do remember, they all will try to stop you!")
    #This is where you choose your weapon
    print("But before you go you might consider choosing a weapon it might assist you in your adventure")
    weapon_list = ["Spear","Staff","Sword","Bow and Arrow","Dagger"]
    chollenger = Challenger()
    chollenger.weapon()
    



