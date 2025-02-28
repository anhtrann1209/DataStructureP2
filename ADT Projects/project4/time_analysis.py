import time
import matplotlib.pyplot as plt
from random import randint
import math

# Point class definition for testing
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Helper function to calculate distance between two points
def distance_between(a: Point, b: Point) -> float:
    return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)

# Brute Force Algorithm to find the closest pair
def closest_pair_brute_force(S: list[Point]) -> tuple[Point, Point] | None:
    if len(S) < 2:
        return None

    tempCloses = (S[0], S[1])
    tempClosesDistance = float('inf')

    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            distance = distance_between(S[i], S[j])
            if distance < tempClosesDistance:
                tempClosesDistance = distance
                tempCloses = (S[i], S[j])

    return tuple(sorted(tempCloses, key=lambda p: (p.x, p.y)))

# Divide and Conquer Algorithm to find the closest pair
def closest_pair_dac_start(S: list[Point]) -> tuple[Point, Point] | None:
    if len(S) < 2:
        return None

    S_sorted_x = sorted(S, key=lambda point: point.x)
    S_sorted_y = sorted(S, key=lambda point: point.y)
    return closest_pair_dac(S_sorted_x, S_sorted_x, S_sorted_y)

def closest_pair_dac(P: list[Point], X: list[Point], Y: list[Point]) -> tuple[Point, Point] | None:
    if len(P) < 2:
        return None

    if len(P) <= 3:
        return closest_pair_brute_force(P)

    mid = len(P) // 2
    mid_x = X[mid].x
    left_half = X[:mid]
    right_half = X[mid:]

    left_y = [p for p in Y if p in left_half]
    right_y = [p for p in Y if p in right_half]

    closest_pair_left = closest_pair_dac(left_half, left_half, left_y)
    closest_pair_right = closest_pair_dac(right_half, right_half, right_y)

    if not closest_pair_left:
        closest_pair_left = closest_pair_right
    if not closest_pair_right:
        closest_pair_right = closest_pair_left

    delta_left = distance_between(*closest_pair_left) if closest_pair_left else float('inf')
    delta_right = distance_between(*closest_pair_right) if closest_pair_right else float('inf')

    delta = min(delta_left, delta_right)
    closest_pair = closest_pair_left if delta_left < delta_right else closest_pair_right

    cross_points = [p for p in Y if abs(p.x - mid_x) < delta]

    for i in range(len(cross_points)):
        for j in range(i + 1, min(i + 8, len(cross_points))):
            d = distance_between(cross_points[i], cross_points[j])
            if d < delta:
                delta = d
                closest_pair = (cross_points[i], cross_points[j])

    return closest_pair

# Helper function to generate random points
def generate_points(n: int) -> list[Point] | None:
    return [Point(randint(0, 100), randint(0, 100)) for _ in range(n)]

# Brute Force Runtime Test
def brute_force_runtime_test(max_n: int, step: int, number_of_trials: int):
    n_values = []
    time_values = []

    for n in range(step, max_n + 1, step):
        points = generate_points(n)

        start_time = time.time()
        for _ in range(number_of_trials):
            closest_pair_brute_force(points)
        end_time = time.time()

        elapsed_time = end_time - start_time
        average_runtime = elapsed_time / number_of_trials

        print(f"Brute Force - Number of points: {n}, Time taken: {elapsed_time:.6f} seconds")

        n_values.append(n)
        time_values.append(average_runtime)

    return n_values, time_values

# Divide and Conquer Runtime Test
def dac_runtime_test(max_n: int, step: int, number_of_trials: int):
    n_values = []
    time_values = []

    for n in range(step, max_n + 1, step):
        points = generate_points(n)

        start_time = time.time()
        for _ in range(number_of_trials):
            closest_pair_dac_start(points)
        end_time = time.time()

        elapsed_time = end_time - start_time
        average_runtime = elapsed_time / number_of_trials

        print(f"Divide & Conquer - Number of points: {n}, Time taken: {elapsed_time:.6f} seconds")

        n_values.append(n)
        time_values.append(average_runtime)

    return n_values, time_values

# Parameters for the test
max_n = 3600  # Maximum number of points
step = 200     # Step by which n increases
number_of_trials = 10  # Number of trials to average

# Run the brute force and divide and conquer tests
n_values_bf, time_values_bf = brute_force_runtime_test(max_n, step, number_of_trials)
n_values_dac, time_values_dac = dac_runtime_test(max_n, step, number_of_trials)

# Plotting Brute Force Runtime (Figure 1)
plt.figure(figsize=(10, 6))
plt.plot(n_values_bf, time_values_bf, label="Brute Force", color='b')
plt.title("Brute Force Runtime")
plt.xlabel("Number of Points (n)")
plt.ylabel("Average Runtime (seconds)")
plt.legend()
plt.grid(True)
plt.show()  # Show Figure 1

# Plotting Divide & Conquer Runtime (Figure 2)
plt.figure(figsize=(10, 6))
plt.plot(n_values_dac, time_values_dac, label="Divide & Conquer", color='r')
plt.title("Divide & Conquer Runtime")
plt.xlabel("Number of Points (n)")
plt.ylabel("Average Runtime (seconds)")
plt.legend()
plt.grid(True)
plt.show()  # Show Figure 2
