from game.die import Die


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
        Haha alright I lost at 5600 (por fin, finally!) So the trick was to add a line in the director file inside of the “while self.is_playing:” loop, after the other 3 functions are called, that sets the score to 0 (“self.score = 0" was all I did). Then, I also changed the double equals sign “==” on the last line of that same file to a singular equals sign. This allowed the game to have an end.
React


Ryan Schmidt  7 hours ago
Not sure if that was part of the assignment, if it is, we can cut this question and answer out, but that was happening to me on the completed one too so I figured I would share. Thanks! :)
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.dice = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(5):
            die = Die()
            self.dice.append(die)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.score = 0

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        roll_dice = input("Roll dice? [y/n] ")
        self.is_playing = (roll_dice == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing = (self.score > 0)
        if self.is_playing == False:
            print(f'Thanks for playing! Your final score was: {self.total_score}')