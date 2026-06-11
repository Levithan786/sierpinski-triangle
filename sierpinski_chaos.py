import numpy as np
import matplotlib.pyplot as plt
import random

def sierpinski_chaos_game(iterations=50000):
    vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
    point = np.random.rand(2) * 1.0
    points = np.zeros((iterations, 2))
    for i in range(iterations):
        vertex = vertices[random.randint(0, 2)]
        point = (point + vertex) / 2
        points[i] = point
    plt.figure(figsize=(8, 8 * np.sqrt(3)/2))
    plt.scatter(points[:, 0], points[:, 1], s=0.5, color='darkblue', alpha=0.6)
    plt.axis('equal')
    plt.axis('off')
    plt.title('Sierpinski Triangle – Chaos Game (from inside out)')
    plt.savefig('sierpinski_chaos.png')
    plt.show()

if __name__ == "__main__":
    sierpinski_chaos_game(100000)
