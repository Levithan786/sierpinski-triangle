"""ASCII Sierpinski triangle using bitwise operations.
Prepended as another gap-filler: console-only, no dependencies."""

def print_sierpinski(levels=5):
    size = 1 << levels
    for y in range(size):
        row = ''.join('*' if (x & y) == 0 else ' ' for x in range(size))
        print(row)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Print ASCII Sierpinski')
    parser.add_argument('--levels', type=int, default=6)
    args = parser.parse_args()
    print_sierpinski(args.levels)

# Example usage: python ascii_sierpinski.py --levels 7