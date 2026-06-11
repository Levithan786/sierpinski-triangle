import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import argparse

def draw_carpet(x, y, size, depth, ax):
    """Recursive function to draw Sierpinski carpet."""
    if depth == 0:
        ax.add_patch(Rectangle((x, y), size, size, fill=True, color='black'))
        return
    new_size = size / 3.0
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue  # remove center square
            draw_carpet(x + i * new_size, y + j * new_size, new_size, depth - 1, ax)

def main():
    parser = argparse.ArgumentParser(description='Sierpinski Carpet')
    parser.add_argument('--depth', type=int, default=5, help='Recursion depth')
    args = parser.parse_args()

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    draw_carpet(0, 0, 1, args.depth, ax)
    ax.axis('off')
    plt.title(f'Sierpinski Carpet - Depth {args.depth}')
    plt.savefig(f'sierpinski_carpet_depth_{args.depth}.png')
    plt.show()

if __name__ == "__main__":
    main()
