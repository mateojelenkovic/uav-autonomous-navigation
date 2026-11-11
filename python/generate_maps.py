# creating simple grid for UAV navigation
grid = [ 
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

# Define the start and goal positions
start = (0, 0)
goal = (4, 4)


# Visualize the grid and the start/goal positions
import matplotlib.pyplot as plt

# Display the grid
plt.imshow(grid, cmap="Greys", vmin=0, vmax=1)

# Display the drone's start and goal
plt.scatter(start[1], start[0], color="green", s=200, label="Start")
plt.scatter(goal[1], goal[0], color="blue", s=200, label="Goal")

# Add labels and title
plt.title("UAV Navigation Environment")
plt.legend()



# Setting the directions for movement (up, down, left, right)
directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]

# Initialize the frontier with the start position and a set to keep track of reached positions
frontier = [start]
reached = {start}
came_from = {start: None}

# Exploring the grid using a simple breadth-first search algorithm
while frontier:
    current = frontier.pop(0)
    print("Exploring:", current)

    if current == goal:
        print("Destination reached!")
        break

    for dr, dc in directions:
        new_row = current[0] + dr
        new_col = current[1] + dc

        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            next_pos = (new_row, new_col)

            if grid[new_row][new_col] == 0 and next_pos not in reached:
                frontier.append(next_pos)
                reached.add(next_pos)
                came_from[next_pos] = current

# Reconstruct the path from start to goal
path = []
current = goal

while current is not None:
    path.append(current)
    current = came_from[current]

path.reverse()

print("Final path:", path)

# Visualize the path on the grid
path_rows = []
path_cols = []
for row, col in path:
    path_rows.append(row)
    path_cols.append(col)

plt.plot(path_cols, path_rows, color="red", linewidth=3, label="BFS Path")

plt.legend()
plt.show()