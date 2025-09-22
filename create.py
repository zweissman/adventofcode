import argparse
from pathlib import Path
from shutil import copyfile

TEMPLATE = "day-template.py"

parser = argparse.ArgumentParser()
parser.add_argument("day", type=int, help="The day of the puzzle", nargs=1)
parser.add_argument("year", type=int, help="The year of the puzzle", nargs=1)
args = parser.parse_args()

day = args.day[0]
year = args.year[0]

if day > year:
    year, day = day, year

day = f"{day:02d}"

if not Path.exists(Path(f"{year}")):
    Path.mkdir(Path(f"{year}"))

if not Path.exists(Path(f"{year}/input")):
    Path.mkdir(Path(f"{year}/input"))

code_file = f"{year}/advent-{year}-day{day}.py"
if not Path.exists(Path(code_file)):
    copyfile(Path(TEMPLATE), code_file)

input_file = f"{year}/input/{day}.txt"
if not Path.exists(Path(input_file)):
    Path(f"{year}/input/{day}.txt").touch()

input_test_file = f"{year}/input/{day}-test.txt"
if not Path.exists(Path(input_test_file)):
    Path(input_test_file).touch()

print(f"Created files for Advent of Code {year} Day {day}")
