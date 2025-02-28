def largestGreenArea(li):
    n = len(li)
    m = len(li[0])

    # Convert pixels to binary: 1 for green, 0 otherwise
    for r in range(len(li)):
        for c in range(len(li[0])):
            pixel = li[r][c]
            if pixel[1] > pixel[0] and pixel[1] > pixel[2] and pixel[1] > 50:
                li[r][c] = 1
            else:
                li[r][c] = 0


    print(li)
    # Initialize maximum area
    max_area = 0

    # Brute force to find all possible rectangles
    for i in range(n):
        for j in range(m):
            if li[i][j] == 0:
                continue
            for k in range(i, n):
                for l in range(j, m):
                    # Check if all pixels in the rectangle are green
                    is_all_green = True
                    for x in range(i, k + 1):
                        for y in range(j, l + 1):
                            if li[x][y] == 0:
                                is_all_green = False
                                break
                        if not is_all_green:
                            break
                    if is_all_green:
                        width = l - j + 1
                        height = k - i + 1
                        area = width * height
                        # Choose the one with greater value
                        max_area = max(max_area, area)

    print(f"Max green field area: {max_area}")

def main():
    # Input is a 2D list of RGB values
    image = [
        [(0, 0, 0), (0, 100, 0), (0, 120, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 110, 0), (0, 130, 0), (0, 140, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 120, 0), (0, 150, 0), (0, 170, 0), (0, 180, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    ]

    largestGreenArea(image)

if __name__ == "__main__":
    main()
