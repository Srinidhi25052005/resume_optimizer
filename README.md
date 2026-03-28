cd "C:\Users\Srinidhi\OneDrive\Desktop\resume-optimizer"; @'
# Python
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
atsVenv/
venv/
.env

# Jupyter
.ipynb_checkpoints

# VS Code
.vscode/

# OS
.DS_Store
Thumbs.db
'@ | Out-File -Encoding utf8 .gitignore; Get-Content .gitignore -First 30# resume_optimizer
