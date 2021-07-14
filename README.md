Create a new environment
```bash
conda create --n wineq python=3.7 -y

Activated the new env
```bash
conda activate wineq

create requirements.txt file
--Created from the editor.

Installed requirements.txt
```bash
pip install -r requirements.txt

Download the data from Github:
```bash
git init
```bash
dvc init
```bash
dvc add data_given/winequality.csv 
git add . 
git commit -m 'first commit'

Online updates for readme.md
```bash
git add . && git commit -m "update Readme.md"

Create an empty repository on github:
```bash
git remote add origin https://github.com/sagar61205/simple_dvc.git
git branch -M main
git push -u origin main



