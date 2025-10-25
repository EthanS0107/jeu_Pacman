from tkinter import *
import tkinter.font as font
from random import randint

from .Pacman import Pacman
from .ghosts.RedGhost import RedGhost
from .ghosts.PinkGhost import PinkGhost
from .ghosts.OrangeGhost import OrangeGhost
from .ghosts.BlueGhost import BlueGhost
from .ghosts.Ghost import Ghost

class GameInterface:
    def __init__(self):
        self.murs = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1],
                    [1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1],
                    [1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1],
                    [1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1],
                    [0, 0, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 0, 0],
                    [0, 0, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 0, 0],
                    [1, 1, 1, 2, 2, 2, 1, 1, 0, 1, 1, 2, 2, 2, 1, 1, 1],
                    [0, 2, 2, 2, 1, 2, 1, 0, 0, 0, 1, 2, 1, 2, 2, 2, 0],
                    [1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1],
                    [0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0],
                    [1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1],
                    [1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1],
                    [1, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1],
                    [1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 1],
                    [1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.root = Tk()
        self.root.title("Pacman Game")
        self.root.geometry("710x515")

        self.canvas = Canvas(self.root, width=510,height=510, bg="black")
        self.canvas.place(x=0, y=0)
        
        self.f = font.Font(family='Arial', size=70)
        self.f_100 = font.Font(family='Arial', size=40)  # Police pour l'écran de fin
        self.score = Label(self.root, text="0", fg="red")
        self.score.place(x=545, y=200)
        self.score['font'] = self.f

        self.create_maze()
        self.pacman = Pacman(self.canvas, 30, 30, self.murs, self.score, self.f, self)
        # Instancie 4 fantômes : rouge (au-dessus), et les trois autres en dessous
        # Placement sur la grille (col, row) converti en pixels par *30
        # Blinky (rouge) au-dessus de la maison, Pinky/Orange/Inky en dessous
        red_col, red_row = 8, 6    # au-dessus
        pink_col, pink_row = 7, 8  # en dessous gauche
        orange_col, orange_row = 8, 8
        blue_col, blue_row = 9, 8

        red_x, red_y = red_col * 30, red_row * 30
        pink_x, pink_y = pink_col * 30, pink_row * 30
        orange_x, orange_y = orange_col * 30, orange_row * 30
        blue_x, blue_y = blue_col * 30, blue_row * 30

        self.fantome_rouge = RedGhost(self.canvas, red_x, red_y, self.pacman, self)
        self.fantome_rose = PinkGhost(self.canvas, pink_x, pink_y, self.pacman, self)
        self.fantome_orange = OrangeGhost(self.canvas, orange_x, orange_y, self.pacman, self)
        self.fantome_bleu = BlueGhost(self.canvas, blue_x, blue_y, self.pacman, self)

        # Debug: afficher et logger les positions de spawn (retirez ces lignes quand validé)
        # try:
        #    print(f"Spawn Blinky (rouge): col={red_col}, row={red_row}, cell={self.murs[red_row][red_col]}")
        #    print(f"Spawn Pinky (rose): col={pink_col}, row={pink_row}, cell={self.murs[pink_row][pink_col]}")
        #    print(f"Spawn Orange: col={orange_col}, row={orange_row}, cell={self.murs[orange_row][orange_col]}")
        #    print(f"Spawn Inky (bleu): col={blue_col}, row={blue_row}, cell={self.murs[blue_row][blue_col]}")
        #    # Marqueurs visuels
        #    self.canvas.create_rectangle(red_x+8, red_y+8, red_x+22, red_y+22, outline="red", width=2, tags="spawn_marker")
        #    self.canvas.create_rectangle(pink_x+8, pink_y+8, pink_x+22, pink_y+22, outline="#FFC0CB", width=2, tags="spawn_marker")
        #    self.canvas.create_rectangle(orange_x+8, orange_y+8, orange_x+22, orange_y+22, outline="orange", width=2, tags="spawn_marker")
        #    self.canvas.create_rectangle(blue_x+8, blue_y+8, blue_x+22, blue_y+22, outline="blue", width=2, tags="spawn_marker")
        #except Exception:
        #    pass

        # Démarre l'animation de Pac-Man
        self.pacman.animate()

        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.mainloop()

    def create_maze(self):
        for y in range(len(self.murs)):
            for x in range(len(self.murs[y])):
                if self.murs[y][x] == 1:
                    self.canvas.create_rectangle(30*x,30*y,30*x+30,30*y+30, fill="blue", tags="wall")
                elif self.murs[y][x] == 2:
                    self.canvas.create_oval(30*x +12, 30*y+12, 30*x+18, 30*y+18, fill="orange", tags="orange_candy")

    def end_game(self, result):
        # Arrête tous les mouvements
        self.fantome_rouge.stop()
        self.fantome_rose.stop()
        self.fantome_orange.stop()
        self.fantome_bleu.stop()
        self.pacman.stop_animation()
        
        # Détruit la fenêtre principale
        self.root.destroy()

        # Crée la fenêtre de fin
        end_window = Tk()
        end_window.title("Fin de la partie")
        end_window.geometry("710x515")
        end_window.configure(bg="black")

        center_frame = Frame(end_window, bg="black")
        center_frame.pack(expand=True)

        if result == "win":
            message = "Félicitations, vous avez gagné !"
            color = "green"
        else:
            message = "Dommage, vous avez perdu. Essayez encore !"
            color = "red"

        label = Label(center_frame, text=message, fg=color, bg="black", font=self.f_100)
        label.pack(pady=(10, 20))

        quit_button = Button(center_frame, text="Quitter", command=end_window.quit, font=("Arial", 14))
        quit_button.pack()

        end_window.mainloop()

    def game_over(self):
         self.end_game("lose")

    def move_up(self, event):
        self.pacman.move("haut")
        if not self.check_collision():
            self.fantome_rouge.move()
            self.fantome_rose.move()
            self.fantome_orange.move()
            self.fantome_bleu.move()

    def move_down(self, event):
        self.pacman.move("bas")
        if not self.check_collision():
            self.fantome_rouge.move()
            self.fantome_rose.move()
            self.fantome_orange.move()
            self.fantome_bleu.move()

    def move_left(self, event):
        self.pacman.move("gauche")
        if not self.check_collision():
            self.fantome_rouge.move()
            self.fantome_rose.move()
            self.fantome_orange.move()
            self.fantome_bleu.move()

    def move_right(self, event):
        self.pacman.move("droite")
        if not self.check_collision():
            self.fantome_rouge.move()
            self.fantome_rose.move()
            self.fantome_orange.move()
            self.fantome_bleu.move()

    def check_collision(self):
        if (self.fantome_rouge.x, self.fantome_rouge.y) == (self.pacman.x, self.pacman.y):
            self.game_over()
            return True
        elif (self.fantome_rose.x, self.fantome_rose.y) == (self.pacman.x, self.pacman.y):
            self.game_over()
            return True
        elif (self.fantome_orange.x, self.fantome_orange.y) == (self.pacman.x, self.pacman.y):
            self.game_over()
            return True
        elif (self.fantome_bleu.x, self.fantome_bleu.y) == (self.pacman.x, self.pacman.y):
            self.game_over()
            return True
        return False
        

if __name__ == "__main__":
    game = GameInterface()