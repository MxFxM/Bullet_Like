"""
The game map.

The map(s) feature destructable enviornment.
Also the texture changes depending on level.
"""

import random  # for random maps

# some constants to tune
SIZE_MIN = 20
ONE_ROOM_PER_THIS_SIZE = 7


class BL_MAP:
    """
    The map as a class.

    Layout code is:
    0: indestructable wall
    1: destructable wall
    2: empty floor
    """

    def __init__(self):
        """
        Creation of the map object.
        Also creates a map with the given parameters.
        """

        # size of the map
        self.X_SIZE = 20
        self.Y_SIZE = 20
        if self.X_SIZE < SIZE_MIN:
            self.X_SIZE = SIZE_MIN
        if self.Y_SIZE < SIZE_MIN:
            self.Y_SIZE = SIZE_MIN

        # layout is the map data
        self.layout = [[0 for x in range(self.X_SIZE + 2)]
                       for y in range(self.Y_SIZE + 2)]

        # this fills the in map data
        self.createMap("random")
        for y in range(self.Y_SIZE + 2):
            for x in range(self.X_SIZE + 2):
                print(self.layout[y][x], end="")
            print("")

    def createMap(self, floor):
        """
        Creates a map with the given parameters.
        """

        if floor == "random":
            # random map creation

            # the outer bounds are indestructable,
            # the rest gets filled with walls
            for x in range(1, self.X_SIZE + 1):
                for y in range(1, self.Y_SIZE + 1):
                    self.layout[y][x] = 1

            # number of rooms in map depending on map size
            x_rooms = int(self.X_SIZE / ONE_ROOM_PER_THIS_SIZE)
            y_rooms = int(self.Y_SIZE / ONE_ROOM_PER_THIS_SIZE)
            nr_rooms = x_rooms * y_rooms

            room_positions = []

            # create rooms
            for room in range(nr_rooms):
                room_x_size = random.randint(
                    2, int(self.X_SIZE/ONE_ROOM_PER_THIS_SIZE))
                room_y_size = random.randint(
                    2, int(self.Y_SIZE/ONE_ROOM_PER_THIS_SIZE))
                new_position = [random.randint(room_x_size+1, self.X_SIZE-room_x_size-1),
                                random.randint(room_y_size+1, self.Y_SIZE-room_y_size-1)]
                for x in range(new_position[0] - room_x_size, new_position[0] + room_x_size):
                    for y in range(new_position[1] - room_y_size, new_position[1] + room_y_size):
                        self.layout[y][x] = 2
                room_positions.append(new_position)
                print(new_position, room_x_size, room_y_size)

            # create corridors between rooms !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            for room in range(nr_rooms - 1):
                for x in range(room_positions[room][0], room_positions[room+1][0]):
                    self.layout[room_positions[room][1]][x] = 2
                for y in range(room_positions[room][1], room_positions[room+1][1]):
                    self.layout[y][room_positions[room+1][0]] = 2


if __name__ == "__main__":
    print("Please run bullet_like.py")

    # test
    m = BL_MAP()
