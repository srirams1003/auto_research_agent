0. `git checkout main` -> switch to main branch before pulling
1. `git pull` -> pull most recent changes before making your own changes
2. `git checkout -b pranav_example_branch` -> replace with your name 
3. make changes 
4. `git add .`
5. `git commit -m "meaningful commit message"`
6. `git push -u origin pranav_example_branch` -> push your new branch to the upstream
7. create a pull request from the github UI

### Miscallaneous Git commands that are good to have:

- View all git branches: `git branch -va`
- `git status`
- `git log` -> get list of commits on current branch and their history
- `git diff` -> see what changes you made between now and the latest commit on the current branch
