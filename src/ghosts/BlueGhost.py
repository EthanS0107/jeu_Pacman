from random import choice
from .Ghost import Ghost

class BlueGhost(Ghost):
    def __init__(self, canvas, x, y, pacman, interface):
        super().__init__(canvas, x, y, pacman, interface, "blue")
        self.move_count = 0
        self.start_sequence = [(x - 30, y), (x - 30, y - 30), (x - 30, y - 60)]
        
    def get_next_position(self):
        if self.move_count < len(self.start_sequence):
            next_pos = self.start_sequence[self.move_count]
            self.move_count += 1
            return next_pos
        else:
            direction = self.random_move()
            attempts = 0
            while not self.direction_sans_mur(direction) and attempts < 4:
                direction = self.random_move()
                attempts += 1
            next_pos = self.calculate_next_position(direction)
            self.move_count += 1
            return next_pos if next_pos else None

    def direction_sans_mur(self, direction):
        next_position = self.calculate_next_position(direction)
        return next_position is not None

    def move_to_start_zone(self):
        next_position = self.start_sequence[self.move_count]
        self.x, self.y = next_position

        self.canvas.delete(self.fantome_bleu)
        self.fantome_bleu = self.canvas.create_oval(self.x, self.y, self.x + 30, self.y + 30, fill="blue")
          
        
    def random_move(self):
        possible_moves = ["droite", "gauche", "bas", "haut"]
        return choice(possible_moves)
    
    def calculate_next_position(self, direction):
        next_x, next_y = self.x, self.y

        if direction == "droite" and self.x < 480 and self.pacman.murs[self.y // 30][self.x // 30 + 1] != 1:
            next_x += 30
        elif direction == "gauche" and self.x > 0 and self.pacman.murs[self.y // 30][self.x // 30 - 1] != 1:
            next_x -= 30
        elif direction == "bas" and self.y < 480 and self.pacman.murs[self.y // 30 + 1][self.x // 30] != 1:
            next_y += 30
        elif direction == "haut" and self.y > 0 and self.pacman.murs[self.y // 30 - 1][self.x // 30] != 1:
            next_y -= 30

        return (next_x, next_y) if (next_x, next_y) != (self.x, self.y) else None
    