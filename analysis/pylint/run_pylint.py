import os
import subprocess
import json


summary = {}
warnings = {}


def run_linter(path):
    global summary, warnings

    for file in os.listdir(path):
        n_path = path + "/" + file
        if os.path.isdir(n_path):
            run_linter(n_path)
        else:
            output = "./" + \
                (n_path.replace("/", "__").replace(".", "")) + "-output.json"
            # -f json
            os.system("python3 -m pylint " + n_path + " > " + output)

            path_end = n_path.replace("../..", "")
            path_json = {"score": 0, "warnings": set()}

            with open(output) as input:
                for line in input:
                    if line.startswith("/"):
                        path_end_i = line.find(path_end) + len(path_end)
                        warning = line.strip()[path_end_i:]
                        warning = warning[warning.find(" ") + 1:]

                        processed = warning.split(": ", 1)

                        path_json["warnings"].add(processed[0])
                        warnings[processed[0]] = processed[1]
                    elif line.startswith("Your code has been rated at "):
                        tmp = line.strip()
                        start = tmp.find("at ") + 3
                        end = tmp.find("/")
                        path_json["score"] = tmp[start:end]

            summary[n_path] = path_json


# print(files)
run_linter("../../src/flask")
summary["warnings"] = warnings


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


with open('../pylint.json', 'w') as file:
    json.dump(summary, file, indent=4, default=set_default)
