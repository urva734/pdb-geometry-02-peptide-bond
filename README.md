## 🔗 PDB Geometry 02 - Peptide Bond

A pure-Python tool that validates peptide bond geometry. Checks if C-N bond between consecutive residues is ~1.33A, a core rule of protein structure.

👤 Author
Urva Sohail

## ✨ Features
- **📏 Distance Check:** Calculates C-N distance between residues
- **✅ Validation:** Flags bonds outside 1.0-1.5A range
- **📊 Summary:** Counts total violations
- **🧹 Clean Repo:** PDB ignored via .gitignore
- **🐍 Pure Python:** Only math + pathlib

## 🧠 Logic
1. Parse PDB: Read 1aki.pdb line by line, filter only ATOM lines
2. Extract Atoms: For each residue, get C atom (x,y,z) and N atom (x,y,z)
3. Store: residues[res_id] = {'C': (x,y,z), 'N': (x,y,z)}
4. Calculate Distance: For i -> i+1, distance = sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2) between C of residue i and N of residue i+1
5. Validate: If 1.0 <= distance <= 1.5 => [OK] else [VIOLATION]
6. Report: Count total violations

## 💻 Technologies Used
- **Python 3+:** Core language
-**math.sqrt:** For Euclidean distance
- **pathlib:** For file handling
- **PDB Parser:** Custom ATOM line parser

## 🚀 How to Run
Using VS Code
1. Open folder pdb-geometry-02-peptide-bond
2. Copy 1aki.pdb from Project 01 into this folder
3. Run:
```
 python main.py
```

## 📥 Sample Input & Output
## Input
1aki.pdb file (Lysozyme 129aa)

## Output
```
=== PDB Geometry 02: Peptide Bond Check ===
File: 1aki.pdb | Total residues: 129
Residue 1 C -> 2 N : 1.322 A [OK]
Residue 2 C -> 3 N : 1.315 A [OK]
Residue 3 C -> 4 N : 1.330 A [OK]
...
Residue 128 C -> 129 N : 1.328 A [OK]
Total violations: 0
Ideal peptide bond C-N should be ~1.33A
```

## 📊 Result
- Total Residues Parsed: 129
- Total Peptide Bonds Checked: 128
- Bond Range Found: 1.31A - 1.34A
- Average C-N Distance: ~1.325A
- Violations: 0
- Status: PASS - All peptide bonds are in ideal geometry

## ⚙️ How It Works
- Program parses 1aki.pdb and reads ATOM lines
- For each residue, it extracts C atom xyz and N atom xyz
- It loops i to i+1 and calculates Euclidean distance
- If distance is between 1.0 and 1.5A, it marks OK else VIOLATION
- At end it prints total violations (ideal 0 for good PDB)

## 🔮 Future Improvements
- [ ] Check CA-CA 3.8A distance also
- [ ] Export violations to CSV for analysis
- [ ] Check N-CA-C angle too
- [ ] Add .cif format support
- [ ] Visualize violations in PyMOL
