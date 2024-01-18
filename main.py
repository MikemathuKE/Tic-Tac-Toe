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

        a1_coord = [0, 0]
        a1 = tk.Button(self.main_frame, textvariable=self.game_grid[0][0], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(a1_coord))
        a1.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

        a2_coord = [0, 1]
        a2 = tk.Button(self.main_frame, textvariable=self.game_grid[0][1], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(a2_coord))
        a2.grid(row=0, column=1, padx=5, pady=5, sticky="n")

        a3_coord = [0, 2]
        a3 = tk.Button(self.main_frame, textvariable=self.game_grid[0][2], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(a3_coord))
        a3.grid(row=0, column=2, padx=5, pady=5, sticky="ne")

        b1_coord = [1, 0]
        b1 = tk.Button(self.main_frame, textvariable=self.game_grid[1][0], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(b1_coord))
        b1.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        b2_coord = [1, 1]
        b2 = tk.Button(self.main_frame, textvariable=self.game_grid[1][1], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(b2_coord))
        b2.grid(row=1, column=1, padx=5, pady=5)

        b3_coord = [1, 2]
        b3 = tk.Button(self.main_frame, textvariable=self.game_grid[1][2], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(b3_coord))
        b3.grid(row=1, column=2, padx=5, pady=5, sticky="e")

        c1_coord = [2, 0]
        c1 = tk.Button(self.main_frame, textvariable=self.game_grid[2][0], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(c1_coord))
        c1.grid(row=2, column=0, padx=5, pady=5, sticky="sw")

        c2_coord = [2, 1]
        c2 = tk.Button(self.main_frame, textvariable=self.game_grid[2][1], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(c2_coord))
        c2.grid(row=2, column=1, padx=5, pady=5, sticky="s")

        c3_coord = [2, 2]
        c3 = tk.Button(self.main_frame, textvariable=self.game_grid[2][2], bg="white", fg="black", width=20, height=10, font=self.main_font, command= lambda: self.button_press(c3_coord))
        c3.grid(row=2, column=2, padx=5, pady=5, sticky="se")

        self.buttons = [
            [a1, a2, a3],
            [b1, b2, b3],
            [c1, c2, c3]
        ]

        self.main_frame.pack()

        self.win_text = tk.StringVar()
        self.win_frame = tk.Frame(window, bg="black", width=400, height=400, padx=30, pady=30)
        self.win_label = tk.Label(self.win_frame, textvariable=self.win_text, bg="green", width=400, height=31, fg="white", font=self.main_font)
        self.win_button = tk.Button(self.win_frame, text="Play Again", bg="white", fg="black", width=350, height=2, font=self.main_font, command= lambda: self.restart_game())
        self.win_label.pack()
        self.win_button.pack()

    def change_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def check_win(self):
        horizontal = ""
        filled = 0
        for row in self.game_grid:
            horizontal = ''.join([val.get() for val in row])
            if horizontal == "XXX":
                return "X"
            elif horizontal == "OOO":
                return "O"
            
            filled += len(str(horizontal))
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
        
        if filled == 9:
            return "X0"
        
        return None
    
    def button_press(self, coord):
        self.game_grid[coord[0]][coord[1]].set(self.turn)
        self.buttons[coord[0]][coord[1]]['state'] = tk.DISABLED
        self.change_turn()
        result = self.check_win()
        if result:
            if result == "X0":
                self.win_text.set("It's a tie!!")
            else:
                self.win_text.set(result + " wins!")
            self.main_frame.pack_forget()
            self.win_frame.pack()

    def restart_game(self):
        self.main_frame.pack()
        self.win_frame.pack_forget()
        self.win_text.set("")
        self.turn = "X"
        for row in self.game_grid:
            for val in row:
                val.set("")
        for row in self.buttons:
            for val in row:
                val['state'] = tk.NORMAL

        

if __name__== '__main__':
    root=tk.Tk()
    tictactoe=TicTacToe(root)
    root.mainloop()