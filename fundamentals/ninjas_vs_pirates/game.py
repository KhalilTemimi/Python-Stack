from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()
michelangelo.show_stats()
jack_sparrow.attack(michelangelo)

battle = True
while battle == True:
    if (jack_sparrow.health>0 and michelangelo.health>0):
        choice = input("\nshoose the player you want to attack\n")
        if (choice == "jack sparrow"):
            michelangelo.attack(jack_sparrow)
            jack_sparrow.show_stats()
            michelangelo.show_stats()
        elif (choice == "michelangelo"):
            jack_sparrow.attack(michelangelo)
            jack_sparrow.show_stats()
            michelangelo.show_stats()
        else:
            print (f"there is no player called {choice}")
    elif(jack_sparrow.health<=0):
        print(f"Game over!!!  {michelangelo.name} is the WINNER!!!\n")
        battle = False
    elif(michelangelo.health<=0):
        print(f"Game over!\n {jack_sparrow.name} is the WINNER!!!")
        battle = False