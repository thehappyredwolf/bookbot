# BookBot

BookBot is a small command-line Python project that analyzes a text file and prints a readable report.

The report includes:

- Total word count
- Character frequency count (letters only in the printed report)
- Characters sorted from most frequent to least frequent

## What this project does

BookBot reads a text file, counts the words and characters, then prints a summary report showing word count and character frequency sorted from most to least common.

## Project structure

- [main.py](main.py) — Main entry point that handles file reading, analysis, and output
- [stats.py](stats.py) — Helper functions for counting words and characters

## Requirements

- Python 3.x

## How to run

From the project root, run:

`python3 main.py <path_to_book>`

Example:

`python3 main.py books/frankenstein.txt`

## Output format

BookBot prints output in this structure:

```
============ BOOKBOT ============
Analyzing book found at <path>...
----------- Word Count ----------
Found <N> total words
--------- Character Count -------
a: <count>
b: <count>
...
============= END ===============
```

Only alphabetic characters are shown in the character section of the report.

## Notes

- Text is converted to lowercase before counting
- Only alphabetic characters are displayed in the final report
- The script requires exactly one argument: the file path

## License

MIT License - See [LICENSE](LICENSE) file for details.
