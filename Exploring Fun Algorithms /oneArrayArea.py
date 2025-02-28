def OneArrayAreaBruteForce(li: list):
    if not li:  
        print(0)
        return

    maxi = 0 

    for i in range(len(li)):
        height = li[i]

        left = i
        # Check the left sides
        while left > 0 and li[left - 1] >= height:
            left -= 1

        right = i 
        # Check the right side
        while right < len(li) - 1 and li[right + 1] >= height:
            right += 1 #increment to keep looping

        # checking right - left give the distance between two index.
        # choose the larger area value
        maxi = max(maxi, height * (right - left + 1))

    print(maxi)  

def OneArrayAreaOofN(li: list):

    stack = []  # stack list
    max_area = 0 
    n = len(li) 

    for i in range(n + 1):  
        # help to empty the list
        if i < n:
            #Assign current height
            current_height = li[i]
        else:
            current_height = 0 
        # pop an element from stack if the current height less than the top value in stack
        while stack and (i == n or current_height < li[stack[-1]]):
            index = stack.pop()
            # height of rect is height of the index pop from stack
            height = li[index]
            # from current index to top of index - 1
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i) # append index
    return max_area


def main():
  maxArea = OneArrayAreaBruteForce([1,2, 1, 1, 1, 1])
  maxArea2 = OneArrayAreaOofN([1, 3, 4, 4, 4, 4])
  print(maxArea2)
if __name__ == "__main__":
  main()