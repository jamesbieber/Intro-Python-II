from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# print(room['outside'].n_to.name)
#
# Main
#
player = Player('James', room['outside'])
print(
    f'Wecome to generic_adventure_game! you are at {player.current_room}')

game = True
while game:
    try:
        # print(f'You are currently {player}')
        selection = input(
            "Choose a direction to go N, E, W, S to Exit:  \n").capitalize()
        if selection == 'N':
            player.move_player(selection)
        elif selection == 'E':
            player.move_player(selection)
        elif selection == 'S':
            player.move_player(selection)
        elif selection == 'W':
            player.move_player(selection)
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
