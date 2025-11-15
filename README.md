# Pac-Man (Python)

Une version de Pac-Man écrite en Python (interface Tkinter) — jeu éducatif/loisir.

**Statut:** dépôt local de développement.

**Prérequis**

- Python 3.10 ou plus récent
- `pip` pour installer les dépendances

**Installer les dépendances**

Ouvrez PowerShell puis (optionnel: créer et activer un environnement virtuel):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Remarque: le projet nécessite `pygame` (listé dans `requirements.txt`). Si l'installation de `pygame` échoue, installez la version précompilée compatible avec votre Python/OS ou consultez la documentation officielle de `pygame`.

**Exécuter le jeu**

La méthode recommandée (gère correctement les imports relatifs) :

```powershell
python -m src.main
```

Alternatives:

- Exécuter depuis le dossier `src` : `python main.py` (le fichier `src/main.py` contient un fallback d'import, mais l'exécution comme module est préférable).

**Organisation du dépôt**

- `src/` : code source du jeu
- `requirements.txt` : dépendances Python
- `README.md` : ce fichier
