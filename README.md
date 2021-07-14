
Create a new environment:
```
conda create --n wineq python=3.7 -y
```
Activate the new environment:
```
conda activate wineq
```
Create requirements.txt file
```
touch requirements.txt
```
Installed requirements.txt
```
pip install -r requirements.txt

```
Download the data(winequality.csv) from Github:
https://drive.google.com/drive/folders/1xw0XX-WK74uxtFFLySbtnX-ODdmdK5Ec/
```bash
git init
```
```bash
dvc init
```
```bash
dvc add data_given/winequality.csv 
git add . 
git commit -m 'first commit'
```
Online updates for 'readme.md':
```
git add . && git commit -m "update Readme.md"
```
Create an empty repository on github:
```
git remote add origin https://github.com/sagar61205/simple_dvc.git
git branch -M main
git push -u origin main
