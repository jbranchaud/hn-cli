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

FIXMEs
------

- A 31st link is being displayed for going to page 2 of HackerNews, need to ignore this.

TODOs
-----

- Fancy up the formatting a little
- Think about shortening the links (e.g. http://github.com/jbranchaud/hn-cli --> github.com)

Related
-------

- [hnews - Hacker News CLI](https://github.com/bencevans/hnews) by [bencevans](https://github.com/bencevans)
- [hackernews](https://bitbucket.org/zalew/hackernews) by [Zalew](https://bitbucket.org/zalew)

