Georgetown Calendar
===================
**A simple calendar in Python**

This library is a reference for those of you attempting to do the Georgetown Calendar project on your own. If you're reading this, you're in the syllabus branch of the project- hopefully to compare what we did in class to what you have written from scratch.

This README will talk a little bit about how to install and use the program in a simple fashion. Note that although this code has tests, it's not complete - as it was for a course example only. Be aware of what you're doing, lest you create Calendar files all over your operating system!

## Installation ##
This library wouldn't be useful if you couldn't play around with it, here's how to get it on your system.

### Option One ###
To install the script, simply download the package from Github at the following link:
    
    https://github.com/bbengfort/georgetown-calendar/archive/syllabus.zip

This will download this particular branch of the project. Go ahead and unzip the syllabus file. To install run the setup.py in the root directory as follows:

    $ python setup.py install

However, I think you might get more benefit out of the slightly harder way with option two, as it will allow you to play with the code like a developer might.

### Option Two ###
This isn't totally necessary, and it will install a `gtcal` script as well as all the calendar packages on your computer. If you prefer, you can simply work on the code in the local directory like you were developing it. Follow these steps (assuming you have virtualenv and virtualenvwrapper installed):

    $ git clone https://github.com/bbengfort/georgetown-calendar.git
    $ cd georgetown-calendar
    $ git checkout syllabus
    $ git branch --list 
    
You should now have a clone of the repository, and be in the syllabus branch (you can confirm with the `git branch --list` command or by seeing if there is actually code in the files). Create the virtualenv:
    
    $ mkvirtualenv -a $(pwd) -r requirements.txt gtcal

This should install the virtualenv with this as the project directory, along with all the requirements in the environment. You should now see:

    (gtcal) $ 

As your prompt. 

## Running the Script ##

**Make sure you're in the root directory of the project**. 

If you do an `ls` you should see the setup.py script, requirements.txt, a scripts folder, a fixtures folder, the tests folder, and the gtcal folder. 

    $ ls
    LICENSE          fixtures         requirements.txt setup.py
    README.md        gtcal            scripts          tests
   
This is because by default, the `gtcal` script in the `scripts` directory is going to try to use the `calendar.csv` in the `fixtures` directory, and here is where you want to be. 

Try to run the tests:

    $ nosetests -v
    
You should see a bunch of nosetests pop out. 

You can also run the script:

    $ scripts/gtcal
    Calendar at fixtures/calendar.csv with 3 events
    
If you have any errors or exceptions, you may be in the wrong directory, or the script might not be executable. 

**Note**: If you used install option one, you just replace `scripts/gtcal` with `gtcal` and it should work just fine.

Try the following things:

    $ scripts/gtcal add
    ...
    
    $ scripts/gtcal agenda
    ...
    
    $ scripts/gtcal view
    ...
    
Note for the agenda, you might have to add some events that happen today. You can do this by just specifying start and end times rather than whole dates, e.g.:

    $ scripts/gtcal add
    name: Software Engineering for Data
    start: 18:00
    end: 21:00
    location: Georgetown Chinatown Campus
    notes: Be on time!
