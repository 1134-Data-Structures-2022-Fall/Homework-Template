import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
from submission import *

# Solution for the question being tested
# Not always necessary, but can be useful
def func_solution(n):
    pass

class TestHW_Q_(unittest.TestCase):
    tests_run = -2  # Offset for intro and summary "test"s
    tests_passed = 0

    # Run before each test method
    def setUp(self):
        self.__class__.tests_run += 1
        self._test_passed = False
        self.longMessage = False  # Remove default assertion messages

    # Run after each test method
    def tearDown(self):
        if self._test_passed:
            self.__class__.tests_passed += 1

    # Displays a summary of the test results to the grader
    @number("0")
    @visibility("hidden")
    @weight(0)
    def test_ZZ_summary(self):
        print(f"Tests passed: {self.__class__.tests_passed}/{self.__class__.tests_run}")

    # Displays an introduction to the student and grader
    @number("1")
    @visibility("visible")
    @weight(0)
    def test_intro(self):
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
    def test_given_example(self):
        print("Testing with given example: func(10).")
        expected_output = func_solution(100)
        student_output = func(100)
        self.assertEqual(expected_output, student_output, f"Error: The output is not correct.\nValues generated: {student_output}\nValues expected: {expected_output}")
        print("Test Passed: given test case passed.")
        self._test_passed = True

    @number("20")
    @visibility("visible")
    @weight(0)
    def test_mystery_number(self):
        print("Testing with mystery number.")
        expected_output = func_solution(100)
        student_output = func(100)
        self.assertTrue(expected_output == student_output, "Mystery test failed.")
        print("Test Passed: mystery test case passed.")
        self._test_passed = True

    @number("30")
    @visibility("hidden")
    @weight(0)
    def test_10_random_numbers(self):
        print("Testing 10 random numbers between 1 and 1000000.")
        import random
        for _ in range(10):
            num = random.randint(1, 1000000)
            expected_output = func_solution(num)
            student_output = func(num)
            self.assertEqual(expected_output, student_output, f"Error: func({num}))")
        print("Test Passed: 10 random tests passed.")
        self._test_passed = True
