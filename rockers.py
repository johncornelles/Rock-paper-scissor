import random

choices = ["rock", "paper", "scissor"]
levels = ["normal", "hard"]

class Game:
    def __init__(self):
        self.hardChoice = []
        self.computerChoice = ""
        while True:
            self.level = input(f"Enter your desired difficulty {levels}").lower()
            if self.level not in levels:
                print("Invalid difficulty level")
            else:
                self.playerChoice = input(f"Enter your choice from {choices}").lower()
                if self.playerChoice not in choices:
                    print("Invalid choice")
                else:
                    if self.level.lower() == "normal":
                        self.normal()
                    elif self.level.lower() == "hard":
                        self.hard()
                        self.result()
                    break

    def normal(self):
        self.computerChoice = random.choice(choices)
        self.result()
  
    def hard(self):
      if self.playerChoice == "rock":
          self.hardChoice = ["paper", "rock", "scissor"]
      elif self.playerChoice == "paper":
          self.hardChoice = ["scissor", "paper", "rock"]
      elif self.playerChoice == "scissor":
          self.hardChoice = ["rock", "scissor", "paper"]
      self.computerChoice = random.choices(self.hardChoice, weights=[6, 3, 1])[0]

      
    def result(self):
        print("You chose", self.playerChoice)
        print("The computer chose", self.computerChoice)
        if self.playerChoice == self.computerChoice:
            print("It's a tie!")
        elif self.playerChoice == "rock" and self.computerChoice == "scissor":
            print("You win!")
        elif self.playerChoice == "paper" and self.computerChoice == "rock":
            print("You win!")
        elif self.playerChoice == "scissor" and self.computerChoice == "paper":
            print("You win!")
        else:
            print("You lose!")

gameStart = Game()