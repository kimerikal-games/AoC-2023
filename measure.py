#!/usr/bin/env python3
import pathlib
import subprocess
import statistics

import pandas as pd
from tqdm.auto import tqdm

TIME_REPEAT = 5
TIME_TOPK = 3
MEM_WORSTK = 3


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

for day_path in (pbar := tqdm(sorted(pathlib.Path("day").iterdir()))):
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
        for i in range(TIME_REPEAT):
            pbar.set_description_str(f"Day {day:02d} {interpreter_name:>8s} {i+1:2d}/{TIME_REPEAT}")
            time = subprocess.run(
                ["time", "-f", "%S %U %M", interpreter_cmd, str(day_path / "program.py")],
                stdin=open(day_path / "in.txt"),
                capture_output=True,
                text=True,
            )
            time = time.stderr.split()
            time, memory = float(time[0]) + float(time[1]), float(time[2])
            times.append(time)
            memories.append(memory)

        times = sorted(times)[:TIME_TOPK]
        memories = sorted(memories)[-MEM_WORSTK:]

        result[f"{interpreter_name} Time [s]"] = f"{statistics.fmean(times):.3f}"
        result[f"{interpreter_name} Memory [KB]"] = f"{round(statistics.fmean(memories), -3):.0f}"

    results.append(result)

df = pd.DataFrame(results).set_index("Day").sort_index()

md = df.to_markdown()
start = "<!-- region measurements -->"
end = "<!-- endregion measurements -->"
with open("README.md", "r") as f:
    readme = f.read()

start_index = readme.index(start)
end_index = readme.index(end)

readme = readme[: start_index + len(start)] + "\n" + md + "\n" + readme[end_index:]

with open("README.md", "w") as f:
    f.write(readme)

print(df)
