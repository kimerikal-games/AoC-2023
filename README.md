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
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/05/program.py">5</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/06/program.py">6</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/07/program.py">7</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/08/program.py">8</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/09/program.py">9</a></td>
        </tr>
        <tr>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/10/program.py">10</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/11/program.py">11</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/12/program.py">12</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/13/program.py">13</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/14/program.py">14</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/15/program.py">15</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/16/program.py">16</a></td>
        </tr>
        <tr>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2023/src/branch/main/day/17/program.py">17</a></td>
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
- CPython: Python 3.10.12
- PyPy: Python 3.10.13 (f1607341da97ff5a1e93430b6e8c4af0ad1aa019, Sep 28 2023, 05:41:26) [PyPy 7.3.13 with GCC 10.2.1 20210130 (Red Hat 10.2.1-11)]

|   Day |   Lines |   Words |   Bytes |   CPython Time [ms] |   CPython Memory [KB] |   PyPy Time [ms] |   PyPy Memory [KB] |
|------:|--------:|--------:|--------:|--------------------:|----------------------:|-----------------:|-------------------:|
|     1 |      47 |     144 |    1237 |                   8 |         9152          |               40 |     62080          |
|     2 |      53 |     142 |    1447 |                   5 |         9568          |               30 |     62592          |
|     3 |     109 |     384 |    2926 |                  20 |        10368          |               70 |     65152          |
|     4 |      41 |     131 |    1124 |                   0 |         8960          |               20 |     61568          |
|     5 |      97 |     305 |    2917 |               10440 |         9088          |              960 |     61440          |
|     6 |      38 |     119 |    1091 |                   0 |         9024          |               10 |     52768          |
|     7 |      76 |     212 |    2231 |                  20 |        10752          |               80 |     66944          |
|     8 |      59 |     172 |    1550 |                  20 |        10112          |               30 |     63232          |
|     9 |      39 |     104 |     958 |                   8 |         9120          |               30 |     62080          |
|    10 |     127 |     409 |    3256 |                  20 |        11272          |               40 |     65408          |
|    11 |      57 |     190 |    1308 |                  30 |         8960          |               20 |     61824          |
|    12 |      59 |     205 |    1709 |                4510 |        10112          |              640 |    105472          |
|    13 |      80 |     256 |    2215 |                  10 |        10656          |               30 |     64512          |
|    14 |      83 |     239 |    2023 |                 730 |        11776          |              350 |    103040          |
|    15 |      80 |     224 |    1942 |                  20 |        10368          |               50 |     64256          |
|    16 |      84 |     322 |    2327 |                1780 |        11892          |              840 |    131744          |
|    17 |     186 |    1010 |    7029 |              104080 |            1.3469e+06 |            76800 |         1.4609e+06 |
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

`in.txt` files are visible only in local.

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
