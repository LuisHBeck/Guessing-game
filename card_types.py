from card import Card

# VEHICLES
car = Card("Car")
car.add_tips("Has a windshield",
            "Has four doors",
            "Has four wheels",
            "Has five seats",
            "Needs a driver",)

motorcycle = Card("Motorcycle")
motorcycle.add_tips("Has two seats",
                    "Has two wheels",
                    "Has no doors",
                    "You can do a wheelie",
                    "Randandandandandan")


vehicles = [car, motorcycle]


#COUNTRY
brasil = Card('Brasil')
brasil.add_tips("Soccer",
                "Bad governments",
                "Rice and beans",
                "Street Carnival",
                "Samba")

germany = Card("Germany")
germany.add_tips("Robert Bosch was born",
                 "Bosch head office",
                 "Berlin Wall",
                 "First world country",
                 "Where the car was invented")


country = [brasil, germany]

vetores = Card('Valderrama')
vetores.add_tips("Vectors",
                "Engineer",
                "Earphone",
                "Black man",
                "German's driver")
               

john_peter = Card("Pedrinho")
john_peter.add_tips('Agitated person',
                    'Tkinter man',
                    'Crazy',
                    'Kid',
                    'Genius ideas')
           

people = [vetores, john_peter]


