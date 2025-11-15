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
        # Essayer de forcer le focus/fenêtre au premier plan (utile après 'Rejouer' sous Windows)
        try:
            self.root.lift()
            self.root.attributes('-topmost', True)
            # Retirer le flag topmost juste après pour permettre un comportement normal
            self.root.after(100, lambda: self.root.attributes('-topmost', False))
            self.root.focus_force()
        except Exception:
            pass

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
        # Crée la fenêtre de fin stylée
        end_window = Tk()
        end_window.title("Fin de la partie")
        end_window.geometry("710x515")
        end_window.configure(bg="#111111")

        # Mettre la fenêtre au premier plan et en focus
        try:
            end_window.lift()
            end_window.attributes('-topmost', True)
            end_window.after(100, lambda: end_window.attributes('-topmost', False))
            end_window.focus_force()
        except Exception:
            pass

        # Cadre central
        center_frame = Frame(end_window, bg="#111111")
        center_frame.pack(expand=True)

        # Message principal
        if result == "win":
            title_text = "Félicitations !"
            subtitle_text = "Vous avez gagné la partie"
            title_color = "#4CAF50"
        else:
            title_text = "Partie terminée"
            subtitle_text = "Dommage, vous avez perdu."
            title_color = "#F44336"

        title_label = Label(center_frame, text=title_text, fg=title_color, bg="#111111", font=self.f)
        title_label.pack(pady=(10, 5))

        subtitle_label = Label(center_frame, text=subtitle_text, fg="white", bg="#111111", font=("Arial", 20))
        subtitle_label.pack(pady=(0, 10))

        # Affiche le score final
        try:
            final_score = getattr(self.pacman, 'pacman_score', 0)
        except Exception:
            final_score = 0
        score_label = Label(center_frame, text=f"Score: {final_score}", fg="#FFD54F", bg="#111111", font=("Arial", 26, "bold"))
        score_label.pack(pady=(0, 20))

        # Actions (boutons) horizontaux
        action_frame = Frame(center_frame, bg="#111111")
        action_frame.pack(pady=(0, 10))

        replay_flag = {"value": False}

        def on_replay(event=None):
            replay_flag["value"] = True
            try:
                end_window.quit()
            except Exception:
                pass

        def on_quit(event=None):
            try:
                end_window.quit()
            except Exception:
                pass

        def on_menu(event=None):
            # Ferme la fenêtre de fin puis appelle le menu centralisé (src.menu.show_menu)
            try:
                end_window.quit()
                end_window.destroy()
            except Exception:
                pass
            try:
                from .menu import show_menu
            except Exception:
                try:
                    from menu import show_menu
                except Exception:
                    show_menu = None
            if show_menu:
                try:
                    show_menu()
                except Exception:
                    pass

        replay_button = Button(action_frame, text="Rejouer", command=on_replay, bg="#2E8B57", fg="white", activebackground="#1E6B45", font=("Arial", 14), width=12)
        replay_button.grid(row=0, column=0, padx=8)

        menu_button = Button(action_frame, text="Menu", command=on_menu, bg="#3F51B5", fg="white", activebackground="#2E3A9A", font=("Arial", 14), width=12)
        menu_button.grid(row=0, column=1, padx=8)

        quit_button = Button(action_frame, text="Quitter", command=on_quit, bg="#9E9E9E", fg="white", activebackground="#7E7E7E", font=("Arial", 14), width=12)
        quit_button.grid(row=0, column=2, padx=8)

        # Raccourcis clavier : R = rejouer, Q = quitter
        try:
            end_window.bind('<r>', on_replay)
            end_window.bind('<R>', on_replay)
            end_window.bind('<q>', on_quit)
            end_window.bind('<Q>', on_quit)
        except Exception:
            pass

        # Forcer modalité et focus
        try:
            end_window.grab_set()
        except Exception:
            pass

        # Affiche la fenêtre et attend interaction
        end_window.mainloop()

        try:
            end_window.destroy()
        except Exception:
            pass

        # Si l'utilisateur a cliqué sur Rejouer, instancie une nouvelle partie
        if replay_flag.get("value"):
            GameInterface()

    def game_over(self):
         self.end_game("lose")

    def move_up(self, event):
        prev_pos = (self.pacman.x, self.pacman.y)
        self.pacman.move("haut")
        # Ne déplacer les fantômes que si Pac-Man a réellement bougé
        if (self.pacman.x, self.pacman.y) != prev_pos:
            if not self.check_collision():
                self.fantome_rouge.move()
                self.fantome_rose.move()
                self.fantome_orange.move()
                self.fantome_bleu.move()

    def move_down(self, event):
        prev_pos = (self.pacman.x, self.pacman.y)
        self.pacman.move("bas")
        # Ne déplacer les fantômes que si Pac-Man a réellement bougé
        if (self.pacman.x, self.pacman.y) != prev_pos:
            if not self.check_collision():
                self.fantome_rouge.move()
                self.fantome_rose.move()
                self.fantome_orange.move()
                self.fantome_bleu.move()

    def move_left(self, event):
        prev_pos = (self.pacman.x, self.pacman.y)
        self.pacman.move("gauche")
        # Ne déplacer les fantômes que si Pac-Man a réellement bougé
        if (self.pacman.x, self.pacman.y) != prev_pos:
            if not self.check_collision():
                self.fantome_rouge.move()
                self.fantome_rose.move()
                self.fantome_orange.move()
                self.fantome_bleu.move()

    def move_right(self, event):
        prev_pos = (self.pacman.x, self.pacman.y)
        self.pacman.move("droite")
        # Ne déplacer les fantômes que si Pac-Man a réellement bougé
        if (self.pacman.x, self.pacman.y) != prev_pos:
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