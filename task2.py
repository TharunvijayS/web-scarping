class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_name(self):
        return self.name.upper()

    def get_age(self, current_year):
        age = current_year - self.birth_year
        return age



current_year =2023
names=User(name='john',birth_year=1999)
john=names.get_age(current_year)
print(john)

names=User(name='john',birth_year=1999)
john_upper = names.get_name() 
print(john_upper)