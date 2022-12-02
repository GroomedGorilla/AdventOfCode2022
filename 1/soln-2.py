from pathlib import Path

p = Path(__file__).with_name("input.txt")
elves = []
total = 0

with p.open("r") as f:
    while line := f.readline():
        if line.strip():
            total += int(line)
        else:
            elves.append(total)
            total = 0
    elves.append(total)

elves_sorted = sorted(elves, reverse=True)
chonkmaster = elves_sorted[0]
print(f"Chonkiest elf is num {chonkmaster + 1} with {max(elves)} Calories ")

top_3_chonkers = elves_sorted[:3]
total_cals_top_3 = sum(top_3_chonkers)
print(f"Top 3 chonkers carrying {total_cals_top_3} Calories")
