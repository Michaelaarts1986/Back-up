
print (
    "hello world" #string
)

#Klasse
class Fitnesscentrum:
                def __init__(self, ruimtes, staff,  trainingtools, m2):
                        self.ruimtes = ruimtes
                        self.staff = staff
                        self.trainingtools = trainingtools
                        self.m2 = m2
                    
            

# Init functie is een contructor


#instantie
Fit = Fitnesscentrum(3,10,["krachtmachine", "dumbells"],500)


class Sporter():
    #constructor for initialization
    def __init__(self, name, age, sport):
            self.name = name
            self.age = age
            self.sport = sport
    #instance method
    def data_sporter(self):
        print('Naam van sporter : ', self.name)
        print('Voorkeur sport : ', self.sport)

#instantie
Sporter1 = Sporter("Angela",30,"hardlopen")
    

 
print (
        Sporter1.age
)
