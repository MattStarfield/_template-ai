# Guide: Cloning GitHub Project Repo to Local PC

This guide describes the steps to clone the GitHub project repository (repo) to your local PC. Once the project repo is cloned to your PC, you can sync your local copy with the GitHub repo to download ("pull") updates by other users, or upload ("push") updates made by you to the central repository on GitHub.<p>

## Prerequisites
### <img src="/img/assets/github_icon.png" alt="github_icon.png" width="20"> GitHub
1. The user must [register for a <img src="/img/assets/github_icon.png" alt=".jpg" width="15"> GitHub Account](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)
2. The user must be added as a **Collaborator** by the [repo owner (MattStarfield)](https://github.com/MattStarfield)<br><img src="/img/assets/github_collaborators.png" alt="github_collaborators.png" width="600">

### <img src="/img/assets/sourcetree_icon.png" alt="sourcetree_icon.png" width="20"> SourceTree

[<img src="/img/assets/sourcetree_icon.png" alt=".jpg" width="15"> SourceTree](https://www.sourcetreeapp.com/) is a free Git GUI application that provides a simple point-and-click interface for synchronizing GitHub projects with a local PC (as opposed to the standard Command Line Interface).

1. Download and Install [<img src="/img/assets/sourcetree_icon.png" alt=".jpg" width="15"> SourceTree](https://www.sourcetreeapp.com/)

### Connect <img src="/img/assets/sourcetree_icon.png" alt="sourcetree_icon.png" width="20"> SourceTree to <img src="/img/assets/github_icon.png" alt="github_icon.png" width="20"> GitHub

1. In <img src="/img/assets/sourcetree_icon.png" alt="sourcetree_icon.png" width="15"> SourceTree, go to **Tools > Options**<br><img src="/img/assets/sourcetree_options.png" alt="sourcetree_options.png" width="400">
1. In **Options**, got to **Authentication > Add**<br><img src="/img/assets/sourcetree_authentication.png" alt="sourcetree_authentication.png" width="400">
1. Hosting Service: **GitHub**<br>
Authentication: **OAuth**<br>
Click **Refresh OAuth Token**<br><img src="/img/assets/sourcetree_oauth.png" alt="sourcetree_oauth.png" width="400">
1. <img src="/img/assets/sourcetree_icon.png" alt="sourcetree_icon.png" width="15"> SourceTree will check if you're already authenticated with <img src="/img/assets/github_icon.png" alt="github_icon.png" width="15"> GitHub, and if not, it will ask you to log in. Once completed, you will see **Authentication OK**. Click **OK**<br><img src="/img/assets/sourcetree_authentication_ok.png" alt="sourcetree_authentication_ok.png" width="400">
1. Now you should see your <img src="/img/assets/github_icon.png" alt="github_icon.png" width="15"> GitHub account saved under **Accounts**<br><img src="/img/assets/sourcetree_authentication_saved.png" alt="sourcetree_authentication_saved.png" width="400">

## Clone Project Repo to PC with <img src="/img/assets/sourcetree_icon.png" alt=".jpg" width="20"> SourceTree

1. Create a new, empty folder on your PC for the project repo we will be cloning, such as<br>`C:/Git/[Project_Name]`
1. Open <img src="/img/assets/sourcetree_icon.png" alt="sourcetree_icon.png" width="15"> SourceTree and go to **File > Clone / New**<br><img src="/img/assets/sourcetree_clone_new.png" alt="sourcetree_clone_new.png" width="250">
1. Click <img src="/img/assets/sourcetree_remote_icon.png" alt="sourcetree_remote_icon.png" width="20">  **Remote**
1. Search for the project name and click **Clone**<br><img src="/img/assets/sourcetree_remote_clone.png" alt=".jpg" width="400">
1. Browse to the folder we created in step 1 (`C:/Git/[Project_Name]`) and click **Clone**<br><img src="/img/assets/sourcetree_clone.png" alt="sourcetree_clone.png" width="400">
1. <img src="/img/assets/sourcetree_icon.png" alt="sourcetree_icon.png" width="15"> SourceTree will now clone all of the project files to your PC at that location<br><img src="/img/assets/sourcetree_main_screen.png" alt="sourcetree_main_screen.png" width="600">

----
### Proceed to [**Guide: Using <img src="/img/assets/sourcetree_icon.png" alt=".jpg" width="15"> SourceTree with <img src="/img/assets/github_icon.png" alt="github_icon.png" width="15"> GitHub**](guide_using_sourcetree_with_github.md)
----
