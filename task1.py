class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_name(self):
        return self.name.upper()

    def get_age(self, current_year):
        age = current_year - self.birth_year
        return age
