# ---------------- #
# -- Generators -- #
# ---------------- #
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not From Begining
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# -----------------------------------------------------------------

import sys  # For measuring the size of objects in memory
from datetime import datetime  # For tracking execution time
import random  # For generating random student data
import memory_profiler  # For measuring memory usage

# Define some example students and majors
Students = ["Mohamed", "Ahmed", "Hany", "Yousef"]
majors = ["Math", "Physics", "Concrete", "Structure"]

# Measure initial memory usage
print(f"Memory (Before): {memory_profiler.memory_usage()[0]}Mb")


def students_generator(students):
    """
    Generator function to create a specified number of student records.

    Args:
        students (int): The number of student records to generate.

    Yields:
        dict: A dictionary representing a student's details.
    """
    for i in range(students):
        student = {
            "id": i,  # Unique ID for each student
            "name": random.choice(Students),  # Randomly choose a name
            "major": random.choice(majors),  # Randomly choose a major
        }
        yield student  # Yield the student dictionary one at a time


# Record the start time
t1 = datetime.now()

# Create a generator object for 1,000,000 students
student_class = students_generator(1000000)

# Measure the size of the generator object in bytes
generator_size = sys.getsizeof(student_class)
print(f"Size of Generator: {generator_size} bytes")

# Iterate through the generator to simulate processing each student record
for student in student_class:
    pass  # No operation; just iterating through the generator

# Record the end time
t2 = datetime.now()

# Measure final memory usage
print(f"Memory (After): {memory_profiler.memory_usage()[0]}Mb")

# Calculate and print the time taken for the entire process
print(f"Took {t2 - t1} Seconds")
