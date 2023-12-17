#!/usr/bin/env python3
import pathlib
import subprocess
import statistics
import time as time_

import pandas as pd
from tqdm.auto import tqdm


REPEATS = 5

interpreters = [
    ("CPython", "python3.10"),
    ("PyPy", "pypy3.10"),
]


print("Interpreters:")
for interpreter_name, interpreter_cmd in interpreters:
    out = subprocess.run([interpreter_cmd, "--version"], check=True, capture_output=True, text=True)
    print("-", interpreter_name)
    print(out.stdout.strip())
print()


results = []

paths = sorted(pathlib.Path("day").iterdir())
pbar_total = len(paths) * len(interpreters) * REPEATS
pbar_format = "{l_bar}|{bar}| {n_fmt}/{total_fmt}{postfix}"
for day_path in (pbar := tqdm(paths, total=pbar_total, bar_format=pbar_format)):
    result = {}
    day = int(day_path.name)
    if day == 0:
        continue
    result["Day"] = day

    wc = subprocess.run(["wc", str(day_path / "program.py")], check=True, capture_output=True, text=True)
    lines, words, chars = map(int, wc.stdout.split()[:3])
    result["Lines"] = lines
    result["Words"] = words
    result["Bytes"] = chars

    for interpreter_name, interpreter_cmd in interpreters:
        times = []
        memories = []
        for i in range(REPEATS):
            pbar.set_description_str(f"Day {day:02d} {interpreter_name:>8s} {i+1:2d}/{REPEATS}")
            pbar.update()
            time_.sleep(0.1)

            time = subprocess.run(
                ["time", "-f", "%S %U %M", interpreter_cmd, str(day_path / "program.py")],
                stdin=open(day_path / "in.txt"),
                capture_output=True,
                text=True,
            )
            time = time.stderr.split()
            time, memory = 1000 * (float(time[0]) + float(time[1])), float(time[2])
            if time > 10:
                break
            times.append(time)
            memories.append(memory)
        else:
            time = round(statistics.fmean(sorted(times)[:-1]))
            memory = round(statistics.fmean(sorted(memories)[:-1]))

        result[f"{interpreter_name} Time [ms]"] = time
        result[f"{interpreter_name} Memory [KB]"] = memory

    results.append(result)

df = pd.DataFrame(results).set_index("Day").sort_index()

print(df)


md = ""
for interpreter_name, interpreter_cmd in interpreters:
    out = subprocess.run([interpreter_cmd, "--version"], check=True, capture_output=True, text=True)
    out = out.stdout.replace("\n", " ").strip()
    md += f"- {interpreter_name}: {out}\n"
md += "\n"

md += df.to_markdown()


start = "<!-- region measurements -->"
end = "<!-- endregion measurements -->"

with open("README.md", "r") as f:
    readme = f.read()

start_index = readme.index(start)
end_index = readme.index(end)

readme = readme[: start_index + len(start)] + "\n" + md + "\n" + readme[end_index:]

with open("README.md", "w") as f:
    f.write(readme)
