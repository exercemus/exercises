import json

muscle_groups = {
    'arms': [
        'forearms', 'biceps', 'triceps', 'brachialis',
    ],
    'legs': [
        'abductors', 'adductors', 'quads', 'hamstrings', 'glutes',
    ],
    'core': ['abs', 'obliques'],
    'chest': ['chest', 'serratus anterior'],
    'back': [
        'neck', 'traps', 'lats', 'lower back', 'middle back',
    ],
    'shoulders': ['shoulders'],
    'calves': ['calves', 'soleus'],
}
categories = [
    'strength',
    'stretching',
    'plyometrics',
    'strongman',
    'powerlifting',
    'cardio',
    'olympic weightlifting',
    'crossfit',
    'calisthenics',
]
equipment = [
    'ez curl bar'
    'barbell',
    'dumbbell',
    'gym mat',
    'exercise ball',
    'medicine ball',
    'pull-up bar',
    'none (bodyweight exercise)',
    'bench',
    'incline bench',
    'kettlebell',
    'machine',
    'cable',
    'bands',
    'foam roll',
]
muscles = [
    'forearms',
    'abductors',
    'adductors',
    'middle back',
    'neck'
    'biceps',
    'shoulders',
    'serratus anterior',
    'chest',
    'triceps',
    'abs',
    'calves',
    'glutes',
    'traps',
    'quads',
    'hamstrings',
    'lats',
    'brachialis',
    'obliques',
    'soleus',
    'lower back',
]


def combine_sources(sources):
    exercises = []
    for exercise_source in sources:
        with open(exercise_source, 'r') as file:
            exercises.extend(json.load(file))
    return exercises


def write_pretty(filename, data):
    with open(filename, 'w') as output:
        output.write(json.dumps(data, sort_keys=True, indent=2))


def write_compressed(filename, data):
    with open(filename, 'w') as output:
        output.write(json.dumps(data))


if __name__ == '__main__':
    sources = ['wger/exercises.json', 'exercises_json/exercises.json']
    exercises = combine_sources(sources)
    data = {
        'muscle_groups': muscle_groups,
        'categories': categories,
        'equipment': equipment,
        'muscles': muscles,
        'exercises': exercises,
    }
    write_pretty('exercises.json', data)
    write_compressed('exercises-minified.json', data)
