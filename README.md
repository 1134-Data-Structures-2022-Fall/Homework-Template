# Autograder files for hw

## Repository Structure

* Each homework assignment has its own repository. In the future this might change to a mono-repo with all assignments in a single repo.

## File Structure

* Questions separated into question folders `q1/`, `q2/`, etc.
* Tests for questions located in `q/tests/`.
  * Any helper files such as `ArrayList.py` should be located outside the `tests/` folder inside `q/`.
  * Other files should not need need to be modified.
* Output zips to be uploaded to Gradescope can be found in `autograder_zips/`
  * Export autograder zip files using [`export_autograders.py`](./export_autograders.py)
  * Old autograders before Fall 2022 are located in `autograder_zips/pre_fall_2022/`
  * Testing the autograder as student code can be found in `autograder_zips/autograder_student_tests/`

## Test Structure

Look in `q1-example/` for examples.

Tests are executed in alphabetical order. Test methods must start with `test` to be run by the Gradescope autograder.

Test methods are named using the following format:

* A - intro
  * Prints basic information about the question to the student.
* B - public tests
  * Tests visible to the student. Generally has more verbose error messages to help students debug.
* C - mystery tests
  * Tests visible to the student but without showing output or errors. Allows student to check that their function works for an input besides the given example but without knowing the exact input.
* Z - hidden tests
  * Tests not visible to the student. Generally contains a set of random tests and edge cases for the question.
* ZZ - summary
  * Testing summary displayed to graders.
