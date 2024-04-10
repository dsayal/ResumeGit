import math 
class Car:
    def __init__(self, x=0 , y=0 , heading=0):
        """This function sets three attributes to the values of theier corresponding parameters.

        Args:
            x (int, optional): The starting x coordinate of the car as a float. Defaults to 0.
            y (int, optional): The starting y coordinateof the car as a float. Defaults to 0.
            heading (int, optional): The starting heading as a float. Defaults to 0.
        """
        self.x=x
        self.y=y
        self.heading=heading
    def turn(self, degrees):
        """This function assigns a new value to the heading attribute.

        Args:
            degrees (float): A positive number of degrees indicates a clockwise turn, a negative number of degrees indicates a counterclockwise turn.
        """
        self.heading= (self.heading + degrees) % 360
    def drive(self,distance):
        """This function serves as converting the heading from degrees to radians

        Args:
            distance (float): The distance the car drives denoted by variable d.
        """
        self.x+= math.sin(math.radians(self.heading))*distance
        self.y-= math.cos(math.radians(self.heading))*distance
def sanity_check():
    """This function takes no arguments and prints the location of your instance on one line and the heading on the next line.

    Returns:
        float: Returns the instance we created.
    """
    c=Car()
    c.turn(90)
    c.drive(10)
    c.turn(30)
    c.drive(20)
    print (f"Location: {c.x}, {c.y}")
    print (f"Heading: {c.heading}")
    return c
if __name__ == "__main__":
    """This function invokes the sanity_check() function.
    """
    sanity_check()
    