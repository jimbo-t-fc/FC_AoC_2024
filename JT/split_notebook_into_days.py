import nbformat
import os

def split_notebook(notebook_path, output_dir):
    # Load the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    # Get the import statements from the first cell
    first_cell = notebook.cells[0]
    if first_cell.cell_type != "code":
        raise ValueError("The first cell must contain imports as a code cell.")
    imports = first_cell.source.strip().replace('from get_test_input', 'from ..get_test_input')

    # Prepare the output directory
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through the notebook cells and split the content
    for i in range(1, len(notebook.cells), 2):
        # Ensure correct markdown and code cell pairing
        if i + 1 >= len(notebook.cells):
            break
        markdown_cell = notebook.cells[i]
        code_cell = notebook.cells[i + 1]
        
        # Verify markdown cell contains "Day X"
        if markdown_cell.cell_type == "markdown" and "Day" in markdown_cell.source:
            day_name = markdown_cell.source.strip().replace('#','')
            day_file = os.path.join(output_dir, f"{day_name.strip().replace(' ','_')}.py")
            
            # Write imports and code to the respective Python file
            with open(day_file, 'w', encoding='utf-8') as py_file:
                py_file.write(f"# {day_name}\n")
                py_file.write(f"{imports}\n\n")
                py_file.write(code_cell.source.strip())
                print(f"Created: {day_file}")

if __name__ == "__main__":
    # Define the notebook path and output directory
    notebook_path = r"/Users/jterrill002/Library/CloudStorage/OneDrive-PwC/Documents/AoC/2024/JT/AoC 2024.ipynb"
    output_dir = r"/Users/jterrill002/Library/CloudStorage/OneDrive-PwC/Documents/AoC/2024/JT/Days"

    split_notebook(notebook_path, output_dir)