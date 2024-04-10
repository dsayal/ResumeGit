"""Create routes between cities on a map."""
import sys
import argparse

class City():
    def __init__(self, name):
        """
          Initialize a new instance of the class.

        Parameters:
        name (str): The name of the instance being initialized.

        Attributes:
        name (str): The name assigned to the instance.
        neighbors (dict): A dictionary representing the neighbors of the instance. 
        
        """
        self.name = name
        self.neighbors = {}
        
        
    def __repr__(self):
        """
        This method returns the name of the instance.

        Returns:
        str: The name of the instance.
        """
        return self.name
    
    def add_neighbor(self, neighbor, distance, interstate):
        """ 
        This function adds a neighbor to the instance with distance and interstate information.

        Parameters:
        neighbor (str): The City object that will be connected to this instance (and vice versa).
        distance (float): The distance between the two cities. 
        interstate (str): The interstate number that connects the cities. 
        """
        if neighbor not in self.neighbors:
            self.neighbors[neighbor] = (distance, str(interstate))
        if self not in neighbor.neighbors:
            neighbor.neighbors[self] = (distance, str(interstate))
            
            
        
class Map():
    def __init__(self,relationships):
        """
        Initialize a new instance of the class.

        Parameters:
        relationships (dict): A dictionary where the keys are individual cities and the values are a
                              list of tuples where the first element in the tuple is a string representing a 
                              City that is connected to the key (city), the second element is the distance between 
                              the cities, and the third element is the interstate that connects them.
        """
        self.cities = []
        for key in relationships:
            if key not in [t.name for t in self.cities]:
                s = City(key)
                self.cities.append(s)
            city_index = [t.name for t in self.cities].index(key)
            for neighbor, distance, interstate in relationships[key]:
                if neighbor not in [t.name for t in self.cities]:
                    new_city = City(neighbor)
                    self.cities.append(new_city)
                new_city_index = [t.name for t in self.cities].index(neighbor)
                self.cities[new_city_index].add_neighbor(self.cities[city_index], distance, interstate)
    
                    
    def __repr__(self):
        """
        This method returns the name of the instance.

        Returns:
        str: The name of the instance.
        """
        return str(self.cities)
    
    
def bfs(graph, start, goal):
    """
    This function will implement the bfs (Breadth First Search) algorithm to find the shortest paths
    between the two nodes in a graph structure. If a path is found, it returns 
    the path as a list of nodes. If no path exists, it returns None.

    Parameters:
    Graph(Map): A map object representing the graph that we will be traversing
    start (str):The starting node for the search(starting city).
    goal (str): The goal node to reach(destination city).

    Returns:
    list or None: A list representing the path otherwise None.  
    """
    explored = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            x = [c.name for c in graph.cities]
            neighbors = graph.cities[x.index(str(node))].neighbors
            for key in neighbors:
                new_path = list(path)
                new_path.append(key)
                queue.append(new_path)
                if str(key) == goal:
                    return [str(i) for i in new_path]
            explored.append(node)
    print("No Path Found.")
    return None
    

def main(start, destination, graph):
    """
    This function will create a Map object with the connections data being passed in. It will then use
    bfs() to find the path between a start City and a destination City. It will parse the returned value
    and instruct the user on where they should drive given a start node and an end node.
        
    Parameters:
    start (str): The name of the starting city
    destination (str): The name of the destination city.
    Graph(dict): A dictionary representing an adjecency list of cities and the cities to which they connect.
    Returns:
    A string that contains all of the same contents that we have printed out to the terminal. 
    """
    
    graph = Map(graph)
    instructions = bfs(graph, start, destination)
    
    output_message = ""
    if instructions:
        for index, city_name in enumerate(instructions):
            if index == 0:
                output_message += (f"Starting at {start}")
                print(f"Starting at {start}")
            if index < len(instructions)-1:
                y = [x.name for x in graph.cities].index(city_name)
                current_city = graph.cities[y].neighbors
                new_dict = {}
                for key, value in current_city.items():
                    new_dict[str(key)] = value
                next_city = instructions[index+1]
                
                distance, interstate = new_dict[next_city]
                output_message += (f"Drive {distance} miles on {interstate} towards {next_city}, then")
                print(f"Drive {distance} miles on {interstate} towards {next_city}, then")
            if index == len(instructions)-1:
                output_message += (f"You will arrive at your destination")
                print(f"You will arrive at your destination")
                
    else: 
        raise Exception("No Path Found.")
    
    return output_message

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """

    parser = argparse.ArgumentParser()
    
    parser.add_argument('--starting_city', type = str, help = 'The starting city in a route.')
    parser.add_argument('--destination_city', type = str, help = 'The destination city in a route.')
    
    args = parser.parse_args(args_list)
    
    return args

if __name__ == "__main__":
    
    connections = {  
        "Baltimore": [("Washington", 39, "95"), ("Philadelphia", 106, "95")],
        "Washington": [("Baltimore", 39, "95"), ("Fredericksburg", 53, "95"), ("Bedford", 137, "70")], 
        "Fredericksburg": [("Washington", 53, "95"), ("Richmond", 60, "95")],
        "Richmond": [("Charlottesville", 71, "64"), ("Williamsburg", 51, "64"), ("Durham", 151, "85")],
        "Durham": [("Richmond", 151, "85"), ("Raleigh", 29, "40"), ("Greensboro", 54, "40")],
        "Raleigh": [("Durham", 29, "40"), ("Wilmington", 129, "40"), ("Richmond", 171, "95")],
        "Greensboro": [("Charlotte", 92, "85"), ("Durham", 54, "40"), ("Ashville", 173, "40")],
        "Ashville": [("Greensboro", 173, "40"), ("Charlotte", 130, "40"), ("Knoxville", 116, "40"), ("Atlanta", 208, "85")],
        "Charlotte": [("Atlanta", 245, "85"), ("Ashville", 130, "40"), ("Greensboro", 92, "85")],
        "Jacksonville": [("Atlanta", 346, "75"), ("Tallahassee", 164, "10"), ("Daytona Beach", 86, "95")],
        "Daytona Beach": [("Orlando", 56, "4"), ("Miami", 95, "268")],
        "Orlando": [("Tampa", 94, "4"), ("Daytona Beach", 56, "4")],
        "Tampa": [("Miami", 281, "75"), ("Orlando", 94, "4"), ("Atlanta", 456, "75"), ("Tallahassee", 243, "98")],
        "Atlanta": [("Charlotte", 245, "85"), ("Ashville", 208, "85"), ("Chattanooga", 118, "75"), ("Macon", 83, "75"), ("Tampa", 456, "75"), ("Jacksonville", 346, "75"), ("Tallahassee", 273, "27") ],
        "Chattanooga": [("Atlanta", 118, "75"), ("Knoxville", 112, "75"), ("Nashville", 134, "24"), ("Birmingham", 148, "59")],
        "Knoxville": [("Chattanooga", 112,"75"), ("Lexington", 172, "75"), ("Nashville", 180, "40"), ("Ashville", 116, "40")],
        "Nashville": [("Knoxville", 180, "40"), ("Chattanooga", 134, "24"), ("Birmingam", 191, "65"), ("Memphis", 212, "40"), ("Louisville", 176, "65")],
        "Louisville": [("Nashville", 176, "65"), ("Cincinnati", 100, "71"), ("Indianapolis", 114, "65"), ("St. Louis", 260, "64"), ("Lexington", 78, "64") ],
        "Cincinnati": [("Louisville", 100, "71"), ("Indianapolis,", 112, "74"), ("Columbus", 107, "71"), ("Lexington", 83, "75"), ("Detroit", 263, "75")],
        "Columbus": [("Cincinnati", 107, "71"), ("Indianapolis", 176, "70"), ("Cleveland", 143, "71"), ("Pittsburgh", 185, "70")],
        "Detroit": [("Cincinnati", 263, "75"), ("Chicago", 283, "94"), ("Mississauga", 218, "401")],
        "Cleveland":[("Chicago", 344, "80"), ("Columbus", 143, "71"), ("Youngstown", 75, "80"), ("Buffalo", 194, "90")],
        "Youngstown":[("Pittsburgh", 67, "76")],
        "Indianapolis": [("Columbus", 175, "70"), ("Cincinnati", 112, "74"), ("St. Louis", 242, "70"), ("Chicago", 183, "65"), ("Louisville", 114, "65"), ("Mississauga", 498, "401")],
        "Pittsburg": [("Columbus", 185, "70"), ("Youngstown", 67, "76"), ("Philadelphia", 304, "76"), ("New York", 391, "76"), ("Bedford", 107, "76")],
        "Bedford": [("Pittsburg", 107, "76")], #COMEBACK
        "Chicago": [("Indianapolis", 182, "65"), ("St. Louis", 297, "55"), ("Milwaukee", 92, "94"), ("Detroit", 282, "94"), ("Cleveland", 344, "90")],
        "New York": [("Philadelphia", 95, "95"), ("Albany", 156, "87"), ("Scranton", 121, "80"), ("Providence,", 95, "181"), ("Pittsburgh", 389, "76")],
        "Scranton": [("Syracuse", 130, "81")],
        "Philadelphia": [("Washington", 139, "95"), ("Pittsburgh", 305, "76"), ("Baltimore", 101, "95"), ("New York", 95, "95")]
    }
    
    args = parse_args(sys.argv[1:])
    main(args.starting_city, args.destination_city, connections)