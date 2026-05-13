"""Generate an original Wendling model structure diagram for the README."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def add_box(ax, xy, width, height, label, face, edge):
    x, y = xy
    box = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.04,rounding_size=0.04",
        linewidth=2.0,
        facecolor=face,
        edgecolor=edge,
    )
    ax.add_patch(box)
    ax.text(
        x + width / 2,
        y + height / 2,
        label,
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
        color="#233142",
    )


def add_arrow(ax, start, end, color, label=None, rad=0.0, inhibitory=False):
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="-[" if inhibitory else "->",
        mutation_scale=14,
        linewidth=2.2,
        color=color,
        connectionstyle=f"arc3,rad={rad}",
    )
    ax.add_patch(arrow)
    if label:
        mx = (start[0] + end[0]) / 2
        my = (start[1] + end[1]) / 2
        ax.text(
            mx,
            my + 0.12,
            label,
            ha="center",
            va="center",
            fontsize=9,
            color=color,
            bbox=dict(boxstyle="round,pad=0.18", facecolor="white", edgecolor="none"),
        )


fig, ax = plt.subplots(figsize=(11, 6.5))
ax.set_xlim(0, 11)
ax.set_ylim(0, 6.5)
ax.axis("off")

exc = "#2f80ed"
inh_slow = "#8e44ad"
inh_fast = "#d35400"

add_box(ax, (4.0, 3.05), 3.0, 1.05, "Pyramidal cells\noutput: y1 - y2 - y3", "#f7fbff", "#233142")
add_box(ax, (0.8, 4.85), 2.4, 0.85, "Excitatory\ninterneurons", "#edf6ff", exc)
add_box(ax, (0.8, 1.0), 2.4, 0.85, "Slow inhibitory\ninterneurons", "#f5edff", inh_slow)
add_box(ax, (7.8, 1.0), 2.4, 0.85, "Fast inhibitory\ninterneurons", "#fff3e8", inh_fast)
add_box(ax, (4.3, 5.25), 2.4, 0.7, "External input", "#f6f6f6", "#666666")

add_arrow(ax, (5.5, 5.25), (5.5, 4.1), "#666666", "stochastic drive")
add_arrow(ax, (3.2, 5.25), (4.0, 3.85), exc, "A, a", rad=-0.15)
add_arrow(ax, (4.0, 3.35), (3.2, 1.55), inh_slow, "B, b", rad=-0.14, inhibitory=True)
add_arrow(ax, (7.0, 3.35), (7.8, 1.55), inh_fast, "G, g", rad=0.14, inhibitory=True)
add_arrow(ax, (4.0, 3.55), (3.2, 5.15), exc, "feedback", rad=0.15)
add_arrow(ax, (7.0, 3.55), (7.8, 1.35), inh_fast, "feedback", rad=-0.16)

ax.text(5.5, 6.18, "Wendling Neural Mass Model: Four-Population Cortical Column", ha="center", fontsize=15, fontweight="bold", color="#233142")
ax.text(5.5, 0.32, "Original schematic drawn for this demo. It summarizes modeled connections rather than reproducing a paper figure.", ha="center", fontsize=9.5, color="#555555")

ax.plot([0.55, 10.45], [0.62, 0.62], color="#dddddd", linewidth=1)
ax.text(0.8, 0.14, "Blue: excitatory pathway", fontsize=9, color=exc)
ax.text(3.65, 0.14, "Purple/orange: inhibitory pathways", fontsize=9, color=inh_slow)
ax.text(7.0, 0.14, "A/B/G: gains; a/b/g: time constants", fontsize=9, color="#555555")

plt.tight_layout()
plt.savefig("docs/images/wendling_architecture.png", dpi=180, bbox_inches="tight", facecolor="white")
plt.close()
print("docs/images/wendling_architecture.png")
