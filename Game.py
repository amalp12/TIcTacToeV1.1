from classesandfunctions import *
 
# Creating and labeling the master window 
master = tk.Tk()
master.geometry('1000x1000')
master.title('Tic Tac Toe Game')



startHumanBtn = tk.Button( master, text = 'Play With a Friend', command = lambda :playWithFriend(master)) 
startComputerBtn = tk.Button(master, text = 'Play With Computer', command = lambda : playWithComputer(master))
quitBtn = tk.Button(master, text = 'Quit Game', command = lambda: master.destroy())



startHumanBtn.pack()
startComputerBtn.pack()
quitBtn.pack()

master.mainloop()


