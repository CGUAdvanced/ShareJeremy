# Code Girls United: Advanced+ 2026 — share a change on GitHub

**Project:** Advanced+ 2026
**GitHub:** [https://github.com/CGUAdvanced/ShareJeremy](https://github.com/CGUAdvanced/ShareJeremy)

You already write Python. Today you practice how a team shares code.

You will install **Visual Studio Code**, connect it to **GitHub**, copy this project onto your computer, **run** it, add your name, **check in** that change, and open a **pull request**. A partner merges your pull request. You download their merge and run the program again.

Do the steps in order. Check the box when a step works.

---

## Who this is for

| If you are | What you do |
| --- | --- |
| **13 or older** | Use the GitHub account you already made with your `@codegirlsunited.org` email. If you do not have it yet, stop and tell Jeremy. |
| **Under 13** | **Stop.** Do not create a GitHub account. Tell Jeremy on Classroom. |

Jeremy will never ask for your password. Do not put a password in Chat, Classroom, or this repo.

---

## The path, in one look

1. Install Git, Python, and Visual Studio Code.
2. Sign in to GitHub.
3. Clone the project (this puts it on your computer).
4. Run `main.py`.
5. Make a branch and add your name to `CONTRIBUTORS.md`.
6. Commit (that is the check-in) and push.
7. Open a pull request.
8. A partner merges it. You do not merge your own.
9. Pull the updated project and run it again. Your name should print.

---

## Words

| Word | What it means here |
| --- | --- |
| **Repo** | This project folder, plus the history of every check-in |
| **Clone** | Download the repo to your computer the first time |
| **Pull** | Download new check-ins that landed after your clone |
| **Branch** | Your own side path, so `main` stays stable while you work |
| **Commit / check in** | Save a checkpoint, with a short message about why |
| **Push** | Upload your commits to GitHub |
| **Pull request** | Ask the class to take your branch into `main` |
| **Merge** | Accept that pull request. A **partner** does this, not you |

Talk about the work in **Google Chat** with your Code Girls United email. GitHub is for the code and the pull request.

---

## 1. Install Git

Git is the program that check-ins use. Visual Studio Code does not include it.

1. Open [https://git-scm.com/download/win](https://git-scm.com/download/win).
2. Run the installer. Keep the default options. Leave **Git from the command line and also from 3rd-party software** selected if you see it.
3. Close any old Terminal window. Open a new **PowerShell** or **Command Prompt** and run:

```text
git --version
```

You want a line that starts with `git version`.

**Mac:** install Git from [https://git-scm.com/download/mac](https://git-scm.com/download/mac), then run `git --version` in Terminal.

If the school computer will not install Git, stop and tell Jeremy in Chat. Say the exact message on the screen.

---

## 2. Install Python

1. Open [https://www.python.org/downloads/](https://www.python.org/downloads/) on the computer you will use in class.
2. Download Python 3 and run the installer.
3. On the first screen, check **Add python.exe to PATH** if you see that box. Then install.
4. Close the old terminal. Open a new one and run:

```text
py --version
```

You want `Python 3` and a version number. If `py` is not found, try `python --version`. On a Mac, try `python3 --version`. Remember which word worked. You will type that same word later.

---

## 3. Install Visual Studio Code

1. Open [https://code.visualstudio.com](https://code.visualstudio.com).
2. Download the **Windows** installer (Mac: the Mac download). Run it.
3. Leave **Add to PATH** checked if you see it.
4. Open **Visual Studio Code**. The icon is blue. The installer name includes the word **Code**.

When it is open:

1. Open **Extensions** (left bar, or `Ctrl+Shift+X`).
2. Install **Python** (publisher: **Microsoft**).

---

## 4. Sign in to GitHub

1. In Visual Studio Code, open **Extensions** and install **GitHub Pull Requests** (publisher: **GitHub**).
2. Click the **Accounts** icon at the bottom of the left side (a person outline).
3. Choose **Sign in with GitHub**.
4. A browser page opens. Sign in with your `@codegirlsunited.org` GitHub account.
5. Approve the access request and return to Visual Studio Code.

You are signed in when the Accounts menu shows your GitHub username.

Stuck on a captcha, a school filter, or a second-factor code? Tell Jeremy in Chat. Do not make a second account.

---

## 5. Clone the project onto your computer

**Clone** is the first download. **Pull** comes later, after someone else has merged.

1. Press `Ctrl+Shift+P` (`Cmd+Shift+P` on a Mac). This opens the Command Palette.
2. Type `Git: Clone` and press Enter.
3. Paste this URL and press Enter:

```text
https://github.com/CGUAdvanced/ShareJeremy
```

4. Choose a folder you can find again, such as `Documents`.
5. When Visual Studio Code asks if you want to open the cloned repository, click **Open**.

You should see these files in the Explorer:

- `README.md`
- `STUDENT-GUIDE.md`
- `CONTRIBUTORS.md`
- `main.py`

The folder on your computer is named `ShareJeremy`. That folder is the Advanced+ 2026 project.

---

## 6. Run the program

1. In Visual Studio Code, choose **Terminal → New Terminal**.
2. Run the word that worked in step 2:

```text
py main.py
```

Use `python main.py` or `python3 main.py` if that is the word that printed a Python 3 version.

You should see J-Ashby's name and a count:

```text
Code Girls United — Advanced+ 2026
People on this project:
- J-Ashby
1 contributor(s)
```

Leave `main.py` as it is today. Your change is your name on the list, not a rewrite of the program.

---

## 7. Make a branch and add your name

A **branch** keeps your edit off `main` until a partner accepts it.

1. Click the branch name in the **bottom-left** status bar. It says `main`.
2. Choose **Create new branch…**
3. Name it with your first name, lowercase, and hyphens. Examples: `add-name-maya`, `add-name-jordan-t`.
4. Press Enter. The status bar should now show your branch name.

Then edit the list:

1. Open `CONTRIBUTORS.md`.
2. Go to the bottom of the **Names** list.
3. Add **one** new line, in the same shape as the line that is already there:

```text
- Maya R
```

Use your real first name and last initial, or your GitHub username. No email. No phone. No home address.

4. Save the file (`Ctrl+S`).

Do not delete `- J-Ashby`. Do not change anyone else's line. Do not add a second person on your pull request.

---

## 8. Check in the change and push it

**Check in** means **commit**: a saved checkpoint with a message.

1. Click the **Source Control** icon on the left (it looks like a branch). Or press `Ctrl+Shift+G`.
2. `CONTRIBUTORS.md` should appear under **Changes**.
3. Click the **+** next to that file. It moves to **Staged Changes**.
4. In the message box, write what you did and why. Example:

```text
Add Maya R to the Advanced+ 2026 contributors list
```

5. Click **Commit**.
6. Click **Publish Branch** or **Push**. Use your GitHub account if a browser window asks you to sign in. This is the same account as step 4.

The check-in is on GitHub when your branch shows on the website. Open [https://github.com/CGUAdvanced/ShareJeremy](https://github.com/CGUAdvanced/ShareJeremy) and look for your branch.

If Git says it needs your name or email before the first commit, tell Jeremy. Use the email on your GitHub account. Do not invent one.

---

## 9. Open a pull request

A pull request asks the class to take your branch into `main`.

1. On the GitHub website, open the project.
2. If you see a yellow banner that says **Compare & pull request**, click it.
3. If you do not see that banner: open the **Pull requests** tab → **New pull request**. Set **base: main** and **compare: your branch**.
4. Title: `Add Maya R to contributors` (use your own name).
5. In the comment box, write one or two sentences. What you changed, and that you want it on `main`.
6. Click **Create pull request**.
7. Copy the pull request link into Google Chat and tag your partner.

**Stop.** Do not click **Merge**.

---

## 10. A partner merges your pull request

Trade links with one other girl. You merge **her** pull request. She merges **yours**.

On **her** pull request:

1. Open the link she posted.
2. Open the **Files changed** tab.
3. Check all of these before you merge:
   - The only file is `CONTRIBUTORS.md`
   - She added one line, at the bottom
   - Nobody else's name was deleted
   - The line has no email, phone number, or address
4. If that is all true: open **Conversation** → **Merge pull request** → **Confirm merge**.
5. Reply in Chat: `Merged` and her link.

If the page says there are **conflicts**, do not guess and do not delete her name. Tell her and Jeremy. She updates her branch so **both** names stay, pushes again, and then you merge.

If something else looks wrong, do not merge. Write what you saw in Chat and wait for Jeremy.

---

## 11. Pull and run again

After your partner says `Merged`:

1. In Visual Studio Code, click your branch name in the bottom-left status bar.
2. Choose `main`.
3. Open the Terminal and run:

```text
git pull
```

4. Open `CONTRIBUTORS.md`. Your line should be there, and so should your partner's line if her pull request was merged too.
5. Run the program again:

```text
py main.py
```

The count should be higher than 1, and the new names should print.

That is the whole loop: clone, run, branch, check in, pull request, someone else merges, pull, run.

---

## If you get stuck

Copy the **exact** error into Google Chat to Jeremy. Also say which step number you are on.

Useful things to try once:

- Close the terminal, open a new one, and run the command again.
- Save `CONTRIBUTORS.md` before you commit.
- Make sure the status bar shows **your** branch, not `main`, before you commit your name.
- If push is rejected because `main` moved, run `git pull`, keep **every** name in `CONTRIBUTORS.md`, commit, and push again.

Do not post a password. Do not zip the folder and email it. Do not make a second GitHub account.

---

## Done when

- [ ] `git --version` prints a version
- [ ] `py --version` (or `python --version`) prints Python 3
- [ ] Visual Studio Code is signed in to your GitHub account
- [ ] You cloned `https://github.com/CGUAdvanced/ShareJeremy`
- [ ] `py main.py` printed the contributor list **before** you edited
- [ ] Your name is one new line at the bottom of `CONTRIBUTORS.md`
- [ ] You committed on a branch and pushed that branch
- [ ] You opened a pull request and did **not** merge it yourself
- [ ] You merged a partner's pull request after you read the file change
- [ ] On `main`, `git pull` then `py main.py` shows the merged names
