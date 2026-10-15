# PS2 — Simple Statistics

Implement three functions in `math_utils.py` for three numbers: max, mean, and mean+std.

You already practiced `find_max_number` in **Tutorial 2**; here you also add `find_mean` and `find_mean_std` (and can refine max if needed).

## What to change

Edit **only** `math_utils.py`. Keep the function names and signatures.

| Function | Returns |
| --- | --- |
| `find_max_number(num1, num2, num3)` | the largest of the three |
| `find_mean(num1, num2, num3)` | arithmetic mean (`n = 3`) |
| `find_mean_std(num1, num2, num3)` | `(mean, std)` with population std (`÷ n`) |

## Practice in Colab (optional)

**From GitHub:** use **Ctrl+click** / **⌘+click** (or middle-click) so Colab opens in a new tab — GitHub ignores `target=_blank` on README links.


<a href="https://colab.research.google.com/github/TelHai-python-Odyssey-CS-2027/ps2/blob/main/simple_statistic.ipynb" target="_blank" rel="noopener noreferrer"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

The notebook is not graded — only `math_utils.py` counts. Each function in the notebook is followed with a **self-check** cell that runs the same cases as the autograder (and prints expected / got / hint) - run it before you copy your code into the `.py` file.

## Submit

1. Accept the Classroom 50 assignment.
2. Open `math_utils.py` in your repository.
3. Implement the three functions, then **Commit changes**.
4. Check the latest autograding run for your score.
5. If a test fails, read the message, fix, and commit again.

## Grading — 10 points

Points are split across cases; a failing case shows the exact input, expected value, your value, and a hint in the autograding **Details**.

| Check | Points |
| --- | ---: |
| `find_max_number` — distinct values / negatives / float | 2 |
| `find_max_number` — ties (e.g. `3, 3, 1`) | 2 |
| `find_mean` — `(1,2,3)`, with negatives, equal values | 1 + 1 + 1 |
| `find_mean_std` — `(1,2,3)`, equal values, `(4,8,12)` | 1 + 1 + 1 |
