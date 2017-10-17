# Scheduling Lab

This is a lab exercise from NYU `CSIC-UA 202 Operating Systems` that emulates how different scheduling algorithms work in an OS. The algorithms implemented are:

	1. FCFS (First Come First Serve)
	2. RR (Round Robin)
	3. SJF (Shortest Job First)
	4. HPRN (Highest Penalty Ratio Next)

## Setup

To run this program you need `python3`. It does not use external libraries. Download/clone this repository or cd into the repository. The sample inputs from Professor Gottlieb's website are already in the repository but if you wish you can download them with the following commandline in the repository directory.

```sh
$ sh download.sh
```

Inside `glb.py` are the global variables used for this program. The only thing you might want to change is the location of the random number file. If you downloaded the files by using the `download.sh` file or by cloning the entire repo, the random number file should be in the root of the repository.

```py
rf = 'random-numbers.txt'
```

# Run

If you have the input files and the random number file, you can generally use this command to run the program:

```sh
$ python3 scheduler.py <input-filename>
```

Additionally there are `--verbose` and `--show-random` options to show the state and burst of every process at each cycle and to show the random number selected, respectively.
```sh
$ python3 scheduler.py --verbose <input-filename>
$ python3 scheduler.py --show-random <input-filename>
$ python3 scheduler.py --verbose --show-random <input-filename>
```

If the program is run without additional arguments it will automatically take `input/input-1.txt` as input with both `--verbose` and `--show-random` options.



