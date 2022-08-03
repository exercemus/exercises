import json


def read_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)


# Throw an exception if the new exercises.json file is invalid
if __name__ == '__main__':
    data = read_data('exercises.json')
    # TODO use schema library to validate format as well
