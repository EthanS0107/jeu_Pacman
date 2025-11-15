"""
Point d'entrée principal du jeu Pac-Man
"""
import os
import sys

# Ajouter le dossier src au PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

try:
    from .GameInterface import GameInterface
except Exception:
    from GameInterface import GameInterface

if __name__ == "__main__":
    # Utiliser le menu centralisé si disponible
    try:
        from .menu import show_menu
    except Exception:
        try:
            from menu import show_menu
        except Exception:
            show_menu = None

    if show_menu:
        show_menu()
    else:
        GameInterface()
