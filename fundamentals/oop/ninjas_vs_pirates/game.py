from urllib import response
from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")
naruto = Ninja("Naruto")
jacob = Ninja("Jacob")
shay = Ninja("Shay")


jack_sparrow = Pirate("Jack Sparrow")
maverick = Pirate("Maverick")
reece = Pirate("Reece")
kyva = Pirate("Kyva")
leo = Pirate("Leo")
koda = Pirate("Koda")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

while(True):
    response = input ("Select your character: \n 1) Michelangelo \n 2) Naruto \n 3) Jacob")
    if response == '1':
        while(michelangelo.health > 0 and jack_sparrow.health > 0):
            response = input("You're Michelanglo, will you attack or defend? \n 1) attack \n 2) meditate")