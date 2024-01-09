This project is a requiremnet for alx AirBnB project.

It is a console that that allows for creation, rading, updating and deleting of users data.

The console works this way in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

And in non-interactive mode:

```
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
```

For Testing:

```
$ python3 unittest -m discover tests
```

Also:

```
$ python3 unittest -m tests/test_console.py
```
