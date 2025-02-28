from HW4_Utils import raiseNotDefined, Point
import math
from random import randint
import dudraw

'''
Programming Project 4 - Closest Pair
Name: Anh Tran
Date: 02/21/25
Collaborators: None
'''

# Helper functions
# Q1
def distance_between(a: Point, b: Point) -> float:
    '''
    Calculates the distance between two points
    a, b: points
    Return: Distance between the two points
    '''
    # calculate distance sqrt( (x2-x1)^2 - (y2-y1)^2 )
    return math.sqrt((b.x-a.x)**2 + (b.y-a.y)**2)

# Q2 - Brute Force
def closest_pair_brute_force(S: list[Point]) -> tuple[Point, Point] | None:
    '''
    Calculates the pair of points that are closest together using brute force
    S: list of points
    Return: Tuple containing the closest two points
    '''
    if len(S) < 2:  # Added check for fewer than 2 points
        return None  # No points or only one point to compare, so return None
    
    tempCloses = (S[0], S[1])
    tempClosesDistance = float('inf')
    
    # for every points in S list
    for i in range(len(S)):
        for j in range(i + 1, len(S)):  # for every other point in S except i
            distance = distance_between(S[i], S[j])  # calculate the distance of every points
            if distance < tempClosesDistance:  # if it smaller than temp distance, replace
                tempClosesDistance = distance 
                tempCloses = (S[i], S[j])  # change the new closest pair
    
    return tuple(sorted(tempCloses, key=lambda p: (p.x, p.y)))


# Q3a
def closest_pair_dac_start(S: list[Point]) -> tuple[Point, Point] | None:
    '''
    Starts calculating the closest pair of points using the divide and conquer algorithm described in the book.
    S: list of points
    Return: Tuple containing the closest two points
    '''
    # main
    # delta1 = CP(P-left) ,  delta2 = CP(P-right)
    # min of (delta1, delta2) is the closes point
    if len(S) < 2:
        return None
    
    
    S_sorted_x = sorted(S, key=lambda point: point.x)  # sort x-axis
    S_sorted_y = sorted(S, key=lambda point: point.y)  # sort y-axis
    # call to calculate the closes pair recursively.
    return closest_pair_dac(S_sorted_x, S_sorted_x, S_sorted_y)


# Q3b
def closest_pair_dac(P: list[Point], X: list[Point], Y: list[Point]) -> tuple[Point, Point] | None:
    '''
    Recursively computes closest pair
    P: list of points, subset of Q
    X: all points in P, sorted by x value
    Y: all points in P, sorted by y value
    Return: tuple containing the closest two points
    '''
    # Now you have list x and list y sorted.
    # return the closes pair using brute force if less then three.
    if len(P) < 2:
        return None

    if len(P) <= 3:
        return closest_pair_brute_force(P)  # returns closest pair by brute force if <= 3 points
    
    mid = len(P) // 2  # divide the list
    mid_x = X[mid].x 
    left_half = X[:mid]  # first half of the list
    right_half = X[mid:]  # second half of the list
    
    # list of y values on the left and right side of the median
    left_y = [p for p in Y if p in left_half]  
    right_y = [p for p in Y if p in right_half]  
    
    # recursive calls to find closest pairs on the left and right
    closest_pair_left = closest_pair_dac(left_half, left_half, left_y) 
    closest_pair_right = closest_pair_dac(right_half, right_half, right_y)

    # if one of the recursive calls returns None possible the list is small
    if not closest_pair_left:
        closest_pair_left = closest_pair_right
    if not closest_pair_right:
        closest_pair_right = closest_pair_left
    
    delta_left = distance_between(*closest_pair_left) if closest_pair_left else float('inf')
    delta_right = distance_between(*closest_pair_right) if closest_pair_right else float('inf')

    delta = min(delta_left, delta_right)  # comparing the closest distances

    # determine the closest pair by comparing delta_left and delta_right.
    closest_pair = closest_pair_left if delta_left < delta_right else closest_pair_right
    
    # list of points that are closer to delta distance for the middle line (x-coordinate)
    cross_points = [p for p in Y if abs(p.x - mid_x) < delta]

    for i in range(len(cross_points)):  # compare points in the cross section
        for j in range(i + 1, min(i + 8, len(cross_points))):  # no more than 7 points of neighbors
            d = distance_between(cross_points[i], cross_points[j])
            if d < delta:  # if the distance is less than delta
                delta = d  # update the closest distance
                closest_pair = (cross_points[i], cross_points[j])  # update closest pair
    
    return closest_pair

def generate_points(n: int) -> list[Point] | None:
    '''
    In order to test that your algorithm works, you can randomly generate a set of points.
    You can then use these random points in the draw_hull() function.
    n = number of Points
    '''
    P = [] # points list

    # randomly generates set of points.
    return [Point(randint(2, 100), randint(2, 100)) for _ in range(n)]


        
def draw_closest_pair(points: list[Point], closest_pair: tuple[Point, Point]) -> None:
    '''
    Draw the points and the closest pair of points
    points: list of points
    closest_pair: tuple containing the closest two points
    '''
    if not closest_pair:
        return  

    dudraw.clear(dudraw.WHITE)

    # the closes pair of points
    p1, p2 = closest_pair

    for p in points:
        # check if the point have same value as the closes point
        if p == p1 or p == p2:  
            dudraw.set_pen_color(dudraw.RED)
        else:
            # draw closes point in another color
            dudraw.set_pen_color(dudraw.DARK_GRAY)
        dudraw.filled_circle(p.x, p.y, 2)


    dudraw.show(10000)

def main():
    dudraw.set_canvas_size(500, 500)  
    dudraw.set_x_scale(0, 102)
    dudraw.set_y_scale(0, 102)

    # number of points to generate
    num_points = 20  

    # generate random points
    points = generate_points(num_points)

    # find closest pair using brute force
    brute_force_closest = closest_pair_brute_force(points)

    # find closest pair using divide and conquer
    dac_closest = closest_pair_dac_start(points)

    print("Brute Force Closest Pair:", brute_force_closest)
    print("Divide & Conquer Closest Pair:", dac_closest)

    if dac_closest:
        draw_closest_pair(points, dac_closest)
    else:
        print("No closest pair found.")

if __name__ == "__main__":
    main()

