# Using the Terminal

## The Terminal and the Shell

If all of your previous experience has been on Windows or Mac OS, a Linux system may feel odd at first.

The most obvious point of departure is the *terminal*, the place where you type commands for the system to execute. Windows and Mac 
systems do have built-in terminals&mdash;it's called the Command Prompt in Windows&mdash;but they favor graphical user interfaces
(GUIs) for most tasks.

Linux systems are pretty much the opposite: most modern distributions support GUIs, but it's traditional for all serious work to be 
done in the terminal environment. Many configuration and maintenance tasks (common in the server realm) are actually easier to handle 
with typed commands than they would be with graphical menus.

The program that receives your commands, interprets them, and launches new programs is called the *shell*. The default shell program 
on most Linux systems is called `bash`.

The shell program prints a prompt for your commands, which typically identifies your username and the current working directory. On
Mimir, my prompt looks like this:

```
user@mimir: ~ >
```

For clarity, I will just use

```
>
```

## Paths and Directories

The Linux file system is organized as a tree. The top level directory is called the *root directory* and is denoted by `/`.

Every file and directory on the system has a *path* that describes its place in the file system tree. An *absolute path* gives the 
position of the object relative to the root. For example, the path

```
/home/dan/CMS_380/example.py
```

identifies a file named `example.py`, which resides in a directory called `CMS_380`, which is itself in a directory 
called `dan`. The `dmyers` directory is located in the `home` directory under the root, `/`. Here's a picture&mdash;I've added a
few more directories at each level to illustrate the tree structure:

```                          
                          / (the root dir)
                             |
                             |
              -----------------------------------
              |     |      |       |      |     |
              |     |      |       |      |     |
             bin   lib    home  include  etc   usr
                           |
                           |
                  ---------------------------------
                  |                 |             |
                  |                 |             |
                 dan         jcarrington    jaanderson       
                  |
                  |
           -------------------------
           |            |          |
           |            |          |
        CMS_380     teaching   research
           |
           |
01b-Linux_and_the_Shell.md
```

The top-level directories right beneath `/` are fairly standard across systems. `home` contains a series of *home directories* for
each system account. The example shows three home directories for three different users. `bin` is short for *binaries* and stores 
common executable programs.


## Moving Around and Creating Directories

The shell program recognizes one *working directory* at any given time. This is the directory that you are currently "in" and all of 
your commands will be executed with respect to it.

The `pwd` command prints the shell's present working directory.

```
> pwd
/home/dan/
>
```

You can list the contents of the current directory using `ls`.
```
> ls
```

Your initial home directory is probably empty, so the `ls` command won't display anything. Try listing the contens of some other directories:

```
> ls /
```

Let's create a directory to hold your files for this course. Use `mkdir` to make a new directory.

```
> mkdir CMS_380
```

Note that `mkdir` does not produce any output when it executes: it just creates the new directory, finishes, and then the prompt 
reappears. In the Unix world, *silence is golden*. Programs that run correctly tend to finish and exit without producing unnecessary
output.

Issue another `ls` command and you should see that the `CMS_380` directory now exists.

```
> ls
CMS_380
```

The `cd` command changes 
the working directory to the location you specify. If you don't supply a full absolute path, the shell will treat the path as 
*relative* and resolve it with respect to the current working directory.

```
> cd CMS_380
```

The `pwd` command will now show that your present working directory has changed to `CMS_380`.

```
> pwd
/home/dan/CMS_380
```

## Moving Back

Sometimes you need to move back up the directory hierarchy to the parent directory. Linux uses `..` to refer to the parent, so a `cd ..` command will bring you up one level in the hierarchy.

```
> cd ..
> pwd
/home/dan
```

There are two other special directory shortcuts that are useful to know:

- `.` always refers to the present directory

- `~` always refers to your home directory, `/home/dan` in these examples; `cd ~` is a quick way to return to your home from anywhere in the directory hierarchy

## In the Future

You will get plenty of practice working with the shell throughout this course. Refer back to this note for a refresher while 
you're working on the first assignment.
