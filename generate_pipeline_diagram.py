"""Generate a pipeline workflow diagram for the showcase README."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(14, 5))
ax.set_xlim(0, 14)
ax.set_ylim(0, 5)
ax.axis('off')

# Color scheme
C_DATA = '#3498db'
C_MODEL = '#e74c3c'
C_OPT = '#f39c12'
C_RESULT = '#2ecc71'
C_ARROW = '#555555'

box_style = dict(boxstyle='round,pad=0.5', linewidth=2)

# ---- Row 1: Main pipeline ----
boxes = [
    (1.5, 3.5, 'Resting-State\nEEG Data', C_DATA),
    (4.5, 3.5, 'PSD Extraction\n(Welch + SpecParam)', C_DATA),
    (7.5, 3.5, 'Evolutionary\nOptimization', C_OPT),
    (10.5, 3.5, 'Optimized\nParameters', C_RESULT),
    (13.0, 3.5, 'Validation\n& Report', C_RESULT),
]

for x, y, text, color in boxes:
    bbox = dict(boxstyle='round,pad=0.45', facecolor=color, alpha=0.15,
                edgecolor=color, linewidth=2)
    ax.text(x, y, text, ha='center', va='center', fontsize=11,
            fontweight='bold', bbox=bbox, color='#2c3e50')

# Arrows between main boxes
arrow_props = dict(arrowstyle='->', color=C_ARROW, lw=2, 
                   connectionstyle='arc3,rad=0')
for (x1, _, _, _), (x2, _, _, _) in zip(boxes[:-1], boxes[1:]):
    ax.annotate('', xy=(x2 - 1.1, 3.5), xytext=(x1 + 1.1, 3.5),
                arrowprops=arrow_props)

# ---- Row 2: Model feedback loop ----
ax.text(7.5, 1.3, 'Wendling Neural\nMass Model', ha='center', va='center',
        fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.45', facecolor=C_MODEL, alpha=0.15,
                  edgecolor=C_MODEL, linewidth=2), color='#2c3e50')

ax.text(10.5, 1.3, 'Simulated\nPSD', ha='center', va='center',
        fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.45', facecolor=C_MODEL, alpha=0.15,
                  edgecolor=C_MODEL, linewidth=2), color='#2c3e50')

# Arrow: Optimization -> Model
ax.annotate('', xy=(7.5, 1.95), xytext=(7.5, 2.85),
            arrowprops=dict(arrowstyle='->', color=C_ARROW, lw=2))
ax.text(7.0, 2.4, 'params', fontsize=9, fontstyle='italic', color='#777')

# Arrow: Model -> Simulated PSD
ax.annotate('', xy=(9.4, 1.3), xytext=(8.6, 1.3),
            arrowprops=arrow_props)

# Arrow: Simulated PSD -> Optimization (loss)
ax.annotate('', xy=(8.6, 3.0), xytext=(10.5, 1.95),
            arrowprops=dict(arrowstyle='->', color=C_OPT, lw=2,
                            connectionstyle='arc3,rad=-0.3'))
ax.text(10.2, 2.5, 'loss', fontsize=9, fontstyle='italic', color='#777')

# Arrow: Empirical PSD -> Optimization (target)
ax.annotate('', xy=(6.9, 3.0), xytext=(5.6, 3.2),
            arrowprops=dict(arrowstyle='->', color=C_DATA, lw=1.5,
                            connectionstyle='arc3,rad=0.2', linestyle='dashed'))
ax.text(5.8, 2.7, 'target', fontsize=9, fontstyle='italic', color='#777')

# Labels
ax.text(7.5, 0.3, 'Optimization Loop (50 generations × 50 individuals)',
        ha='center', va='center', fontsize=10, fontstyle='italic', color='#888')

# Title
ax.text(7.0, 4.7, 'Pipeline: EEG → Model Fitting → Validation',
        ha='center', va='center', fontsize=14, fontweight='bold', color='#2c3e50')

plt.tight_layout()
plt.savefig('docs/images/pipeline_diagram.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
print("→ docs/images/pipeline_diagram.png")
