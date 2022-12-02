from pathlib import Path

p = Path("input.txt")
elves = []
sum = 0

with p.open('r') as f:
    while line := f.readline():
        if line.strip():
            sum += int(line)
        else:
            elves.append(sum)
            sum = 0
    elves.append(sum)

chonkmaster = elves.index(max(elves))
print(f'Chonkiest elf is num {chonkmaster + 1} with {max(elves)} Calories ')
