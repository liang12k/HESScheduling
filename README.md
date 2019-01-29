for git syntax: https://help.github.com/articles/basic-writing-and-formatting-syntax/

# HESScheduling
> HES scheduling for E

## helps assist w. scheduling HES items for E

starting as of Dec.02.2018

the goal is to have students + their session dates for the Month/Year combination
- store this output into a .txt for easier scheduling

## TODO: 
- [ ] provide a summary of students entered so far
- [ ] clarify Thurs is TH
- [ ] make Tues a TU
- [ ] determine which days are NYC DOE holidays and put an asterisk
- [x] add a checklist per each session row for each student
- [x] save files to /OutputFiles directory


## Modules to install:
- tabulate https://bitbucket.org/astanin/python-tabulate


================================================================================================
## HOW TO RUN

::from the left-side pane::

1. go to Runners folder, expand and get to the file 'generate_studentinfo_sessiondates.py'


2a. right click 'generate_studentinfo_sessiondates.py'
    click on the option to 'Run' this file (there's a green play symbol)

-or-

2b.  you can run 'generate_studentinfo_sessiondates.py' from the top-left
     ensure this filename is in the text box, click the play button
     - if this doesn't work, use approach in 2a.


3. now you can interact in the bottom window portion terminal
   follow the example inputs given, hit enter when done for each entry
   *** NOTE: Thursday is TH ***

4. to quit/exit the program, type in 'quit' or 'exit' w/o the single quotes at any time

5. when done, an output file text file will be generated in Outputs/StudentSessionDates directory
   from the left-side pane, you'll see a new text file that's in red (indicating a new file)
   *** NOTE: you can also view the text file from the Finder window ***
