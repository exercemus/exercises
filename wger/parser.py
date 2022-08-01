import os
import json
import copy


def init_data_from_source(data_dir):
    return_data = {}
    for filename in os.listdir(data_dir):
        with open(os.path.join(data_dir, filename), 'r') as file:
            data_list = json.load(file)
            for entry in data_list:
                data_type = entry['model'].split('.')[-1]
                if data_type not in return_data:
                    return_data[data_type] = {}
                return_data[data_type][entry['pk']] = entry['fields']
    return return_data


def join_to_exercises(parsed_data):
    data = copy.deepcopy(parsed_data)
    for exercise in data['exercise'].values():
        exercise_base = data['exercisebase'][exercise['exercise_base']]
        del exercise['exercise_base']
        to_copy_from_base = [
            'category', 'equipment', 'muscles', 'muscles_secondary', 'variations',
        ]
        for to_copy in to_copy_from_base:
            exercise[to_copy] = exercise_base[to_copy]

        exercise['license'] = data['license'][exercise['license']]
        exercise['language'] = data['language'][exercise['language']]['short_name']
        exercise['category'] = data['exercisecategory'][exercise['category']]['name']
        exercise['equipment'] = list(map(
            lambda key: data['equipment'][key]['name'].lower(),
            exercise['equipment'],
        ))

        muscle_lists_to_join = ['muscles', 'muscles_secondary']
        for list_to_join in muscle_lists_to_join:
            def get_name(muscle):
                muscle_name = muscle['name_en'] if 'name_en' in muscle else muscle['name']
                return muscle_name.lower()
            exercise[list_to_join] = list(map(
                lambda key: get_name(data['muscle'][key]),
                exercise[list_to_join],
            ))

        to_rename = {'variations': 'variation_id', 'muscles': 'primary_muscles',
                     'muscles_secondary': 'secondary_muscles', }
        for old, new in to_rename.items():
            exercise[new] = exercise[old]
            del exercise[old]

        equipment_renames = {
            'sz-bar': 'ez curl bar',
            'swiss ball': 'exercise ball',
            'none (bodyweight exercise)': 'none',
        }
        for old, new in equipment_renames.items():
            for index, equipment in enumerate(exercise['equipment']):
                if equipment == old:
                    exercise['equipment'][index] = new

        fields_to_delete = ['uuid', 'status',
                            'name_original', 'creation_date', 'category']
        for field in fields_to_delete:
            del exercise[field]

    return list(data['exercise'].values())


def write_pretty(filename, data):
    with open(filename, 'w') as output:
        output.write(json.dumps(data, sort_keys=True, indent=2))


if __name__ == '__main__':
    data = init_data_from_source('source_data')
    write_pretty('all_data.json', data)

    exercises = join_to_exercises(data)
    write_pretty('all_exercises.json', exercises)

    def _remove_lang(exercise):
        del exercise['language']
        return exercise
    filtered_exercises = list(map(_remove_lang, filter(
        lambda exercise: exercise['language'] == 'en',
        exercises,
    )))
    write_pretty('exercises.json', filtered_exercises)
