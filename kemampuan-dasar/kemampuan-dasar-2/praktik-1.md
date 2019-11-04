STEP 1

root@rindha:~/Documents# git clone https://github.com/rindhaf/coba-rhymes.git
Cloning into 'coba-rhymes'...
warning: You appear to have cloned an empty repository.
root@rindha:~/Documents# mkdir rhymes
root@rindha:~/Documents# cd rhymes
root@rindha:~/Documents/rhymes# git init
Initialized empty Git repository in /root/Documents/rhymes/.git/
root@rindha:~/Documents/rhymes# touch README.txt
root@rindha:~/Documents/rhymes# git add README.txt
root@rindha:~/Documents/rhymes# git commit -m "First commit"
[master (root-commit) ffa0e7b] First commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.txt
root@rindha:~/Documents/coba-rhymes# echo 'This repo is a collection of my favorite nursery rhymes.' >> README.txt
root@rindha:~/Documents/coba-rhymes# git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	README.txt

nothing added to commit but untracked files present (use "git add" to track)
root@rindha:~/Documents/coba-rhymes# git diff
root@rindha:~/Documents/coba-rhymes# git add README.txt
root@rindha:~/Documents/coba-rhymes# git commit -m 'Added project overview to README.txt'
[master (root-commit) df2a871] Added project overview to README.txt
 1 file changed, 1 insertion(+)
 create mode 100644 README.txt
root@rindha:~/Documents/coba-rhymes# wget https://www.acquia.com/sites/default/files/blog/all-around-the-mulberry-bush.txt
--2019-11-04 14:06:32--  https://www.acquia.com/sites/default/files/blog/all-around-the-mulberry-bush.txt
Resolving www.acquia.com (www.acquia.com)... 104.16.117.45, 104.16.118.45, 2606:4700::6810:762d, ...
Connecting to www.acquia.com (www.acquia.com)|104.16.117.45|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2019-11-04 14:06:35 ERROR 404: Not Found.

root@rindha:~/Documents/coba-rhymes# wget https://www.acquia.com/sites/default/files/blog/jack-and-jill.txt
--2019-11-04 14:06:53--  https://www.acquia.com/sites/default/files/blog/jack-and-jill.txt
Resolving www.acquia.com (www.acquia.com)... 104.16.118.45, 104.16.117.45, 2606:4700::6810:752d, ...
Connecting to www.acquia.com (www.acquia.com)|104.16.118.45|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2019-11-04 14:06:59 ERROR 404: Not Found.

root@rindha:~/Documents/coba-rhymes# wget https://www.acquia.com/sites/default/files/blog/old-mother-hubbard.txt
--2019-11-04 14:06:59--  https://www.acquia.com/sites/default/files/blog/old-mother-hubbard.txt
Resolving www.acquia.com (www.acquia.com)... 104.16.117.45, 104.16.118.45, 2606:4700::6810:762d, ...
Connecting to www.acquia.com (www.acquia.com)|104.16.117.45|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2019-11-04 14:07:03 ERROR 404: Not Found.

root@rindha:~/Documents/coba-rhymes# wget https://www.acquia.com/sites/default/files/blog/twinkle-twinkle.txt
--2019-11-04 14:07:03--  https://www.acquia.com/sites/default/files/blog/twinkle-twinkle.txt
Resolving www.acquia.com (www.acquia.com)... 104.16.118.45, 104.16.117.45, 2606:4700::6810:752d, ...
Connecting to www.acquia.com (www.acquia.com)|104.16.118.45|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2019-11-04 14:07:06 ERROR 404: Not Found.

root@rindha:~/Documents/coba-rhymes# wget https://www.acquia.com/sites/default/files/blog/hokey-pokey.txt
--2019-11-04 14:07:27--  https://www.acquia.com/sites/default/files/blog/hokey-pokey.txt
Resolving www.acquia.com (www.acquia.com)... 104.16.117.45, 104.16.118.45, 2606:4700::6810:762d, ...
Connecting to www.acquia.com (www.acquia.com)|104.16.117.45|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2019-11-04 14:07:29 ERROR 404: Not Found.

root@rindha:~/Documents/coba-rhymes# git add all-around-the-mulberry-bush.txt
fatal: pathspec 'all-around-the-mulberry-bush.txt' did not match any files
root@rindha:~/Documents/coba-rhymes# git status
On branch master
Your branch is based on 'origin/master', but the upstream is gone.
  (use "git branch --unset-upstream" to fixup)

nothing to commit, working tree clean
root@rindha:~/Documents/coba-rhymes# git commit -m 'Added all-around-the-mulberry-bush.txt'
On branch master
Your branch is based on 'origin/master', but the upstream is gone.
  (use "git branch --unset-upstream" to fixup)

nothing to commit, working tree clean
root@rindha:~/Documents/coba-rhymes# git add jack-and-jill.txt
fatal: pathspec 'jack-and-jill.txt' did not match any files
root@rindha:~/Documents/coba-rhymes# git commit -m 'Added jack-and-jill.txt.'
On branch master
Your branch is based on 'origin/master', but the upstream is gone.
  (use "git branch --unset-upstream" to fixup)

nothing to commit, working tree clean
root@rindha:~/Documents/coba-rhymes# git add .
root@rindha:~/Documents/coba-rhymes# git commit -m 'Added old-mother-hubbard.txt, twinkle-twinkle.txt, hokey-pokey.txt'
On branch master
Your branch is based on 'origin/master', but the upstream is gone.
  (use "git branch --unset-upstream" to fixup)

nothing to commit, working tree clean
root@rindha:~/Documents/coba-rhymes# git log
commit df2a871331014aca4db6e98f4ea2d7418c99a17f (HEAD -> master)
Author: rindhaf <rindhafajirul@hmail.com>
Date:   Mon Nov 4 14:06:12 2019 +0700

    Added project overview to README.txt
root@rindha:~/Documents/coba-rhymes# git log --oneline
df2a871 (HEAD -> master) Added project overview to README.txt
root@rindha:~/Documents/coba-rhymes# git log -p
commit df2a871331014aca4db6e98f4ea2d7418c99a17f (HEAD -> master)
Author: rindhaf <rindhafajirul@hmail.com>
Date:   Mon Nov 4 14:06:12 2019 +0700

    Added project overview to README.txt

diff --git a/README.txt b/README.txt
new file mode 100644
index 0000000..c83e022
--- /dev/null
+++ b/README.txt
@@ -0,0 +1 @@
+This repo is a collection of my favorite nursery rhymes.
root@rindha:~/Documents/coba-rhymes# git remote add origin https://github.com/rindhaf/coba-rhymes.git
fatal: remote origin already exists.
root@rindha:~/Documents/coba-rhymes# git push -u origin master
Username for 'https://github.com': rindhaf
Password for 'https://rindhaf@github.com': 
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 290 bytes | 290.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/rindhaf/coba-rhymes.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
root@rindha:~/Documents/coba-rhymes# 


STEP 2
root@rindha:~/Documents/coba-rhymes# git checkout -b hickory-dickory
Switched to a new branch 'hickory-dickory'
root@rindha:~/Documents/coba-rhymes# wget https://www.acquia.com/sites/default/files/blog/hickory-dickory-dock.txt...
--2019-11-04 14:17:19--  https://www.acquia.com/sites/default/files/blog/hickory-dickory-dock.txt...
Resolving www.acquia.com (www.acquia.com)... 104.16.118.45, 104.16.117.45, 2606:4700::6810:752d, ...
Connecting to www.acquia.com (www.acquia.com)|104.16.118.45|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2019-11-04 14:17:22 ERROR 404: Not Found.

root@rindha:~/Documents/coba-rhymes# add hickory-dickory-dock.txt
bash: add: command not found
root@rindha:~/Documents/coba-rhymes# git commit -m 'Added hickory-dickory-dock.txt.'
On branch hickory-dickory
nothing to commit, working tree clean
root@rindha:~/Documents/coba-rhymes# git push origin hickory-dickory
Username for 'https://github.com': rindhaf
Password for 'https://rindhaf@github.com': 
Total 0 (delta 0), reused 0 (delta 0)
remote: 
remote: Create a pull request for 'hickory-dickory' on GitHub by visiting:
remote:      https://github.com/rindhaf/coba-rhymes/pull/new/hickory-dickory
remote: 
To https://github.com/rindhaf/coba-rhymes.git
 * [new branch]      hickory-dickory -> hickory-dickory
root@rindha:~/Documents/coba-rhymes# 

STEP 3
root@rindha:~/Documents/coba-rhymes# git remote rename origin alice
root@rindha:~/Documents/coba-rhymes# git remote add bob https://github.com/rindhaf/coba-rhymes.git
root@rindha:~/Documents/coba-rhymes# git remote
alice
bob
root@rindha:~/Documents/coba-rhymes# git remote -v
alice	https://github.com/rindhaf/coba-rhymes.git (fetch)
alice	https://github.com/rindhaf/coba-rhymes.git (push)
bob	https://github.com/rindhaf/coba-rhymes.git (fetch)
bob	https://github.com/rindhaf/coba-rhymes.git (push)
root@rindha:~/Documents/coba-rhymes# git fetch bob
From https://github.com/rindhaf/coba-rhymes
 * [new branch]      hickory-dickory -> bob/hickory-dickory
 * [new branch]      master          -> bob/master
root@rindha:~/Documents/coba-rhymes# git branch -a
* hickory-dickory
  master
  remotes/alice/hickory-dickory
  remotes/alice/master
  remotes/bob/hickory-dickory
  remotes/bob/master
root@rindha:~/Documents/coba-rhymes# git checkout -b hickory-dickory bob/hickory-dickory
fatal: A branch named 'hickory-dickory' already exists.
root@rindha:~/Documents/coba-rhymes# git diff master hickory-dickory
root@rindha:~/Documents/coba-rhymes# git log -1 -p
commit df2a871331014aca4db6e98f4ea2d7418c99a17f (HEAD -> hickory-dickory, bob/master, bob/hickory-dickory, alice/master, alice/hickory-dickory, master)
Author: rindhaf <rindhafajirul@hmail.com>
Date:   Mon Nov 4 14:06:12 2019 +0700

    Added project overview to README.txt

diff --git a/README.txt b/README.txt
new file mode 100644
index 0000000..c83e022
--- /dev/null
+++ b/README.txt
@@ -0,0 +1 @@
+This repo is a collection of my favorite nursery rhymes.
root@rindha:~/Documents/coba-rhymes# git checkout master
Switched to branch 'master'
Your branch is up to date with 'alice/master'.
root@rindha:~/Documents/coba-rhymes# git merge hickory-dickory
Already up to date.
root@rindha:~/Documents/coba-rhymes# git branch -D hickory-dickory
Deleted branch hickory-dickory (was df2a871).
root@rindha:~/Documents/coba-rhymes# 

STEP 4
root@rindha:~/Documents/coba-rhymes# git remote rename origin bob
fatal: No such remote: 'origin'
root@rindha:~/Documents/coba-rhymes# git remote add alice https://github.com/rindhaf/coba-rhymes.git
fatal: remote alice already exists.
root@rindha:~/Documents/coba-rhymes# git remote
alice
bob
root@rindha:~/Documents/coba-rhymes# git remote -v
alice	https://github.com/rindhaf/coba-rhymes.git (fetch)
alice	https://github.com/rindhaf/coba-rhymes.git (push)
bob	https://github.com/rindhaf/coba-rhymes.git (fetch)
bob	https://github.com/rindhaf/coba-rhymes.git (push)
root@rindha:~/Documents/coba-rhymes# git remote update
Fetching alice
Fetching bob
root@rindha:~/Documents/coba-rhymes# git checkout master
Already on 'master'
Your branch is up to date with 'alice/master'.
root@rindha:~/Documents/coba-rhymes# git merge alice/master
Already up to date.
root@rindha:~/Documents/coba-rhymes# git diff alice/master
root@rindha:~/Documents/coba-rhymes# git push bob master
Username for 'https://github.com': rindhaf
Password for 'https://rindhaf@github.com': 
Everything up-to-date
root@rindha:~/Documents/coba-rhymes# git checkout -b bobs-changes
Switched to a new branch 'bobs-changes'
root@rindha:~/Documents/coba-rhymes# wget https://www.acquia.com/sites/default/files/blog/jack-be-nimble.txt
--2019-11-04 14:35:28--  https://www.acquia.com/sites/default/files/blog/jack-be-nimble.txt
Resolving www.acquia.com (www.acquia.com)... 104.16.117.45, 104.16.118.45, 2606:4700::6810:762d, ...
Connecting to www.acquia.com (www.acquia.com)|104.16.117.45|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2019-11-04 14:35:31 ERROR 404: Not Found.

root@rindha:~/Documents/coba-rhymes# git add jack-be-nimble.txt
fatal: pathspec 'jack-be-nimble.txt' did not match any files
root@rindha:~/Documents/coba-rhymes# git commit -m 'Added jack-be-nimble.txt.'
On branch bobs-changes
nothing to commit, working tree clean
root@rindha:~/Documents/coba-rhymes# wget https://www.acquia.com/sites/default/files/blog/mother-goose.txt
--2019-11-04 14:35:31--  https://www.acquia.com/sites/default/files/blog/mother-goose.txt
Resolving www.acquia.com (www.acquia.com)... 104.16.118.45, 104.16.117.45, 2606:4700::6810:752d, ...
Connecting to www.acquia.com (www.acquia.com)|104.16.118.45|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2019-11-04 14:35:32 ERROR 404: Not Found.

root@rindha:~/Documents/coba-rhymes# git add mother-goose.txt
fatal: pathspec 'mother-goose.txt' did not match any files
root@rindha:~/Documents/coba-rhymes# git commit -m 'Added mother-goose.txt.'
On branch bobs-changes
nothing to commit, working tree clean
root@rindha:~/Documents/coba-rhymes# git commit -am 'Updated README.txt.'
On branch bobs-changes
nothing to commit, working tree clean
root@rindha:~/Documents/coba-rhymes# git diff --word-diff
root@rindha:~/Documents/coba-rhymes# git commit -am 'Fixed typo in README.txt.'
On branch bobs-changes
nothing to commit, working tree clean
root@rindha:~/Documents/coba-rhymes# git commit -am 'Updated README.txt.'
On branch bobs-changes
nothing to commit, working tree clean
root@rindha:~/Documents/coba-rhymes# git commit -am 'Updated README.txt.'
On branch bobs-changes
nothing to commit, working tree clean
root@rindha:~/Documents/coba-rhymes# wget https://www.acquia.com/sites/default/files/blog/old-king-cole.txt
--2019-11-04 14:38:28--  https://www.acquia.com/sites/default/files/blog/old-king-cole.txt
Resolving www.acquia.com (www.acquia.com)... 104.16.117.45, 104.16.118.45, 2606:4700::6810:762d, ...
Connecting to www.acquia.com (www.acquia.com)|104.16.117.45|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2019-11-04 14:38:30 ERROR 404: Not Found.

root@rindha:~/Documents/coba-rhymes# git add old-king-cole.txt git commit -m 'Added old-king-cole.txt.'
error: unknown switch `m'
usage: git add [<options>] [--] <pathspec>...

    -n, --dry-run         dry run
    -v, --verbose         be verbose

    -i, --interactive     interactive picking
    -p, --patch           select hunks interactively
    -e, --edit            edit current diff and apply
    -f, --force           allow adding otherwise ignored files
    -u, --update          update tracked files
    --renormalize         renormalize EOL of tracked files (implies -u)
    -N, --intent-to-add   record only the fact that the path will be added later
    -A, --all             add changes from all tracked and untracked files
    --ignore-removal      ignore paths removed in the working tree (same as --no-all)
    --refresh             don't add, only refresh the index
    --ignore-errors       just skip files which cannot be added because of errors
    --ignore-missing      check if - even missing - files are ignored in dry run
    --chmod (+|-)x        override the executable bit of the listed files

root@rindha:~/Documents/coba-rhymes# wget https://www.acquia.com/sites/default/files/blog/twinkle-twinkle.txt
--2019-11-04 14:38:30--  https://www.acquia.com/sites/default/files/blog/twinkle-twinkle.txt
Resolving www.acquia.com (www.acquia.com)... 104.16.118.45, 104.16.117.45, 2606:4700::6810:752d, ...
Connecting to www.acquia.com (www.acquia.com)|104.16.118.45|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2019-11-04 14:38:31 ERROR 404: Not Found.

root@rindha:~/Documents/coba-rhymes# git add twinkle-twinkle.txt
fatal: pathspec 'twinkle-twinkle.txt' did not match any files
root@rindha:~/Documents/coba-rhymes# git commit -m 'Added twinkle-twinkle.txt.'
On branch bobs-changes
nothing to commit, working tree clean
root@rindha:~/Documents/coba-rhymes# git commit -am 'Updated README.txt.'
On branch bobs-changes
nothing to commit, working tree clean
root@rindha:~/Documents/coba-rhymes# git log git log --oneline
fatal: ambiguous argument 'git': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'
root@rindha:~/Documents/coba-rhymes#

STEP 5

root@rindha:~/Documents/coba-rhymes# git log git log --oneline
fatal: ambiguous argument 'git': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'
root@rindha:~/Documents/coba-rhymes# git log git log --online
fatal: ambiguous argument 'git': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'
root@rindha:~/Documents/coba-rhymes# git log --oneline
df2a871 (HEAD -> bobs-changes, bob/master, bob/hickory-dickory, alice/master, alice/hickory-dickory, master) Added project overview to README.txt
root@rindha:~/Documents/coba-rhymes# 77886c1 Updated README.txt.
bash: 77886c1: command not found
root@rindha:~/Documents/coba-rhymes# fbe874e Added old-king-cole.txt.
bash: fbe874e: command not found
root@rindha:~/Documents/coba-rhymes# 6256b8a Updated README.txt.
bash: 6256b8a: command not found
root@rindha:~/Documents/coba-rhymes# d1ba481 Updated README.txt.
bash: d1ba481: command not found
root@rindha:~/Documents/coba-rhymes# b7e5732 Fixed typo in README.txt.
bash: b7e5732: command not found
root@rindha:~/Documents/coba-rhymes# 642477c Updated README.txt.
bash: 642477c: command not found
root@rindha:~/Documents/coba-rhymes# 9e48a45 Added mother-goose.txt.
bash: 9e48a45: command not found
root@rindha:~/Documents/coba-rhymes# 8aea9be Added jack-be-nimble.txt.
bash: 8aea9be: command not found
root@rindha:~/Documents/coba-rhymes# 4b15370 Added hickory-dickory-dock.txt.
bash: 4b15370: command not found
root@rindha:~/Documents/coba-rhymes# 4ada881 Added old-mother-hubbard.txt, twinkle-twinkle.txt, hokey-pokey.txt
bash: 4ada881: command not found
root@rindha:~/Documents/coba-rhymes# 10e0e68 Added jack-and-jill.txt.
bash: 10e0e68: command not found
root@rindha:~/Documents/coba-rhymes# 6a69e0f Added all-around-the-mulberry-bush.txt.
bash: 6a69e0f: command not found
root@rindha:~/Documents/coba-rhymes# d30493a Added project overview to README.txt
bash: d30493a: command not found
root@rindha:~/Documents/coba-rhymes# 710f4bd First commit.
bash: 710f4bd: command not found
root@rindha:~/Documents/coba-rhymes# git rebase -i 4b15370
fatal: invalid upstream '4b15370'
root@rindha:~/Documents/coba-rhymes# pick 8aea9be Added jack-be-nimble.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick 9e48a45 Added mother-goose.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick 642477c Updated README.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick b7e5732 Fixed typo in README.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick d1ba481 Updated README.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick 6256b8a Updated README.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick fbe874e Added old-king-cole.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick 77886c1 Updated README.txt. 
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick 8aea9be Added jack-be-nimble.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick 9e48a45 Added mother-goose.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick fbe874e Added old-king-cole.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick 642477c Updated README.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick b7e5732 Fixed typo in README.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick d1ba481 Updated README.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick 6256b8a Updated README.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick 77886c1 Updated README.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick 8aea9be Added jack-be-nimble.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick 9e48a45 Added mother-goose.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick fbe874e Added old-king-cole.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# pick 642477c Updated README.txt.
bash: pick: command not found
root@rindha:~/Documents/coba-rhymes# squash b7e5732 Fixed typo in README.txt.
bash: squash: command not found
root@rindha:~/Documents/coba-rhymes# squash d1ba481 Updated README.txt.
bash: squash: command not found
root@rindha:~/Documents/coba-rhymes# squash 6256b8a Updated README.txt.
bash: squash: command not found
root@rindha:~/Documents/coba-rhymes# squash 77886c1 Updated README.txt.
bash: squash: command not found
root@rindha:~/Documents/coba-rhymes# git log --oneline
df2a871 (HEAD -> bobs-changes, bob/master, bob/hickory-dickory, alice/master, alice/hickory-dickory, master) Added project overview to README.txt
root@rindha:~/Documents/coba-rhymes# 80e8a59 Updated README.txt.
bash: 80e8a59: command not found
root@rindha:~/Documents/coba-rhymes# 1d57351 Added old-king-cole.txt.
bash: 1d57351: command not found
root@rindha:~/Documents/coba-rhymes# 9e48a45 Added mother-goose.txt.
bash: 9e48a45: command not found
root@rindha:~/Documents/coba-rhymes# 8aea9be Added jack-be-nimble.txt.
bash: 8aea9be: command not found
root@rindha:~/Documents/coba-rhymes# 4b15370 Added hickory-dickory-dock.txt.
bash: 4b15370: command not found
root@rindha:~/Documents/coba-rhymes# 4ada881 Added old-mother-hubbard.txt, twinkle-twinkle.txt, hokey-pokey.txt
bash: 4ada881: command not found
root@rindha:~/Documents/coba-rhymes# 10e0e68 Added jack-and-jill.txt.
bash: 10e0e68: command not found
root@rindha:~/Documents/coba-rhymes# 6a69e0f Added all-around-the-mulberry-bush.txt.
bash: 6a69e0f: command not found
root@rindha:~/Documents/coba-rhymes# d30493a Added project overview to README.txt
bash: d30493a: command not found
root@rindha:~/Documents/coba-rhymes# 710f4bd First commit.
bash: 710f4bd: command not found
root@rindha:~/Documents/coba-rhymes# 
