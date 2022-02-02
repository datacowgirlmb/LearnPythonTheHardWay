class Room(object):
    
    def __init__(self, name, description, floor):
        self.name = name
        self.description = description
        self.floor = floor
        self.paths = {}
        
    def go(self, direction):
        return self.paths.get(direction, None)
        
    def add_paths(self, paths):
        self.paths.update(paths)