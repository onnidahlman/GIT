git remote add upstream https://course-gitlab.tuni.fi/git-course/basics-materials.git
git pull upstream main --allow-unrelated-histories
git merge upstream/main
git add .
git commit -m "Lisää tekstin"
git push upstream main

