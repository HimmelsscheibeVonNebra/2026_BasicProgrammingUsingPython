# Your GitHub Homepage

Week 11 / Setup recovery lab

Intel Mac, Homebrew, Git, and Antigravity

Copy-and-paste lab / Instructor: MinGi KYUNG
---
# The finished website

An existing GitHub account is enough to start.
- Example: account octocat, repository octocat.github.io.
- Final address: https://octocat.github.io/
- This lab creates a public static homepage with HTML and CSS.
- Keep this Terminal window open. Later commands reuse its variables.
> TIP: Paste one block at a time. Wait for each command to finish.
---
# Mac compatibility check

Intel hardware and an old macOS version are separate issues.
```bash
uname -m
sw_vers -productVersion
```
- Intel should print x86_64. Apple Silicon usually prints arm64.
- Homebrew currently classifies Intel Macs as Tier 3. Installs may fail.
- Antigravity requirements depend on the downloaded product and release.
> TIP: If macOS or an installer blocks you, use the browser route near the end.
---
# Apple command line tools

Run this in Terminal, then finish the Apple installer dialog.
```bash
xcode-select --install
```
- If the tools are already installed, continue.
- Wait for the installation to finish before running the next block.
```bash
xcode-select -p
/usr/bin/git --version
```
> TIP: An unavailable tools package may require a supported macOS update. Ask the instructor.
---
# Homebrew installation

The installer may ask for your Mac login password and Return.
```bash
curl -fsSL https://raw.githubusercontent.com/\
Homebrew/install/HEAD/install.sh -o /tmp/install-brew.sh
/bin/bash /tmp/install-brew.sh
```
- Password characters stay invisible while you type. Press Return.
- Keep the backslash and newline when copying this block.
- If Homebrew reports an unsupported system or fails, stop this route.
> TIP: Use the browser route instead of repeatedly reinstalling Homebrew.
---
# Homebrew on an Intel Mac

A standard Intel installation uses /usr/local.
```bash
eval "$(/usr/local/bin/brew shellenv)"
grep -qxF 'eval "$(/usr/local/bin/brew shellenv)"' \
  ~/.zprofile 2>/dev/null || \
  echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
brew --version
brew --prefix
```
- The prefix should be /usr/local. Use zsh for this lab.
- On Apple Silicon, use the installer's own Next steps instead.
> TIP: If /usr/local/bin/brew is missing, return to the installer output.
---
# Git and GitHub CLI

Git tracks files. GitHub CLI handles login and repository setup.
```bash
brew install git gh
rehash
command -v git
git --version
gh --version
```
- The Homebrew Git path normally starts with /usr/local/.
- Source builds on an old Mac may take a long time or fail.
> TIP: Apple Git can work without Homebrew. If gh cannot install, use the browser route.
---
# GitHub login

Use your existing GitHub account in the browser.
```bash
gh auth login --hostname github.com --git-protocol https --web
gh auth setup-git
gh auth status
GH_USER=$(gh api user --jq .login)
printf 'Logged in as: %s\n' "$GH_USER"
```
- Complete the device-code login shown in Terminal.
- Confirm that the printed account is your own GitHub username.
> TIP: Browser authentication is interactive. A GitHub password does not authenticate git push.
---
# Commit identity

This example uses GitHub's private commit email format.
```bash
GH_ID=$(gh api user --jq .id)
git config --global user.name "$GH_USER"
git config --global user.email \
  "${GH_ID}+${GH_USER}@users.noreply.github.com"
git config --global init.defaultBranch main
```
- These settings apply to future repositories on this Mac.
- You may use your own preferred commit name instead.
---
# The homepage repository

First check whether your account already has a homepage repository.
```bash
REPO="${GH_USER}.github.io"
gh repo view "$GH_USER/$REPO" --json name,url
```
- If this prints a repository, use the existing-repository slide next.
- If GitHub reports that the repository does not exist, use the new-repository slide.
- For login or network errors, fix that error before choosing a route.
> TIP: GitHub allows one user homepage per account. Reuse an existing homepage carefully.
---
# Existing repository route

Run this slide only if your homepage repository already exists.
```bash
mkdir -p ~/Documents/week11
cd ~/Documents/week11
gh repo clone "$GH_USER/$REPO"
cd "$REPO"
git status
ls
```
- If the folder already exists, enter it and inspect git status instead.
- Keep existing work. Ask Antigravity to update the homepage without deleting files.
- Continue at Antigravity installation. Skip the new-repository slide.
---
# New repository route

Run this slide only if your homepage repository does not exist.
```bash
mkdir -p ~/Documents/week11
cd ~/Documents/week11
mkdir "$REPO"
cd "$REPO"
git init -b main
gh repo create "$GH_USER/$REPO" --public \
  --source=. --remote=origin
```
- If mkdir reports an existing folder, inspect it before continuing.
> TIP: The exact repository name is your-username.github.io.
---
# Antigravity installation

The IDE cask requires macOS 12 or later. Check the current release too.
```bash
brew install --cask antigravity-ide
open -a "Antigravity IDE" .
```
- Finish the Google sign-in prompts with an existing eligible Google account.
- If the folder does not open, choose Open Folder and select this repository.
- If the cask fails, open the official download page, find Antigravity IDE, and choose Intel.
```bash
open https://antigravity.google/download
```
> TIP: Check the requirements for that download. An unsupported Mac needs the browser route.
---
# The Antigravity prompt

Paste this into the Antigravity agent chat with your repository open.
```text
Create a student homepage in this repository.
Use index.html and style.css, with no build tools.
Include About Me, My Python Project, and Contact.
Use sample text and no real personal information.
Make it readable on phones and keyboard accessible.
Use relative paths. Create .nojekyll at the root.
Preserve existing files and explain any replacements.
Do not commit, push, or change repository settings.
Tell me how to preview it by opening index.html.
```
- Review proposed edits. Let the agent create the files.
---
# Local preview

Return to the same Terminal window in your homepage folder.
```bash
pwd
ls
open index.html
git status --short
git diff --stat
```
- Check the title, navigation, project text, and a narrow browser window.
- git diff shows changes to tracked files. Open new files in the editor too.
- Only publish text and images you want everyone to see.
> TIP: Missing index.html? Ask Antigravity to put it at the repository root.
---
# The first website commit

Stage only the files you reviewed.
```bash
touch .nojekyll
git add index.html style.css .nojekyll
git diff --cached --stat
git commit -m "Create student homepage"
git branch --show-current
```
- If your agent created another CSS filename, adjust the git add command.
- For a new repository, the branch should be main.
- For an existing repository, use its actual publishing branch below.
---
# Upload to GitHub

Run this block when your current branch is main.
```bash
git push -u origin main
gh repo view --web
```
- Check that index.html appears at the repository root on GitHub.
- If an existing repository uses another branch, substitute that branch.
- If push is rejected, inspect the remote history with the instructor.
> TIP: Avoid force push. Preserve any existing homepage commits.
---
# GitHub Pages activation

For a new Pages site, publish the root of the main branch.
```bash
gh api --method POST "repos/$GH_USER/$REPO/pages" \
  -f 'source[branch]=main' -f 'source[path]=/'
```
- For another publishing branch, replace main with its name.
- If GitHub says Pages already exists, inspect the current source first.
```bash
gh api "repos/$GH_USER/$REPO/pages" \
  --jq '{url: .html_url, source: .source, status: .status}'
```
> TIP: A 403 may indicate account policy or permissions. Use repository Settings, Pages to investigate.
---
# The public website

Deployment takes time. A successful push alone does not publish Pages.
```bash
open "https://${GH_USER}.github.io/"
gh run list --repo "$GH_USER/$REPO" --limit 3
```
- If the page returns 404, wait a few minutes and check the Pages build.
- Check Settings, Pages for the configured branch and root folder.
- Confirm the entry filename is exactly index.html, with lowercase letters.
- A user homepage has no extra repository segment in its address.
---
# The next website update

Ask Antigravity for a small change, then preview and publish it.
```bash
open index.html
git status --short
git diff
git add index.html style.css
git diff --cached
git commit -m "Update project description"
git push
```
- Review new files separately and add them explicitly if needed.
- Pages rebuilds after a push to the configured publishing branch.
---
# Recovery after a new Terminal window

Variables from the old window do not survive automatically.
```bash
GH_USER=$(gh api user --jq .login)
REPO="${GH_USER}.github.io"
cd "$HOME/Documents/week11/$REPO"
git status
git remote -v
```
- brew: command not found: rerun the Intel shellenv command.
- Authentication failed: run gh auth login, then gh auth setup-git.
- Antigravity cannot start: use the browser route on the next slide.
---
# Browser route for an unsupported Mac

Complete the same website without a local Homebrew installation.
```bash
open https://github.com/new
```
- Sign in. Create a public repository named your-username.github.io.
- If it already exists, open that repository instead.
- Choose Add file, Create new file. Name the file index.html.
- Paste the starter on the next slide and commit to main.
- Create an empty .nojekyll file with the same workflow.
> TIP: If Antigravity runs elsewhere, paste its generated HTML here. Otherwise use the supplied starter.
---
# Browser starter: index.html

This single file works without a build step or a separate stylesheet.
```text
<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>My Student Homepage</title>
<body><h1>My Student Homepage</h1>
<h2>About Me</h2><p>I am learning Python.</p>
<h2>My Python Project</h2><p>A study time logger.</p>
<h2>Contact</h2><p>Find my projects on GitHub.</p></body></html>
```
- Replace the sample text before publishing if you wish.
---
# Browser publishing and submission

In the repository, open Settings, Pages.
- Under Build and deployment, choose Deploy from a branch.
- Select main and / (root), then Save.
- Wait for the build. Open https://your-username.github.io/.
- Submit your website URL and repository URL.
- Explain one change you made to the generated page.
> CHECK: Both the local and browser routes finish at the same public website.
---
# Official references

Requirements can change. Check these pages when an installer disagrees.
- Homebrew installation: https://docs.brew.sh/Installation
- Homebrew support: https://docs.brew.sh/Support-Tiers
- Antigravity IDE: https://formulae.brew.sh/cask/antigravity-ide
- Antigravity downloads: https://antigravity.google/download
- GitHub CLI login: https://cli.github.com/manual/gh_auth_login
- Repository creation: https://cli.github.com/manual/gh_repo_create
- Pages API: https://docs.github.com/en/rest/pages/pages
- Pages setup: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

Requirements checked on November 5, 2026.
