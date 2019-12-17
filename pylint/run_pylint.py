import os
import subprocess
import json

FLASK_SRC_PATH = "src/flask"

summary = {}
warnings = {}


def run_linter(path):
    """ run linter for the given path """
    global summary, warnings

    for file in os.listdir(path):
        # for each file
        n_path = path + "/" + file

        # if it is a directory
        if os.path.isdir(n_path):
            run_linter(n_path)

        # or a file
        else:
            # linter command
            output = "./pylints/" + \
                (n_path.replace("/", "__").replace(".", "")) + "-output.json"
            # -f json
            # write output to a file
            os.system("python3 -m pylint " + n_path + " > " + output)

            path_end = n_path.replace("../..", "")
            path_json = {"score": 0, "warnings": set()}

            # read the output file
            with open(output) as input:
                for line in input:
                    # for each warning
                    if line.startswith("/"):
                        path_end_i = line.find(path_end) + len(path_end)
                        warning = line.strip()[path_end_i:]
                        warning = warning[warning.find(" ") + 1:]

                        processed = warning.split(": ", 1)
                        # remember the warning
                        path_json["warnings"].add(processed[0])
                        warnings[processed[0]] = processed[1]
                    
                    # get summary
                    elif line.startswith("Your code has been rated at "):
                        tmp = line.strip()
                        start = tmp.find("at ") + 3
                        end = tmp.find("/")
                        path_json["score"] = tmp[start:end]

            # remember the summary for the file
            summary[n_path] = path_json

# run linter
run_linter(FLASK_SRC_PATH)
summary["warnings"] = warnings


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

# then write it to the file
with open('./pylint.json', 'w') as file:
    json.dump(summary, file, indent=4, default=set_default)
