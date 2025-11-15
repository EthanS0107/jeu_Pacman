from tkinter import Tk, Label, Button, Frame

def show_menu():
    """Affiche le menu principal. Quand l'utilisateur démarre, instancie GameInterface.
    Cette fonction importe `GameInterface` à l'intérieur pour éviter les dépendances circulaires.
    """
    try:
        menu = Tk()
    except Exception:
        # Si tkinter indisponible, lance directement le jeu
        try:
            from .GameInterface import GameInterface
        except Exception:
            from GameInterface import GameInterface
        GameInterface()
        return

    menu.title("Pac-Man - Menu")
    menu.geometry("400x220")
    menu.configure(bg="#0b0b0b")

    header = Label(menu, text="Pac-Man", fg="#FFD54F", bg="#0b0b0b", font=("Arial", 28, "bold"))
    header.pack(pady=(18, 6))

    subtitle = Label(menu, text="Appuyez sur Démarrer pour jouer", fg="white", bg="#0b0b0b", font=("Arial", 12))
    subtitle.pack(pady=(0, 12))

    btn_frame = Frame(menu, bg="#0b0b0b")
    btn_frame.pack(pady=(6, 12))

    def start_game_from_menu(event=None):
        try:
            menu.quit()
            menu.destroy()
        except Exception:
            pass
        # import GameInterface lazily to avoid circular imports
        try:
            from .GameInterface import GameInterface
        except Exception:
            from GameInterface import GameInterface
        GameInterface()

    def quit_app_from_menu(event=None):
        try:
            menu.quit()
            menu.destroy()
        except Exception:
            pass

    start_btn = Button(btn_frame, text="Démarrer", command=start_game_from_menu, bg="#2E8B57", fg="white", width=12, font=("Arial", 12))
    start_btn.grid(row=0, column=0, padx=8)

    quit_btn = Button(btn_frame, text="Quitter", command=quit_app_from_menu, bg="#9E9E9E", fg="white", width=12, font=("Arial", 12))
    quit_btn.grid(row=0, column=1, padx=8)

    try:
        menu.bind('<Return>', start_game_from_menu)
        menu.bind('<Escape>', quit_app_from_menu)
    except Exception:
        pass

    try:
        menu.lift()
        menu.attributes('-topmost', True)
        menu.after(100, lambda: menu.attributes('-topmost', False))
        menu.focus_force()
    except Exception:
        pass

    menu.mainloop()
