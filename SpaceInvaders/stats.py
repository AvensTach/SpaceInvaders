class Stats():
    """stats"""


    def __init__(self):
        """init stats"""
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """change stats during game"""
        self.guns_left = 2
