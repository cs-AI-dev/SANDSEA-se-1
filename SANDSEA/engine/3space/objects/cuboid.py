class cuboid:
    def __init__(self, pos1, pos2, behavior):
        print("[sandsea/engine/3space/objects/cuboid.py] Initializing cuboid ...", end="")
        self.behavior = behavior
        if (type(pos1) == type((1, 2, 3)) and type(pos2) == type((1, 2, 3))) == False:
            print("ERROR: Positions not passed in as coordinates.")
            exit()
        else:
            
