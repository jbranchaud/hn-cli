# HackerNews Command-Line Inteface - hn-cli

Because *real* hackers access HackerNews from their terminal.

hn-cli is a command-line interface for [HackerNews](http://news.ycombinator.com).
It essentially allows you
to view the front page of HackerNews from your favorite terminal and then open
up the links in your favorite browser.

## Installation

For now, simply put `hn` in a directory that is on your system's path.
For instance, you can just throw it in `/usr/local/bin` which is probably on
your path. If you're not sure, type `echo $PATH`.

## Usage

`hn` - grabs and displays the 30 items from the [HackerNews](http://news.ycombinator.com) homepage.

`hn [open|view] [num]` - finds the cached link corresponding to the given num and opens it.

`hn update` - updates your cached HackerNews items and then displays them (same as `hn`).

`hn list [num]` - grabs the first num items (or all items) from the cached list and displays them.

`hn help` - displays the usage info, but if you are reading this, then I guess you don't really need it.

## Requirements

The following is a list of non-standard python libraries needed to run this script:

- [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)

## FIXMEs

- Some unicode characters appear funky in the output, find out what to do about this.
- Need more graceful failure for various errors (e.g. when server cannot be reached).

## TODOs

- Consider incorporating [Baker](https://pypi.python.org/pypi/Baker) to
    make it easier to implement the command-line interface
- Create an animated GIF to embed in this readme that demonstrates how hn works
- Add a comments option (either `hn view 1 comments` `hn view -c 1` or `hn comments 1`
- In preparation for some fancier features, switch from .hn file to .hn directory
- Allow for multiple articles to be opened at once (e.g. `hn open 2 5 14`)
- Add a `history` command that allows you to see the last n items that you accessed
- Fancy up the formatting a little
- Try playing with color for the different elements of the HN item. Try using
    [Curses](http://docs.python.org/2/howto/curses.html) for this.
- Favorite words and favorite URLs list that will highlight HN items based on your preferences
- Add a `summ` or `summary` command that gives some idea of what the article is about.
- Add a `ran`, `-r`, or `random` command that will open a random article

## Related

- [hnews - Hacker News CLI](https://github.com/bencevans/hnews) by [bencevans](https://github.com/bencevans)
- [hackernews (hn)](https://github.com/jeyb/hackernews) by [jeyb](https://github.com/jeyb)
- [hackernews](https://bitbucket.org/zalew/hackernews) by [Zalew](https://bitbucket.org/zalew)

## License

Copyright &copy; 2013 [Josh Branchaud](http://joshbranchaud.com)
under the MIT License.
See [LICENSE](https://github.com/jbranchaud/hn-cli/blob/master/LICENSE)
for details.

