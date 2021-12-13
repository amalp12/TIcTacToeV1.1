from classesandfunctions import *
 
# Creating and labeling the master window 
master = tk.Tk()
master.geometry('1000x1000')
master.title('Tic Tac Toe Game')


 
startHumanBtn = tk.Button( master, height = 5, width = 20, text = 'Play With a Friend', command = lambda :playWithFriend(master)) 
startComputerBtn = tk.Button(master, height = 5, width = 20, text = 'Play With Computer', command = lambda : playWithComputer(master))
quitBtn = tk.Button(master, height = 5, width = 20, text = 'Quit Game', command = lambda: master.destroy())



startHumanBtn.pack(pady = 10)
startComputerBtn.pack(pady = 10)
quitBtn.pack(pady = 10)

master.mainloop()


