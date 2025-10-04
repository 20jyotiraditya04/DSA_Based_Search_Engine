# Generate prob_names.txt from the new Database directory
import os

db_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Database'))
files = os.listdir(db_dir)
out_path = os.path.join(os.path.dirname(__file__), 'prob_names.txt')
count = 0
with open(out_path, 'w', encoding='utf-8') as f:
    for file in files:
        if file.endswith('.txt'):
            name = file[:-4]  # remove .txt
            if os.path.exists(os.path.join(db_dir, file)):
                f.write(name + '\n')
                count += 1
print(f"Wrote {count} problem names to {out_path}.")
