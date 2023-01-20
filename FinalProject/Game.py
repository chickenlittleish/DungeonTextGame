import sys
import time

def Calling_Heavens_Will():
    print("'You decide to go through the pure white gate. May luck be with you challenger, one who tries to challenge the will of the heavens.")
    time.sleep(1)
    print("The screen disappears as you walk to the white gate and push it open.")
    time.sleep(1)
    print("As it opens, you cover your eyes as a blinding light shines and you proceed into the gate as it locks behind you.")
    Heavens_Will()

def Heavens_Will():
    print("As you pass through the gate. You are immediately blocked by a pay wall stating you don't have access to the Heavenly Realm Expansion")
    time.sleep(6)
    print("Just kidding Just kidding. This is still a work in development so it will be added later but I wanted to say thanks for playing this small little project")
    sys.exit()

def Calling_Hells_Eternal_Grasp():
    print("'You decide to go through the pure black gate. May luck be with you challenger, one who tries to challenge the very labyrinth of hell.'")
    time.sleep(1)
    print("The screen disappears as you walk to the black gate and push it open.")
    time.sleep(1)
    print("As it opens, a torrent of hot air hits you as you cover your face to protect yourself and proceed into the gate as it locks behind you.")
    Hells_Eternal_Grasp()

def Hells_Eternal_Grasp():
    print("As you pass through the gate. You are immediately blocked by a pay wall stating you don't have access to the Heavenly Realm Expansion")
    time.sleep(6)
    print("Just kidding Just kidding. This is still a work in development so it will be added later but I wanted to say thanks for playing this small little project")
    sys.exit()

def AdministratorDeath1():
    print("'The impudence.'")
    time.sleep(1)
    print("You hear as you suddenly feel yourself flying. Then you see it, your body is still chained up and the adminsitrator is behind you. He cut off you head.")
    time.sleep(3)
    print("A screen suddenly appears in front of you.")
    chollenger.kill()


def Confrontation1():
    print("'Error. Breech of plausability has been detectected. Calling administrator.'")
    print("The screen that appeared glitched out as you saw a bit of light appearing before you. A crack was forming in the space above you as you.")
    time.sleep(4)
    print("You see a being emerge from the crack as a man with horns and angel wings in a suit emerged from it.")
    print("A screen appeared infront of you.")
    print("Error")
    time.sleep(1)
    print("Error")
    time.sleep(1)
    print("Administrator detected in prison.")
    time.sleep(2)
    print("Administrator identified as Administrator Xyron of the Central Star Bureau. Notifying hig-")
    print("'I swear that system is always so annoying, I told them we should remove it.'")
    time.sleep(3)
    print("'So I guess you're the anomoly that broke the plausability of'. As he said this he looked up at you and snapped his fingers.")
    time.sleep(6)
    print("Out of nowhere chain appeared and held you in place. You couldn't move at all.")
    time.sleep(3)
    print("'Listen here, I'm currently busy dealing with the mess that Apollo caused in the Greek sector so I don't have the time to deal with this. Now explain, how the hell does a mere mortal know of secrets that only administators know of?'")
    time.sleep(3)
    print("'Like do you know how much of a mess we're in right now due to you? This is even worse than what Apollo, that drunk screw-up did. You've breeched the plausability of this prison to the point that now the higher-ups are demanding for a check of the fairness of this prison and it's trials.'")
    confrontation = input()
    confrontationlist = ["talk", "stay silent", "spit", "try to break free"]
    if confrontation in confrontationlist: 
        if confrontation == "talk":
            print("'Explain Now!' He demands.")
            confrontation1_2 = input()
            confrontation1_2list = ["fair?","lie"]
            if confrontation1_2 in confrontation1_2list:
                if confrontation1_2 == "lie":
                    AdministratorDeath1()
                if confrontation1_2 == "fair?":
                    print("'What did you say? You yell at him.")
                    print("You respond that this prison was never fair to begin withand that he has no right to talk about fairness when he literally accepts bribes from the Chinese sector and the Indian sector to make the prison harder for certain contestants you greedy bastard.")
                    time.sleep(7)
                    print("You then mention how it also breaks the rules of the prison for an administrator to descend in their true form infront of a contestant so what would happen if you were to report him now? So unless he wants to get reported and deleted, he should leave and stay silent.")
                    time.sleep(9)
                    print("'Fine you win this time but the next time you get reported will be your last.'")
                    print("He walks back through the crack in space as it closes up behind him.")
                    chollenger.divine_weapon_making()
                else:
                    AdministratorDeath1()
        if confrontation == "stay silent":
            AdministratorDeath1()
        if confrontation == "spit":
            AdministratorDeath1()
        if confrontation == "try to break free":
            AdministratorDeath1()
    else:
        AdministratorDeath1()



class Challenger():
    def __init__(self):
            self.name = name
            self.equipped_weapon = None
            self.alive = True
            self.weapon_choices = weapon_list
            self.health = 100
            self.mana = 100
            self.possessed_divine_artifact = None
            self.divine_weapon = None
    
    def stats(self):
        print("Stats: ")
        print(f"Challenger ID: {self.name}")
        print(f"Weapon: {self.equipped_weapon}")
        print(f"Life Status: {self.alive}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")
        print(f"Divine Treasure: {self.possessed_divine_artifact} ")
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
        if action1_1.lower() == "break them":
            print("Error")
            action1_2 = input()
            if action1_2.lower() == "break that which seals the truth of reality":
                print("'Which statue would you like to break? The left or right one? The rising angel or the fallen angel? But be warned, you can only choose one.'")
                time.sleep(1)
                print("A screen appears infront of you that says heavenly or demonic, which shall you choose?")
                statue_break = input()
                if statue_break.lower() == "heavenly":
                    print("You walk over to the left statue of the angel with the scale and sword and with your " + self.equipped_weapon + " you strike the statue breaking it in 2")
                    time.sleep(1)
                    print("You've gained the divine artifact: Brightest Fragment of the 9th Brilliant Light, Ariel")
                    self.possessed_divine_artifact = "Brightest Fragment of the 9th Brilliant Light, Ariel"
                if statue_break.lower() == "demonic":
                    print("You walk over to the right statue of the angel crying blood who is stabbing herself and with your " + self.equipped_weapon + " you strike the statue breaking it in 2.")
                    time.sleep(1)
                    print("You've gained the divine artifact: Horn of the Incarnation of Chaos, Baphomet")
                    self.possessed_divine_artifact = "Horn of the Incarnation of Chaos, Baphomet"

    def God_Weapons(self):
        if self.possessed_divine_artifact == "Horn of the Incarnation of Chaos, Baphomet":
            if self.equipped_weapon == "spear":
                print("You're 3 choices are: ")
                print("1) Point of Decemation")
                print("2) Chaos Origin Spear")
                print("3) Chaotic Hellfire Spear")
                God_weapon = input()
                God_weapon_list = ["point of decemation", "chaos origin spear", "chaotic hellfire spear"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")
            if self.equipped_weapon == "magic staff":
                print("You're 3 choices are: ")
                print("1) Eternal Fire Staff")
                print("2) Primordial Chaos Staff")
                print("3) Hell Summoning Staff")
                God_weapon = input()
                God_weapon_list = ["eteral fire staff", "primordial chaos staff", "hell summoning staff"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")
            if self.equipped_weapon == "sword":
                print("You're 3 choices are: ")
                print("1) Soul Splitting Blade")
                print("2) Sword of 6 Reincarnations")
                print("3) Blade of a 1000 Sufferings")
                God_weapon = input()
                God_weapon_list = ["soul splitting blade", "sword of 6 reincarnations", "blade of a 1000 sufferings"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")
            if self.equipped_weapon == "bow and arrow ":
                print("You're 3 choices are: ")
                print("1) Soul Chasing Arrow")
                print("2) Cloud Piercer")
                print("3) Void Shattering Bow")
                God_weapon = input()
                God_weapon_list = ["soul chasing bow", "cloud piercer", "void shattering bow"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")
            if self.equipped_weapon == "dagger":
                print("You're 3 choices are: ")
                print("1) Sickles of Death")
                print("2) Baphomets Fangs")
                print("3) Prmordial Blood Daggers of the First Demon")
                God_weapon = input()
                God_weapon_list = ["Sickles of Death", "baphomets fangs", "primordial blood daggers of the first demon"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")

            if self.equipped_weapon == "shield":
                print("You're 3 choices are: ")
                print("1) Hells Barricade")
                print("2) Gates of Hell")
                print("3) Starved Gluttonous Shield")
                God_weapon = input()
                God_weapon_list = ["hells barricade", "gates of hell", "starved gluttonous shield"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")

            if self.equipped_weapon == "gauntlets":
                print("You're 3 choices are: ")
                print("1) Soul Grasping Fist")
                print("2) Chains of Hell")
                print("3) Claws of Cerberus")
                God_weapon = input()
                God_weapon_list = ["soul grasping fist", "chains of hell", "claws of cerberus"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")

            if self.equipped_weapon == "axe":
                print("You're 3 choices are: ")
                print("1) Executioner of Life")
                print("2) Soul Severing Axe")
                print("3) Blood Gods Fury")
                God_weapon = input()
                God_weapon_list = ["executioner of life", "soul severing axe", "blood gods fury"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")

        if self.possessed_divine_artifact == "Brightest Fragment of the 9th Brilliant Light, Ariel":
            if self.equipped_weapon == "spear":
                print("You're 3 choices are: ")
                print("1) Holy Light Gods Spear")
                print("2) Primordial Lightning Spear")
                print("3) World Piercer")
                God_weapon = input()
                God_weapon_list = ["holy light gods spear", "primordial lightning spear", "world piercer"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")

            if self.equipped_weapon == "magic staff":
                print("You're 3 choices are: ")
                print("1) Staff of the Constellation")
                print("2) Bifröst Caller")
                print("3) Branch of the World Tree")
                God_weapon = input()
                God_weapon_list = ["staff of the constellation", "bifröst caller", "branch of the world tree"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")

            if self.equipped_weapon == "sword":
                print("You're 3 choices are: ")
                print("1) Final Cut")
                print("2) Severance of Life and Death")
                print("3) Dawn of Judgement")
                God_weapon = input()
                God_weapon_list = ["final cut", "severance of life and death", "dawn of judgement"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + "."):

            if self.equipped_weapon == "bow and arrow":
                print("You're 3 choices are: ")
                print("1) Spirit Whisperer")
                print("2) Eternal Shining Light")
                print("3) Last Light of a Crumbling World")
                God_weapon = input()
                God_weapon_list = ["spirit whisperer", "eternal shining light", "last light of a crumbling world"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")
            
            if self.equipped_weapon == "dagger":
                print("You're 3 choices are: ")
                print("1) Fragments of Light")
                print("2) Sunforged Daggers")
                print("3) Moonlight Daggers")
                God_weapon = input()
                God_weapon_list = ["fragments of light", "sunforged daggers", "moonlight daggers"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")

            if self.equipped_weapon == "shield":
                print("You're 3 choices are: ")
                print("1) Wall of Light")
                print("2) Worlds Edge")
                print("3) Barrier of the Heavenly Realm")
                God_weapon = input()
                God_weapon_list = ["wall of light", "worlds edge", "barrier of the heavenly realm"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")

            if self.equipped_weapon == "gauntlets":
                print("You're 3 choices are: ")
                print("1) Divine Retribution")
                print("2) Wrath of the Gods")
                print("3) Divine Dragons Roar")
                God_weapon = input()
                God_weapon_list = ["divine retribution", "wrath of the gods", "divine dragons roar"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")

            if self.equipped_weapon == "axe":
                print("You're 3 choices are: ")
                print("1) Universal Severance")
                print("2) Divine Star Splitter")
                print("3) Fate Severing Axe")
                God_weapon = input()
                God_weapon_list = ["universal severance", "divine star splitter", "fate severing axe"]
                if God_weapon.lower() in God_weapon_list:
                    self.divine_weapon = God_weapon
                    print("You've chosen: " + God_weapon + " for your final crafted item. You now possess the " + God_weapon + ".")

            

    def divine_weapon_making(self):
        print("A screen appears infront of you.")
        time.sleep(1)
        print("Setting up crafting system.")
        time.sleep(1)
        print("Booting up Forge of the Stars")
        time.sleep(6)
        print("'Welcome to the forge of the world, also known as the crafting system, as you are the first of the 563rd generation to open the crafting system you get a prize: you're first try is free!'")
        time.sleep(7)
        print("'Now what what ingredients would you like to use?'")
        ingredient1list = [self.possessed_divine_artifact, self.equipped_weapon]
        print("Currently possessed ingredients:" + str(ingredient1list) + ". Please choose one these items or you could leave if you want.")
        ingredient1 = input()
        if ingredient1 == self.possessed_divine_artifact:
            print("Ingredient 1: " + self.possessed_divine_artifact + " has been used. Please choose ingredient 2.")
            print("Ingredients left: " + self.equipped_weapon)
            ingredient2 = input()
            if ingredient2.lower() == self.equipped_weapon:
                print("you have chosen: " + self.equipped_weapon + " as you 2nd ingredient. Combining " + self.equipped_weapon + " with " + self.possessed_divine_artifact + ". Please wait dear contestant.")
                time.sleep(7)
                print("Done. Your ingredients have been combined. You have 3 choices to choose from for your final crafted item.")
                self.God_Weapons()
                ingredient2 = input()
        if ingredient1.lower() == self.equipped_weapon:
            print("Ingredient 1: " + self.equipped_weapon + " has been used. Please choose ingredient 2.")
            print("Ingredients left: " + self.possessed_divine_artifact)
            ingredient2 = input()
            if ingredient2 == self.possessed_divine_artifact:
                print("you have chosen: " + self.possessed_divine_artifact + " as you 2nd ingredient. Combining " + self.possessed_divine_artifact + " with " + self.equipped_weapon + ". Please wait dear contestant.")
                time.sleep(7)
                print("Done. Your ingredients have been combined. You have 3 choices to choose from for your final crafted item.")
                self.God_Weapons()
                ingredient2 = input()
        if ingredient1 == "leave":
            print("Exiting crafting system and returning back to the prison.")
            print("A screen appears infront of you: 'Choose left or right.'")
            action2 = input()
            action2list = ["left","right"]
            if action2.lower() in action2list:
                if action2.lower() == "left":
                    Calling_Heavens_Will()
                if action2.lower() == "right":
                    Calling_Hells_Eternal_Grasp()
        else:
            print("That is not a valid option, please choose from the list provided")
            ingredient1 = input()
        



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
            print("0th Administrator of the system: Saif")
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
                print("Command not applicable. Administrator system defense protocol activated: shutting down program.")
                sys.exit()
        else:
            print("Welcome, " + name + " to your eternal prison. May luck be with you, one who dares try to escape from their eternal resting place but do remember, they all will try to stop you!")
            time.sleep(3)
            #This is where you choose your weapon
            print("But before I leave you to your eternal suffering, I'll take pity on you and allow you to choose a weapon to assisst you but it won't change a thing, you won't ever be able to escape, no one has.")
            weapon_list = ["spear","magic staff","sword","bow and arrow","dagger","shield","gauntlets","axe"]
            chollenger = Challenger()
            chollenger.weapon()
            print("A screen appears infront of you.")
            time.sleep(1)
            print("'You may now choose to go through the left door or right door.'")
            time.sleep(1)
            print("Your 2 choices are: left or right.")
            action1 = input()
            action1list = ["left","right","break the doors at the edge of the universe to unveil that which has been sealed away"]
            if action1.lower() in action1list:
                if action1.lower() == "left":
                    Calling_Heavens_Will()
                if action1.lower() == "right":
                    Calling_Hells_Eternal_Grasp()
                if action1.lower() == "break the doors at the edge of the universe to unveil that which has been sealed away":
                    chollenger.divine_artifact()
                    print("The same screen appears infront of you: 'Choose left or right.'")
                    action2 = input()
                    action2list = ["left","right","combine the 3 realms to shatter them and shatter them to combine them"]
                    if action2.lower() in action2list:
                        if action2.lower() == "left":
                            Calling_Heavens_Will()
                        if action2.lower() == "right":
                            Calling_Hells_Eternal_Grasp()
                        if action2.lower() == "combine the 3 realms to shatter them and shatter them to combine them":
                            if chollenger.possessed_divine_artifact.lower() == "Horn of the Incarnation of Chaos, Baphomet" or "Brightest Fragment of the 9th Brilliant Light, Ariel":
                                Confrontation1()
                            else:
                                print("'option does not exist.")
                                print("please choose a valid option: left or right.")
                                action1 = input()
            while action1.lower() not in action1list:
                print("'Please choose one of the options provided to you.'")
                action1 = input()

        

