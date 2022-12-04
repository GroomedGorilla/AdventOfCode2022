from pathlib import Path

p = Path(__file__).with_name("input.txt")

# X = Rock ; Y = Paper ; Z = Scissors
move_score = {"X": 1, "Y": 2, "Z": 3}

# A = Rock ; B = Paper ; C = Scissors
winning_move = {
    "A": {"X": 3, "Y": 6, "Z": 0},  # opponent plays rock
    "B": {"X": 0, "Y": 3, "Z": 6},  # opponent plays paper
    "C": {"X": 6, "Y": 0, "Z": 3},  # opponent plays scissors
}

# X = Lose ; Y = Draw ; Z = Win
move_to_make = {
    "A": {"X": "Z", "Y": "X", "Z": "Y"},  # Rock      : Scissors, Rock, Paper
    "B": {"X": "X", "Y": "Y", "Z": "Z"},  # Paper     : Rock, Paper, Scissors
    "C": {"X": "Y", "Y": "Z", "Z": "X"},  # Scissors  : Paper, Scissors, Rock
}

round_score = 0

with p.open("r") as f:
    while line := f.readline().strip():
        opp, outcome = line.split(" ")
        my_move = move_to_make[opp][outcome]
        round_score += winning_move[opp][my_move] + move_score[my_move]

print(round_score)
