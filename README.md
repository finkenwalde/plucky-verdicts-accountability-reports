# plucky-verdicts-accountability
A project to integrate accountability reporting into Single Eye Software's self-control software Plucky (formerly known as Pluckeye).

## What is Plucky?
*Please note that I am not employed by Single Eye Software -- I am simply one of their customers.*
Plucky (formerly known as Pluckeye) is a self-control and filtering software developed by Single Eye Software. Please see [getplucky.net](getplucky.net) and [pluckeye.net](pluckeye.net) for more details. To help support the continued development of Plucky, please consider [remunerating](https://s.pluckeye.net/remunerate). 

## What is this project for?
Plucky does not natively feature the ability to email accountability partners with internet activity. This project is attempting to develop a program that will work in conjunction with Plucky software to be able to send emails to accountability partners with reports of user-defined explicit sites that have been visited over a certain frequency (daily, weekly, etc.). 

## How does it work?
This project relies on the [verdicts](https://docs.pluckeye.net/verdicts) feature of Plucky, which is capable of returning a live log of Plucky's background activity. As of the initial commit for this project, there exist two scripts and two text files that work together:
### explicit-sites.txt
This is a user-defined list of sites that are to be considered as explicit in nature.
### accountability-report.txt
This is the log file that **plucky-verdicts-monitor.py** will create and fill when an explicit site from **explicit-sites.txt** is detected by Plucky Verdicts.
### plucky-verdicts-monitor.py
This script runs `pluck verdicts -f` for a live feed of Plucky's background activity and parses the results to log any explicit sites (from **explicit-sites.txt**) visited to **accountability-report.txt**. A sample return of what 
### email-accountability-partners.py
This script can be configured to send the contents of **accountability-report.txt** to a list of accountability partners' emails. It can also be scheduled to run daily or weekly.

## Some Notes
- This project is clearly a very rough draft, and I am not a professional software developer. I am interested, however, in gauging the community's interest in this project.
- The structure and functionality of this project right now requires that **plucky-verdicts-monitor.py** and **email-accountability-partners.py** be run continually and simultaneously in order for everything to work as intended. I realize this is probably not a very efficient method. Suggestions, forks, pull requests are welcome!
