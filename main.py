import os
import subprocess

def create_blank_file():
    # Get the current directory
    current_dir = os.getcwd()

    # Check if it's a git repository
    result = subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], stdout=subprocess.PIPE)
    if result.returncode != 0 or result.stdout.decode().strip() != "true":
        print("Not a Git repository.")
        return

    # Get the commit hash
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], stdout=subprocess.PIPE)
    commit_hash = result.stdout.decode().strip()

    # Create a blank file with the commit hash as the name
    file_name = f"{commit_hash}.txt"
    with open(file_name, "w") as file:
        pass  # Blank file, nothing to write

    print(f"Blank file '{file_name}' created.")

if __name__ == "__main__":
    create_blank_file()
