git remote add upstream https://course-gitlab.tuni.fi/git-course/basics-materials.git
git config pull.rebase false
git pull upstream main --allow-unrelated-histories
git push origin main

