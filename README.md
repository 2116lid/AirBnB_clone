About
This is the First Project towards our AirBnB clone project at ALX. Done by Noah

General Use

Step 1. Clone the repository and cd into the repository
Step 2. Inside the repository, there is a "console.py" file which contains the command line interpreter. Run this command in the terminal to see how it works "$ python3 console.py"
Step 3. When this command is run this appears (hbnb)
Step 4. Type help to view all the commands in the interpreter

Execution

The shell works like this in interactive mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

it might sometimes show miscellenous commands
do not worry because it doesn't affect our console.
