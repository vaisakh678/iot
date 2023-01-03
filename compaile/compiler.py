import os
import pydash

circuits_path = "/Users/vaisakh/programs/iot/compaile/circuits"
template = "/Users/vaisakh/programs/iot/compaile/template.js"
outfile = "/Users/vaisakh/programs/iot/bundle.txt"

template = open(template).read()
circuits = {}
for fileName in os.listdir(circuits_path):
    circuit = open(os.path.join(circuits_path, fileName), "r").read()
    circuits[
        pydash.camel_case(fileName.split(".")[0])
    ] = circuit

compiled = template.replace('{"replace-code-here-mf"}', str(circuits)).replace("\n", " ").replace("    ", " ")
open(outfile, "w").write(compiled)
    

