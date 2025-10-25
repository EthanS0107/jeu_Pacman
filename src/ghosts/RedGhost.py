from .Ghost import Ghost

class RedGhost(Ghost):
    def __init__(self, canvas, x, y, pacman, interface):
        super().__init__(canvas, x, y, pacman, interface, "red")

    def get_next_position(self):
        start = (self.x // 30, self.y // 30)
        end = (self.pacman.x // 30, self.pacman.y // 30)

        stock_chemain = self.recherche_chemain(start, end)

        if stock_chemain and len(stock_chemain) > 1:
            next_position = stock_chemain[1]
            return next_position[0] * 30, next_position[1] * 30
        return None

    def recherche_chemain(self, start, end):
        visited = set()
        queue = [(start, [start])]

        while queue:
            position_actuel, stock_chemain = queue.pop(0)
            if position_actuel in visited:
                continue # permet d'éviter de rechercherle même chemain et donc passe à la suite de la boucle, cela évite de devoir rajouté un grand nombre de condition
            visited.add(position_actuel)

            if position_actuel == end:
                return stock_chemain

            for voisin in self.position_voisine(position_actuel):
                queue.append((voisin, stock_chemain + [voisin]))
        return []

    def position_voisine(self, pos):
        x, y = pos
        candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        valid_position_voisine = [voisin for voisin in candidates if 0 <= voisin[0] < len(self.pacman.murs[0]) and 0 <= voisin[1] < len(self.pacman.murs) and self.pacman.murs[voisin[1]][voisin[0]] != 1]
        return valid_position_voisine