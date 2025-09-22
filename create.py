import argparse
from pathlib import Path
from shutil import copyfile

TEMPLATE = "day-template.py"

parser = argparse.ArgumentParser()
parser.add_argument("day", type=int, help="The day of the puzzle", nargs=1)
parser.add_argument("year", type=int, help="The year of the puzzle", nargs=1)
args = parser.parse_args()

day = f"{args.day[0]:02d}"
year = args.year[0]

if not Path.exists(Path(f"{year}")):
    Path.mkdir(Path(f"{year}"))

if not Path.exists(Path(f"{year}/input")):
    Path.mkdir(Path(f"{year}/input"))

copyfile(Path(TEMPLATE), f"{year}/advent-{year}-day{day}.py")
Path(f"{year}/input/{day}.txt").touch()
Path(f"{year}/input/{day}-test.txt").touch()
print(f"Created files for Advent of Code {year} Day {day}")
