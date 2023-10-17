# Linux_learn
Repository for learning Linux

Q1 Write bash functions marco and polo that do the following. Whenever you execute marco the current working directory should be saved in some manner, then when you execute polo, no matter what directory you are in, polo should cd you back to the directory where you executed marco. For ease of debugging you can write the code in a file marco.sh and (re)load the definitions to your shell by executing source marco.sh. Script marco.sh has functions marco and polo. The script is sourced which has an environment variable exported to be used by another function.

Steps for running the scripts
Step 1: Source marco.sh in a directory.
Step 2: Run the function marco.
Step 3: Navigate to any other directory.
Step 4: Run the function polo.


Q3 Say you have a command that fails rarely. In order to debug it you need to capture its output but it can be time consuming to get a failure run. Write a bash script that runs the following script until it fails and captures its standard output and error streams to files and prints everything at the end. Bonus points if you can also report how many runs it took for the script to fail.

Steps for running the scripts
1. Ensure random.sh and repeat.sh to be in the same directory.
2. Source repeat.sh script to see the desired output.
