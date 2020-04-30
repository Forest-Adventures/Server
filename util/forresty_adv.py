

import random

class Room: 
    def __init__(self, x, y):
        self.id = id
        self.name = None
        self.description = None
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y

    def room_connections(self, direction, destination):
        dirstring = f"{direction}_to"
        # destRoom = destination.dirstring

        if direction == "n_to": 
            self.n_to = destination
        if direction == "s_to": 
            self.s_to = destination
        if direction == "e_to": 
            self.e_to = destination
        if direction == "w_to": 
            self.w_to = destination
        else: 
            print("Invalid direction")
            return 

class Player: 
    def __init__(self, name, current_room): 
        self.name = name
        self.current_room = current_room

    def move(self, direction): 
        # forward = setattr(self, self.current_room, f"{direction}_to")
        # reverse = setattr(self.current_room, f"{direction}_to", self)
        # attri = Generate_Grid()
        # def cb(self, input):
        #     if input.e_to: 
        #         self.current_room[0] = self.current_room[0] + 1
        #         return self.current_room

        grid = Generate_Grid()
        # self.current_room = grid.__repr__().split('\"')
        # self.current_room = attri.attributes(cb(self))
        new_room = getattr(self.current_room, f"{direction}_to")
        print(new_room)
        if new_room is not None: 
            self.current_room = new_room
            room = Room(0,0)
            room.room_connections(direction, self.current_room)
        else: 
            print("can't go that way!")

    def player_input(self):
        route = input("pick one n,s,e,w: ")
        self.move(route)
class Generate_Grid: 
    def __init__(self): 
        self.grid = None
        self.storage_x = []
        self.storage_y = []
        self.e_to= self.storage_y[:]
        self.x = None
    def loop(self): 
        # self.storage.y.append()
        self.grid = Room(0,0)
        for i in range(0,5): 
            self.grid = Room(i,0)
            self.storage_x.append((self.grid.x, self.grid.y))
            
        # return getattr(self, str(self.storage_x), str(self.e_to))
    def attributes(self, cb):
        setattr(self, str(self.grid), str(cb(self.e_to)))
        if self.grid.x: 
            self.grid.x += 1
    def __repr__(self): 
        return f"({self.storage_x})"

Grid = Generate_Grid()
Grid.loop()
print(Grid.__repr__())
player = Player('tj', (0,0))
print(player.player_input())