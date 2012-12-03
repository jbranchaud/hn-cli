hn-cli
======

hn-cli is a command-line interface for HackerNews

Installation
------------
For now, simply put `hn` in a directory that is on your system's path.
For instance, you can just throw it in `/usr/local/bin` which is probably on
your path. If you're not sure, type `echo $PATH`.

Usage
-----

`hn` - grabs and displays the 30 items from the [HackerNews](http://news.ycombinator.com) homepage.

`hn [open|view] [num]` - finds the cached link corresponding to the given num and opens it.

`hn update` - updates your cached HackerNews items and then displays them (same as `hn`).

`hn list [num]` - grabs the first num items (or all items) from the cached list and displays them.

`hn help` - displays the usage info, but if you are reading this, then I guess you don't really need it.

Requirements
------------
The following is a list of non-standard python libraries needed to run this script:

- [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)

FIXMEs
------

- Some unicode characters appear funky in the output, find out what to do about this.

TODOs
-----

- Fancy up the formatting a little
- Try playing with color for the different elements of the HN item
- Favorite words and favorite URLs list that will highlight HN items based on your preferences

Related
-------

- [hnews - Hacker News CLI](https://github.com/bencevans/hnews) by [bencevans](https://github.com/bencevans)
- [hackernews (hn)](https://github.com/jeyb/hackernews) by [jeyb](https://github.com/jeyb)
- [hackernews](https://bitbucket.org/zalew/hackernews) by [Zalew](https://bitbucket.org/zalew)

