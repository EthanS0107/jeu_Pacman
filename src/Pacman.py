from tkinter import *
import tkinter.font as font
from random import randint

class Pacman:
    def __init__(self, canvas, x, y, murs, score_lab, f, interface):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.murs = murs
        self.pacman_score = 0
        self.bouche_ouverte = True
        self.angle_bouche = 30  # Angle d'ouverture de la bouche
        self.pacman = canvas.create_arc(x, y, x + 30, y + 30, fill="yellow", start=15, extent=330)
        self.score_lab = score_lab
        self.f = f
        self.interface = interface
        self.direction_actuelle = "droite"  # Direction par défaut

    def move(self, direction):
        global colonne, ligne
        colonne = self.x // 30
        ligne = self.y // 30
        self.canvas.delete(self.pacman)
        self.eat_orange_candy(direction)
        if direction == "bas" and self.y < 510 and self.murs[ligne + 1][colonne] != 1:
            self.y += 30
        elif direction == "haut" and self.y > 0 and self.murs[ligne - 1][colonne] != 1:
            self.y -= 30
        elif direction == "gauche" and self.x > 0 and self.murs[ligne][colonne - 1] != 1:
            self.x -= 30
            if self.y == 240 and self.x == 0:
                self.x = 480
                self.y = 240
        elif direction == "droite" and self.x < 480 and self.murs[ligne][colonne + 1] != 1:
            self.x += 30
            if self.y == 240 and self.x == 480:
                self.x = 0
                self.y = 240
        self.update_pacman(direction)
        self.position = (self.x, self.y)
        

    def update_pacman(self, direction):
        # Met à jour la direction actuelle
        self.direction_actuelle = direction
        
        # Anime la bouche (ouverture/fermeture)
        self.bouche_ouverte = not self.bouche_ouverte
        extent = 330 if self.bouche_ouverte else 359
        
        # Détermine l'angle de départ selon la direction
        if direction == "droite":
            start_angle = 15
        elif direction == "gauche":
            start_angle = 195
        elif direction == "bas":
            start_angle = 285
        elif direction == "haut":
            start_angle = 105
        
        # Supprime l'ancien Pac-Man et crée le nouveau
        self.canvas.delete(self.pacman)
        self.pacman = self.canvas.create_arc(
            self.x, self.y, 
            self.x + 30, self.y + 30, 
            fill="yellow",
            start=start_angle,
            extent=extent
        )
            
    def eat_orange_candy(self, direction) :
        if direction == "droite" :
            if self.murs[ligne][colonne + 1] == 2 :
                self.murs[ligne][colonne + 1]=0
                self.canvas.create_oval(30*(colonne+1) +12, 30*ligne+12, 30*(colonne+1)+18, 30*ligne+18, fill="#000000")
                self.pacman_score = self.pacman_score + 1
                self.score_lab.config(text=self.pacman_score)
        if direction == "gauche" :
            if self.murs[ligne][colonne - 1] == 2 :
                self.murs[ligne][colonne - 1]=0
                self.canvas.create_oval(30*(colonne-1) +12, 30*ligne+12, 30*(colonne-1)+18, 30*ligne+18, fill="#000000")
                self.pacman_score = self.pacman_score + 1
                self.score_lab.config(text=self.pacman_score)
        if direction == "bas" :
            if self.murs[ligne + 1][colonne] == 2 :
                self.murs[ligne + 1][colonne]=0
                self.canvas.create_oval(30*colonne +12, 30*(ligne+1)+12, 30*colonne+18, 30*(ligne+1)+18, fill="#000000")
                self.pacman_score = self.pacman_score + 1
                self.score_lab.config(text=self.pacman_score)
        if direction == "haut" :
            if self.murs[ligne - 1][colonne] == 2 :
                self.murs[ligne - 1][colonne]=0
                self.canvas.create_oval(30*colonne +12, 30*(ligne-1)+12, 30*colonne+18, 30*(ligne-1)+18, fill="#000000")
                self.pacman_score = self.pacman_score + 1
                self.score_lab.config(text=self.pacman_score)
                
        if self.pacman_score == 125 :
            self.interface.end_game("win")
            
    def animate(self):
        """Anime la bouche de Pac-Man même quand il ne bouge pas"""
        try:
            self.update_pacman(self.direction_actuelle)
            # Programme la prochaine animation dans 100ms
            self.animation_id = self.canvas.after(100, self.animate)
        except:
            # En cas d'erreur (fenêtre fermée), arrête l'animation
            pass
            
    def stop_animation(self):
        """Arrête l'animation de Pac-Man"""
        if hasattr(self, 'animation_id'):
            self.canvas.after_cancel(self.animation_id)