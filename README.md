# Bataille Navale (Battleship) in Python

**Auteures : Kombila Jamelia et Maha Bouslimani.**
*Team project by Jamelia Kombila and Maha Bouslimani.*

> A console implementation of the classic Battleship game in Python. Three progressive versions are provided: a single-player mode against a hidden computer fleet, a two-player mode where both sides place their ships, and a final version where the computer plays with a smart targeting strategy.
>
> Une implémentation console du jeu classique de la Bataille Navale en Python. Trois versions progressives sont proposées : un mode solo où le joueur cherche la flotte de l'ordinateur, un mode à deux où chaque camp place ses bateaux, et une version finale où l'ordinateur joue avec une stratégie de ciblage intelligente.

---

[English](#english) | [Français](#français)

---

## English

### Overview

A classic Battleship game implemented in Python and played in the terminal. The grid is a 10 by 10 board, with rows labelled A to J and columns 1 to 10. Each side hides a fleet of five ships of different sizes, and players take turns firing at coordinates until one side has sunk the entire enemy fleet. The project was developed as a Python programming assignment (IMDS3A, academic year 2024/2025, submitted in January 2025).

### Game principle

Each player owns a 10 by 10 grid and places a fleet of five ships. Ships are placed either horizontally or vertically, cannot overlap, and must stay within the grid. Players take turns calling out a coordinate (row letter and column number). The opponent reveals whether the shot missed, touched a ship, or sunk it. The first player to sink the opponent's entire fleet wins.

### Fleet

| Ship | Size (cells) |
|------|--------------|
| Aircraft carrier (porte-avion) | 5 |
| Cruiser (croiseur) | 4 |
| Submarine (sous-marin) | 3 |
| Destroyer (torpilleur) | 2 |
| Rowboat (barque) | 1 |

### Display

The board is rendered in the console with these symbols:

| Symbol | Meaning |
|--------|---------|
| `.` | Empty water |
| `*` | Missed shot |
| `+` | Ship cell that was hit |
| `x` | Cell of a fully sunk ship |
| letter of the ship | Ship cell on the player's own solution grid |

### The three versions

1. **Version 1 (single player).** The computer places its fleet randomly. The player enters coordinates one by one to try to find and sink all the enemy ships. A second grid reveals the full solution at the end.
2. **Version 2 (two players, random AI).** The player places their own fleet ship by ship, the computer places its fleet randomly, and both sides alternate turns. The computer shoots random coordinates it has not already played.
3. **Version 3 (two players, smart AI).** Same as version 2 but the computer switches to a targeting mode as soon as it hits a ship: it tries the adjacent cells, infers the ship orientation once it has two consecutive hits, and follows that axis until the ship is fully sunk. This makes the computer a much more challenging opponent.

### Project structure

```
├── src/
│   ├── bataille_navale_v1.py   Single-player version
│   ├── bataille_navale_v2.py   Two-player version with random AI
│   └── bataille_navale_v3.py   Two-player version with smart AI
├── LICENSE
└── README.md
```

### How to run

Requirements: Python 3.8 or later. No external dependencies.

```bash
git clone https://github.com/jokombila/battleship-python.git
cd battleship-python

# Pick the version you want to play
python3 src/bataille_navale_v1.py
python3 src/bataille_navale_v2.py
python3 src/bataille_navale_v3.py
```

Input format: a row letter from `A` to `J` followed by a column number from `1` to `10`, for example `B4` or `H10`. In version 2 and 3, when placing your own ships you enter the starting coordinate and then a direction (`h` for horizontal, `v` for vertical).

### Implementation

- Grid represented as a list of lists of characters, initialised with `.` for empty water
- Random placement with collision and boundary checks via a dedicated `case_libre` function
- Turn-based game loop with input validation for row letter and column number
- Hit, sink, and miss detection based on comparing the shot grid with the solution grid
- Win detection based on counting sunk ships (`flotte_coules`)
- Smart AI in version 3 keeps a short memory of recent hits, switches between random search and targeting mode, and infers the ship orientation to speed up sinking

---

## Français

### Auteures

Auteures : Kombila Jamelia et Maha Bouslimani.
Pour le projet Python de l'année IMDS3A (année universitaire 2024/2025, rendu en janvier 2025).

### Présentation

Implémentation console du jeu classique de la Bataille Navale en Python. La grille est un damier 10 par 10 dont les lignes sont étiquetées de A à J et les colonnes de 1 à 10. Chaque camp dispose d'une flotte de cinq bateaux de tailles différentes, et les joueurs tirent à tour de rôle sur des coordonnées jusqu'à ce qu'une flotte soit entièrement coulée.

### Principe du jeu

Chaque joueur possède une grille 10 par 10 sur laquelle il place une flotte de cinq bateaux. Les bateaux sont disposés horizontalement ou verticalement, ne peuvent pas se chevaucher et doivent tenir dans la grille. Les joueurs annoncent tour à tour une coordonnée (lettre de ligne et numéro de colonne). L'adversaire indique si le tir est à l'eau, touche un bateau, ou le coule. Le premier joueur à couler toute la flotte adverse gagne la partie.

### Flotte

| Bateau | Taille (cases) |
|--------|----------------|
| Porte-avion | 5 |
| Croiseur | 4 |
| Sous-marin | 3 |
| Torpilleur | 2 |
| Barque | 1 |

### Interface

Nous avons choisi de représenter le jeu en console avec les motifs suivants :

| Motif | Signification |
|-------|---------------|
| `.` | Case vide |
| `*` | Tir dans l'eau |
| `+` | Case d'un bateau touché |
| `x` | Case d'un bateau coulé |
| lettre du bateau | Case d'un bateau sur la grille solution |

### Les trois versions

1. **Version 1 (solo).** L'ordinateur place sa flotte aléatoirement. Le joueur saisit des coordonnées une par une pour tenter de trouver et couler tous les bateaux. Une seconde grille révèle la solution complète à la fin.
2. **Version 2 (deux joueurs, IA aléatoire).** Le joueur place lui-même sa flotte bateau par bateau, l'ordinateur place la sienne aléatoirement, et les deux camps jouent à tour de rôle. L'ordinateur tire à des coordonnées aléatoires qu'il n'a pas déjà jouées.
3. **Version 3 (deux joueurs, IA intelligente).** Identique à la version 2 mais l'ordinateur bascule en mode ciblage dès qu'il touche un bateau : il essaie les cases adjacentes, déduit l'orientation du bateau dès qu'il a deux touches consécutives, et continue selon cet axe jusqu'à couler le bateau. Cela rend l'ordinateur beaucoup plus redoutable.

### Structure du projet

```
├── src/
│   ├── bataille_navale_v1.py   Version solo
│   ├── bataille_navale_v2.py   Version à deux avec IA aléatoire
│   └── bataille_navale_v3.py   Version à deux avec IA intelligente
├── LICENSE
└── README.md
```

### Comment lancer le jeu

Prérequis : Python 3.8 ou supérieur. Aucune dépendance externe.

```bash
git clone https://github.com/jokombila/battleship-python.git
cd battleship-python

# Choisir la version à jouer
python3 src/bataille_navale_v1.py
python3 src/bataille_navale_v2.py
python3 src/bataille_navale_v3.py
```

Format de saisie : une lettre de ligne de `A` à `J` suivie d'un numéro de colonne de `1` à `10`, par exemple `B4` ou `H10`. Dans les versions 2 et 3, pour placer vos propres bateaux vous saisissez la coordonnée de départ puis une direction (`h` pour horizontal, `v` pour vertical).

### Réalisation

- Grille représentée par une liste de listes de caractères, initialisée avec `.` pour l'eau
- Placement aléatoire avec vérification des collisions et des limites via une fonction `case_libre`
- Boucle de jeu tour par tour avec validation des entrées (lettre de ligne, numéro de colonne)
- Détection des coups (à l'eau, touché, coulé) en comparant la grille de tirs avec la grille solution
- Détection de victoire basée sur le comptage des bateaux coulés (`flotte_coules`)
- IA intelligente en version 3 : mémoire courte des touches récentes, bascule entre recherche aléatoire et mode ciblage, et déduction de l'orientation du bateau pour accélérer la mise à mort

### Auteures

Projet réalisé par **Jamelia Kombila** et **Maha Bouslimani** dans le cadre de la formation IMDS3A en Informatique (2024/2025).
GitHub : [@jokombila](https://github.com/jokombila)

---

## License / Licence

This project is licensed under the MIT License, see [LICENSE](LICENSE).
Ce projet est distribué sous licence MIT, voir [LICENSE](LICENSE).
