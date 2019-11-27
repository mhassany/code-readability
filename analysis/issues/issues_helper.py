import os
import json
from collections import namedtuple


def issues():
    for number in range(1, 3439):
        path = "./jsons/" + str(number) + ".json"

        if os.path.exists(path):
            file = open(path, "r")
            issue = json.load(file,
                              object_hook=lambda d: namedtuple(
                                  'X', d.keys()
                              )(*d.values()))
            file.close()
            yield issue
