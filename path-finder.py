import curses
from curses import wrapper
import queue
import time

# Maze layout where:
# '#' = wall, 'O' = start, 'X' = end, ' ' = walkable path
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def print_maze(maze, stdscr, path=[]):
    """Render the maze to the terminal, highlighting the path and start/end."""
    BLUE = curses.color_pair(1)  # Blue for walls and normal cells
    RED = curses.color_pair(2)   # Red for the path, start, and end

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            char = value
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", RED)  # Draw path as red X
            elif value in ("O", "X"):
                stdscr.addstr(i, j * 2, char, RED)  # Start and End
            else:
                stdscr.addstr(i, j * 2, char, BLUE)  # Walls and empty spaces


def find_start(maze, start):
    """Find the coordinates of the start character (e.g., 'O') in the maze."""
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None


def find_path(maze, stdscr):
    """Run BFS to find the shortest path from 'O' to 'X', animating the search."""
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    # BFS queue: stores tuples of (current_position, path_to_here)
    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        # Clear and redraw maze with current path
        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        # Check if we've reached the goal
        if maze[row][col] == end:
            return path

        # Explore valid neighboring positions
        neighbours = find_neighbors(maze, row, col)

        for neighbour in neighbours:
            if neighbour in visited:
                continue

            visited.add(neighbour)  # Mark as visited to avoid revisiting

            r, c = neighbour
            if maze[r][c] == "#":
                continue  # Skip walls

            new_path = path + [neighbour]  # Build new path
            q.put((neighbour, new_path))   # Enqueue next move


def find_neighbors(maze, row, col):
    """Return a list of valid neighboring coordinates (up, down, left, right)."""
    neighbors = []

    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT
        neighbors.append((row, col + 1))

    return neighbors


def main(stdscr):
    """Set up curses and start the pathfinding visualization."""
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)  # For maze
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)   # For path

    find_path(maze, stdscr)  # Run BFS and animate
    stdscr.getch()  # Wait for key press before exiting


wrapper(main)  # Start the curses wrapper which handles setup and teardown
