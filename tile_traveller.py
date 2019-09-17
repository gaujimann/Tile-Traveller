#Make function to tell you the valid direction
#Make function to let you pick a direction
#Write a code to check your input
#Run input through the movement function
#Write code for victiory condition

def dir(x,y,i):
    if i.lower() == "n":
        y += 1
        return(y)
    elif i.lower() == "s":
        y -= 1
        return(y)
    elif i.lower() == "e":
        x += 1
        return(x)
    elif i.lower() == "w":
        x -= 1
        return(x)



def validdir(x,y):              #make value of invalid directions 0
    north = 1
    east = 2
    south = 3
    west = 4
    if x == 1:
        west = 0
        if y == 1:
            east = 0
            south = 0
        if y == 3:
            north = 0
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
    return(str(north) + str(east) + str(south) + str(west))   #return a string that is then used to determine the valid directions 

x = 1
y = 1

while(True):
    valid = "You can travel: "
    N = "(N)orth"
    E = "(E)ast"
    S = "(S)outh"
    W = "(W)est"
    north = bool()
    east = bool()
    south = bool()
    west = bool()
    for ind, ch in enumerate(validdir(x,y)):
        if ch == "1":
            valid = valid + N
            north = True
        if ch == "2":
            if north:
                valid = valid + " or " + E
            else:
                valid += E
            east = True
        if ch == "3":
            if north or east:
                valid = valid + " or " + S
            else:
                valid += S
            south = True
        if ch == "4":
            if north or east or south:
                valid = valid + " or " + W
            else:
                valid += W
            west = True
    
    print(valid)

    while(True):
        move = input("Direction: ")
        d = dir(x,y,move)
        if (move.lower() == "n" and north) or (move.lower() == "s" and south):
            y = dir(x,y,move)
            break
        elif (move.lower() == "e" and east) or (move.lower() == "w" and west):
            x = dir(x,y,move)
            break
        else:
            print("Not a valid driection!")
    
    if x == 3 and y == 1:
        print("Victory!")
        break