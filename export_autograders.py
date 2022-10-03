import zipfile
import pathlib

QUESTION_DIRECTORIES = [f"q{i}" for i in range(1, 8)]  # CHANGE: q1-q7

ZIP_OUTPUT_LOCATION  = "autograder_zips"               # NO CHANGE NEEDED
TEMPLATE_DIRECTORY   = "template"                      # NO CHANGE NEEDED
TEMPLATE_FILES       = ["requirements.txt",            # NO CHANGE NEEDED
                        "run_autograder",
                        "run_tests.py",
                        "setup.sh"]

for dir in QUESTION_DIRECTORIES:
    with zipfile.ZipFile(f"{ZIP_OUTPUT_LOCATION}/hw{dir}.zip", mode="w") as archive:
        for file in TEMPLATE_FILES:  # Archive template files
            archive.write(f"{TEMPLATE_DIRECTORY}/{file}", arcname=file)  # Archive test files
        for file in pathlib.Path(dir).rglob("*.py"):  # Recursively search for python files
            archive.write(file, arcname=file.relative_to(dir))
