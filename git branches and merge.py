# Initialize repo
git init

# Track files
git add .

# Commit
git commit -m "Initial commit"

# Add remote
git remote add origin https://github.com/username/repo.git

# Push
git push -u origin main

# Create branch
git checkout -b feature-branch

# Merge branch
git checkout main
git merge feature-branch

#Release and Tag
git tag -a v1.0.0 -m "First release of the project"
git push origin v1.0.0
