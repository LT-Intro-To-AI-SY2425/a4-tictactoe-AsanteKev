# object oriented programming

# (define-struct dog [fur_color name age favorite_food])
#The constuctor refers to 

class Dog: 
    #species = "Canislupus"
    def __init__(self, n, a):
        self.name = n 
        self.age = a
        self.fetch_count = 0
    
    
#-> returns string
def __str__(self) -> str:
    s = f"{self.name} is {self.age} years old"
    #return s


def __playfetch__(self, num_fetch):
    self.fetch_count += num_fetch


def __resetfetch__(self):
    self.fetch_count = 0


#Three instances of the dog class
logan = Dog("logan", 8)
#cookie = Dog("cookie", 8)
#maple = Dog("maple", 1)

logan.playfetch(6)

#print(logan.fetch_count)
#print(cookie)
#print(maple)