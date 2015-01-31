# Progects
Anything to do with /r/Progects, the only subreddit dedicated to virtual hackathons. As a friendly programming community focused on group projects, we're hoping for monthly programming sessions in small groups over the world wide web. 

Our [IRC channel](http://webchat.freenode.net/) will be #Progects @ Freenode

Current Work is being done on the reddit bot in Python 3 with PRAW

Short Term Goals:
  
  * Be able to search for specific strings, store the comment id in a separate text file, and not reply to the same comments again
  
Eventually:
  
  * Receive commands to (un)register self or teams to events
  * Organize teams based on registration commands
  * Scan for threads that have dates and send out notifications to registered people prior to event
  * If error occurs, create log file and email it
  
Current Bugs:
  
  * Bot does not currently read the whole text file for unique string ID's to filter out of search. I"m guessing that it is only reading the first line, although I could be wrong. Haven't tested.
  
  * For loops might not be the most efficient way of writing the criteria to meet. I originally thought it would reply twice to the same comment, but as long as the ID is stored and read correctly, it should be fine.
  
  * These issues should be fixed once it reads the file correctly and writes to it correctly.

Goals for /r/Progects! To get the ball rolling, this is what I want to accomplish before actually starting:

* Project Ideas
* Organizing the subreddit and writing things down in the sidebar
* Finding a public ventrilo/teamspeak server for now to voice communicate during events. If things take off, I wouldn't mind paying for a dedicated server. 
* Starting an IRC channel and organizing that. - Starting with this one first
* Creating a guide for people interested
* rules and guidelines for the events

