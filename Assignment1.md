# Git/GitHub Assignment

* **INDIVIDUAL ASSIGNMENT**
* **Deadline**: Sept-10th 11:59PM
* **How to submit**: For each empty grey box, please provide with an answer to the item in a document. Do the following to *submit* the **Part 1** of your assignment:
1. Create a new repository under your GitHub account called *INF502*; 
2. create a file called *"Assignment1.md"* and paste your answers there (tip: click on *"Raw"* at the right-top of this file to get the markdown source); 
3. invite me to see your new repository. This will allow you to keep a private repository that only you and me will be able to see

For **Part 2** the pull request created will the submission (except for item 4, which you need to add to the end of the Assignemnt1.md).

* **Value**: Part of homework grade

## Description
This assignment is composed of two parts. 
- [Part 1](#Part-1-Dealing-with-git) consists of executing a sequence of commands and giving explanations about the commands you have to run. 
For each item in the assignment, please provide appropriate explanation and/or the details requested.
- [Part 2](#Part-2-Using-GitHub) consists of creating a Markdown file on a fork of this course and creating a pull request towards this repo.

### Part 1: Dealing with git

To conduct this, you will have to download [handson.zip](handson.zip) and unzip it.
handson folder is a git repository. Using the command line change the directory to "handson/"

The empty boxes
```

```
represent the content you need to fill and post on your private repository


1. Draw a diagram of the commits and branches in repository.

    - Use `git branch` to list the branches in this repository.
    - Use `git checkout` to explore each branch.
    - Use `git log --decorate` to explore the structure of commits.


```
 Git Branch: 
  Arvins-MacBook-Pro:handson arvinnatadihardja$ git branch
* master
  math
Arvins-MacBook-Pro:handson arvinnatadihardja$ git checkout math
Switched to branch 'math'
Arvins-MacBook-Pro:handson arvinnatadihardja$ git branch
  master
* math

 Git Log --Decorate:     
        Arvins-MacBook-Pro:handson arvinnatadihardja$ git log --decorate
commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (HEAD -> math)
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:13:48 2019 -0700

    Adding some more knowledge to the function

commit 654b490a181dedf82dd6deda5f9848d6cca05918
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:12:14 2019 -0700

    Added a draft of A.py

commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:08:47 2019 -0700

     Creating all files (all empty)
```

2. Try `git log --graph --all` to see the commit tree. What do you see?


```
Git log graph function, display the graph log for commit tree

```

3. Use `git diff BRANCH_NAME` to view the differences from a branch and the current branch.
   
```
Summarize the difference from master to the other branch.
    The current branch (math) is lacking :-   print 'my knowledge is limited'    
    The other branch (master) lacking : 
    +   if operator == 'sum':
    +      print num1 + num2
    +      print 'That was easy buddy'
    +   else:
    +      if operator == 'subtraction':
    +         print num1 - num2
    +         print 'I could handle that...'
    +      else:
    +         print 'my knowledge is limited'

```

4. Write a command sequence to merge the non-master branch into `master`
    


```
git merge math\master
```

5. Write a command (or sequence) to (i) create a new branch called `math` (from the `master`) 
and (ii) change to this branch

```
math already exist; can't create another branch called math

```
   
6. Edit B.py adding the following source code below the content you have there
```
echo 'I Know Math Look:' >> B.py
echo 2+2 >> B .py

```

7. Write a command (or sequence) to commit your changes
```
git add .
git commit -a -m 'editing b.py'

```

8. Change back to the `master` branch and change B.py adding the following source code (commit your change to `master`):
```
git checkout master
echo 'hello world' >> B.py
git add .
git commit -a -m "editing B.py in master"
```

9. Write a command sequence to merge the `math` branch into `master` and describe what happened
```
is not something we can merge aka merge conflict.
Merge conflict happens because we're trying to edit the same exact section on the file & git didn't aware which file to save.

```
   
10. Write a set of commands to abort the merge
```
git merge --abort

```
   
11. Now repeat item 9, but proceed with the manual merge (Editing B.py). All implemented methods are needed. Explain your procedure
```
for some reason, my bash is not allowing me to merge the 2 files. 
```

12. Write a command (or set of commands) to proceed with the merge and make `master` branch up-to-date
```
put the comment in
press ":wq" to quit

```

### Part 2: Using GitHub

The goal of this assignment is to put you in touch with the fork-pullrequest process, with an extra of dealing a little bit with Markdown. To learn more about Markdown [click here](https://guides.github.com/features/mastering-markdown/).

**You must fork this repo and submit a pull request back**

1. Into the students folder, create a file called LASTNAME_FIRSTNAME.md (please change LASTNAME_FIRSTNAME for your actual last and first names). 
2. Use Markdown to structure the following information about the last paper you've read (you can structure your markdown the way you want):
- Title
- Venue (journal name/conference)
- Number of pages
- 3 outcomes of the paper
- link to the paper online

3. Send your file back to this repository until creating a pull request (your pull request needs to appear [here](https://github.com/igorsteinmacher/CS502-Fall2019/pulls)).

4. Report your experience of making this submission, including the steps followed, commands used, and hurdles faced (within the file you created for the **Part 1**.

```
Part 2
I would describe my experience utilizing github on pull/ fork request went fairly smooth.
```




