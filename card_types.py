from card import Card

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


