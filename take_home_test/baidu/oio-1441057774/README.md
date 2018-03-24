# Glob

## Problem
Given a pattern and a list of filenames, return the filenames which match the given pattern in a separate list. The pattern should support two wild card characters '?' and '\*', where '?' can match zero or one characters and '\*' can match any number of characters. For the sake of simplicity, you can assume the input filenames only contain alphabets.

## Instructions

### Building the binary
For Linux and Mac users, you can use the included Makefile to compile and run the project.
```shell
# Compile only
make
# Compile and run
make run
```

For Windows Visual Studio users, a vcproj template is included. Alternatively you can compile and run with the included Makefile.vs in Developer Command Prompt:
```shell
# cd to project directory
# Compile only
nmake -f Makefile.vs
# Compile and run
nmake -f Makefile.vs run
```

Please find the skeleton code in the file `project.cpp` and implement the `Match` function. Please avoid using any regex or glob modules/libraries.

For example,
```c
// should return vector<string>({"abcd", "dabc", "abc"})
Glob().Match("?abc*", {"abcd", "dabc", "abc", "efabc"});
```

Your solution will be scored in the descending priority of correctness, memory & time complexity, and comprehensibility.

## Submission
Upon completion, please follow the instructions described in the website (where you found the instructions to download the project) to submit your solution. You can submit as many times as you prefer. Your last submission will be used for evaluation as well as marking the end of your coding assessment.

Lastly, do not be concerned if you are running a little bit over time (0-10 minutes). We do not penalize moderately tardy submissions.
