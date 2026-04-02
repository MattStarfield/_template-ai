# Guide: Using <img src="/img/assets/sourcetree_icon.png" alt=".jpg" width="30"> SourceTree with <img src="/img/assets/github_icon.png" alt=".jpg" width="30"> GitHub (a Git Primer)

[<img src="/img/assets/sourcetree_icon.png" alt=".jpg" width="15"> SourceTree](https://www.sourcetreeapp.com/) is a free program that provides a GUI (Graphical User Interface) for the Git version control system. Without a Git GUI application, Git must be used with a "command line interface" which can be challenging or unintuitive for some users.

Before proceeding, ensure that you have completed the steps in **[Guide: Cloning GitHub Project Repo to Local PC](docs/guide_cloning_github_project_repo_to_local_pc.md)**

<img src="/img/assets/git_workflow.jpg" alt="git_workflow.jpg" width="500">

## Fetch
The **Fetch** button checks to see if there are updates in the cloud GitHub repo that are not yet reflected on your local PC. If updates are available, the **Pull** button will indicate how many (see [Pull](#Pull))

1. Click **Fetch**<br><img src="/img/assets/sourcetree_fetch.png" alt="sourcetree_fetch.png" width="400">


## Pull

>It's best practice to **Pull** whenever the Pull Button indicates that there are updates available to keep you local copy up to date and reduce file conflicts

After clicking **Fetch**, the **Pull** button will indicate how many updates in the cloud GitHub repo are available to be downloaded to your local PC

1. Click **Pull** to **Download** updates from GitHub that have not yet been synced to your local PC<br><img src="/img/assets/sourcetree_pull.png" alt="sourcetree_pull.png" width="400">

## Commit

A **Commit** creates a project-wide "save point" on your local PC. **Commits** are the building blocks of Git's version control scheme. Each **commit** creates a snap-shot of the project at that point in time which the developer can "roll back" to if something goes wrong, or use to create a new **branch** (see [Branches](#branches)).<br>

As you're working on a project, you may be editing multiple files simultaneously (especially when coding). We're used to clicking "save" on each individual file to save our progress, but when the changes to one or more files represents a step-forward for the project as a whole, we use **commit** to collect these changes into a "project save-point" and provide a description of the changes made so that other users can understand what these changes have accomplished.<br>

A developer should perform a **commit** anytime they make a useful update to the project, or when they want to create a save point for the project. Each **commit** must be accompanied by a text description of the changes that were made. This description can be simple, but it should be *meaningful* to other developers to convey the changes that are being saved (e.g. "fixed rebooting bug", "added set up instructions to User Guide", etc.)

1. When individual project files are updated **and saved**, <img src="/img/assets/sourcetree_icon.png" alt=".jpg" width="15"> SourceTree will show that a new **Commit** is pending and the updated files will be listed in **File Status > Unstaged Files**.<br>
Clicking on a **text file** in the "Unstaged Files" list will show the changes made to the files since the last commit. Text that was deleted will be  highlighted RED and text that was added will be highlighted GREEN.<br><br>
Non-text files (e.g. image files, CAD files, etc.) also known as "binary files" cannot show line-by-line changes, so they will only indicate that they have been changed when listed in the "Unstaged Files" section.<br><br><img src="/img/assets/sourcetree_commit_files_updated.png" alt="sourcetree_commit_files_updated.png" width="800">
1. Now we need to "**stage**" the files that we want to include in this commit. This step allows us to choose which of the changed files are relevant to the "progress step" we will be describing and saving. We can click **Stage All** to include all changed files in this commit,
or click on individual files in the list and click **Stage Selected**<br><img src="/img/assets/sourcetree_commit_stage.png" alt="sourcetree_commit_stage.png" width="800">
1. Write a short description of the changes contained in this **commit**. This description should clearly convey what was updated in this commit to other developers.<br><img src="/img/assets/sourcetree_commit_description.png" alt="sourcetree_commit_description.png" width="800">
1. Click **Commit** to create the project save point on your local PC.<br>
If **Push changes immediately** is checked, this commit will also be **Pushed** to the cloud GitHub repo and be accessible to other collaborators. This is best practice to ensure that the latest updates are saved in the cloud.<br><img src="/img/assets/sourcetree_commit_push.png" alt="sourcetree_commit_push.png" width="800">
1. When all changes have been **committed**, <img src="/img/assets/sourcetree_icon.png" alt=".jpg" width="15"> SourceTree will show there is "Nothing to Commit"<img src="/img/assets/sourcetree_nothing_to_commit.png" alt="sourcetree_nothing_to_commit.png" width="800">

## Push
>If **Push changes immediately** is checked, pushes will happen automatically with each **Commit**. This is best practice.

If **Push changes immediately** is **NOT** checked (see [Commit](#commit)), **commits** will be collected and stored locally until the user **Pushes** the commits to the cloud GitHub repo.

1. Click **Push** when the button indicates that **commits** are pending<br><img src="/img/assets/sourcetree_push.png" alt="sourcetree_push.png" width="400">

## Branches
<img src="/img/assets/sourcetree_branches.png" alt="sourcetree_branches.png" width="800"><br>

**Branches** are concurrent/parallel copies of the project repo that are isolated from one another. When a **branch** is created, the developer creates a copy of the project from any previous "save point" (commit). While working within a **branch**, all changes/updates are isolated within the **branch** and do not affect other branches. If the developer chooses, they can **merge** 2 **branches** to combine the updates made in one branch with another. In this way, developers can work on the same files in parallel without interfering with one another.

> _**NOTE**_: If the same section of a file is changed in 2 branches, a **conflict** will occur when those branches are merged. This is undesirable, but fairly common. When a this occurs, a developer must decide which of the 2 versions should be kept in order to **resolve** the conflict. For this reason, merging branches is usually left to the lead developer.

>* When multiple developers are working on a project, it is often best practice to work in separate branches.
>* The **"current working branch"** will have a small circle icon next to it under **Branches** in the sidebar. In the image above, the "main" branch is selected.

### Creating a New Branch

1. **IMPORTANT**: Close the IDE and **_all project files_** before creating a new branch or switching branches! Failing to do so may cause file conflicts!
1. Click **Branch**<br><img src="/img/assets/sourcetree_branch_button.png" alt="sourcetree_branch_button.png" width="400">
1. Give the branch a descriptive name and click **Create Branch**<br><img src="/img/assets/sourcetree_create_branch.png" alt="sourcetree_create_branch.png" width="400">
1. <img src="/img/assets/sourcetree_icon.png" alt=".jpg" width="15"> SourceTree will create the new branch and mark it as the **"current working branch"**. Now all file updates will only affect this branch.<br><img src="/img/assets/sourcetree_new_branch.png" alt="sourcetree_new_branch.png" width="800">

### Switching Branches

1. **IMPORTANT**: Close the IDE and **_all project files_** before creating a new branch or switching branches! Failing to do so may cause file conflicts!
1. Double click on the branch you would like to switch to
1. <img src="/img/assets/sourcetree_icon.png" alt=".jpg" width="15"> SourceTree will show a progress bar as it updates the local versions of the project files to match the selected **branch**<br><img src="/img/assets/sourcetree_switching_branches.png" alt="sourcetree_switching_branches.png" width="400">

### Deleting a Branch

When a branch is no longer in use, it should be deleted to keep the repo "clean". A branch can be deleted after it is **merged** into another branch, or if the development path of that particular branch is no longer useful.

1. **IMPORTANT**: Close the IDE and **_all project files_** before creating a new branch or switching branches! Failing to do so may cause file conflicts!
1. Switch to a branch that is not being deleted (see **Switching Branches**)
1. Right click on the branch to be deleted and select **Delete [branch name]**<br><img src="/img/assets/sourcetree_delete_branch.png" alt="sourcetree_delete_branch.png" width="400">
