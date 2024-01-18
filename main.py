import tkinter as tk
import tkinter.font as font

class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("600x600")


        self.main_frame = tk.Frame(window, bg="black", width=570, height=570)

        self.game_grid = [
            [tk.StringVar(), tk.StringVar(), tk.StringVar()],
            [tk.StringVar(), tk.StringVar(), tk.StringVar()],
            [tk.StringVar(), tk.StringVar(), tk.StringVar()]
        ]

        self.turn = "X"
        self.main_font = font.Font(family="Helvetica", size=10, weight="bold")

        self.a1_coord = [0, 0]
        self.a1 = tk.Button(self.main_frame, textvariable=self.game_grid[0][0], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(self.a1_coord))
        self.a1.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

        self.a2_coord = [0, 1]
        self.a2 = tk.Button(self.main_frame, textvariable=self.game_grid[0][1], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(self.a2_coord))
        self.a2.grid(row=0, column=1, padx=5, pady=5, sticky="n")

        self.a3_coord = [0, 2]
        self.a3 = tk.Button(self.main_frame, textvariable=self.game_grid[0][2], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(self.a3_coord))
        self.a3.grid(row=0, column=2, padx=5, pady=5, sticky="ne")

        self.b1_coord = [1, 0]
        self.b1 = tk.Button(self.main_frame, textvariable=self.game_grid[1][0], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(self.b1_coord))
        self.b1.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.b2_coord = [1, 1]
        self.b2 = tk.Button(self.main_frame, textvariable=self.game_grid[1][1], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(self.b2_coord))
        self.b2.grid(row=1, column=1, padx=5, pady=5)

        self.b3_coord = [1, 2]
        self.b3 = tk.Button(self.main_frame, textvariable=self.game_grid[1][2], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(self.b3_coord))
        self.b3.grid(row=1, column=2, padx=5, pady=5, sticky="e")

        self.c1_coord = [2, 0]
        self.c1 = tk.Button(self.main_frame, textvariable=self.game_grid[2][0], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(self.c1_coord))
        self.c1.grid(row=2, column=0, padx=5, pady=5, sticky="sw")

        self.c2_coord = [2, 1]
        self.c2 = tk.Button(self.main_frame, textvariable=self.game_grid[2][1], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(self.c2_coord))
        self.c2.grid(row=2, column=1, padx=5, pady=5, sticky="s")

        self.c3_coord = [2, 2]
        self.c3 = tk.Button(self.main_frame, textvariable=self.game_grid[2][2], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(self.c3_coord))
        self.c3.grid(row=2, column=2, padx=5, pady=5, sticky="se")

        self.main_frame.pack()

        self.win_text = tk.StringVar()
        self.win_frame = tk.Frame(window, bg="black", width=400, height=400, padx=65, pady=65)
        self.win_label = tk.Label(self.win_frame, textvariable=self.win_text, bg="green", fg="white", width=400, height=400, font=self.main_font)
        self.win_label.pack()

    def change_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def check_win(self):
        horizontal = ""
        for row in self.game_grid:
            horizontal = (val.get() for val in row)
            if horizontal == "XXX":
                return "X"
            elif horizontal == "OOO":
                return "O"
            horizontal = ""
            
        vertical = ""
        for i in range(3):
            for row in self.game_grid:
                vertical += row[i].get()
            if vertical == "XXX":
                return "X"
            elif vertical == "OOO":
                return "O"
            vertical = ""

        diagonal = ""
        for i in range(3):
            diagonal += self.game_grid[i][i].get()
        if diagonal == "XXX":
            return "X"
        elif diagonal == "OOO":
            return "O"
        
        diagonal = ""
        for i in range(3):
            diagonal += self.game_grid[i][(2-i)].get()
        if diagonal == "XXX":
            return "X"
        elif diagonal == "OOO":
            return "O"
        
        print(len(vertical), len(horizontal), len(diagonal))
        
        if len(vertical) == 3 and len(horizontal) == 3 and len(diagonal) == 3:
            return "X0"
        
        return None
    
    def button_press(self, coord):
        self.game_grid[coord[0]][coord[1]].set(self.turn)
        self.change_turn()
        result = self.check_win()
        if result:
            if result == "X0":
                self.win_text.set("It's a tie!!")
            else:
                self.win_text.set(result + " wins!")
            self.main_frame.pack_forget()
            self.win_frame.pack()

        

if __name__== '__main__':
    root=tk.Tk()
    tictactoe=TicTacToe(root)
    root.mainloop()