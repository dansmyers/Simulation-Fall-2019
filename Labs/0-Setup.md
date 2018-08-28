# Setup

This lab will help you setup codeanywhere, our online development environment. You'll get to review some basic Linux terminal commands
and practice cloning and pushing with GitHub.

## codeanywhere

Many of you used the Cloud 9 online development environment in previous classes. Since being purchased by Amazon, they've totally changed
how their system works, to the point that it's no longer appropriate for us to use in classes.

Dr. Summet and I have decided to switch over to an alternate web environment: codeanywhere. It's very similar to Cloud 9, in that it
gives you both an IDE and a Linux terminal in the browser. It's slightly different, however, in that you only have one workspace in
codeanywhere. In Cloud 9, we typically made a new workspace for each course; now, you'll have one private workspace with subdirectories
for each course you're taking.

### Creation

**If you've already created your account and workspace you can skip this section**.

If you haven't done so, create an account at `https://codeanywhere.com/`. You only need one account, so don't make another one if you
already created one for another class. You'll need to put in a valid e-mail to approve your account, but you won't need to pay or input a
credit card number.

Once you are signed in for the first time, you'll want to create your workspace. Make the workspace name

```
YOURNAME
```

where `YOURNAME` is your Rollins e-mail id. For example, mine would be `dmyers`.

When you open the workspace for the first time, you'll see a panel that says "Connection Wizard" at the top. This will allow you to choose
the virtual machine stack and default environment for your workspace. This is not as important as it sounds, because you can always
install new tools later through the terminal.

Put your Rollins id name in the `Name` field of the Connection Wizard.

Scroll down and select the **Python3** stack on the **Ubuntu 14.04** OS. **Double-check that you've chosen the stack with the Ubuntu OS**.

Don't check the "Enable Always On" box: you don't have that feature on the free plan. Click the "Create" button to build the workspace.
After a minute or so you will see the editor window appear with a tab giving information on the workspace and a tab with a Linux terminal.

### Sharing Time

Click on the icon in the top bar that looks like a paper airplane. Enter my e-mail, `dmyers@rollins.edu`, and keep the "Can Edit" option
selected. Click "Done" to share your workspace with me. Note that your workspace is private by default: other students can't access it.

## Terminal

This section will help you practice basic commands in the terminal and also set up your directory for this class.

The basic idea of the terminal is simple: you type commands at the prompt, press `ENTER`, and the terminal program (also called the
shell) will execute them for you. The main challenge is learning the most common Linux OS commands.

First, a little bit about the Linux file system. It's always organized as a tree with a single root directory denoted by `/`. A file
or directory can be identified by its absolute path name starting from the root.

Type the command `pwd` at the prompt and press `ENTER`.

```
$ pwd
```

(I'm using the `$` symbol to represent the prompt; don't type another `$`). `pwd` stands for "present working directory" and the command
prints the absolute path of your current working directory.

The working directory is the directory that your shell is "in" right now. You should see something like

```
/home/cabox/workspace
```

All of your clas-specific directories will go underneath this workspace directory.

Use 'mkdir' to create a new directory within the current one:

```
$ mkdir cms380
```

When the command executes it doesn't print anything (this is normal behavior for Unix / Linux commands&mdash*silence is golden*), but
you can verify that it succeeded by listing the contents of the directory.

```
$ ls
```

The `cms380` directory is now listed underneath your current `workspace` directory.

You can `ls` other directories outside of your current one. Try listing the root directory:

```
$ ls /
```

You also get more information on each item by adding the `-l` flag to the command (that's the letter l, for "long"):

```
$ ls -l
$ ls -l /
```

When you're working on CMS 380 projects, you'll want them to go in the `cms380` directory. Change to the `cms380` directory
using `cd` ("change directory"):

```
$ cd cms380
```

Throw down another `pwd` and verify that your working directory now ends with `workspace/cms380`.

At some point, you'll want to go back up the directory hierarchy to the hgher-level "parent" directory of `cms380`. Linux uses the
special shorthand `..` to represent the parent of the current working directory.

```
$ cd ..
```

Use `pwd` and verify that you're back in the original workspace directory. Now use `cd` to return to `cms380`.

Make one more new directory called `python_examples` and `cd` into it.

### Quirk

You might have noticed that the file explorer pane on the left side of your screen does not show the `cms380` directory. To make it appear, you need to right-click on the connection name and select `Refresh`.

Also notice the `SSH Terminal` option in the right-click connection menu. Use that to re-open your terminal if you accidentally close
it.

## The End

This is the end of this brief setup. You will have more opportunities to practice with the terminal in class and in our future labs
and projects.

Our next goal is to get comfortable writing and running Python programs.
