
invited_names = []

with open("invited_names.txt", "r") as f:
    invited_names = f.readlines()

with open("letter.txt") as f:
    line = f.read()
    for name in invited_names:
        striped_name = name.strip()
        new_letter = line.replace("[Name]", striped_name)
        with open(f"./letter_for_{striped_name}.txt", "w") as f_1:
            f_1.write(new_letter)
