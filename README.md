# exercises
## An open source exercise list curated from [exercemus](https://exercemus.com), [wger.de](https://github.com/wger-project/wger), and [exercises.json](https://github.com/wrkout/exercises.json)
### You can see the final results in [the exercemus exercise library](https://exercem.us/exercises).

After struggling to find an easy-to-use, open source exercise list for exercemus, I decided to curate this open source list. The initial list was created from wger.de and exercises.json (big thanks to these projects). In the future, as exercises are modified and submitted to exercemus by users, they will open automated PRs and be added to this repository for all to enjoy. It is my personal belief that data like that provided here should be readily accessible by all.

You can use the latest exercise data directly in your code from here (yes, it is really this simple):
https://raw.githubusercontent.com/exercemus/exercises/main/exercises-minified.json

## NOTICE
This list is still a WIP, so please expect duplicates and slightly broken schema (until ~September 2022) until I can manually review and fix all the data. However, feel free to use the data as-is. Anticipated changes:
- Dev ops: automatic minification in a separate branch (minified file will move branches)
- `instructions` not nullable after all merges?

## Format
`exercises.json` has the following fields:
- `categories`, a `list<string>` which defines the different exercise categories
- `equipment`, a `list<string>` which defines the different exercise equipment
- `muscles`, a `list<string>` which defines the different muscles
- `muscle_groups`, a `map<string, list<string>>` which defines which muscle group corresponds to which muscles (useful for filtering exercises by muscle group)
- `exercises`, a `list<exercise>` (see below for schema) that has all of the exercises

Each `exercise` has the following schema:
- `category`, from `categories` above
  - `strength` is the general catch-all category for exercises that are sport-agnostic
- `name`, as a `string` with no underscores and (url safe) characters
- `aliases` as a `list<string>?` for other names of the exercise
- `description` as a `string?`
- `instructions` as a `list<string>?`
- `tips` as a `list<string>?`
- `equipment` as a `list<string>`
- `primary_muscles` as a `list<string>`
- `secondary_muscles` as a `list<string>`
- `tempo` as a `string?` (`3-1-1-0`, for example)
- `images` as a `list<string>?` of urls
- `video` as a `string?` url (embeddable YouTube videos used when possible)
- `variation_on` as a `list<string>`
  - Example 1: Close-Grip Incline Bench Press is both a variation on `close-grip bench press` and also `incline bench press`)
  - Example 2: Zottman Preacher Curl is both a variation on `zottman curl` and `preacher curl`
- `license_author` as a `string?` (wger-specific: who submitted the exercise online on wger)
- `license` as a `map<string, string>?` (wger-specific):
  - `full_name` as a `string`
  - `short_name` as a `string`
  - `url` as a `string`

## Licensing Notes
All code in this repository is under the MIT License to enable free use. However, all exercises in this repository have a license associated with them that you must follow. Only exercises with a (relatively) free open source license are included in this repository, but care must be taken to ensure that you follow each exercise's licensing requirements. *THIS IS NOT ADVICE ON HOW TO PROPERLY HANDLE THESE LICENSES*, but this typically involves just displaying the author, license, and link to the license alongside each exercise.
