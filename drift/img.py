import matplotlib.pyplot as plt

# Define node positions with aggressive spacing
positions = {
    'ESQ': (0, 0),
    'PhD': (0, 3),
    'R01': (-3, 6),
    'LLC': (3, 6)
}

# Create larger figure
plt.figure(figsize=(12, 10))

# Plot nodes
for node, (x, y) in positions.items():
    plt.scatter(x, y, s=900, zorder=3, color='skyblue', edgecolor='k', linewidth=1.5)
    plt.text(x, y + 0.35, node, ha='center', va='bottom', fontsize=16, fontweight='bold', color='black')

# Plot edges with color coding
edges = [
    ('ESQ', 'PhD', 'solid', 'blue'),
    ('PhD', 'R01', 'solid', 'blue'),
    ('PhD', 'LLC', 'dashed', 'orange')
]
for start, end, style, color in edges:
    x_values = [positions[start][0], positions[end][0]]
    y_values = [positions[start][1], positions[end][1]]
    plt.plot(x_values, y_values, linestyle=style, color=color, linewidth=3, zorder=2)

# Add colored annotations with extra vertical spacing
plt.text(-3, 6.6, 'Stable Attractor', color='blue', fontsize=15, fontweight='bold', ha='center')
plt.text(3, 6.6, 'Drift Path', color='orange', fontsize=15, fontweight='bold', ha='center')

# Remove axes
plt.axis('off')

# Add title with extra padding
plt.title('Phase-Space Mapping: ESQ → PhD → {R01, LLC}', fontsize=22, pad=50, fontweight='bold')

# Save figure
plt.savefig('bifurcation.jpg', bbox_inches='tight', dpi=300)

# Show plot
plt.show()
