# AoC-2023

My solutions for [Advent of Code 2023](https://adventofcode.com/2023).

## Advent Calendar

<div align="center">
<table>
    <thead>
        <tr>
            <th colspan="7"><div align="center">December 2023</div></th>
        </tr>
        <tr>
            <th align="center">S</th>
            <th align="center">M</th>
            <th align="center">T</th>
            <th align="center">W</th>
            <th align="center">T</th>
            <th align="center">F</th>
            <th align="center">S</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/01/program.py">1</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/02/program.py">2</a></td>
        </tr>
        <tr>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/03/program.py">3</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/04/program.py">4</a></td>
            <td align="center">5</td>
            <td align="center">6</td>
            <td align="center">7</td>
            <td align="center">8</td>
            <td align="center">9</td>
        </tr>
        <tr>
            <td align="center">10</td>
            <td align="center">11</td>
            <td align="center">12</td>
            <td align="center">13</td>
            <td align="center">14</td>
            <td align="center">15</td>
            <td align="center">16</td>
        </tr>
        <tr>
            <td align="center">17</td>
            <td align="center">18</td>
            <td align="center">19</td>
            <td align="center">20</td>
            <td align="center">21</td>
            <td align="center">22</td>
            <td align="center">23</td>
        </tr>
        <tr>
            <td align="center">24</td>
            <td align="center">25</td>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"></td>
        </tr>
    </tbody>
</table>
<small>
    Note: The link always points to the code in <code>main</code> branch.
</small>
</div>

## Measurements

<!-- region measurements -->
|   Day |   Lines |   Words |   Bytes |   CPython Time [ms] |   CPython Memory [KB] |   PyPy Time [ms] |   PyPy Memory [KB] |
|------:|--------:|--------:|--------:|--------------------:|----------------------:|-----------------:|-------------------:|
|     1 |      59 |     169 |    1366 |                  10 |                  9754 |               30 |              61798 |
|     2 |      71 |     161 |    1557 |                   8 |                  9882 |               20 |              61952 |
|     3 |      94 |     328 |    2745 |                  10 |                 10112 |               40 |              63360 |
|     4 |      41 |     112 |    1016 |                   8 |                  9728 |               18 |              61466 |
<!-- endregion measurements -->

## Structure

```plain
.
├── config.json         # Current year, name, and email
├── generate.py         # Prepare directory for new puzzle
├── measure.py          # Measure code length, running time/memory
├── day
│   ├── 00              # Template directory
│   │   ├── in.txt
│   │   ├── out.txt
│   │   └── program.py
│   ├── 01
│   │   ├── in.txt      # Full input text
│   │   ├── out.txt     # Puzzle answer
│   │   └── program.py  # Solution code
│   ├── ...
│   └── 25
│       ├── in.txt
│       ├── out.txt
│       └── program.py
├── LICENSE
└── README.md
```

## Usage

For the first time, set up `config.json`.

```bash
# Generate a directory
$ python3 generate.py <day>

# Measure performance
$ python3 measure.py
```

Running measure.py will automatically update *Measurements* section in this `README.md` file.

## Other helpful tools

- [Visual Studio Code](https://code.visualstudio.com/)
- [Competitive Programming Helper (cph)](https://marketplace.visualstudio.com/items?itemName=DivyanshuAgrawal.competitive-programming-helper)

## License

See `LICENSE` file.
