# argparser.py 
"""
Parser module for handling arguments passed to program when running from cli.

Usage:
    See examples.py for example usage of argparser(), or try running: 
    $ python3 examples.py --help
"""
import sys


_HELPFLAGS = {"-h", "--help"}
_DEMOFLAGS = {"--demo", "--test"}
_ARGDICT = {"-f": None, "-b": []}

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
        TypeError: If a flag is not defined or there is missing arguments.
    ---

    """
    flag = None
    for arg in sys.argv[1:]:
        if arg.startswith('-'):
            if arg in _ARGDICT:
                flag = arg

            elif arg in _DEMOFLAGS:
                try:
                    demo()
                except NameError:
                    raise NotImplementedError(arg)
                exit()

            elif arg in _HELPFLAGS:
                print(help)
                exit()

            else:
                raise TypeError(f"{arg}\n{help}")
                
        else:
            if flag == "-b":
                _ARGDICT[flag].append(int(arg))

            elif flag:
                _ARGDICT[flag] = arg

            else:
                raise TypeError(f"{arg}\n{help}")
                

    if all(_ARGDICT.values()):
        return list(_ARGDICT.values())
    
    else:
        raise TypeError(f"{_ARGDICT}\n{help}")