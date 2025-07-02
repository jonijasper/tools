# argparser.py 
"""
Parser module for handling arguments passed to program when running from cli.

Usage:
    See examples.py for example usage of argparser(), or try running: 
    $ python3 examples.py --help
"""
import sys


_HELPTAGS = ["-h", "--help"]
_DEMOTAGS = ["--demo", "--test"]
_ARGDICT = {"-f": None, "-b": None}

def argparser(*, help: str=__doc__, demo: callable=None) -> list:
    """Hanldes arguments passed to program when running from cli.
    
    Args:
        help: Help message which is displayed when running with flag -h or --help.
            Defaults to *__doc__*, meaning the docstring of *argparser.py*, and
            should be replaced with *__doc__* of the calling file or any other 
            more relevant message.
        demo: Called when running the program with flag --demo or --test.

    Returns:
        A list of the arguments, without the flags. Order and flags defined in _ARGDICT

    Raises:
        NotImplementedError: When demo() is called but not defined.
        TypeError: If a flag encountered is defined in _ARGDICT but the following
            argument is a flag or missing.
    ---

    """
    args = sys.argv[1:]
    
    for i, arg in enumerate(args):
        if arg in _ARGDICT:
            try:
                value = args[i+1]
                err = False
            except IndexError:
                err = True

            if err or value.startswith('-'):
                raise TypeError(f"No argument found for flag {arg}.\n{help}")
            else:
                _ARGDICT[arg] = args[i+1]

        elif arg in _DEMOTAGS:
            try:
                demo()
            except NameError:
                raise NotImplementedError(arg)

        elif arg in _HELPTAGS:
            print(help)
            exit()

    return list(_ARGDICT.values())