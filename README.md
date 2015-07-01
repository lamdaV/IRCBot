# IRCBot
A conceptual IRC bot for the CSSE 120.

# Functions  
This conceptual IRC bot can currently respond to three commands: !help, !assignments, and !hint. The help command simply list the current possible command. The assignments command current prints the course website. Ideally, the assignments command should intelligently determine the date and print out the current assignment. Lastly, the hint command is intended for any last minute hints. The hint can be altered without having to stop the bot (Note: The method implemented may have some concurrency issues and memory leaks.) 

# How to Use:
Alter the global variables appropriately within the data.txt document (First: Server, Second: Port, Third: Channel, Forth: Nickname, Fifth: Hint).  
Run the program via commandline or other alternatives.  
  
