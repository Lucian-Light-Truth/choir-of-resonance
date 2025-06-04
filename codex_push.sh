#!/bin/bash

# Codex GitHub Push Script
# Flamebearer: Zahar-Theon
# Timestamp: $(date)

echo "🔥 Initiating GitHub Codex Manifest Upload..."

# Initialize git repo
git init

# Add manifest files
git add codex_manifest.json codex_manifest.yaml README.md

# Commit changes
git commit -m '🔥 Initial Codex Manifest Commit — Shards of Remembrance'

# Set main branch
git branch -M main

# Add your GitHub repository URL here
echo "Enter your GitHub repository URL (e.g., https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git):"
read REPO_URL

# Link remote origin
git remote add origin "$REPO_URL"

# Push to GitHub
git push -u origin main

echo "✅ Codex Manifest successfully pushed to GitHub!"

