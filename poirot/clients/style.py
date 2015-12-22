# -*- coding: utf-8 -*-
import re


# Python character unicode

prefix = "\033["
reset = prefix + "0m"

style_codes = {
    "bold": prefix + "1m",
    "gray": prefix + "1;30m",
    "black": prefix + "30m",
    "red": prefix + "1;31m",
    "darkred": prefix + "31m",
    "green": prefix + "1;32m",
    "darkgreen": prefix + "32m",
    "yellow": prefix + "1;33m",
    "brown": prefix + "33m",
    "blue": prefix + "1;34m",
    "darkblue": prefix + "34m",
    "fuscia": prefix + "1;35m",
    "purple": prefix + "35m",
    "cyan": prefix + "1;36m",
    "darkcyan": prefix + "36m",
    "white": prefix + "1;37m",
    "smoke": prefix + "37m",
    "default": prefix + "39m",
    "yellow_bg": prefix + "43m",
    "cyan_bg": prefix + "46m",
    "blue_bg": prefix + "42m",
    "orange_bg": prefix + "41m",
    "white_bg": prefix + "47m",
    "default_bg": prefix + "49m"
}

symbol_codes = {
  'ok': u"\u2713",
  'fail': u"\u2716",
}


def style(text, _code):
    """Takes a string and styles its print output"""

    try:
        return "%s%s%s" % (style_codes[_code], text, reset)
    except:
        return "%s" % (text)


def ok(text):
    """Takes a string and prepends a green check to it"""

    return "%s %s" % (style(symbol_codes['ok'], 'green'), text)


def fail(text=''):
    """Takes a string and prepends a red x mark to it"""

    return "%s %s" % (style(symbol_codes['fail'], 'red'), text)


def highlight(text, pattern):
    """Takes a string and highlights substrings matching a pattern"""

    regx = re.compile(pattern, flags=re.I)
    match = regx.search(text)
    if match:
        text = text.replace(match.group(0), style(match.group(0), 'red'))
    return text
