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
    'cardio',
    'olympic weightlifting',
    'crossfit',
    'calisthenics',
]
equipment = [
    'none',
    'ez curl bar',
    'barbell',
    'dumbbell',
    'gym mat',
    'exercise ball',
    'medicine ball',
    'pull-up bar',
    'bench',
    'incline bench',
    'kettlebell',
    'machine',
    'cable',
    'bands',
    'foam roll',
    'other',
]
muscles = [
    'forearms',
    'abductors',
    'adductors',
    'middle back',
    'neck',
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


def read_exercises(exercise_source):
    with open(exercise_source, 'r') as file:
        return json.load(file)


def write_pretty(filename, data):
    with open(filename, 'w') as output:
        output.write(json.dumps(data, sort_keys=True, indent=2))


if __name__ == '__main__':
    data = {
        'muscle_groups': muscle_groups,
        'categories': categories,
        'equipment': equipment,
        'muscles': muscles,
        'exercises': read_exercises('exercises_json/exercises.json'),
        'exercises_to_merge': read_exercises('wger/exercises.json'),
    }
    write_pretty('combined.json', data)
