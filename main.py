# PDB Geometry 02 - Peptide Bond 1.33A Check
# Author: Urva Sohail

import math
from pathlib import Path

def calc_distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def parse_pdb(pdb_file):
    residues = {}
    with open(pdb_file) as f:
        for line in f:
            if line.startswith("ATOM"):
                res_id = int(line[22:26])
                atom = line[12:16].strip()
                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])
                if res_id not in residues:
                    residues[res_id] = {}
                if atom in ["C", "N"]:
                    residues[res_id][atom] = (x,y,z)
    return residues

pdb_path = Path("1aki.pdb")
if not pdb_path.exists():
    print("1aki.pdb not found! Copy from Project 01")
    exit()

residues = parse_pdb(pdb_path)
print(f"=== PDB Geometry 02: Peptide Bond Check ===")
print(f"File: {pdb_path} | Total residues: {len(residues)}\n")

violations = 0
for i in sorted(residues.keys())[:-1]:
    j = i + 1
    if j in residues and "C" in residues[i] and "N" in residues[j]:
        d = calc_distance(residues[i]["C"], residues[j]["N"])
        status = "OK" if 1.0 <= d <= 1.5 else "VIOLATION"
        if status == "VIOLATION":
            violations += 1
        print(f"Residue {i} C -> {j} N : {d:.3f} A [{status}]")

print(f"\nTotal violations: {violations}")
print("Ideal peptide bond C-N should be ~1.33A")