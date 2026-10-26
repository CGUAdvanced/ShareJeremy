# Code Girls United: Advanced+ 2026 — share a change on GitHub

**Project:** Advanced+ 2026

**This class uses Windows.**

You already write a little Python. Today you will put this project on your computer, run last week's practice, add your own name file, and ask a partner to accept the change.

Do one small step. Then look at the screen. Then do the next step.

The project folder on the website is:

https://github.com/CGUAdvanced/ShareJeremy

---

## Who this is for

**You are 13 or older.** Use the GitHub account that goes with your `@codegirlsunited.org` email. If you do not have that account yet, stop and tell Jeremy.

**You are under 13.** Stop. Do not make a GitHub account. Tell Jeremy.

Jeremy will not ask for your password. Do not type a password in Chat, Classroom, or this project.

---

## Words for today

**Repo.** The project folder on GitHub, plus the history of every saved change.

**Clone.** The first download. The computer copies the project into a folder you can open.

**Branch.** Your own side copy. The class copy is named `main`. Your edit stays on your branch until a partner accepts it.

**Commit.** A check-in. You save a checkpoint and a short note about what changed.

**Push.** Upload your check-in to the GitHub website.

**Pull request.** A page on the website that says, "Please add my change to the class copy."

**Merge.** The click that accepts a pull request. A partner does this. You do not merge your own.

**Pull.** Download the newest class copy after a partner merges.

Talk in Google Chat with your Code Girls United email. Use GitHub for the code.

---

## 1. Check Git

You should already have this. If it is missing, do it now.

Git is the program that stores each check-in.

1. Click the Start button. Type `PowerShell`. Click **Windows PowerShell**.
2. A window opens. It is blue or black. A cursor blinks at the end of a line.
3. Click in that window. Type this, then press Enter:

```text
git --version
```

> You should see one line that starts with `git version`, then numbers. Example: `git version 2.47.1`

If the window says `git` is not recognized, install Git:

1. Open https://git-scm.com/download/win
2. Run the installer. Keep the choices it suggests.
3. If you see **Git from the command line and also from 3rd-party software**, leave that choice on.
4. Close PowerShell. Open it again. Type `git --version` again.

If the school computer blocks the install, stop. In Chat, tell Jeremy the step number and the exact words on the screen.

---

## 2. Check Python

You should already have this. If it is missing, do it now.

1. In the same PowerShell window, type this and press Enter:

```text
py --version
```

> You should see `Python 3` and a version number. Example: `Python 3.12.4`

If the window says `py` is not recognized:

1. Open https://www.python.org/downloads/
2. Download Python 3. Run the installer.
3. On the first screen, check the box **Add python.exe to PATH**. Then click **Install Now**.
4. Close PowerShell. Open it again. Type `py --version` again.

The word you will type later is `py`. This class runs the program with `py main.py`.

---

## 3. Check Visual Studio Code

You should already have this. If it is missing, do it now.

Visual Studio Code is the editor. The icon is blue. The name under the icon is **Visual Studio Code** or **Code**.

1. Click Start. Type `Visual Studio Code`. Click the app.
2. A big window opens.

> You should see a menu across the top: **File**, **Edit**, **Selection**, **View**, **Go**, **Run**, **Terminal**, **Help**.

If Start cannot find it:

1. Open https://code.visualstudio.com
2. Download the Windows installer. Run it.
3. If you see **Add to PATH**, leave it checked.
4. Open Visual Studio Code. Check the top menu again.

Next, add the Python helper:

1. On the far left, click the icon of four squares. The label is **Extensions**. You can also press `Ctrl+Shift+X`.
2. A search box opens at the top of that side panel. Type `Python`.
3. Click the extension named **Python**. Under the name it says **Microsoft**.
4. Click the blue **Install** button.

> When the install finishes, that button changes. It may say **Uninstall**, or it may become a gear. Either one means Python is installed.

---

## 4. Sign in to GitHub

GitHub is the website that holds the class project. This step connects Visual Studio Code to your GitHub account.

1. Press `Ctrl+Shift+P`. A box opens at the top of the window. It says you can type a command.
2. Type `Sign in to GitHub`.
3. Click the line **GitHub Pull Requests: Sign in to GitHub**. If you only see **Sign in with GitHub**, click that.
4. A browser window opens. The address bar shows `github.com`.

> If you are not signed in yet, you see a GitHub sign-in page. Sign in with the account that uses your `@codegirlsunited.org` email.

5. GitHub asks whether Visual Studio Code may use your account. Click the green **Authorize** button. The words may be **Authorize Visual Studio Code** or **Continue**.
6. The browser may say you can close the page. Go back to Visual Studio Code.
7. Look at the bottom of the far left bar. Click the person outline. That is the **Accounts** icon.

> You should see your GitHub username in that menu. That means you are signed in.

A puzzle, a school filter, or a code from email? Tell Jeremy in Chat. Do not make a second account. Do not send a password.

---

## 5. Clone the project

**Clone** means this: copy the project from GitHub onto your computer for the first time. You choose the folder. Git creates a new folder inside it and fills that folder with the files.

The address you must use is exactly this:

```text
https://github.com/CGUAdvanced/ShareJeremy
```

1. In Visual Studio Code, press `Ctrl+Shift+P` again.
2. Type `Git: Clone`. Click **Git: Clone**.
3. A box asks for the URL. Paste the address above. Press Enter.
4. A Windows folder window opens. It is asking where to put the project. Click **Documents** on the left. Then click **Select as Repository Destination**. The button might say **Select Repository Location**.

> Wait. A small note pops up at the bottom right of Visual Studio Code when the copy is done. Click **Open**.

What a finished clone looks like:

> The top of the window, or the top of the left file list, says **SHAREJEREMY**. The left list shows `main.py`, a folder named `practice`, a folder named `names`, `README.md`, and `STUDENT-GUIDE.md`.

The folder on the computer is:

```text
Documents\ShareJeremy
```

That folder is the Advanced+ 2026 project.

If you still see the welcome screen (a picture, **Start**, and **Clone Git Repository**, and no file names), the folder is not open yet.

1. Click **File**, then **Open Folder**.
2. Go to **Documents**. Click the folder **ShareJeremy**.
3. Click **Select Folder**.

> The file names listed above should appear on the left.

---

## 6. Run last week's practice, then the name list

1. At the top, click **Terminal**, then **New Terminal**.
2. A panel opens across the bottom. Click in it. The line you type on should mention `ShareJeremy`.
3. Type this and press Enter:

```text
py practice\practice_bank.py
```

> The first line should look like this: `11 categories, 38 examples.` After that you see questions. The questions change each time you run it. That means last week's code and `questions.json` are on your computer.

4. In the same terminal, type this and press Enter:

```text
py main.py
```

> You should see these lines:
>
> ```text
> Code Girls United — Advanced+ 2026
> People on this project:
> - J-Ashby — code
> 1 contributor(s)
> ```

If it says `py` is not recognized, go back to step 2. Then click **Terminal → New Terminal** and try again.

Leave `practice_bank.py`, `questions.json`, and `main.py` as they are. Today your change is a new file with your name. Do not edit someone else's file.

---

## 7. Make a branch

A **branch** is your side copy, with its own name. The class copy stays on `main` until a partner accepts your work.

Look at the blue bar along the bottom of Visual Studio Code. On the left end of that bar, you should see a small branch mark and the word `main`.

1. Click the word `main` in that blue bar.
2. A list opens at the top. Click **Create new branch...**
3. Type a branch name. Use your first name in lowercase, with hyphens. Examples: `add-name-maya` or `add-name-jordan`.
4. Press Enter.

> The blue bar now shows your branch name. It should no longer say `main`.

If it still says `main`, click that word again and click your new branch name before you type your name into the file.

---

## 8. Make your own name file

If the whole class types into one file, Git gets stuck. Two people changed the same lines. Git calls that a **conflict**. It does not know whose lines to keep. That is code contention. A shared list is the worst case, because every pull request touches the same file.

Your own new file does not touch anyone else's file. The pull requests can merge without a fight.

1. On the left, click the `names` folder so it opens.
2. You should see `j-ashby.txt`. Do not open it to edit it. That file is the example.
3. Click **File**, then **New Text File**.
4. Type two lines. Line 1 is your name. Line 2 is the part you want to work on. Use one of these words: `questions`, `front end`, `code`, or `docs`.

```text
Maya R
questions
```

Use your first name and last initial, or your GitHub username. One person only. Do not type an email, a phone number, or a home address.

5. Press `Ctrl+S`. A save window opens. On the left, open your project folder, then the `names` folder.
6. In the file name box, type your name in lowercase with a hyphen, then `.txt`. Example: `maya-r.txt`. Click **Save**.

> On the left, under `names`, you should see your new file and `j-ashby.txt`.

Do not delete `j-ashby.txt`. Do not change another girl's file. Do not add your name inside someone else's file.

---

## 9. Check in the change

**Commit** means check in. Visual Studio Code saves a checkpoint of your file and keeps the note you type.

1. On the far left, click the **Source Control** icon. It looks like a small branch: a circle with lines. It sits under the files icon. You can also press `Ctrl+Shift+G`.
2. The side panel changes.

> You should see a heading **Changes**. Under it is your new file, such as `names/maya-r.txt`.

3. Move the mouse onto your file. Click the **+** that appears. The file moves under a heading **Staged Changes**. Staged means "include this file in the check-in."
4. Click the box at the top of that panel. The hint in the box says **Message**. Type a note like this, with your own name:

```text
Add Maya R to the Advanced+ 2026 name list
```

5. Click the blue **Commit** button.

> The **Changes** list becomes empty, or a note says there is nothing left to commit. The checkpoint is now on your computer. It is not on the website yet.

If a message says Git needs your name or email before the first commit, stop and tell Jeremy. Use the email on your GitHub account. Do not invent an email.

---

## 10. Push the branch

**Push** means upload. Your branch leaves your computer and shows up on the GitHub website.

1. Stay in the Source Control panel.
2. Click **Publish Branch**. The first time, that is the button you want. If you only see **Push**, click **Push**.
3. If a browser or a small window asks you to sign in, use the same `@codegirlsunited.org` GitHub account.

Now check the website with your eyes:

1. Open the browser. Go to https://github.com/CGUAdvanced/ShareJeremy
2. You should see the name **ShareJeremy** and a green **Code** button.
3. Find the branch button near the top left of the file list. It says **main** and has a branch mark.
4. Click it. A list of branch names opens. Click your branch, such as `add-name-maya`.

> The file list reloads. Click the `names` folder, then your file. You should see your two lines on the website.

If your branch is not in that list, the push did not finish. Tell Jeremy the words Visual Studio Code showed.

---

## 11. Open a pull request on the website

A **pull request** asks the class to take your branch into `main`. You make it on the GitHub website.

1. Stay on https://github.com/CGUAdvanced/ShareJeremy
2. Look just under the top of the page. If you see a yellow bar that says **your branch had recent pushes** and a green button **Compare & pull request**, click that green button. Then skip to step 7.
3. If you do not see that yellow bar, click the **Pull requests** tab. It sits in the row with **Code**.
4. Click the green **New pull request** button.
5. Two menus appear. **base** must be `main`. **compare** must be your branch name.
6. If **compare** says `main`, click it and choose your branch. Then click **Create pull request**.
7. A form opens. Click the **title** box. Type `Add Maya R`, with your own name.
8. Click the big comment box. Write one or two sentences. Say that you added your own name file, and that you want it on `main`.
9. Click the green **Create pull request** button.

> The page changes. Your title is at the top. A label says **Open**. The address in the browser bar is the link to your pull request.

10. Copy that address. Paste it in Google Chat for your partner, so she can open it. Do not message Jeremy yet. He wants the Chat message after the code is merged.

Stop here on your own pull request. Do not click **Merge pull request**.

---

## 12. A partner merges it

Trade links with one other girl. You merge her pull request. She merges yours.

On her page:

1. Open the link she posted in Chat.
2. Click the **Files changed** tab. It is near the top of her pull request.
3. Read the green and red lines. Check every item:
   - The only new file is one file inside `names`, such as `names/maya-r.txt`
   - The file has her name, then one lane: `questions`, `front end`, `code`, or `docs`
   - She did not delete another girl's file
   - The file has no email, no phone number, and no home address
4. If every item is true, click the **Conversation** tab.
5. Click the green **Merge pull request** button.
6. A second button appears. Click **Confirm merge**.

> You should see a box that says the pull request is merged. It is often purple.

7. Open Google Chat. Sign in with your `@codegirlsunited.org` email. Open the class space Jeremy already gave you. If you cannot see it, reply on Classroom. Do not make a new space.
8. Message Jeremy there. Paste the pull request link. Say whose code you merged. Example: `Merged Maya's pull request` and the link.

That Chat message happens after the merge. Opening the pull request is not the message.

If the page says there are conflicts, stop. Do not delete her file. Message Jeremy in Google Chat and say the step number. Do not guess.

If something else looks wrong, do not merge. Write what you saw in Chat. Wait for Jeremy.

---

## 13. Pull, then run it again

Wait until your partner says `Merged`.

1. In Visual Studio Code, click your branch name in the blue bar at the bottom.
2. Click `main` in the list.

> The blue bar now says `main`.

3. Click **Terminal**, then **New Terminal**, if the bottom panel is closed.
4. Type this and press Enter:

```text
git pull
```

> You should see `Updating` or `Already up to date`. You should not see a red error.

5. Click the `names` folder. Your file should be there. Your partner's file should be there too if her pull request was merged.
6. Click in the terminal. Type this and press Enter:

```text
py main.py
```

> You should see `Code Girls United — Advanced+ 2026`, then each name and lane, then a count. The count should be higher than 1.

7. You can run the practice again:

```text
py practice\practice_bank.py
```

That is the whole loop. Clone. Run the practice. Make a branch. Add your own file. Check in. Push. Open a pull request. A partner merges and messages Jeremy in Google Chat. Pull. Run again.

---

## If you get stuck

Copy the exact words from the screen into Google Chat. Tell Jeremy the step number.

Try these once:

- Close the terminal panel. Open a new terminal. Type the command again.
- Press `Ctrl+S` on your name file before you commit.
- Look at the blue bar. It must show your branch name, not `main`, before you commit your file.
- If push says it was rejected, stop and tell Jeremy in Google Chat. Do not delete a file to force it through.

Do not post a password. Do not zip the folder and email it. Do not make a second GitHub account.

---

## Done when

- [ ] `git --version` printed a version
- [ ] `py --version` printed Python 3
- [ ] The Accounts icon shows your GitHub username
- [ ] The folder `Documents\ShareJeremy` is open, and you can see `main.py` and the `practice` folder
- [ ] `py practice\practice_bank.py` printed categories and questions
- [ ] `py main.py` printed J-Ashby before you added a file
- [ ] You added your own file in `names`, such as `names/maya-r.txt`
- [ ] The file has no email, phone number, or home address
- [ ] You committed on your branch and pushed that branch
- [ ] You opened a pull request and did not merge it yourself
- [ ] You merged a partner's pull request after you read **Files changed**
- [ ] After that merge, you messaged Jeremy in Google Chat with the link
- [ ] On `main`, `git pull` and then `py main.py` show the merged names

Code Girls United · https://codegirlsunited.org
