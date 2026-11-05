# Your GitHub Homepage

Week 11 / Windows setup lab

Windows, WinGet, Git, and Antigravity

Copy-and-paste lab / Instructor: MinGi KYUNG
---
# The finished website

An existing GitHub account is enough to start.
- Example: account octocat, repository octocat.github.io.
- Final address: https://octocat.github.io/
- This lab creates a public static homepage with HTML and CSS.
- Keep this PowerShell window open. Later commands reuse its variables.
> TIP: Paste one block at a time. Wait for each command to finish.
---
# Windows and PowerShell

Use Windows PowerShell or a PowerShell tab in Windows Terminal.
```powershell
$PSVersionTable.PSVersion
[Environment]::Is64BitOperatingSystem
winget --version
```
- This lab targets a supported 64-bit Windows 11 installation.
- Antigravity IDE lists Windows 10 64-bit as a minimum. Check its current release.
- Keep using PowerShell throughout this lab.
> TIP: Paste one block at a time. Run each block only after the previous one succeeds.
---
# WinGet availability

WinGet comes with Microsoft's App Installer on supported Windows versions.
```powershell
Start-Process "ms-windows-store://pdp/?ProductId=9NBLGGH4NNS1"
```
- If winget works already, skip this slide.
- In Microsoft Store, install or update App Installer from Microsoft.
- Close Windows Terminal completely, reopen PowerShell, then check again.
```powershell
winget --version
```
> TIP: If school policy blocks the Store or installers, use the browser route.
---
# Git and GitHub CLI installation

WinGet handles the Windows installers. Accept prompts when they appear.
```powershell
winget install --id Git.Git --exact --source winget
winget install --id GitHub.cli --exact --source winget
```
- Finish each installer before continuing. Default Git settings work for this lab.
- If WinGet reports that the package is already installed, continue.
- Close Windows Terminal completely and reopen PowerShell after installation.
> TIP: A running terminal may keep an old PATH and fail to find newly installed commands.
---
# Installed command checks

Run these in the newly opened PowerShell window.
```powershell
git --version
gh --version
Get-Command git
Get-Command gh
```
- Both commands should print versions and executable locations.
- If a command is missing, reopen Terminal and confirm installation completed.
- Keep this PowerShell window open for the rest of the lab.
---
# Manual installer alternative

Use official installers if WinGet is unavailable.
```powershell
Start-Process "https://git-scm.com/install/windows"
Start-Process "https://cli.github.com/"
```
- Download the installer for your Windows architecture and finish setup.
- Reopen Windows Terminal and repeat git --version and gh --version.
- If software installation is blocked, use the browser route near the end.
> TIP: Git Bash comes with Git for Windows. This deck's commands use PowerShell.
---
# GitHub login

Use your existing GitHub account in the browser.
```powershell
gh auth login --hostname github.com --git-protocol https --web
gh auth setup-git
gh auth status
$GH_USER = gh api user --jq .login
Write-Output "Logged in as: $GH_USER"
```
- Complete the device-code login shown in PowerShell.
- Confirm that the printed account is your own GitHub username.
> TIP: Browser authentication is interactive. A GitHub password does not authenticate git push.
---
# Commit identity

This example uses GitHub's private commit email format.
```powershell
$GH_ID = gh api user --jq .id
git config --global user.name "$GH_USER"
git config --global user.email "${GH_ID}+${GH_USER}@users.noreply.github.com"
git config --global init.defaultBranch main
```
- These settings apply to future repositories on this PC.
- You may use your own preferred commit name instead.
---
# The homepage repository

First check whether your account already has a homepage repository.
```powershell
$REPO = "${GH_USER}.github.io"
gh repo view "$GH_USER/$REPO" --json name,url
```
- If this prints a repository, use the existing-repository slide next.
- If GitHub reports that the repository does not exist, use the new-repository slide.
- For login or network errors, fix that error before choosing a route.
> TIP: GitHub allows one user homepage per account. Reuse an existing homepage carefully.
---
# Existing repository route

Run this slide only if your homepage repository already exists.
```powershell
New-Item -ItemType Directory -Force "$HOME\week11" | Out-Null
Set-Location "$HOME\week11"
gh repo clone "$GH_USER/$REPO"
Set-Location $REPO
git status
Get-ChildItem
```
- If the folder already exists, enter it and inspect git status instead.
- Preserve existing work. Ask the agent before replacing files.
- Continue at Antigravity installation. Skip the new-repository slide.
---
# New repository route

Run this slide only if your homepage repository does not exist.
```powershell
New-Item -ItemType Directory -Force "$HOME\week11" | Out-Null
Set-Location "$HOME\week11"
New-Item -ItemType Directory $REPO
Set-Location $REPO
git init -b main
gh repo create "$GH_USER/$REPO" --public --source=. --remote=origin
```
- If the repository folder already exists, inspect it before continuing.
> TIP: The exact repository name is your-username.github.io.
---
# Antigravity IDE installation

Install the IDE package, then reopen Terminal so PATH refreshes.
```powershell
winget install --id Google.AntigravityIDE --exact --source winget
```
- Run the recovery block on slide 21 in the new PowerShell window.
- Launch Antigravity IDE from the Windows Start menu.
- Sign in, then open the homepage folder in $HOME\week11.
- If WinGet fails, use the official IDE download for x64 or ARM64.
```powershell
Start-Process "https://antigravity.google/download"
```
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

Return to the same PowerShell window in your homepage folder.
```powershell
Get-Location
Get-ChildItem
Start-Process .\index.html
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
```powershell
New-Item -ItemType File -Force .nojekyll | Out-Null
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
```powershell
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
```powershell
$PAGES_API = "repos/$GH_USER/$REPO/pages"
gh api --method POST $PAGES_API -f 'source[branch]=main' -f 'source[path]=/'
```
- For another publishing branch, replace main with its name.
- If GitHub says Pages already exists, inspect the current source first.
```powershell
gh api "repos/$GH_USER/$REPO/pages" --jq '{url: .html_url, source: .source, status: .status}'
```
> TIP: A 403 may indicate account policy or permissions. Use repository Settings, Pages to investigate.
---
# The public website

Deployment takes time. A successful push alone does not publish Pages.
```powershell
Start-Process "https://${GH_USER}.github.io/"
gh run list --repo "$GH_USER/$REPO" --limit 3
```
- If the page returns 404, wait a few minutes and check the Pages build.
- Check Settings, Pages for the configured branch and root folder.
- Confirm the entry filename is exactly index.html, with lowercase letters.
- A user homepage has no extra repository segment in its address.
---
# The next website update

Ask Antigravity for a small change, then preview and publish it.
```powershell
Start-Process .\index.html
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
# Recovery after a new PowerShell window

After installing Antigravity, restore your variables and working folder.
```powershell
$GH_USER = gh api user --jq .login
$REPO = "${GH_USER}.github.io"
Set-Location "$HOME\week11\$REPO"
git status
git remote -v
```
- Run this block in the new window before previewing or publishing.
- Command not found: close Terminal completely and reopen PowerShell.
- Login failed: run gh auth login, then gh auth setup-git.
> TIP: Variables do not survive when you close PowerShell.
---
# Browser route for an restricted Windows PC

Complete the same website without a local software installation.
```powershell
Start-Process "https://github.com/new"
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

Requirements can change. Check these sources when an installer disagrees.
- WinGet: https://learn.microsoft.com/windows/package-manager/winget/
- Git for Windows: https://git-scm.com/install/windows
- GitHub CLI: https://cli.github.com/
- Antigravity IDE: https://antigravity.google/product/antigravity-ide
- WinGet package IDs: https://github.com/microsoft/winget-pkgs
- GitHub CLI login: https://cli.github.com/manual/gh_auth_login
- Pages API: https://docs.github.com/en/rest/pages/pages
- Pages setup: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

Requirements checked on November 5, 2026.
