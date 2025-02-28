import matplotlib.pyplot as plt
import matplotlib.patches as patches

def contourRectangle(rectangles):
    """
    Compute the contour of a collection of rectangles without sorting events.
    :param rectangles: List of rectangles, each represented as [left, top, right, bottom].
    :return: List of vertices defining the contour.
    """
    # Step 1: Find the range of x-coordinates
    min_x = min(rect[0] for rect in rectangles)
    max_x = max(rect[2] for rect in rectangles)
    
    # Step 2: Create the height map
    heights = [0] * (max_x - min_x + 1)  # Array to store heights at each x-coordinate

    # Step 3: Populate the height map
    for left, top, right, _ in rectangles:
        for x in range(left, right):
            heights[x - min_x] = max(heights[x - min_x], top)

    # Step 4: Extract the contour with vertical edges
    contour = []
    prev_height = 0
    for x in range(len(heights)):
        if heights[x] != prev_height:
            # Add vertical transition if height changes
            contour.append((x + min_x, prev_height))
            contour.append((x + min_x, heights[x]))
            prev_height = heights[x]

    # Ensure the contour ends properly
    contour.append((max_x, 0))
    return contour

def drawRectanglesAndContour(rectangles, contour):
    """
    Visualize the input rectangles and their computed contour.
    :param rectangles: List of rectangles, each represented as [left, top, right, bottom].
    :param contour: List of vertices defining the contour.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Draw rectangles
    for left, top, right, bottom in rectangles:
        width = right - left
        height = top - bottom
        rect = patches.Rectangle((left, bottom), width, height, linewidth=1, edgecolor='blue', facecolor='lightblue', alpha=0.5)
        ax.add_patch(rect)

    # Draw contour
    contour_x, contour_y = zip(*contour)
    ax.plot(contour_x, contour_y, color='red', linewidth=2, label="Contour")

    # Add labels and legend
    ax.set_xlim(0, max(max(rect[2] for rect in rectangles), max(contour_x) + 1))
    ax.set_ylim(0, max(max(rect[1] for rect in rectangles), max(contour_y) + 1))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()
    ax.grid(True)
    plt.title("Rectangles and Contour")
    plt.show()

# Example Input
rectangles = [
    [1, 3, 4, 0],  # Rectangle from (1, 3) to (4, 0)
    [2, 4, 6, 0],  # Rectangle from (2, 4) to (6, 0)
    [5, 2, 8, 0],  # Rectangle from (5, 2) to (8, 0)
]

# Compute the contour
contour = contourRectangle(rectangles)

# Draw the rectangles and contour
drawRectanglesAndContour(rectangles, contour)
