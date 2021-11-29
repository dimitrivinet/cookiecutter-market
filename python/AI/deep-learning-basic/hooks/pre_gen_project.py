import re
import sys

MODULE_REGEX = r"^[a-zA-Z][_a-zA-Z0-9]+$"
module_name = "{{ cookiecutter.module_name }}"

CLASS_REGEX = r"^[A-Z][a-zA-Z0-9]+$"
model_name = "{{ cookiecutter.model_name }}"

if not re.match(MODULE_REGEX, module_name):
    print("ERROR: %s is not a valid Python module name!" % module_name)
    sys.exit(1)

if not re.match(CLASS_REGEX, model_name):
    print("ERROR: %s is not a valid Python model name!" % model_name)
    sys.exit(1)
