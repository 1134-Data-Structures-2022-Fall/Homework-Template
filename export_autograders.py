import zipfile
import pathlib

### MODIFY THESE VARIABLES ###
HOMEWORK_NUMBER = 1  # The homework number (1, 2, 3, etc.)
FIRST_QUESTION  = 1  # The first question number (1, 2, 3, etc.)
LAST_QUESTION   = 1  # The last question number (1, 2, 3, etc.)
##############################

QUESTION_DIRECTORIES = [f"q{i}" for i in range(FIRST_QUESTION, LAST_QUESTION + 1)]  # NO CHANGE NEEDED
ZIP_OUTPUT_LOCATION  = "autograder_zips"               # NO CHANGE NEEDED
TEMPLATE_DIRECTORY   = "template"                      # NO CHANGE NEEDED
TEMPLATE_FILES       = ["requirements.txt",            # NO CHANGE NEEDED
                        "run_autograder",
                        "run_tests.py",
                        "setup.sh"]

for dir in QUESTION_DIRECTORIES:
    with zipfile.ZipFile(f"{ZIP_OUTPUT_LOCATION}/hw{HOMEWORK_NUMBER}{dir}.zip", mode="w") as archive:
        for file in TEMPLATE_FILES:  # Archive template files
            archive.write(f"{TEMPLATE_DIRECTORY}/{file}", arcname=file)  # Archive test files
        for file in pathlib.Path(dir).rglob("*.py"):  # Recursively search for python files
            archive.write(file, arcname=file.relative_to(dir))
