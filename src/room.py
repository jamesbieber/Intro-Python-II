# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=None, n_to=[], e_to=[], s_to=[], w_to=[]):
        self.name = name
        self.description = description
        if items is None:
            self.items = []
        else:
            self.items = items
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to

    def removeItem(self, item):
        self.items.remove(item)

    def addItem(self, item):
        self.items.append(item)

    def __str__(self):
        output = f'{self.name} - {self.description}'

        if(len(self.items) > 1):
            i = 0
            output += f'. There appears to be a '
            while(i < len(self.items) - 2):
                output += f'{self.items[i].name}, a '
                i += 1
            output += f'{self.items[i].name}, a'
            output += f'nd a {self.items[i+1].name}'
        elif(len(self.items) == 1):
            output += f'. There appears to be a {self.items[0].name}'
        elif(len(self.items) == 0):
            pass

        return output
