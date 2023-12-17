#!/usr/bin/python3
import argparse
import json
import re
import shutil
import string

import bs4
import requests


def main(args: argparse.Namespace, config: dict) -> None:
    year = config["year"]
    day = args.day

    url = f"https://adventofcode.com/{year}/day/{day}"
    with requests.get(url) as response:
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise RuntimeError(f"Check if the day is correct and the puzzle is released.") from err
        soup = bs4.BeautifulSoup(response.text, "html.parser")

    title = soup.select_one("article.day-desc h2").text
    title = re.match(r"--- Day \d+: (?P<title>.+) ---", title).group("title")

    shutil.copytree("day/00", f"day/{day:02d}", dirs_exist_ok=True)

    with open(f"day/{day:02d}/program.py", "r") as fr:
        template_str = fr.read()

    substituted = string.Template(template_str).substitute(
        year=year,
        day=day,
        title=title,
        name=config["name"],
        email=config["email"],
    )

    with open(f"day/{day:02d}/program.py", "w") as fw:
        fw.write(substituted)

    with open("README.md", "r") as f:
        readme = f.read()

    readme = readme.replace(
        f'<td align="center">{day}</td>',
        f'<td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/{day:02d}/program.py">{day}</a></td>',
    )

    with open("README.md", "w") as f:
        f.write(readme)

    print("Done!")


if __name__ == "__main__":
    try:
        with open("config.json") as f:
            config = json.load(f)
    except FileNotFoundError as err:
        raise RuntimeError("Please create a config.json file.") from err

    parser = argparse.ArgumentParser(description="Initialize the directory for new puzzle.")
    parser.add_argument("day", help="day number of puzzle", type=int)
    args = parser.parse_args()

    main(args, config)
