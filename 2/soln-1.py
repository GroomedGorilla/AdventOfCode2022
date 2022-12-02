from pathlib import Path

p = Path(__file__).with_name("input.txt")

move_score = {"X": 1, "Y": 2, "Z": 3}

winning_move = {
    "A": {"X": 3, "Y": 6, "Z": 0},  # opponent plays rock
    "B": {"X": 0, "Y": 3, "Z": 6},  # opponent plays paper
    "C": {"X": 6, "Y": 0, "Z": 3},  # opponent plays scissors
}

round_score = 0

with p.open("r") as f:
    while line := f.readline().strip():
        opp, me = line.split(" ")
        round_score += winning_move[opp][me] + move_score[me]

print(round_score)
