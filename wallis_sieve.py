import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import argparse
import math

def draw_wallis_sieve(x, y, size, depth, ax, level=1):
    if depth == 0:
        ax.add_patch(Rectangle((x, y), size, size, fill=True, color='black'))
        return
    n = 2 * level + 1  # 3,5,7,...
    new_size = size / n
    for i in range(n):
        for j in range(n):
            if i == n//2 and j == n//2:
                continue  # remove center
            draw_wallis_sieve(x + i * new_size, y + j * new_size, new_size, depth - 1, ax, level + 1)

def main():
    parser = argparse.ArgumentParser(description='Wallis Sieve')
    parser.add_argument('--depth', type=int, default=4, help='Recursion depth')
    args = parser.parse_args()

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    draw_wallis_sieve(0, 0, 1, args.depth, ax)
    ax.axis('off')
    plt.title(f'Wallis Sieve - Depth {args.depth} (Area → π/4)')
    plt.savefig(f'wallis_sieve_depth_{args.depth}.png')
    plt.show()

    # Approximate remaining area
    area = 1.0
    for k in range(1, args.depth + 1):
        odd = 2 * k + 1
        area *= (odd**2 - 1) / odd**2
    print(f'Approximate remaining area after depth {args.depth}: {area:.6f} (π/4 ≈ {math.pi/4:.6f})')

if __name__ == "__main__":
    main()
