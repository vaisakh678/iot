import os

template = open("template.js").read()
circuits_path = "circuits"

circuits = {}
for fileName in os.listdir(circuits_path):
    circuit = open(os.path.join(circuits_path, fileName), "r").read()
    circuits[fileName.split(".")[0]] = circuit

compiled = template.replace('{"replace-code-here-mf"}', str(circuits)).replace("\n", " ").replace("    ", " ")
open("compiled.txt", "w").write(compiled)
    













