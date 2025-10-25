from .Ghost import Ghost

class YellowGhost(Ghost):
    def __init__(self, canvas, x, y, pacman, interface):
        super().__init__(canvas, x, y, pacman, interface, "yellow")
    def get_next_position(self):
        """Pinky-style: vise 4 cases devant Pac-Man selon sa direction (embuscade)."""
        start = (self.x // 30, self.y // 30)

        pac_col = self.pacman.x // 30
        pac_row = self.pacman.y // 30
        direction = getattr(self.pacman, 'direction_actuelle', 'droite')

        offsets = {
            'droite': (4, 0),
            'gauche': (-4, 0),
            'haut': (0, -4),
            'bas': (0, 4),
        }
        dx, dy = offsets.get(direction, (0, 0))

        # calculer la cible en respectant les bornes du labyrinthe
        max_cols = len(self.pacman.murs[0]) - 1
        max_rows = len(self.pacman.murs) - 1
        end_col = max(0, min(max_cols, pac_col + dx))
        end_row = max(0, min(max_rows, pac_row + dy))
        end = (end_col, end_row)

        stock_chemain = self.recherche_chemain(start, end)

        if stock_chemain and len(stock_chemain) >= 2:
            next_position = stock_chemain[1]
            return next_position[0] * 30, next_position[1] * 30
        return None
    
    def recherche_chemain(self, start, end):
        visited = set()
        queue = [(start, [start])]

        while queue:
            position_actuel, stock_chemain = queue.pop(0)
            if position_actuel in visited:
                continue
            visited.add(position_actuel)

            if position_actuel == end or (position_actuel[0] == end[0] and abs(position_actuel[1] - end[1]) <= 2):
                return stock_chemain

            for voisin in self.position_voisine(position_actuel):
                queue.append((voisin, stock_chemain + [voisin]))
        return []

    def position_voisine(self, pos):
        x, y = pos
        candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        valid_position_voisine = [voisin for voisin in candidates if 0 <= voisin[0] < len(self.pacman.murs[0]) and 0 <= voisin[1] < len(self.pacman.murs) and self.pacman.murs[voisin[1]][voisin[0]] != 1]
        return valid_position_voisine