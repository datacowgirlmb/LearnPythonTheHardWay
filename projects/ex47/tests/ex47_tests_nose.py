from nose.tools import *
from ex47.game import Room

# def setup():
	# print("SETUP!")
	
# def teardown():
	# print("TEAR DOWN!")
	
# def test_basic():
	# print("I RAN!", end='')  
    
def test_room():        # Verify init variables
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""",
                "3rd floor")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})
    assert_equal(gold.floor, "3rd floor")
    
def test_room_paths():  # Verify path values
    center = Room("Center", "Test room in the center", "1st")
    north = Room("North", "Test room in the north.", "2nd")
    south = Room("South", "Test room in the south.", "3rd")
    
    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)
    
def test_map():         # Check values returned from path dictionary
    start = Room("Start", "You can go west and down a hole.", "1st")   # Room with name "Start", description "You can go...", & empty dictionary path
    west = Room("Trees", "There are trees here, you can go east.", "2nd")
    down = Room("Dungeon", "It's dark down here, you can go up.", "3rd")
    
    start.add_paths({'west': west, 'down': down})   # Add west & down to dictionary path
    west.add_paths({'east': start})
    down.add_paths({'up': start})
    
    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)