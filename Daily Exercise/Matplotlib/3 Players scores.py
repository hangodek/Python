import matplotlib.pyplot as plt
import numpy as np

player_a = np.array([15, 20, 30, 25, 40])
player_b = np.array([10, 18, 25, 22, 36])
player_c = np.array([8, 15, 18, 20, 28])

plt.plot(player_a, ls = ":", label = "Player A")
plt.plot(player_b, ls = ":", label = "Player B")
plt.plot(player_c, ls = ":", label = "Player C")
plt.title("Score")
plt.xlabel("Round")
plt.ylabel("Scores")
plt.legend()
plt.show()