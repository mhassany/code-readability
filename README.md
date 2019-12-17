# src/flask
"src/flask" is the codebase of "pallets/flask".

# Install Radon:
https://pypi.org/project/radon/

### Raw: 
1. radon raw -s -j -O raw.json ./src/flask 

### Cyclomatic Complexity: 
1. radon cc -s -a -j --codeclimate -O cc.json ./src/flask

### Halstead 
1. radon hal -j -O hal.json ./src/flask 

### Maintainability Index
1. radon mi -s -j -O mi.json ./src/flask 

### PyLint
1. python3 ./pylint/run_python.py