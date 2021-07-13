# ==============================================
# =                 Task 1                     =
# ==============================================       

class Car:
    def __init__(self, model, year, engine, color, price):
        self.brend = "Toyota"
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.price = price    

    def get_info(self):
        return f'This is {self.brend} - {self.model}, {self.year} year of \
            release. Engine = {self.engine}, color is {self.color}.'
    
    def get_price(self):
        return f'The price = {self.price}'

camry = Car(
    model= 'Camry', 
    year= 2015, 
    engine= '3.5', 
    color = 'red', 
    price = 14000
    )

rav4 = Car(
    model= 'rav4',
    year= 2012, 
    engine= '2.5', 
    color = 'brown', 
    price = 11000
    )

chr = Car(
    model= 'chr', 
    year= 2019, 
    engine= '2.0', 
    color = 'blue', 
    price = 23400
    )

print(camry.get_info())
print(camry.get_price())

print(rav4.get_info())
print(rav4.get_price())

print(chr.get_info())
print(chr.get_price())


# ======================================================
# =                     Task 2                         =
# ======================================================

class Library:
    def __init__(self, name, year, autor,genre, price):
        self.name = name
        self.year = year
        self.autor = autor
        self.genre = genre
        self.price = price

    def get_year(self):
        return f'The {self.name} was written in {self.year}'

    def get_autor(self):
        return f'The {self.name} was written by {self.autor}'

    def get_genre(self):
        return f'The {self.name} is a {self.genre}'

    def get_price(self):
        return f'The cost is {self.price}'

lolita = Library(
    name = 'Lolita', 
    year = 1953, 
    autor = 'Vladimir Nabokov', 
    genre = 'novel', 
    price = 50
    )

shantaram = Library(
    name = 'Shantaram', 
    year = 1993, 
    autor = 'Gregory David Roberts', 
    genre = 'novel', 
    price = 75
    )

print(lolita.get_year())
print(lolita.get_autor())
print(lolita.get_genre())
print(lolita.get_price())


print(shantaram.get_year())
print(shantaram.get_autor())
print(shantaram.get_genre())
print(shantaram.get_price())


# ======================================================
# =                  Task 3                            =
# ======================================================

class Stadium:
    def __init__(self, name, year, country, city, capacity):
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.capacity = capacity

    def get_year(self):
        return f'The {self.name} was opened in {self.year}'
    
    def get_location(self):
        return f'The {self.name} located in {self.country}, \
            {self.city}'

    def get_capacity(self):
        return f'This stadium has {self.capacity} seats'

olimpic_stadium = Stadium(
    name = 'NSC "Olympic"', 
    year = 1923, 
    country = 'Ukraine', 
    city = 'Kyiv', 
    capacity = 70500
    )

camp_nou = Stadium(
    name = 'Camp Nou', 
    year = 1957, 
    country = 'Spain', 
    city = 'Barselona', 
    capacity = 99354
    )

print(olimpic_stadium.get_year())
print(olimpic_stadium.get_location()) 
print(olimpic_stadium.get_capacity()) 

print(camp_nou.get_year())    
print(camp_nou.get_location()) 
print(camp_nou.get_capacity()) 