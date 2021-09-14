class Element:
    def __init__(self, name, city, population):
        self.name = name
        self.city = city
        self.population = population
 
    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))
 
 
