import shutil

ZIP_OUTPUT_LOCATION = "autograder_zips/"

question_directories = [f"q{i}" for i in range(1, 8)] # q1-q7
for dir in question_directories:
    zip_name = f"{ZIP_OUTPUT_LOCATION}/hw2{dir}"
    shutil.make_archive(base_name=zip_name,  # output zip directory and name
                        format="zip",
                        root_dir=dir)  # directory to zip
