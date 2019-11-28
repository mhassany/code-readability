from collections import defaultdict

# Raw Stats By File	
raw = [
    [1, "flask/app.py"],
    [2, "flask/helpers.py"],
    [3, "flask/cli.py"],
    [4, "flask/blueprints.py"],
    [5, "flask/ctx.py"],
    [6, "flask/sessions.py"],
    [7, "flask/json/__init__.py"],
    [8, "flask/json/tag.py"],
    [9, "flask/config.py"],
    [10, "flask/testing.py"],
    [11, "flask/debughelpers.py"],
    [12, "flask/views.py"],
    [13, "flask/templating.py"],
    [14, "flask/_compat.py"],
    [15, "flask/wrappers.py"],
    [16, "flask/logging.py"],
    [17, "flask/signals.py"],
    [18, "flask/globals.py"],
    [19, "flask/__init__.py"],
    [20, "flask/__main__.py"]
]

# Cyclomatic Complexity By File	
cc = [
    [1, "flask/app.py"],
    [2, "flask/cli.py"],
    [3, "flask/ctx.py"],
    [4, "flask/config.py"],
    [5, "flask/testing.py"],
    [6, "flask/blueprints.py"],
    [7, "flask/sessions.py"],
    [8, "flask/templating.py"],
    [9, "flask/json/tag.py"],
    [10, "flask/views.py"],
    [11, "flask/json/__init__.py"],
    [12, "flask/helpers.py"],
    [13, "flask/wrappers.py"],
    [14, "flask/debughelpers.py"],
    [15, "flask/_compat.py"],
    [16, "flask/signals.py"]
]

# Halstead by File					
hal = [
    [1, "flask/app.py"],
    [2, "flask/helpers.py"],
    [3, "flask/cli.py"],
    [4, "flask/ctx.py"],
    [5, "flask/debughelpers.py"],
    [6, "flask/json/__init__.py"],
    [7, "flask/testing.py"],
    [8, "flask/blueprints.py"],
    [9, "flask/config.py"],
    [10, "flask/json/tag.py"],
    [11, "flask/sessions.py"],
    [12, "flask/logging.py"],
    [13, "flask/wrappers.py"],
    [14, "flask/templating.py"],
    [15, "flask/views.py"],
    [16, "flask/_compat.py"],
    [17, "flask/globals.py"],
    [18, "flask/__main__.py"],
    [19, "flask/signals.py"],
    [20, "flask/__init__.py"]
]

# Maintainability Index By File	
mi = [
    [1, "flask/app.py"],
    [2, "flask/cli.py"],
    [3, "flask/helpers.py"],
    [4, "flask/ctx.py"],
    [5, "flask/blueprints.py"],
    [6, "flask/json/__init__.py"],
    [7, "flask/debughelpers.py"],
    [8, "flask/config.py"],
    [9, "flask/sessions.py"],
    [10, "flask/json/tag.py"],
    [11, "flask/views.py"],
    [12, "flask/testing.py"],
    [13, "flask/templating.py"],
    [14, "flask/wrappers.py"],
    [15, "flask/_compat.py"],
    [16, "flask/__main__.py"],
    [17, "flask/logging.py"],
    [18, "flask/globals.py"],
    [19, "flask/__init__.py"],
    [20, "flask/signals.py"]
]

# PyLint Score By File	
py = [
    [1, "flask/signals.py"], 
    [2, "flask/wrappers.py"], 
    [3, "flask/_compat.py"], 
    [4, "flask/globals.py"], 
    [5, "flask/ctx.py"], 
    [6, "flask/blueprints.py"], 
    [7, "flask/sessions.py"], 
    [8, "flask/app.py"], 
    [9, "flask/testing.py"], 
    [10, "flask/json/__init__.py"], 
    [11, "flask/cli.py"], 
    [12, "flask/config.py"], 
    [13, "flask/helpers.py"], 
    [14, "flask/json/tag.py"], 
    [15, "flask/views.py"], 
    [16, "flask/debughelpers.py"], 
    [17, "flask/templating.py"], 
    [18, "flask/logging.py"], 
    [19, "flask/__main__.py"], 
    [20, "flask/__init__.py"]
]

# Line Addition/Removal by File	
ar = [
    [1, "flask/app.py"],
    [2, "flask/cli.py"],
    [3, "flask/helpers.py"],
    [4, "flask/sessions.py"],
    [5, "flask/wrappers.py"],
    [6, "flask/blueprints.py"],
    [7, "flask/ctx.py"],
    [8, "flask/testing.py"],
    [9, "flask/module.py"],
    [10, "flask/json/tag.py"],
    [11, "flask/templating.py"],
    [12, "flask/run.py"],
    [13, "flask/__init__.py"],
    [14, "flask/json.py"],
    [15, "flask/config.py"],
    [16, "flask/debughelpers.py"],
    [17, "flask/_compat.py"],
    [18, "flask/logging.py"],
    [19, "flask/json/__init__.py"],
    [20, "flask/exthook.py"],
    [21, "flask/views.py"],
    [22, "flask/ext/__init__.py"],
    [23, "flask/signals.py"],
    [24, "flask/conf.py"],
    [25, "flask/globals.py"],
    [26, "flask/session.py"],
    [27, "flask/exceptions.py"],
    [28, "flask/__main__.py"]
]

# Number of Contributors	
cn = [
    [1, "flask/app.py"],
    [2, "flask/helpers.py"],
    [3, "flask/cli.py"],
    [4, "flask/wrappers.py"],
    [5, "flask/blueprints.py"],
    [6, "flask/sessions.py"],
    [7, "flask/ctx.py"],
    [8, "flask/json.py"],
    [9, "flask/testing.py"],
    [10, "flask/config.py"],
    [11, "flask/views.py"],
    [12, "flask/_compat.py"],
    [13, "flask/templating.py"],
    [14, "flask/__init__.py"],
    [15, "flask/signals.py"],
    [16, "flask/exthook.py"],
    [17, "flask/module.py"],
    [18, "flask/debughelpers.py"],
    [19, "flask/logging.py"],
    [20, "flask/globals.py"],
    [21, "flask/__main__.py"],
    [22, "flask/json/__init__.py"],
    [23, "flask/ext/__init__.py"],
    [24, "flask/json/tag.py"],
    [25, "flask/session.py"],
    [26, "flask/run.py"],
    [27, "flask/exceptions.py"],
    [28, "flask/conf.py"]
]

# Issue File Hit Count	
fc = [
    [1, "flask/app.py"],
    [2, "flask/cli.py"],
    [3, "flask/helpers.py"],
    [4, "flask/logging.py"],
    [5, "flask/json.py"],
    [6, "flask/_compat.py"],
    [7, "flask/wrappers.py"],
    [8, "flask/blueprints.py"],
    [9, "flask/templating.py"],
    [10, "flask/__init__.py"],
    [11, "flask/ctx.py"],
    [12, "flask/__main__.py"],
    [13, "flask/sessions.py"],
    [14, "flask/exthook.py"],
    [15, "flask/ext/__init__.py"],
    [16, "flask/globals.py"],
    [17, "flask/views.py"],
    [18, "flask/config.py"],
    [19, "flask/testing.py"],
    [20, "flask/debughelpers.py"],
    [21, "flask/json/__init__.py"],
    [22, "flask/json/tag.py"]
]

file_rank_total = defaultdict(int)
file_rank_count = defaultdict(int)

for each in raw:
    file_rank_total[each[1]] += each[0]
    file_rank_count[each[1]] += 1

for each in cc:
    file_rank_total[each[1]] += each[0]
    file_rank_count[each[1]] += 1

for each in hal:
    file_rank_total[each[1]] += each[0]
    file_rank_count[each[1]] += 1

for each in mi:
    file_rank_total[each[1]] += each[0]
    file_rank_count[each[1]] += 1

for each in py:
    file_rank_total[each[1]] += each[0]
    file_rank_count[each[1]] += 1

for each in ar:
    file_rank_total[each[1]] += each[0]
    file_rank_count[each[1]] += 1

for each in cn:
    file_rank_total[each[1]] += each[0]
    file_rank_count[each[1]] += 1

for each in fc:
    file_rank_total[each[1]] += each[0]
    file_rank_count[each[1]] += 1

file_rank = defaultdict(float)

for file, total in file_rank_total.items():
    file_rank[file] = file_rank_total[file] / file_rank_count[file]

file_rank = sorted(file_rank.items(), key=lambda kv: kv[1])

for each in file_rank:
    print(each)
