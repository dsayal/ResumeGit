import players
def play_game():
    """
    This function creates a list that has 3 instances of Red and Blue player. 
    This function invokes the walk method and iterates over the list. 
    This function returns the winner of the game and checks if the isntances are over 1000.
    """
    marathon_players = [players.RedPlayer(f"RedPlayer{i+1}") for i in range(3)] + [players.BluePlayer(f"BluePlayer{i+1}") for i in range(3)]
    num_turns = 0
    winner = None
    

    while True:
        num_turns += 1
        for player in marathon_players:
            player.walk()
            if player.position >= 1000:
                winner = (player.name, num_turns)
                return winner

if __name__ == "__main__":
    print("Running marathon game within marathon.py:")
    winner, num_turns = play_game()
    print(f"The winner is {winner} after {num_turns} turns.")

    print("\nRunning marathon game within players.py:")
    winner, num_turns = players.play_game()
    print(f"The winner is {winner} after {num_turns} turns.")
