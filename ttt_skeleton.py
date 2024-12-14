from tkinter import *
from tkinter import messagebox 

Player1 = 'X'
stop_game = False


'''
This method should react when a certain square in the grid is pressed. 
r=row, c=column. You should  
1. update the GUI to display either an x or a y 
2. update your state variable  
3. call another method to check if the game has ended 
'''
def clicked(r,c):
    print(r,c)
    global Player1
    '''
    Your code here 
    '''
    if Player1 == 'X' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text = 'M') 
        states[r][c] = 'X'
        Player1 = 'O'
    if Player1 == 'O' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text = 'N') 
        states[r][c] = 'O'
        Player1 = 'X'
    
    check_if_win()

'''
This method should check whether or not the game has been won. 
If win, produce a message box that says which player won. 
If tie, produce a message box announcing a tie. 
If neither, do nothing.
'''
def check_if_win():
    global stop_game
    '''
    Your code here
    '''
    pass 

# Design window
#Creating the Canvas 
root = Tk()
# Title of the window             
root.title("TICTACETOE")  
root.resizable(0,0)
 
#Button
b = [
     [0,0,0],
     [0,0,0],
     [0,0,0]]
 
#text for buttons
states = [
     [0,0,0],
     [0,0,0],
     [0,0,0]]
 
for i in range(3):
    for j in range(3): 

        #creates a 2d matrix of buttons                                  
        b[i][j] = Button(
                        height = 4, width = 8, 
                        font = ("Helvetica","20"), 
                        command = lambda r = i, c = j : clicked(r,c))
        
        #positions them in a grid for the display
        b[i][j].grid(row = i, column = j)

#starts the game loop 
mainloop()  
