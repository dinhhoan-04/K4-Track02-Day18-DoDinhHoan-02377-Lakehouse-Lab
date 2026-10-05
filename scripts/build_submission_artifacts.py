"""Generate all 8 executed Jupyter notebooks with rich outputs for submission.

Converts notebooks/*.py (jupytext) to .ipynb, executes them sequentially using
nbclient in notebooks/ directory, and writes the output .ipynb files to submission/notebooks/.
"""
import sys
import os
from pathlib import Path
import jupytext
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NB_DIR = ROOT / "notebooks"
SUBMISSION_NB_DIR = ROOT / "submission" / "notebooks"
SUBMISSION_NB_DIR.mkdir(parents=True, exist_ok=True)

py_files = sorted(p for p in NB_DIR.glob("[0-9]*.py") if not p.name.startswith("_"))
print(f"Found {len(py_files)} notebooks to build:")
for p in py_files:
    print(f" - {p.name}")

# Change CWD to notebooks directory so file-relative imports work as expected
os.chdir(NB_DIR)

for py_file in py_files:
    ipynb_filename = py_file.stem + ".ipynb"
    target_path = SUBMISSION_NB_DIR / ipynb_filename
    print(f"\nProcessing {py_file.name} -> submission/notebooks/{ipynb_filename}...")
    
    nb = jupytext.read(py_file.name)
    client = NotebookClient(nb, timeout=600, kernel_name='python3')
    
    try:
        client.execute()
        print(f"  ✓ Execution succeeded ({len(nb.cells)} cells)")
    except Exception as e:
        print(f"  ❌ Execution failed: {e}")
        sys.exit(1)
        
    with open(target_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
    print(f"  ✓ Saved to {target_path}")

print("\n🎉 All 8 notebooks executed and saved successfully to submission/notebooks/")
