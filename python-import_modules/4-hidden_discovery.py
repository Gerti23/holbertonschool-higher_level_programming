# /tmp/4-hidden_discovery.py
import sys
import importlib.util

if __name__ == "__main__":
    # Load the compiled module
    module_path = "/tmp/hidden_4.pyc"
    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get all names defined in the module
    names = dir(hidden_4)

    # Filter and sort the names
    filtered_names = sorted(name for name in names if not name.startswith("__"))

    # Print each name on a new line
    for name in filtered_names:
        print(name)
