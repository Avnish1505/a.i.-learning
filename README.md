# a.i.-learning

Short notes, notebooks and small programs focused on NumPy, pandas, and beginner AI/ML projects.  
Maintained by Avnish (Avnish1505) as a learning portfolio.

## Goal
Build a strong foundation in data handling and basic ML, then move to deep learning and deployment. Weekly practice, clear commits, and small projects that you can demo.

## Repo structure
- data/        : sample datasets or links (do not push large files)
- notebooks/   : Jupyter/Colab notebooks (one per project)
- scripts/     : reusable Python scripts and utility functions
- models/      : saved model artifacts (or links)
- utils/       : helper modules (e.g., data_loader.py)
- requirements.txt
- README.md

## How to run (local)
1. Clone:
```bash
git clone https://github.com/Avnish1505/a.i.-learning.git
cd a.i.-learning
```
2. Create venv and install:
```bash
python -m venv venv
# mac/linux
source venv/bin/activate
# windows (PowerShell)
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
```
3. Open notebooks:
```bash
jupyter notebook
# or use Google Colab (recommended for quick GPU access)
```

## Best practices for this repo
- Keep notebooks runnable from top to bottom.
- Add a short summary at top: problem, dataset, steps, results.
- Save heavy processed files as parquet and store links in data/README.md instead of pushing large files.
- Use branches: feature/<name> and descriptive commits: "feat: titanic EDA notebook".

## Example checklist for each notebook
- Problem statement (1–2 lines)
- Dataset source (link)
- Cleaning steps done
- Feature engineering done
- Modeling (if any) and metrics
- How to reproduce (Colab link or commands)

## Recommended workflow
- Work on a branch: git checkout -b feature/titanic-cleaning
- Commit often with clear messages
- Open a pull request for larger changes so you can review later

## Resources (start here)
- NumPy & pandas docs
- 3Blue1Brown (math intuition)
- StatQuest (statistics)
- Hugging Face (later, for NLP)
- fast.ai / PyTorch tutorials

## Contact
GitHub: https://github.com/Avnish1505  
If you want, I can add a sample notebook, requirements.txt, and a Colab link to this repo — bol do and I'll push a branch with files.
