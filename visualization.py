""" This script will create a class named Plot. 
"""
import monty_hall
import pandas as pd
import seaborn as sns

class Plot:
    """
    Stores the data for a particular instance of a simulation of the monty hall problem. 
    """

    def __init__(self, doors=3, iterations=200):
        """
        Initialize the Plot class.
        
        Args:
        - doors (int): Number of doors that the simulation will be based on. 
        - iterations (int): The number of iterations that a simulation will be based on. 
        """
        self.doors = doors
        self.iterations = iterations
        self.sequence = []

        for i in range(1, iterations + 1):
            switched = "True" if i % 2 == 0 else "False"
            sim_iteration = monty_hall.Simulation(doors)
            win_percentage = sim_iteration.play_game(switch=(i % 2 == 0), iterations=i)
            self.sequence.append({"iterations": i, "percentage": win_percentage, "doors": doors, "switched": switched})
        
        self.make_plot()

    def make_plot(self):
        """
        Uses the sequence attribute to create a pandas Dataframe. Serves as visulization of data. 
        """
        df = pd.DataFrame(self.sequence)
        plot = sns.lmplot(x="iterations", y="percentage", hue="switched", data=df, fit_reg=False)
        plot.savefig(f"monty_hall_{self.doors}_doors_{self.iterations}_iterations.png")

if __name__ == "__main__":
    plot = Plot(doors=5, iterations=100)
