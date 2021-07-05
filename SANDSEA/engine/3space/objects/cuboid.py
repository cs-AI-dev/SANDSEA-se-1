class cuboid:
    def __init__(self, pos1, pos2, behavior):
        print("[sandsea/engine/3space/objects/cuboid.py] Initializing cuboid ...", end="")
        self.behavior = behavior
        tupleExampTV = (1, 2, 3)
        if (type(pos1) == type(tupleExampTV)) and (type(pos2) == type(tupleExampTV)) == False:
            print("ERROR: Positions not passed in as coordinates.")
            exit()
