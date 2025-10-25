from tkinter import *

class Ghost:
    # Liste pour garder une trace de tous les fantômes
    all_ghosts = []

    def __init__(self, canvas, x, y, pacman, interface, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.pacman = pacman
        self.interface = interface
        self.color = color
        self.is_active = True
        self.ghost_shape = self.canvas.create_oval(x, y, x + 30, y + 30, fill=color)
        # Ajouter ce fantôme à la liste des fantômes
        Ghost.all_ghosts.append(self)

    def move(self):
        """Méthode de base pour le mouvement - à surcharger dans les classes filles"""
        if not self.is_active:
            return

        next_position = self.get_next_position()
        attempts = 0
        max_attempts = 4

        while next_position and attempts < max_attempts:
            if self.update_position(next_position):
                self.check_collision()
                break
            # Si la position est occupée, essayer d'obtenir une nouvelle position
            next_position = self.get_next_position()
            attempts += 1

    def get_next_position(self):
        """Méthode à implémenter dans les classes filles"""
        raise NotImplementedError("Cette méthode doit être implémentée dans les classes filles")

    def update_position(self, position):
        """Met à jour la position du fantôme"""
        new_x, new_y = position
        
        # Vérifier si la nouvelle position est occupée par un autre fantôme
        if not self.is_position_occupied(new_x, new_y):
            self.x, self.y = new_x, new_y
            self.canvas.delete(self.ghost_shape)
            self.ghost_shape = self.canvas.create_oval(
                self.x, self.y, self.x + 30, self.y + 30, fill=self.color
            )
            return True
        return False
        
    def is_position_occupied(self, new_x, new_y):
        """Vérifie si la position est occupée par un autre fantôme"""
        for ghost in Ghost.all_ghosts:
            if ghost != self and ghost.is_active:  # Ne pas se comparer avec soi-même
                # Vérifier si les positions se chevauchent
                if abs(ghost.x - new_x) < 30 and abs(ghost.y - new_y) < 30:
                    return True
        return False

    def check_collision(self):
        """Vérifie si le fantôme touche Pac-Man"""
        if (self.x, self.y) == (self.pacman.x, self.pacman.y):
            self.stop()
            self.interface.game_over()

    def stop(self):
        """Arrête le mouvement du fantôme"""
        self.is_active = False
        if self in Ghost.all_ghosts:
            Ghost.all_ghosts.remove(self)

    def position_voisine(self, pos):
        """Retourne les positions voisines valides"""
        x, y = pos
        candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [voisin for voisin in candidates 
                if 0 <= voisin[0] < len(self.pacman.murs[0]) 
                and 0 <= voisin[1] < len(self.pacman.murs) 
                and self.pacman.murs[voisin[1]][voisin[0]] != 1]