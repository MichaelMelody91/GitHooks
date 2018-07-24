# GitHooks

A collection of Git hooks which can be used to prevent common mistakes when worknig with source control.

Hooks currently implemented:

* pre-commit (Used to inspect the snapshot that is about to be committed)
* commit-msg (Used to inspect a commit message and enforce good practice) 

## Prerequisites

* Git
* Notepad++ (for further development of hooks)

## Installing

* For an existing repo, copy the hook(s) into the __{REPOSITORY_DIR}\.git\hooks__ directory
* For global installation for all current and future repositories:

      git config --global core.hooksPath /path/to/my/centralized/hooks

## Usage

### pre-commit 

Prevents a commit in 2 scenarios

* When attempting to commit directly to develop or master
* When attempting to commit to a branch which is not up to date with its remote

Can be bypassed with:

    git commit --no-verify

### commit-msg

Prevents a commit if the commit message doesn't match the following standards

* The message should contain asubject and a body
* Subject seperated from the body with a blank line
* The subject line between 10-72 characters
* The subject line should be capitalized

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgements 

* http://www.chris.com/ascii/ 
* https://chris.beams.io/posts/git-commit/
