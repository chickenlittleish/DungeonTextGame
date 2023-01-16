import sys
import time


class Challenger():
    def __init__(self):
            self.name = name
            self.equipped_weapon = None
            self.alive = True
            self.weapon_choices = weapon_list
            self.health = 100
            self.mana = 100
            self.divine_artificat = None
            self.divine_weapon = None
    
    def stats(self):
        print("Stats: ")
        print(f"Challenger ID: {self.name}")
        print(f"Weapon: {self.equipped_weapon}")
        print(f"Life Status: {self.alive}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")
        print(f"Divine Treasure: {self.divine_artificat} ")
        print(f"Divine Weapon: {self.divine_weapon}")

    def damage(self, amount):
            self.health -= amount
            print(f"{self.name} received {amount} damage")
            if self.health <=0:
                self.kill()
        
    def kill(self):
            print(f"{self.name} has died and entered the 6 channels of reincarnation.")

    def weapon(self):
        weapon_chosen = input("Choose a weapon to assist you in your feeble adventure: " + str(weapon_list))
        if weapon_chosen.lower() in weapon_list:
                self.equipped_weapon = weapon_chosen
        else:
            print("Hey I already provided you with a list. choose from it genius")

    def divine_artifact(self):
        print("'Sorry, that isn't an option, please choose either left or right.'")
        action1_1 = input()
        if action1_1.lower() == "break":
            print("Error")
            action1_2 = input()
            if action1_2.lower() == "break":
                print("'Which statue would you like to break? The left or right one? The rising angel or the fallen angel? But be warned, you can only choose one.")
                time.sleep(1)
                print("A screen appears infront of you that says heavenly or demonic, which shall you choose?")
                statue_break = input()
                if statue_break.lower() == "heavenly":
                    print("You walk over to the left statue of the angel with the scale and sword and with your " + self.equipped_weapon + " you strike the statue breaking it in 2")
                    time.sleep(1)
                    print("You've gained the divine artifact: Fragment of Brilliant Light")
                    self.divine_artificat = "Fragment of Brilliant Light"
                if statue_break.lower() == "demonic":
                    print("You walk over to the eight statue of the angel crying blood who is stabbing herself and with your " + self.equipped_weapon + " you strike the statue breaking it in 2.")
                    time.sleep(1)
                    print("You've gained the divine artifact: Horn of the Incarnation of Chaos")
                    self.divine_artificat = "Horn of the Incarnation of Chaos"

if __name__ == "__main__":
    while True:
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
        print("A message appears infront of you hovering that says: What is thy name, one who dares to try to escape their eternal prison?")
        name = input()
        #These are names that just win automatically. It also causes some annoyance to a certain person
        if name.lower() in Winners:
            print("Victory!!! Through favoritism and bribing you have been allowed to leave the prison, now leave, I gotta greet the next tortured soul. God, why did Jerry have to quit there's only like 5 gods in charge of torturing souls and now I have to finish his weekly quota. Screw you Jerry.")
            sys.exit()
        #He just wins. No questions asked.
        if name.lower() == "piss master 14, the 5th lord of bathania":
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
                    time.sleep(1)
                    print("Purgatory System: Removed")
                    continue
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
        else:
            #chollenger = Challenger() fix it bitch change position
            print("Welcome, " + name + " to your eternal prison. May luck be with you, one who dares try to escape from their eternal resting place but do remember, they all will try to stop you!")
            time.sleep(3)
            #This is where you choose your weapon
            print("But before I leave you to your eternal suffering, I'll take pity on you and allow you to choose a weapon to assisst you but it won't change a thing, you won't ever be able to escape, no one has.")
            weapon_list = ["spear","magic staff","sword","bow and arrow","dagger","shield","gauntlets","axe"]
            chollenger = Challenger()
            chollenger.weapon()
            print("A screen appears infront of you.")
            time.sleep(1)
            print("'You may now choose to go through the left door or right door.")
            time.sleep(1)
            print("Your 2 choices are: left or right.")
            action1 = input()
            action1list = ["left","right","break"]
            if action1.lower() in action1list:
                if action1.lower() == "left":
                    print("'You decide to go through the pure white gate. May luck be with you challenger, one who tries to challenge the will of the heavens.")
                    time.sleep(1)
                    print("The screen disappears as you walk to the white gate and push it open.")
                    time.sleep(1)
                    print("As it opens, you cover your eyes as a blinding light shines and you proceed into the gate as it locks behind you")
                    Heavens_Will()
                if action1.lower() == "right":
                    print("'You decide to go through the pure black gate. May luck be with you challenger, one who tries to challenge the very labyrinth of hell.'")
                    time.sleep(1)
                    print("The screen disappears as you walk to the black gate and push it open.")
                    time.sleep(1)
                    print("As it opens, a torrent of hot air hits you as you cover your face to protect yourself and proceed into the gate as it locks behind you")
                    Hells_Eternal_Grasp()
                if action1.lower() == "break":
                    chollenger.divine_artifact()
            else:
                while action1.lower() not in action1list:
                    print("'Please choose one of the options provided to you.'")
                    action1 == input()

        



