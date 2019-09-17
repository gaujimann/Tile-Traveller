#Make function to tell you the valid direction
#Make function to let you pick a direction
#Write a code to check your input
#Run input through the movement function
#Write code for victiory condition

def dir(x,y,i):
    if i == "n":
        y += 1
        return(y)
    elif i == "s":
        y -= 1
        return(y)
    elif i == "e":
        x += 1
        return(x)
    elif i == "w":
        x -= 1
        return(x)
x = 1
y = 1
while True:
    move = input("Choose direction: ")
    d = dir(x,y,move)
    if move == "n" or move == "s":
        print(x,d)
        y = dir(x,y,move)
    elif move == "e" or move == "w":
        print(d,y)
        x = dir(x,y,move)
    
    