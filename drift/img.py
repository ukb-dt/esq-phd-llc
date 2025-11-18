import matplotlib.pyplot as plt

# Define node positions
positions = {'ESQ': (0, 0), 'PhD': (0, 1), 'R01': (-1, 2), 'LLC': (1, 2)}

# Plot nodes
plt.figure(figsize=(6,6))
for node, (x, y) in positions.items():
    plt.scatter(x, y, s=500, zorder=3, color='skyblue')
    plt.text(x, y+0.1, node, ha='center', fontsize=12)

# Plot edges with colors and styles
edges = [('ESQ', 'PhD', 'solid', 'blue'), ('PhD', 'R01', 'solid', 'blue'), ('PhD', 'LLC', 'dashed', 'orange')]
for start, end, style, color in edges:
    x_values = [positions[start][0], positions[end][0]]
    y_values = [positions[start][1], positions[end][1]]
    plt.plot(x_values, y_values, linestyle=style, color=color, linewidth=2, zorder=2)

# Add annotations
plt.text(-0.8, 2.1, 'Stable Attractor', color='blue', fontsize=10)
plt.text(0.8, 2.1, 'Drift Path', color='orange', fontsize=10)

plt.axis('off')
plt.title('Phase-Space Mapping: ESQ → PhD → {R01, LLC}', fontsize=14)
plt.show()
