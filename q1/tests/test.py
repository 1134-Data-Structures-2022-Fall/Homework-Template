"""
This is main test file for the autograder. Any tests you want to run on Gradescope
should be defined here. This should be the only file that needs to be modified.
You can define any number of tests you want, but please follow the structure in the
README.

To test the autograder locally, `cd` into this directory and then run this file with
`python test.py` The output will be created in a `results.json` file. This result file
is not exported to Gradescope and only used to verify the autograder.
"""

import unittest  # Testing library
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
import submission  # Student code
from timeout import timeout  # Timeout helper for infinite loops

"""
Helper functions to help with grading. These functions might be solutions
to the question being tested, validators for the student's submission, etc.
"""
def func_solution(n):
    pass

class TestHW(unittest.TestCase):
    # Should not be modified
    tests_run = -2  # Offset for intro and summary "test"s
    tests_passed = 0

    # Should not be modified
    def setUp(self):
        """Run before each test method"""
        self.__class__.tests_run += 1
        self._test_passed = False
        self.longMessage = False  # Remove default assertion messages

    # Should not be modified
    def tearDown(self):
        """Run after each test method"""
        if self._test_passed:
            self.__class__.tests_passed += 1

    # Should not be modified
    @number("0")
    @visibility("hidden")
    @weight(0)
    def test_zz_summary(self):
        """Displays a summary of the test results to the grader"""
        print(f"Tests passed: {self.__class__.tests_passed}/{self.__class__.tests_run}")

    ###############################
    # Modify the tests below here #
    ###############################

    # Displays an introduction to the student and grader
    @number("1")
    @visibility("visible")
    @weight(0)
    def test_AA_intro(self):
        from inspect import cleandoc
        INTRO_STRING = cleandoc("""
        Basic info:
            1. This is the autograder test for HW_ Q_.
            2. Read the instructions carefully and ensure your code works as described in the PDF.
            3. Only submit ONE python file. No jupyter notebooks or PDFs for code submissions.
            4. If you have any questions or have any autograder issues, please ask on Piazza.
            5. Remove or comment out any print statements to ensure the autograder works properly.
            6. Your function must be named 'func()' and it must take one integer argument.
        Tips:
            1. 
        """)
        print(INTRO_STRING)

    @number("10")
    @visibility("visible")
    @weight(0)
    def test_BB_given_example(self):
        print("Testing with given example: func(10).")
        expected_output = func_solution(100)
        student_output = submission.func(100)
        error_message = f"Error: The output is not correct.\nValues expected: {expected_output}\nValues generated: {student_output}"
        self.assertEqual(expected_output, student_output, error_message)
        print("Test Passed: given test case passed.")
        self._test_passed = True

    @number("20")
    @visibility("visible")
    @weight(0)
    def test_CC_mystery_number(self):
        print("Testing with mystery number.")
        expected_output = func_solution(100)
        student_output = submission.func(100)
        self.assertTrue(expected_output == student_output, "Mystery test failed.")
        print("Test Passed: mystery test case passed.")
        self._test_passed = True

    @number("30")
    @visibility("hidden")
    @weight(0)
    def test_ZZ_10_random_numbers(self):
        print("Testing 10 random numbers between 1 and 1000000.")
        import random
        for _ in range(10):
            num = random.randint(1, 1000000)
            expected_output = func_solution(num)
            student_output = submission.func(num)
            self.assertEqual(expected_output, student_output, f"Error: func({num}))")
        print("Test Passed: 10 random tests passed.")
        self._test_passed = True

    @number("31")
    @visibility("hidden")
    @weight(0)
    @timeout(1)
    def test_timeout(self):
        while True:
            pass

# Tests the autograder output for this test file
if __name__ == "__main__":
    import unittest
    from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

    suite = unittest.defaultTestLoader.discover('.')
    with open('results.json', 'w') as f:
        JSONTestRunner(visibility='visible', stream=f).run(suite)
