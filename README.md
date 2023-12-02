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
            <th align="center">Sun</th>
            <th align="center">Mon</th>
            <th align="center">Tue</th>
            <th align="center">Wed</th>
            <th align="center">Thu</th>
            <th align="center">Fri</th>
            <th align="center">Sat</th>
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
            <td align="center">2</td>
        </tr>
        <tr>
            <td align="center">3</td>
            <td align="center">4</td>
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
            <td align="center">26</td>
            <td align="center">27</td>
            <td align="center">28</td>
            <td align="center">29</td>
            <td align="center">30</td>
        </tr>
        <tr>
            <td align="center">31</td>
            <td align="center"></td>
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

## Structure

Each day is stored in its own directory inside `day` directory, with the input in `input.txt` and the solution in `solution.py`.

```plain
.
├── config.json
├── generate.py
├── LICENSE
├── README.md
└── day
     ├── 00  # Template directory
     │   ├── input.txt
     │   └── solution.py
     ├── 01
     │   ├── input.txt
     │   └── solution.py
     ├── ...
     └── 25
         ├── input.txt
         └── solution.py
```

## Usage

First, set up `config.json`.

To **generate a directory** for a new day, run
```sh
$ python3 generate.py <day>
$ python3 generate.py 5 # Populate day/05 directory
```
This will create a copy of template directory `00/` and change the name and contents of the files to match the day and problem title.

To **run the solution** for a day, run
```sh
$ python3 day/<day>/solution.py < day/<day>/input.txt
$ python3 day/05/solution.py < day/05/input.txt  # Example
```
