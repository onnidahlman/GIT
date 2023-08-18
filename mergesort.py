git config pull.rebase false
git config pull.rebase true  
git config pull.ff only

git remote add upstream https://course-gitlab.tuni.fi/git-course/basics-materials.git
git pull upstream main --allow-unrelated-histories
git push origin main

