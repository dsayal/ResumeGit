import random
class Player:
    def __init__(self, name):
        self.position = 0 
        self.name = name 

class RedPlayer(Player):
    def _init__(self, name):
        Player.__init___(self, name)

    def walk(self):
        """
        This function will change the position attribute by a certain amount given the subclass.
        The parameter is self().  
        This function returns a random number, the one given by the subclass. 
        """
        self.position += random.randrange(1,10)

class BluePlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def walk(self):
        """
        This function will change the position attribute by a certain amount given the subclass.
        The parameter is self().  
        This function returns a random number, the one given by the subclass. 
        """
        self.position += random.randrange(4,8)

def play_game():
    """
    This function creates a list that has 3 instances of Red and Blue player. 
    This function invokes the walk method and iterates over the list. 
    This function returns the winner of the game and checks if the instances are over 100.
    """
    BPlist = []
    counter = 0 
    while counter < 3:
        counter += 1 
        BPlist.append(BluePlayer(f'BluePlayer{counter}'))
        BPlist.append(RedPlayer(f'RedPlayer{counter}'))
        winner = None
        
    
    num_turns = 0
    while True:
        num_turns += 1
        for player in BPlist:
            player.walk()
            if player.position >= 100:
                winner = (player.name, num_turns)
                return winner

if __name__ == "__main__":
    winner, num_turns = play_game()
    print(f"The winner is {winner} after {num_turns} turns.")

  
        