theBoxes = open('the-boxes.txt')

boxInfo = theBoxes.readlines()

 
all_data = []

for box in boxInfo:
    # replaces x in string with a comma
    inner_data = []
    box = box.replace("x", ",")
    # splits box into a list
    boxList = box.split(",")
    # converts each string in the list into an integer
    intList = [eval(i) for i in boxList]
    minSize = min(intList)
    # sets the length, width, height based off each integer in the list
    length, width, height = [intList[i] for i in (0, 1, 2)]
    # gets area of each side
    side1 = length * height
    side2 = length * width
    side3 = width * height
    sides = [side1, side2, side3]
    smallestSide = min(sides)
    fullArea = side1 * 2 + side2 * 2 + side3 * 2   
    paperAmount = fullArea + smallestSide
    all_data.append(paperAmount)

print(sum(all_data))
