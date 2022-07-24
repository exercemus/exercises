# exercises
## An open source exercise list curated from [exercemus](https://exercemus.com), [wger.de](https://github.com/wger-project/wger), and [exercises.json](https://github.com/wrkout/exercises.json)

After struggling to find an easy-to-use, open source exercise list for exercemus, I decided to curate this open source list. The initial list was created from wger.de and exercises.json (big thanks to these projects). In the future, as exercises are modified and submitted to exercemus by users, they will also be added to this repository for all to enjoy. It is my personal belief that data like that provided here should be readily accessible by all.

# NOTICE
This list is still a WIP, so please expect format changes. However, feel free to use the data as-is.

## Licensing Notes
All code in this repository is under the MIT License to enable free use. However, all exercises in this repository have a license associated with them that you must follow. Only exercises with a (relatively) free open source license are included in this repository, but care must be taken to ensure that you follow each exercise's licensing requirements. *THIS IS NOT ADVICE ON HOW TO PROPERLY HANDLE THESE LICENSES*, but this typically involves just displaying the author, license, and link to the license alongside each exercise.

## Source Data Structure Notes
Each of the source directories (`exercemus/`, `exercises_json/`, and `wger/`) have their own process that creates an `exercises.json` in the same directory that is in the final format ready to be integrated in the main list.
### [exercemus](https://exercemus.com)
- Coming soon

### [exercises.json](https://github.com/wrkout/exercises.json)
The data file created from the repository as of July 24th, 2022 is in `exercises-original.json`.
`python3 parser.py` in `exercises_json/` will create the corresponding `exercises.json`.

### [wger.de](https://github.com/wger-project/wger)
The following data files were created by `python3 parser.py` in `wger/`:
- `all_data.json` contains all data that I parsed from wger.de in an easier format
- `all_exercises.json` contains all (ready-to-use) exercises from wger.de
- `exercises.json` contains all (ready-to-use) English exercises from wger.de

