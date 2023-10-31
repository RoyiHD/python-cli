#### Python Examples for using Click CLI

This is a basic implementation of click cli in different settings.
I highly recommend to read the full documentation of click
https://click.palletsprojects.com/en/7.x/

### Installation
run setup and install requirements into a virtual environment
```sh
pip install .
```

### Invoke cli with arguments
Invoking the cli with a required input

```sh
python project/cli/arguments.py helo.txt
```

### invoke cli with options
Invoking the cli passing in some input
```sh
python project/cli/options.py --file helo.txt
```

### invoke cli with groups
Groups allow us to package multiple cli commands in a single file
The first parameter is the command we want to invoke withint the group
The second paramenter is the options name 
The third paramenter is the input for ther option


```sh
python project/cli/group.py search -s hi
```

```sh
python project/cli/group.py run --run True
```