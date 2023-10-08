import random

print("welcome to Rise o the Stars: Cosmic Colonization")

def roll_dice():
    return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '?', '?', '?'])

def astronomy_question(current_square):
    questions = [
       "\nDid you know that these planets have different gravities: Earth 9.8 m/s², Mercury 3.7 m/s², Venus 8.8 m/s², Mars 3.7 m/s²? If you are on Earth or Venus, gravity is very strong, and you are running out of fuel. Go back 2 squares.",
        "\nDid you know that an astronomical unit is the distance from Earth to the Sun, approximately 149.6 million kilometers? Congratulations, move forward 3 squares!",
        "\nBe careful! We are passing close to the Sun, which has a surface temperature of 5,772 K and a radius of approximately 1.4 million kilometers. Move back one square with caution.",
        "\nIn general, a typical spacesuit can provide oxygen for approximately 6 to 8 hours. You are very cautious, you packed an extra one. Move forward 2 squares.",
        "\nFor space travel, teamwork is very important. Answer the question correctly, and if you do, everyone moves forward 5 squares. According to this, which planet or planets do you think are the largest?",
        "\nThroughout history, humans have dreamed of colonizing other planets. To conquer a planet, you need to send an expedition probe, like the Dragonfly expedition probe planned to be sent to Titan, one of Saturn's moons, to learn about the planet's conditions. Move forward 5 squares to get closer to it.",
        "\nHuygen was the probe that visited Titan, a moon of Saturn with liquid methane. Do you think humans could colonize this moon? Think about your answer and pass your next turn.",
        "\nPass by Saturn, and your ship was hit by an asteroid. Go back to what you rolled (if you don't want to, use a surprise card if you have one).",
        "\nDid you know that the Sun has an estimated lifespan of about 10 billion years? Hurry up and move forward 10 squares.",
        "\nDid you know that a trip from Earth to Titan takes 8 years? Hurry up and move forward 8 squares.",
        "\nChoose one of your friends and ask them if Pluto is a planet. If they answer incorrectly, tell them to go back to the square of the last person who answered incorrectly. If there is no one behind, tell them to go back 5 squares. |Answer| --> (Pluto is not a planet)",
        "\nDid you know that Mercury takes 88 Earth days to complete an orbit around the Sun? Hurry up and move ten squares.",
        "\nDid you know that Venus takes 225 Earth days to complete an orbit around the Sun? Hurry up and move 10 squares.",
        "\nDid you know that Earth takes 365.25 Earth days to complete an orbit around the Sun? Hurry up and move 10 squares.",
        "\nDid you know that Mars takes 687 Earth days to complete an orbit around the Sun? Hurry up and move 10 squares.",
        "\nDid you know that Jupiter takes 11.86 Earth days to complete an orbit around the Sun? Hurry up and move 12 squares.",
        "\nDid you know that Saturn takes 29.46 Earth years to complete an orbit around the Sun? Hurry up and move 5 squares.",
        "\nDid you know that Uranus takes 84 Earth years to complete an orbit around the Sun? Hurry up and move 5 squares.",
        "\nDid you know that Neptune takes 164.8 Earth years to complete an orbit around the Sun? Hurry up and move 5 squares.",
        "\nDid you know that Pluto and its moon Charon are like two friends traveling together around the Sun instead of one orbiting the other? You can move 2 squares."
    ]

    question = random.choice(questions)
    print(question)

    if "move forward" in question:
        advance = int(question.split("move forward")[1].split("squares")[0].strip())
        current_square += advance
        print(f"You move forward {advance} squares.")
    elif "go back" in question:
        setback = int(question.split("go back")[1].split("squares")[0].strip())
        current_square = max(1, current_square - setback)
        print(f"You move back {setback} squares.")

    return current_square

def advance_player(current_square):
    dice_result = roll_dice()

    if dice_result == '?':
        print("\nAstronomy Question:")
        current_square = astronomy_question(current_square)
    else:
        if dice_result <= 2:
            setback = random.randint(1, 2)
            current_square = max(1, current_square - setback)
            print(f"\nYou move back {setback} squares.")
        else:
            advance = random.randint(1, 6)
            current_square += advance
            print(f"\nYou move forward {advance} squares.")

    return current_square

def play(num_players):
    squares = [1] * num_players

    while max(squares) < 50:
        for player in range(num_players):
            print(f"\nPlayer {player + 1}'s Turn")
            input("Press Enter to roll the dice...")
            squares[player] = advance_player(squares[player])

            if max(squares) >= 25:
                print("\nCONGRATULATIONS, YOU'RE HALFWAY THERE.")
                for i in range(num_players):
                    squares[i] += 5
                print("Everyone moves forward 5 squares!\n")

            print(f"Player {player + 1}, you are on square {squares[player]}.\n")

    print("Congratulations! One of the players has reached square 50. You have won!... NOW YOU ARE A TITANIC")

if __name__ == "__main__":
    while True:
        try:
            num_players = int(input("\nEnter the number of players: "))
            if num_players < 1:
                raise ValueError("Number of players must be at least 1.")
            break  # Exit the loop if valid input is provided
        except ValueError:
            print("Invalid input. Please enter a valid integer greater than or equal to 1.")

    print("\nWelcome to the astronomy board game!\n")
    play(num_players)
