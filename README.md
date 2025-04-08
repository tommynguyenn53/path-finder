# Terminal Maze Pathfinding Visualiser

A terminal-based pathfinding visualiser built with Python and the `curses` library. This project demonstrates the **Breadth-First Search (BFS)** algorithm to find the shortest path in a maze, with live animation directly in the terminal.

## Demo

To run the visualiser locally, follow these steps:

1. **Clone the repository and run code**:
   ```bash
   git clone https://github.com/tommynguyenn53/path-finder.git
   cd path-finder
   python3 path-finder.py

## Features
- **BFS Pathfinding**: Implements the Breadth-First Search algorithm to find the shortest path from a start to an end point.
- **Live Animation**: Visualises the algorithm’s progress step-by-step in the terminal.
- **Color-Coded Display**:
  - Blue: walls and open spaces. 
  - Red: path being explored, start point O, and end point X. 



## Technologies Used
- ****Python** 3**
- **curses**: For terminal-based graphics and rendering.
- **queue**: To manage nodes during BFS.
- **time**: To create delay for animation effect.

