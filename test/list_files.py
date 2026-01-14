from pathlib import Path

# setup the current directory and current file variables
current_dir = Path.cwd() # The following accomplish the same thing Path('.')
current_file = Path(__file__).name

print(f"Files in {current_dir}:")

# filepath syntax is in pathlib/Path module
for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue

    print(f"  - {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encoding='utf-8')
        print(f"    Content: {content}")