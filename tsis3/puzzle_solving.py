def puzzle_solving(numheads, numlegs):
    rabbits = (numlegs - 2*numheads)/2
    chickens = numheads - rabbits
    
    return [rabbits, chickens]