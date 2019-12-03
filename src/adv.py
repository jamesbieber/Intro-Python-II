from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'passage':   Room("Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'chamber': Room("Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'compass': Item("Compass",
                    "The compass is broken. Not very useful."),

    'cup': Item("Cup",
                "The cup has a light, subtle vinegar smell. There's also lipstick on it."),

    'ring': Item("Ring",
                 "The gem is flawless despite the rest of the ring's condition."),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].addItem(item['compass'])
# room['outside'].addItem(item['cup'])
# room['outside'].addItem(item['ring'])


room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['passage']
room['foyer'].addItem(item['cup'])
room['foyer'].addItem(item['ring'])

room['overlook'].s_to = room['foyer']
room['passage'].w_to = room['foyer']
room['passage'].n_to = room['chamber']
room['chamber'].s_to = room['passage']

# print(room['outside'].n_to.name)C
#
# Main
#
player = Player('James', room['outside'])
print(
    f'Wecome to generic_adventure_game! you are at {player.current_room}\n')

game = True
while game:
    try:
        # print(f'You are currently {player}')
        selection = input(
            "Choose a direction to go N, E, W, S or Z to Exit:  \nIf there are items, try 'get *item*' to pick up: ").capitalize()
        print("\n*****" + selection + "*****")
        # print(player.current_room.items[0].name)  # Compass
        # print(player.current_room.name)  # Outside
        # print(player.current_room.items) # Item at item object
        if selection == 'N':
            player.move_player(selection)
        elif selection == 'E':
            player.move_player(selection)
        elif selection == 'S':
            player.move_player(selection)
        elif selection == 'W':
            player.move_player(selection)
        elif selection == 'I' or selection == "Inventory":
            player.show_inventory()
        elif 'Get' in selection:
            thing = (item[selection.split()[1]])
            if thing in player.current_room.items:
                player.pick_up(thing)
                room[player.current_room.name.lower()].removeItem(thing)
            else:
                print(f'Cant find {thing.name} in this room.')
        elif 'Drop' in selection:
            thing = (item[selection.split()[1]])
            if thing in player.inventory:
                player.drop(thing)
                room[player.current_room.name.lower()].addItem(thing)
            else:
                print(f'You dont have a {thing} to drop.')
        elif selection == 'Z':
            game = False
        else:
            print("Please enter a valid choice")
    except Exception as inst:
        print(inst)
        # if room[{player.current_room}]
        # * Prints the current room name
        # * Prints the current description (the textwrap module might be useful here).
        # * Waits for user input and decides what to do.
        #
        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        #
        # If the user enters "q", quit the game.
