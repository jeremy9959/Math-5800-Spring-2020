## A very quick overview of the git workflow

Here is a brief overview of the git workflow for those just starting out.

### Getting Started

#### Set up the online repo site in github.com

Start by creating a project repository in the github site.  Include a README file,
and a License file (usually GNU GPL 3.0).  You can use the website to edit your README
file so it holds a preliminary overview of your project.

For future reference, suppose your git username is gituser and your repository is named
repo.

#### Clone your repository to your local machine.

Cloning makes a copy of your repository on your local machine and establishes the inner
linkages so that it's easy to "push" changes you make locally to the github site.

To clone the repository you need to know the url of the repository, which is going to be
<pre>
http://github.com/gituser/repo.git
</pre>

In the shell (on windows, use the git shell), make sure you are in your home directory and use the command 
```
$ git clone http://github.com/gituser/repo.git
```

This will create a directory on your computer called repo and will copy the files from the remote github site
into that directory.

Now you are set up to edit those files, create new files, and so on.

At this point, there is a marker, called a 'commit' in the history of your repo, set to this point.
Whatever you do, you can always get back to this state.

### The workflow loop

1.  Edit, create, delete, tinker with files however you want.  Do this until you reach a point where you would
    like to preserve your progress for the future, at which point you will move to step 2.   
    *Don't wait too long, move on fairly frequently to record incremental progress.*

2.  To set a checkpoint in your work, you will take the following steps:
    First, check the status of your git repository.
        
```
        $ git status
        On branch master
        Changes not staged for commit:
          (use "git add <file>..." to update what will be committed)
          (use "git checkout -- <file>..." to discard changes in working directory)

                modified:   README.md

        Untracked files:
        (use "git add <file>..." to include in what will be committed)

                new_file.txt
                working.py

        no changes added to commit (use "git add" and/or "git commit -a")
```

3. This tells you that you have modified the file README and created two new files new_file.txt and working.py.  You need to tell git to keep track of these changes, which you do as follows:

```
    $ git add README.md new_file.txt working.py
    $ git status
    On branch master
    Changes to be committed:
        (use "git reset HEAD <file>..." to unstage)

         modified:   README.md
         new file:   new_file.txt
         new file:   working.py
```

4. Notice that the status now lists "changes to be committed."  To actually MAKE the commit,
and preserve the state of things, you do the following:

```
    $ git commit -m 'A message describing your changes'
    3 files changed, 1 insertion(+), 1 deletion(-)
    create mode 100644 new_file.txt
    create mode 100644 working.py
```

5. Now check the status again.

```
    $ git status
    nothing to commit, working tree clean
```

6. At this point, you've preserved the new state of your work *on your local machine*.  But if you
want to preserve it in the cloud (and you should!) there is one more step.

```
    $ git push
```

7. Now you can go back to step 1!

### Summary

Once you've created the repository, the sequence is:
1. Edit your files
2. ```git add``` to tell git you want to track things
3. ```git commit -m message``` to commit your changes to the record
4. ```git push``` to put them in the cloud.

And:
```bash
$ git status
```
to know where things stand!