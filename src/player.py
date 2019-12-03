# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def __str__(self):
        output = f'You are currently {self.current_room.name}'
        return output

    def show_inventory(self):
        i = 0
        output = ""
        while i < len(self.inventory):
            output += self.inventory[i].name
            output += " "
            i += 1

        print(output)

    def pick_up(self, item):
        self.inventory.append(item)
        print(f'Picked up {item}.')

    def drop(self, item):
        self.inventory.remove(item)
        print(f'Dropped {item.name}.')

    def move_player(self, direction):
        if direction == 'N':
            if self.current_room.n_to == []:
                print("Can't move that direction")
            else:
                self.current_room = self.current_room.n_to
                print(
                    f'Player moved to {self.current_room}\n')
        elif direction == 'E':
            if self.current_room.e_to == []:
                print("Can't move that direction")
            else:
                self.current_room = self.current_room.e_to
                print(
                    f'Player moved to {self.current_room}\n')
        elif direction == 'S':
            if self.current_room.s_to == []:
                print("Can't move that direction")
            else:
                self.current_room = self.current_room.s_to
                print(
                    f'Player moved to {self.current_room}\n')
        elif direction == 'W':
            if self.current_room.w_to == []:
                print("Can't move that direction")
            else:
                self.current_room = self.current_room.w_to
                print(
                    f'Player moved to {self.current_room}\n')
        else:
            pass
