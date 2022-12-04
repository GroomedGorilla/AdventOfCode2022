from pathlib import Path
import string

p = Path(__file__).with_name("input.txt")

letters = string.ascii_letters
priority_sum = 0

with p.open("r") as f:
    while rucksack := f.readline().strip():
        half_item_num = int(len(rucksack) / 2)
        comp_1, comp_2 = rucksack[:half_item_num], rucksack[half_item_num:]
        common = [x for x in comp_1 if x in comp_2]
        priority_sum += letters.index(common[0]) + 1

print(priority_sum)
