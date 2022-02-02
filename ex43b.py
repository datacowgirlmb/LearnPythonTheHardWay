from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)
        
        
        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
        current_scene.enter()
        
        
class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your dad's jokes."
    ]
    
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):
    
    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.
            
            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out. He's blocking the door to the Armory and
            about to pull a weapon to blast you.
            """))
        
        action = input("> ")
        
        if action == "shoot!":
            print(dedent("""
                Your laser hits his costume but misses him entirely.
                He eats you.
                """))
            return 'death'
        
        elif action == "dodge!":
            print(dedent("""
                You dodge, weave, slip, & slide
                right as the Gothon's blaster shoots a laser past you.
                The Gothon stomps on your head & eats you.
                """))
            return 'death'
            
        elif action == "tell a joke":
            print(dedent("""
                While he's laughing, you run up & shoot him square in
                the chest, then jump through the Weapons Armory door.
                """))
            return 'laser_weapon_armory'
            
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'
            

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            There's a keypad on the door & you need a code to
            get the bomb out. If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb. The
            code is 3 digits.
            """))
            
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 1
        
        while guess != code and guesses < 10:
            print("Top: ", guesses)
            print("BZZZZZEDDD!")
            guesses += 1
            print("Bottom: ", guesses)
            guess = input("[keypad]> ")
            
        if guess == code:
            print(dedent("""
                The container opens. You grab the neutron bomb and
                run as fast as you can to the bridge where you place
                it in the right spot.
                """))
            return 'the_bridge'
            
        else:
            print(dedent("""
                The lock buzzes one last time. You decide to
                sit there, and finally the Gothons blow up the ship
                from their ship and you die.
                """))
            return 'death'
        
        
class TheBridge(Scene):

    def enter(Scene):
        pass


class EscapePod(Scene):

    def enter(Scene):
        pass
        
        
class Finished(Scene):
    
    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)     # Get class name for specified scene
        return val

        
    def opening_scene(self):
        return self.next_scene(self.start_scene)    # Get class name opening scene by passing start_scene to next_scene function
        
        
a_map = Map('central_corridor')     # Map is-a Central Corridor w/ start_scene of 'central_corridor' & next_scene & opening_scene attributes
a_game = Engine(a_map)              # Engine is-a Map of the Central Corridor w/ next_scene & opening_scene; Now it also has play
a_game.play()