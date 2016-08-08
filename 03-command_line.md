# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

CTRL L: clear
CTRL A: move cursor to start of line
CTRL E: move cursor to end of line
CTRL U: delete left of cursor
CTRL K: delete right of the cursor
CTRL C: End current process
TAB: auto complete
cat: show content of file
mkdir: create dir
mv: move files
cp: copy files
rm: remove files



---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`
`ls -a`
`ls -l`
`ls -lh`
`ls -lah`
`ls -t`
`ls -Glp`

`ls`  List visible files and directories
`ls -a`  List all files and directories
`ls -l`  Display long listing of parent directory
`ls -lh`  long listing with human readable file size
`ls -lah`  long format, all files/folders, human readable size
`ls -t`  list in order of last date first
`ls -Glp`  Bold Cyan, long format, with slash if file is a directory
---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
ls -R list files in dir recursively
ls -m display files in csv format
ls -1 display each file on a row
ls -F Display a slash (`/') immediately after each pathname that is a
      directory, an asterisk (`*') after each that is executable, an at
      sign (`@') after each symbolic link, an equals sign (`=') after
      each socket, a percent sign (`%') after each whiteout, and a ver-
      tical bar (`|') after each that is a FIFO
ls -r Reverse the order of the sort to get reverse lexicographical order

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs command is designed to construct argument lists and invoke other utility. xargs reads items from the standard input or pipes, delimited by blanks or newlines, and executes the command one or more times with any initial-arguments followed by items read from standard input.

example:

find .txt files in dir and one level up and remove them
find . -name "*.txt" -type f -print | xargs /bin/rm -f
