import json


def init_data_from_source(source_file):
    with open(source_file, 'r') as file:
        return json.load(file)['exercises']


def transform_exercises(exercises):
    for exercise in exercises:
        to_rename = {'primaryMuscles': 'primary_muscles',
                     'secondaryMuscles': 'secondary_muscles'}
        for old, new in to_rename.items():
            exercise[new] = exercise[old]
            del exercise[old]

        exercise['equipment'] = [exercise['equipment']] \
            if exercise['equipment'] is not None else ['none']
        if exercise['category'] == 'weighted bodyweight' or exercise['category'] == 'assisted bodyweight':
            exercise['category'] = 'calisthenics'
        if exercise['category'] == 'powerlifting':
            exercise['category'] = 'strength'

        equipment_renames = {
            'body only': 'none',
            'kettlebells': 'kettlebell',
            'e-z curl bar': 'ez curl bar',
        }
        for old, new in equipment_renames.items():
            for index, equipment in enumerate(exercise['equipment']):
                if equipment == old:
                    exercise['equipment'][index] = new

        muscle_renames = {
            'abdominals': 'abs',
            'quadriceps': 'quads',
        }
        for old, new in muscle_renames.items():
            for index, muscle in enumerate(exercise['primary_muscles']):
                if muscle == old:
                    exercise['primary_muscles'][index] = new
            for index, muscle in enumerate(exercise['secondary_muscles']):
                if muscle == old:
                    exercise['secondary_muscles'][index] = new

        to_delete = ['force', 'level', 'mechanic']
        for key in to_delete:
            if key in exercise:
                del exercise[key]


def write_pretty(filename, data):
    with open(filename, 'w') as output:
        output.write(json.dumps(data, sort_keys=True, indent=2))


if __name__ == "__main__":
    exercises = init_data_from_source('exercises-original.json')
    transform_exercises(exercises)
    write_pretty('exercises.json', exercises)
