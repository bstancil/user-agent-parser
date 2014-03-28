user-agent-parser
=================

It's real dumb. Make a csv that has column headers and user agents in the first column. Go to the directory with the file and run this:
    
    python parse_ua.py [source csv] [destination csv]

Boom, you now have a new file that looks the same as the first, but with parsed user agent info appended to it.

Note that this uses the httpagentparser package. (https://github.com/shon/httpagentparser). If you don't have that package, you'll need to install it, probably with this command:

    pip install httpagentparser
    
