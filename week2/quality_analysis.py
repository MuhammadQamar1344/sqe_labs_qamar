import numpy as np
import matplotlib.pyplot as plt

# Labels
categories = [
    "Functional",
    "Performance",
    "Compatibility",
    "Usability",
    "Reliability",
    "Security",
    "Maintainability",
    "Portability"
]

# Your actual ratings
daraz = [4,4,4,5,4,4,4,4]
amazon = [4,4,4,4,4,4,3,4]

# Repeat first value to close shape
daraz += daraz[:1]
amazon += amazon[:1]

N = len(categories)
angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# Plot
fig, ax = plt.subplots(figsize=(8,8), subplot_kw=dict(polar=True))

ax.plot(angles, daraz, linewidth=2, label="Daraz (4.15/5)")
ax.fill(angles, daraz, alpha=0.25)

ax.plot(angles, amazon, linewidth=2, label="Amazon (3.92/5)")
ax.fill(angles, amazon, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

ax.set_yticks([1,2,3,4,5])
ax.set_ylim(0,5)

plt.title("Quality Comparison Radar Chart")
plt.legend(loc="upper right", bbox_to_anchor=(1.3,1.1))

plt.savefig("radar_chart.png", dpi=300, bbox_inches="tight")
plt.show()