from CAE_11a import bug

bugsy = bug(10) 
bugsy.move()   # Now the position is 11 
bugsy.turn() 
bugsy.move()   # Now the position is 10 
bugsy.turn()
bugsy.move() #position 11
bugsy.move() #position 12
bugsy.turn()
print("expected location: 12")
print("actual position: " + str(bugsy.getPosition()))