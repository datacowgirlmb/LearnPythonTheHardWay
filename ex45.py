from sys import exit
from random import randint
from characterslist import characters
from characterslist import weapons

class Room(object):
    pass
    # def enter(self):
        # pass


class Game(object):
    
    def __init__(self, room_map):
        self.room_map = room_map
        
    def play(self):
        current_room = self.room_map.opening_room()
        last_room = self.room_map.next_room('winlose')
        
        while current_room != last_room:
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)
        
        current_room.enter()
        
        
class WinLose(Room):
    
    def enter(self):
        print("You win!")
        exit(1)
        
        
class Kitchen(Room):
    
    def enter(self):
        print("You're in the kitchen.")
        print(characters[randint(0, 5)], "is waiting with the", weapons[randint(0, len(weapons)-1)], ".")
        print("Did she do it?")
        
        action = input("> ")
        if action == "Yes":
            return 'winlose'
        elif action == "Maybe":
            return 'conservatory'
        else:
            return 'hall'
        

class Hall(Room):
    
    def enter(self):
        print("You're in the hall.")
        print("Now go check the conservatory.")
        return 'conservatory'
    
    
class Conservatory(Room):
    def enter(self):
        return 'winlose'
    

class Office(Room):
    pass
    

class Map(object):
    rooms = {
        'hall': Hall(),
        'conservatory': Conservatory(),
        'kitchen': Kitchen(),
        'office': Office(),
        'winlose': WinLose()
    }
    
    def __init__(self, start_room):
        self.start_room = start_room
        
    def next_room(self, room_name):
        r = Map.rooms.get(room_name)
        return r
        
    def opening_room(self):
        return self.next_room(self.start_room)
 
    def get_character(self):
        return characters[randint(0, 5)]

a_map = Map('kitchen')  # list of rooms, next_room(), opening_room() functions
a_game = Game(a_map)    # pass rooms, next_room(), opening_room() to Game, & get play() function
a_game.play()