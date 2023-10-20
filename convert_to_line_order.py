file_path = "The Great Gatsby/ch6sentences.txt"  # Replace with the path to your text file

with open(file_path, 'r') as file:
    lines = file.readlines()

current_color = None
sentences = []

for line in lines:
    if len(line.split(" "))==2:
        current_color = line.split(" ")[0].lower()
    if len(line.split(" "))>=3:
        sentences.append((int(line.split("(")[1].split(")")[0]),line.split(") ")[1],current_color))
for i in sorted(sentences):
    print(f"- ({i[0]}) {i[1].replace(i[2],i[2].upper())}")