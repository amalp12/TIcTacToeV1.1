
import time
import tkinter as tk
from PIL import  ImageTk as itk 
import random



def playWithFriend(rootwin):
    
    clearAll(rootwin)
    # Creates a board
    my_board = Board(rootwin)


    # Creates pieces inside the board
    my_player = Human(my_board)  
    my_player.play()

        
def playWithComputer(rootwin):

    clearAll(rootwin)
    # Creates a board
    my_board = Board(rootwin)


    # Creates pieces inside the board
    my_player = Computer(my_board)  
    my_player.play()

        

#List functions
def mostFrequent(list1):
    highest = 0
    count =0
    for i in list1:
        c = list1.count(i)
        if c >= count :
            count = c
            highest = i

    return highest

def Intersection(list1, list2):
    list3 = []
    for i in list1:
        if i in list2:
            if i not in list3:
                list3.append(i)
    
    return list3
def Difference(list1,list2): # list1-list2
    "list1 - list2"
    
    for i in list2:
        if i in list1:
            count = list1.count(i)
            if count > 1:
                for _ in range(0,count):
                    list1.remove(i)
            else:  list1.remove(i)  

    return list1

def Union(list1,list2):
    list3 = []
    for i in list1:
        if i not in list3:
            list3.append(i)
    for i in list2:
        if i not in list3:
            list3.append(i)
    return list3        



def clearAll(window):
    "Used to clear everything on the window"
    
    #time.sleep(1) # Gives an interval between the function call and execution so that it doesn't appear abrupt
    def all_children (window) :
        _list = window.winfo_children()

        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())

        return _list

    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()
    



class Memory:

    def __init__(self, board):

          
        self.board = board

        # Setting the winner string to empty 
        self.winner = 'N/A'

        # Tells memory whether the game started with player X
        self.start_with_playerx = None
        #Winner announced boolean 
        self.winner_announced = False
        # Counting the moves made my the players
        self.playerx_moves = 0
        self.playero_moves = 0
        self.total_moves = self.playerx_moves + self.playero_moves 

        # Slots that when a certain player occupies, he/she is decided a winner
        self.winning_slots = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]

        # This is the total number of slots, but here we use it to delete taken slots so that images are not overwritten
        self.slots = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
        self.slots_takenx = []
        self.slots_takeno = []

    @property
    def WinnerAnnounced(self):
        return self.winner_announced
    @WinnerAnnounced.setter
    def WinnerAnnounced(self, boolean):
        self.winner_announced = boolean





class Board:
        

    def __init__(self, rootwin, width = 400, height = 400, board_color = 'black', board_bg = 'white'):
            self.rootwin = rootwin  
            self.w = width
            self.h = height
            self.board_color = board_color
            self.board_bg = board_bg
            
            self.info_statement = "Player X, Start the Game By Choosing a Box. Good Luck!  :)"

            # Creating a label to show information
            self.info = tk.Label(self.rootwin, text = self.info_statement)

            # Creatubg label for showing coordinates 
            self.coordinates = tk.Label(self.rootwin,text = '')
            self.canvas = tk.Canvas(self.rootwin, width = self.w, height = self.h, bg = 'white',)

            # Creating a board memory for the board
            self.boardMemory = Memory(self)
            # Winner Announced boolean
            self.winner_announced = self.boardMemory.winner_announced
            # Sets up the board
            self.setupBoard()
            # Packing the  label to show information
            self.info.pack()

    # Checks if a winner is decided
   
    def checkWinner(self):
        x = self.boardMemory.slots_takenx
        o = self.boardMemory.slots_takeno 
        statement = 'No Winners Announced'
        print(x,o)
        if self.boardMemory.winner == 'Player X Won!' or self.boardMemory.winner == 'Player O Won!'  or  self.boardMemory.winner == 'This Game is a Draw!':
            clearAll(self.rootwin)
      
        try:
                
            for i in self.boardMemory.winning_slots:
                    
                if i[0] in x and i[1] in x and i[2] in x:
                    statement = 'Player X Won!'
                    self.info.config(text = statement)
                    self.winner_announced = True 
                    self.endWindow()
                    
                elif i[0] in o and i[1] in o and i[2] in o:
                    statement = 'Player O Won!' 
                    self.info.config(text = statement)
                    self.winner_announced = True
                    self.endWindow()
                    
                elif len(list(self.boardMemory.slots.keys())) == 0 and self.winner_announced == False:
                    statement = 'This Game is a Draw!'
                    self.info.config(text = statement)  
                    self.winner_announced = True
                    self.endWindow()
        except:
            print('Failed CheckWinner', 'Statement : ', statement)
            
        finally:
            print('checkWinner Function Statement : ', statement)  
            if self.winner_announced == False:
                return statement  
            

    def moveMouse(self,event):
        
        self.coordinates.config(text = 'Coordinates X: ' + str(event.x) + ' Y: ' + str(event.y))              
   
            

    def setupBoard(self):

            # Packing the canvas on the screem
            self.canvas.pack_configure(anchor ='center')
           
            # Create lines for the Board
            self.canvas.create_line(self.w/3, 0, self.w/3, self.h, fill = self.board_color)
            self.canvas.create_line(2*self.w/3, 0, 2*self.w/3, self.h, fill = self.board_color)

            self.canvas.create_line(0, self.h/3, self.w, self.h/3, fill = self.board_color)
            self.canvas.create_line(0, 2*self.h/3, self.w, 2*self.h/3, fill = self.board_color)

            # Creating Invisible rectangeles that act as buttons
            self.canvas.create_rectangle(0 , 0, self.w/3, self.h/3,  fill = self.board_bg, tags = 1) # Box 1
            self.canvas.create_rectangle(self.w/3 , 0, 2*self.w/3, self.h/3,  fill = self.board_bg, tags = 2) # Box 2
            self.canvas.create_rectangle(2*self.w/3 , 0, self.w, self.h/3,  fill = self.board_bg, tags =3) # Box 3
            self.canvas.create_rectangle(0 , self.h/3, self.w/3, 2*self.h/3,  fill = self.board_bg, tags = 4) # Box 4
            self.canvas.create_rectangle(self.w/3 , self.h/3, 2*self.w/3, 2*self.h/3,  fill = self.board_bg, tags = 5) # Box 5
            self.canvas.create_rectangle(2*self.w/3 , self.h/3, self.w, 2*self.h/3,  fill = self.board_bg, tags = 6) # Box 6
            self.canvas.create_rectangle(0 , 2*self.h/3, self.w/3, self.h,  fill = self.board_bg, tags = 7) # Box 7
            self.canvas.create_rectangle(self.w/3 , 2*self.h/3, 2*self.w/3, self.h,  fill = self.board_bg, tags = 8) # Box 8
            self.canvas.create_rectangle(2*self.w/3 , 2*self.h/3, self.w, self.h,  fill = self.board_bg, tags = 9) # Box 9

            
            # Displaying coordinates    
            self.coordinates.pack()

            # Binding mousebutton 1 to show the coordinated when clicked
            self.canvas.bind('<Button-1>', self.moveMouse)

    def endWindow(self):
        startHumanBtn = tk.Button( self.rootwin, text = 'Play Again With a Friend', command = lambda :playWithFriend(self.rootwin)) 
        startComputerBtn = tk.Button(self.rootwin, text = 'Play Again With Computer', command = lambda : playWithComputer(self.rootwin))
        quitBtn = tk.Button(self.rootwin, text = 'Quit Game', command = lambda: self.rootwin.destroy())

        
        startHumanBtn.pack()
        startComputerBtn.pack()
        quitBtn.pack()


            

class Player(Board):
    
   
    

    def __init__(self , board, playerx = True):
        
        self.board = board
        self.playerx = playerx

        self.canvas = self.getCanvas()
                     
          
        self.setUpBoardVariables()
        self.setImages()
        self.createBlankBoxes()
        #self.bindCanvas()

    def getCanvas(self) :
        return self.board.canvas
    

    def getBoard(self):
        return self.board    


    def setUpBoardVariables(self):
        self.board = self.getBoard()
        self.boardMemory = self.board.boardMemory
        self.winner_announced = self.boardMemory.winner_announced

        self.info = self.board.info
        
        
        self.rootwin = self.board.rootwin  
        self.w = self.board.w
        self.h = self.board.h
        

        # Access noard memory's variables
        self.slots_takenx = self.boardMemory.slots_takenx
        self.slots_takeno = self.boardMemory.slots_takeno
        self.slots = self.boardMemory.slots
                       
        # Telling  memory that started with player x
        self.board.boardMemory.start_with_playerx =  self.playerx

    def setImages(self):
        # Importing image and keepin a reference so that garbage collection does not delete it
        self.ximg = itk.PhotoImage(file = 'X.png')
        self.oimg = itk.PhotoImage(file = 'O.png')

        self.labelx = tk.Label(image = self.ximg)
        self.labelo = tk.Label(image = self.oimg)

        self.x = self.labelx['image']
        self.o = self.labelo['image']


    def createBlankBoxes(self):
        #Creating Blank boxes to put image
        self.box1 = self.canvas.create_image(self.w/6, self.h/6, image = None , tags = 1 )
        self.box2 = self.canvas.create_image(self.w/2, self.h/6, image = None , tags = 2 )
        self.box3 = self.canvas.create_image(5*self.w/6, self.h/6, image = None , tags = 3)
        self.box4 = self.canvas.create_image(self.w/6, self.h/2, image = None , tags = 4 )
        self.box5 = self.canvas.create_image(self.w/2, self.h/2, image = None , tags = 5 )
        self.box6 = self.canvas.create_image(5*self.w/6, self.h/2, image = None , tags = 6 )
        self.box7 = self.canvas.create_image(self.w/6, 5*self.h/6, image = None , tags = 7 )
        self.box8 = self.canvas.create_image(self.w/2, 5*self.h/6, image = None , tags = 8 ) 
        self.box9 = self.canvas.create_image(5*self.w/6, 5*self.h/6, image = None , tags = 9 )

    def bindCanvas(self, func):
        # Binding the Button one to get the tag of the widget when clicked         
        return self.getCanvas().bind('<Button-1>', func)   

    # Changing Player Label
    def playerOneLabel(self):
        self.board.info.config(text = "Player X's Game")
    
    # Changing Player Label
    def playerTwoLabel(self):
        self.board.info.config(text = "Player O's Game")
               

        
    # Functions that displays the image of X or O
    def one(self, tag):
        #(1,2)
        if self.playerx == True:
            self.canvas.itemconfig(self.box1, image = self.x)
            self.playerx = False
            del self.slots[tag]
            self.slots_takenx.append(tag)
            self.playerTwoLabel()
            
        elif self.playerx == False :
            self.canvas.itemconfig(self.box1, image = self.o)
            self.playerx = True
            del self.slots[tag]
            self.slots_takeno.append(tag)
            self.playerOneLabel()
        else:
            print('Box One Error')

    def two(self, tag):
        #(1,2)
        if self.playerx == True:
            self.canvas.itemconfig(self.box2, image = self.x)
            self.playerx = False
            del self.slots[tag]
            self.slots_takenx.append(tag)
            self.playerTwoLabel()
        elif self.playerx == False :
            self.canvas.itemconfig(self.box2, image = self.o)
            self.playerx = True
            del self.slots[tag]
            self.slots_takeno.append(tag)
            self.playerOneLabel()
        else:
            print('Box Two Error')
            
    def three(self, tag):
        #(1,3)
        if self.playerx == True:
            self.canvas.itemconfig(self.box3, image = self.x)
            self.playerx = False
            del self.slots[tag]
            self.slots_takenx.append(tag)
            self.playerTwoLabel()
        elif self.playerx == False :
            self.canvas.itemconfig(self.box3, image = self.o)
            self.playerx = True
            del self.slots[tag]
            self.slots_takeno.append(tag)
            self.playerOneLabel()
        else:
            print('Box Three Error')

    def four(self, tag):
        #(2,1)
        if self.playerx == True:
            self.canvas.itemconfig(self.box4, image = self.x)
            self.playerx = False
            del self.slots[tag]
            self.slots_takenx.append(tag)
            self.playerTwoLabel()
        elif self.playerx == False :
            self.canvas.itemconfig(self.box4, image = self.o)
            self.playerx = True
            del self.slots[tag]
            self.slots_takeno.append(tag)
            self.playerOneLabel()
        else:
            print('Box Four Error')

    def five(self, tag):
        #(2,2)
        if self.playerx == True:
            self.canvas.itemconfig(self.box5, image = self.x)
            self.playerx = False
            del self.slots[tag]
            self.slots_takenx.append(tag)
            self.playerTwoLabel()
        elif self.playerx == False :
            self.canvas.itemconfig(self.box5, image = self.o)
            self.playerx = True
            del self.slots[tag]
            self.slots_takeno.append(tag)
            self.playerOneLabel()
        else:
            print('Box Five Error')

    def six(self, tag):
        #(2,3)
        if self.playerx == True:
            self.canvas.itemconfig(self.box6, image = self.x)
            self.playerx = False
            del self.slots[tag]
            self.slots_takenx.append(tag)
            self.playerTwoLabel()
        elif self.playerx == False :
            self.canvas.itemconfig(self.box6, image = self.o)
            self.playerx = True
            del self.slots[tag]
            self.slots_takeno.append(tag)
            self.playerOneLabel()
        else:
            print('Box Six Error')

    def seven(self, tag):
        #(3,1)
        if self.playerx == True:
            self.canvas.itemconfig(self.box7, image = self.x)
            self.playerx = False
            del self.slots[tag]
            self.slots_takenx.append(tag)
            self.playerTwoLabel()
        elif self.playerx == False :
            self.canvas.itemconfig(self.box7, image = self.o)
            self.playerx = True
            del self.slots[tag]
            self.slots_takeno.append(tag)
            self.playerOneLabel()
        else:
            print('Box Seven Error')

    def eight(self, tag):
        #(3,2)
        if self.playerx == True:
            self.canvas.itemconfig(self.box8, image = self.x)
            self.playerx = False
            del self.slots[tag]
            self.slots_takenx.append(tag)
            self.playerTwoLabel()
        elif self.playerx == False :
            self.canvas.itemconfig(self.box8, image = self.o)
            self.playerx = True
            del self.slots[tag]
            self.slots_takeno.append(tag)
            self.playerOneLabel()
        else:
            print('Box Eight Error')

    def nine(self, tag):
        #(3,3)
        if self.playerx == True:
            self.canvas.itemconfig(self.box9, image = self.x)
            self.playerx = False
            del self.slots[tag]
            self.slots_takenx.append(tag)
            self.playerTwoLabel()
        elif self.playerx == False :
            self.canvas.itemconfig(self.box9, image = self.o)
            self.playerx = True
            del self.slots[tag]
            self.slots_takeno.append(tag)
            self.playerOneLabel()
        else:
            print('Box Nine Error')
   
        
       
class Human(Player):
    def __init___(self , board, playerx = True):
        
        super().__init__(board, playerx)


    def play(self):
        self.bindCanvas(self.nearestWidget)
        
        
    # def bindCanvas(self):
    #     # Binding the Button one to get the tag of the widget when clicked         
    #     self.canvas.bind('<Button-1>', self.nearestWidget)   

    def nearestWidget(self,event):

    # Getting the nearest psudo widget
    
    
        def onObjectClick(event):  
            #print('Got object click at ', event.x, event.y)
            item = event.widget.find_closest(event.x, event.y)
            #print(self.canvas.gettags(item))
            tag = self.canvas.gettags(item)[0]
            #print(tag)
            return int(tag)

        if self.winner_announced == False:
            tag = onObjectClick(event)

            # Calling the corresponding funtions to display X or O images according to the clicked coordinated
            if tag not in self.slots_takenx and tag not in self.slots_takeno:
                if tag == 1:  self.one(tag)  
                elif tag == 2:  self.two(tag)
                elif tag == 3:  self.three(tag)
                elif tag == 4:  self.four(tag)
                elif tag == 5:  self.five(tag)
                elif tag == 6:  self.six(tag)
                elif tag == 7:  self.seven(tag)
                elif tag == 8:  self.eight(tag)
                elif tag == 9:  self.nine(tag)
                # Checking if the prevous move decided a winner
                self.boardMemory.winner = self.checkWinner()
                if self.winner_announced == True:
                    self.canvas.unbind('<Button-1>', self.nearestWidget)
                
            else:
                print('Click Function not called')

             
class Computer(Player):
    def __init___(self , board, playerx = True):
        super().__init__(board, playerx)
        


    def play(self):
        self.bindCanvas(self.nearestWidgetC)

    def computerMove(self):
                    
                if self.playerx == False:
                    #computer_choice = self.computerRandom()
                    computer_choice = self.computerAI()
                    if computer_choice == 1:  self.one(computer_choice)  
                    elif computer_choice == 2:  self.two(computer_choice)
                    elif computer_choice == 3:  self.three(computer_choice)
                    elif computer_choice == 4:  self.four(computer_choice)
                    elif computer_choice == 5:  self.five(computer_choice)
                    elif computer_choice == 6:  self.six(computer_choice)
                    elif computer_choice == 7:  self.seven(computer_choice)
                    elif computer_choice == 8:  self.eight(computer_choice)
                    elif computer_choice == 9:  self.nine(computer_choice)
                    print('AI Choice', computer_choice)
                    print('Calling computer check winner')  

                    self.boardMemory.winner = self.checkWinner()
                    if self.winner_announced == True:
                        self.canvas.unbind('<Button-1>', self.nearestWidgetC)
                        self.info.config(text = 'Congratulations! You Have Won Against The Computer')
                    elif self.winner_announced == False:
                        self.playerx = True              
                   
                    


    def nearestWidgetC(self,event):

    # Getting the nearest psudo widget
    
    
        def onObjectClick(event):  
            #print('Got object click at ', event.x, event.y)
            item = event.widget.find_closest(event.x, event.y)
            #print(self.canvas.gettags(item))
            tag = self.canvas.gettags(item)[0]
            #print(tag)
            return int(tag)

        tag = onObjectClick(event)

        # Calling the corresponding funtions to display X or O images according to the clicked coordinated
        if tag not in self.slots_takenx and tag not in self.slots_takeno and tag in list(self.slots.keys()):
            if self.playerx == True:
                if tag == 1:  self.one(tag)  
                elif tag == 2:  self.two(tag)
                elif tag == 3:  self.three(tag)
                elif tag == 4:  self.four(tag)
                elif tag == 5:  self.five(tag)
                elif tag == 6:  self.six(tag)
                elif tag == 7:  self.seven(tag)
                elif tag == 8:  self.eight(tag)
                elif tag == 9:  self.nine(tag)
                
                if self.winner_announced == False:
                    # Checking if the prevous move decided a winner
                    self.boardMemory.winner = self.checkWinner()
                    self.computerMove()
                elif self.winner_announced == True:
                    self.canvas.unbind('<Button-1>', self.nearestWidgetC)
            else:
                print('OnObjectClick Function not called')
            
                
            
            
    def computerAI(self):
        slotsleft = list(self.boardMemory.slots.keys())
        takeno = self.boardMemory.slots_takeno
        takenx = self.boardMemory.slots_takenx
        winning_slots = self.boardMemory.winning_slots
        strategy1 = [(5,9,7), (1,5,7), (1,5,3), (3,5,9)]
        str1patch1 = {(5,9,7):(1,3), (1,5,7):(3,9), (1,5,3):(7,9), (3,5,9):(1,7)}
        strategy2 = [(1,3,9), (1,7,9), (3,9,7), (3,1,7)]
        opponent_strategy1  = [(1,3), (3,9), (9,7), (1,7)]
        opponent_strategy2  = [(1,9), (3,7)]
        opponent_strategy3 = [(2,7), (2,9), (6,1), (6,7), (8,1), (8,3), (4,3), (4,9)]
        opponent_strategy4 = {(2,4):1, (2,6):3, (6,8):9, (8,4):7}
        
       # Counters Opponent's corner triangle lock
        if len(slotsleft) == 7:
            if 5 in slotsleft:
                return 5  

        if len(slotsleft) == 6 :
            key_list = list(opponent_strategy4.keys())
            for i in range(0,len(key_list)):
                if key_list[i][0] in takenx and key_list[i][1] in takenx:
                    if opponent_strategy4[key_list[i]] in slotsleft:
                        return opponent_strategy4[key_list[i]]
                


        # Counters against opponent's strategy3
        if len(slotsleft) == 6:
            print('loop6.1')
            opp3patch = [2, 4 ,6, 8]
            for i in range(0, len(opponent_strategy3)):
                print('loop6.2')
                if opponent_strategy3[i][0] in takenx and opponent_strategy3[i][1] in takenx:
                    for j in opp3patch:
                        
                        for k in winning_slots:
                            if j in k:
                                if k[0] not in takenx and k[1] not in takenx and k[2] not in takenx:
                                    if k[0]  in takeno or k[1]  in takeno or k[2]  in takeno:
                                        print('loop6.3')
                                        if j in slotsleft:
                                            print('k : ', k)
                                            return j
                            
         
        # Counters aganst middle triangle strategy (strategy1)                         
        if len(slotsleft)  == 6 :
            for i in range(0,len(opponent_strategy1)):
                print('loop5.1')
                if opponent_strategy1[i][0] in takenx and opponent_strategy1[i][1] in takenx :
                    return_value = (opponent_strategy1[i][0] + opponent_strategy1[i][1])/2
                    return return_value
            for i in range(0,len(opponent_strategy2)):
                print('loop5.2')
                if opponent_strategy2[i][0] in takenx and opponent_strategy2[i][1] in takenx :
                    counter2 = [2,6,4,8]
                                                          
                    for i in range(0,len(winning_slots)):
                        for j in winning_slots[i]:
                            if j in counter2:
                                print('loop5.5')
                                if j in counter2:
                                    return j

               
        # Checks the third winning box with O, and prevents the opponent from winning 
        for i in range(0,len(winning_slots)):
            print('loop1')
                
            intersection = Intersection(winning_slots[i],takeno)
            union = Union(winning_slots[i],takeno)
            print('first intersection', intersection)
            if len(intersection) == 2:
                for j in winning_slots[i]:
                    print('loop1.1')
                    if j not in intersection:
                        if j in slotsleft:
                             return j
        # If there is two winning  boxes with X, checks the third box and secures the win 
        for i in range(0,len(winning_slots)):
            print('loop2')    
            intersection = Intersection(winning_slots[i], takenx)
            union = Union(winning_slots[i],takenx)
            print('second intersection', intersection)
            if len(intersection) == 2:
                for j in winning_slots[i]:
                    print('loop2.1')
                    if j not in intersection:
                        if j in slotsleft:
                            print('returned from 2.1')
                            return j
  
        # Middle triangle lock strategy    
        for i in range(0,len(strategy1)):
            str1patch1sub = str1patch1[strategy1[i]]
            print('loop3')
            if 5 in takenx: break 
               
            elif strategy1[i][0] not in takenx and strategy1[i][1] not in takenx and strategy1[i][2] not in takenx:
                if len(slotsleft) == 8: 
                    if 5 in slotsleft : return 5
                for j in strategy1[i]:
                    print('loop3.1')
                    if j not in takeno:
                        if j in slotsleft:
                            if str1patch1sub[0] in takenx or str1patch1sub[1] in takenx: break
                            return j 
        if len(slotsleft) > 4 :
            # Corner triangle lock strategy
            for i in range(0,len(strategy2)):
                print('loop4')  
             
                if strategy2[i][0] not in takenx and strategy2[i][1] not in takenx and strategy2[i][2] not in takenx:
                    
                    for j in strategy1[i]:
                        print('loop4.1')
                        if j not in takeno:
                            if j in slotsleft:
                                return j
        if len(slotsleft) <= 4:
            xwin_slots1 = []
            xwin_slots2 = []
            for i in range(0,len(winning_slots)):
              for j in slotsleft:
                  if j in winning_slots[i]:
                    if len(Intersection(list(winning_slots[i]), takenx)) == 2:
                        xwin_slots1 += Difference(list(winning_slots[i]),takenx)
                    elif len(Intersection(list(winning_slots[i]), takenx)) == 1:
                        print('Intersection', Intersection(list(winning_slots[i]), takenx))
                        xwin_slots2 += Difference(list(winning_slots[i]),takenx)

                        
            if len(xwin_slots1) !=0 :
                print('Returned from 1')
                return mostFrequent(xwin_slots1)
            elif len(xwin_slots2) !=0 :
                print('Returned from 2')
                return mostFrequent(xwin_slots2)

        
        


        print("AI didn't return anything, Let's hope random guess works!")                      

        # In unexpected situations the algorithim should return a random value                      
        randomguess = random.randint(0, len(slotsleft)-1)
        return slotsleft[randomguess]
            
        print("Didn't return anything, Out of Bounds!") 




