import json


def read_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def write_compressed(filename, data):
    with open(filename, 'w') as output:
        output.write(json.dumps(data))


if __name__ == '__main__':
    data = read_data('exercises.json')

    # TODO once all exercises are merged, remove this
    to_merge = data['exercises_to_merge']
    del data['exercises_to_merge']
    data['exercises'].extend(to_merge)

    write_compressed('exercises-minified.json', data)
