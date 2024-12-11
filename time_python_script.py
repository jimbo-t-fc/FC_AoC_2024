import subprocess
import time
import sys

def measure_script_execution_time(module_name, repetitions=5):
    """
    Measures the average execution time of a Python module over multiple runs,
    ensuring the `if __name__ == "__main__"` block is executed.

    :param module_name: Name of the Python module to measure (e.g., ML.Day_11.Day11b).
    :param repetitions: Number of times to run the module for averaging.
    :return: Average execution time in seconds.
    """
    total_time = 0.0

    try:
        for i in range(repetitions):
            # Start the timer
            start_time = time.time()

            # Run the module as a script using subprocess
            result = subprocess.run(
                [sys.executable, "-m", module_name],
                capture_output=True,
                text=True
            )

            # Check for errors
            if result.returncode != 0:
                print(f"Error on run {i + 1}/{repetitions}:")
                print(f"STDOUT: {result.stdout}")
                print(f"STDERR: {result.stderr}")
                return

            # Calculate elapsed time for this run
            elapsed_time = time.time() - start_time
            total_time += elapsed_time

            print(f"Run {i + 1}/{repetitions}: {elapsed_time:.4f} seconds")

        # Calculate the average time
        average_time = total_time / repetitions
        print(f"\nAverage execution time over {repetitions} runs: {average_time:.4f} seconds")
        return average_time

    except FileNotFoundError:
        print(f"Module not found: {module_name}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Input the module name
    module_name = input("Enter the module name (e.g., JT.Days.Day_1): ").strip()

    # Input the number of repetitions
    repetitions = input("Enter the number of repetitions (default is 5): ").strip()
    repetitions = int(repetitions) if repetitions.isdigit() else 5

    # Measure the script execution time
    measure_script_execution_time(module_name, repetitions)
