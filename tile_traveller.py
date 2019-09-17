#Make function to tell you the valid direction
#Make function to let you pick a direction
#Write a code to check your input
#Run input through the movement function
#Write code for victiory condition

def validdir(x,y):              #make value of invalid directions 0
    north = 1
    south = 2
    west = 3
    east = 4
    if x == 1:
        west = 0
        if y == 1:
            east = 0
            south = 0
    if x == 2:
        if y == 1:
            east = 0
            south = 0
            west = 0
        if y == 2:
            north = 0
            east = 0
        if y == 3:
            north = 0
            south = 0
    if x == 3:
        east = 0
        if y == 1:
            west = 0
            south = 0
        if y == 2:
            west = 0
        if y == 3:
            north = 0
    return(str(north) + str(south) + str(west) + str(east)) 


print (validdir(3,3))
    