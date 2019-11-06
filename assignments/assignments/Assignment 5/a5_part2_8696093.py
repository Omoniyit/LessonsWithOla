class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:
    def __init__(self,point1, point2, color):
         ''' (point,number, number) -> None
        initializes point coordinates to (xcoord, ycoord)'''
         self.point1 = point1
         self.point2 = point2
         self.color = color
        
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Rectangle(Point('+str(self.point1.x)+','+str(self.point1.y)+')'+','+'Point('+str(self.point2.x)+','+str(self.point2.y)+')'+','+"'"+self.color+"'"+')'
 

    def get_color(self):
        '''(none)-> str
        Returns the colour of the point'''
        return self.color

    def get_bottom_left(self):
        '''(none)-> tuple
        Returns a tuple with x and y coordinates of the point at the bottom left'''
        return self.point1
    
    def get_top_right(self):
        '''(none)-> tuple
        Returns a tuple with x and y coordinates of the at the top right'''
        return self.point2
    
    def reset_color(self,new):
        '''(str)-> str
        Resets and returns the new colour'''
        self.color = new
        return new
    
    def move(self,dx,dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        Point.move(self.point1,dx,dy)
        Point.move(self.point2,dx,dy)
    
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y)'''
        return 'I am a ' + self.color + ' rectangle with bottom left corner at ' + '('+ str(self.get_bottom_left().x) + ',' + str(self.get_bottom_left().y) + ')' + ' and top right corner at ' + '(' + str(self.get_top_right().x) + ',' + str(self.get_top_right().y) +').'
        
    
    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.point1 == other.point1 and self.point2 == other.point2
    
    def get_perimeter(self):
        '''(none)-> int
        Returns the perimeter of the rectangle'''
        return ((self.point2.x - self.point1.x)*2 + (self.point2.y - self.point1.y)*2)
    
    def get_area(self):
        '''(none)-> int
        Returns the area of the rectangle'''
        return((self.point2.x - self.point1.x)*(self.point2.y - self.point1.y))
    
    def contains(self,x,y):
        '''(point, point)->bool
        Returns true if (x,y) is inside of the calling rectangle and false otherwise'''
        if x >= self.point1.x and x <= self.point2.x and y >= self.point1.y and y<= self.point2.y:
            return True
        else:
            return False
        
    def intersects(self,other):
        '''(none)->bool
        returns True if the calling rectangle intersects the given rectangle and False otherwise'''
        return(not((self.point1.y>other.point2.y) or (self.point2.y<other.point1.y)or (self.point2.x< other.point1.x) or (self.point1.x >other.point2.x)))
        
        
class Canvas:
    def __init__(self):
        '''(point)-> none
        Creates an empty list'''
        self.l= []
        
    def __len__(self):
         '''(point)-> int
        returns the length of the list initiated'''
         return len(self.l)
    
    def add_one_rectangle(self,r):
        '''(int)->int
        Adds the rectangle to the list'''
        self.l.append(r)
        
    def __repr__(self):
        '''(point)->str
        Returns canonical string representation Point'''
        return 'Canvas(' + str(self.l) + ')'
    
    def count_same_color(self,col):
        '''(str)-> int
        Prints the count of rectangles with the same colour'''
        count = 0
        for val in self.l:
            if val.color == col:
                count += 1
        print( count)
        
    def total_perimeter(self):
        '''(point)-> int
        returns the sum of the perimeters of all the rectangles in the calling canvas'''
        tot = 0
        for val in self.l:
            tot += Rectangle.get_perimeter(val)
        print(tot)
    def min_enclosing_rectangle(self):
        '''(point)-> (point, point, colour)
         calculates the minimum enclosing rectangle that contains  all the rectangles in the calling canvas and returns an object of type rectangle in red
         '''
        l = []
        for val in self.l:
            a =Rectangle.get_bottom_left(val)
            l.append(a.x)
            min_x = min(l)
        l = []
        for val in self.l:
            a =Rectangle.get_bottom_left(val)
            l.append(a.y)
        min_y = min(l)
        l = []
        for val in self.l:
            a =Rectangle.get_top_right(val)
            l.append(a.x)
        max_x = max(l)
        l = []
        for val in self.l:
            a =Rectangle.get_top_right(val)
            l.append(a.y)
        max_y = max(l)
        point1 = Point(min_x,min_y)
        point2 = Point(max_x,max_y)
        return Rectangle(point1,point2, 'red')
    def common_point(self):
        '''(point)-> bool
        returns True if there exists a point  that intersects all rectangles in the calling canvas'''
        for i in range(len(self.L)-1):
            for j in range(i+1,len(self.L)-1):
                if self.L[i].interesects(self.L[j])==False:
                     return False
        return True
            

    
