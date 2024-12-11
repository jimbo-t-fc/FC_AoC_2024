import timeit
import sys
import os
import importlib

def measure_script_execution_time(module_name, repetitions=5):
    """
    Measures the average execution time of a Python module over multiple runs using the timeit module.

    :param module_name: Name of the Python module to measure (e.g., ML.Day_11.Day11b).
    :param repetitions: Number of times to run the module for averaging.
    :return: Average execution time in seconds.
    """
    try:
        # Extract the module object
        module = importlib.import_module(module_name)

        # Define a function to execute the module's code
        def run_module():
            importlib.reload(module)  # Reload to ensure the module re-executes

        # Use timeit to measure execution time
        total_time = timeit.timeit(run_module, number=repetitions)
        average_time = total_time / repetitions

        print(f"Average execution time over {repetitions} runs: {average_time:.4f} seconds")
        return average_time

    except ModuleNotFoundError:
        print(f"Module not found: {module_name}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Input the module name
    module_name = input("Enter the module name (e.g., JT.Days.Day_11, won't work if there are spaces): ").strip()

    # Input the number of repetitions
    repetitions = input("Enter the number of repetitions (default is 5): ").strip()
    repetitions = int(repetitions) if repetitions.isdigit() else 5

    # Measure the script execution time
    measure_script_execution_time(module_name, repetitions)
