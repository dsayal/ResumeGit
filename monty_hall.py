import random

class Simulation:
    """Simulation class for the Monty Hall problem."""

    def __init__(self, doornum):
        """
        Initialize the Simulation instance.
        
        Args:
            doornum (int): The number of doors used in the game.
        """
        self.numdoors = doornum

    def set_random_doors(self):
        """
        Create a list of doors with one "car" and the rest as "zonk".
        
        Returns:
            list: List representing the doors with one car and the rest as zonks.
        """
        doors = ["zonk"] * self.numdoors
        car_index = random.randint(0, self.numdoors - 1)
        doors[car_index] = "car"
        return doors

    def choose_doors(self):
        """
        Choose contestant's door and alternate door randomly.
        
        Returns:
            tuple: Contestant's chosen door and the alternate door.
        """
        doors = self.set_random_doors()
        contestant_door = doors.pop(random.randint(0, len(doors) - 1))
        doors.remove("zonk")
        alternate_door = doors.pop(random.randint(0, len(doors) - 1))
        return (contestant_door, alternate_door)

    def play_game(self, switch=False, iterations=1):
        """
        Play the Monty Hall game for a given number of iterations.
        
        Args:
            switch (bool): Determines whether the contestant decides to switch their door.
            iterations (int): The number of times the game will be played.
        
        Returns:
            float: The win percentage.
        """
        wins = 0
        for _ in range(iterations):
            contestant_door, alternate_door = self.choose_doors()
            if switch:
                if alternate_door == "car":
                    wins += 1
            else:
                if contestant_door == "car":
                    wins += 1
        try:
            return wins / iterations
        except ZeroDivisionError:
            return 0.0

if __name__ == "__main__":
    sim = Simulation(3) 
    win_percentage = sim.play_game(switch=True, iterations=1000) 
    print("Win percentage with the switches:", win_percentage)

