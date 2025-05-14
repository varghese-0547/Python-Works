print ('Hi\nIf you have any doubt about the areas or perimeters of any shapes you can clear it here')
def rectangle(): 
    # Program to find the area and perimeter of a rectangle
    print ('Area and perimeter of a rectangle')
    l = float(input('Enter the length'))
    b = float(input('Enter the breadth'))
    area = l*b
    perimeter = 2*(l+b)
    print ('Area of the rectangle is',area,'and perimeter of the rectangle is ',perimeter)

def circle():
    #Program to find the area and circumference of a circle
    print ('Find the area and circumference of a circle')
    r = float(input('Enter the radious'))
    area = 3.141592*r*r
    peri = 2*3.141592*r
    print ('Area of the circle is',area,'and circumference of the circle is',peri)

def square():
    # Program to find the area and perimeter of a square
    print ('Area and perimeter of a square')
    s = int(input("Enter the length of the side"))
    area = s*s
    perimeter = s*4
    print ('Area of the square is',area,'and perimeter is',perimeter)
