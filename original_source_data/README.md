# Original Source Data Directory
This directory is not of much use anymore, but is kept for historical reasons.

## Source Data Structure Notes
Each of the source directories (`exercises_json/` and `wger/`) have their own process that creates an `exercises.json` in the same directory that is in the final format ready to be integrated in the main list. `/combine.py` combines the `wger/exercises.json` and `exercises_json/exercises.json` sources into `combined.json`, for manual review and merging. Then, `exercises.json` can be manually created and updated. In hindsight, I should've opted to use a more structured build system, but this works well enough, especially since it is a one-time process.

### [exercises.json](https://github.com/wrkout/exercises.json)
The data file created from the repository as of July 24th, 2022 is in `exercises-original.json`.
`python3 parser.py` in `exercises_json/` will create the corresponding `exercises.json`.

### [wger.de](https://github.com/wger-project/wger)
The following data files were created by `python3 parser.py` in `wger/`:
- `all_data.json` contains all data that I parsed from wger.de in an easier format
- `all_exercises.json` contains all (ready-to-use) exercises from wger.de
- `exercises.json` contains all (ready-to-use) English exercises from wger.de