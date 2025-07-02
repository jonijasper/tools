# printers.py 
"""
Custom printers
"""
import sys


def xprint(msg: str, level: str="INFO", logfile: str=None):
    """ Autoformat info, warning, error, etc. messages.

    INFO -level (default) messages are directed to stdout, others to stderr.
    
    Message format:

        *** level: msg

    Args:
        msg: A string containing the message.
        level (optional): Prefix for the message. Defaults to "INFO".
        logfile (optional): Path to file. If provided, the message is also
            written to the file.
    ---        
    """
    if level == "INFO":
        stream = sys.stdout
    else:
        stream = sys.stderr

    fmsg = f"*** {level}: {msg}"
    print(fmsg, file=stream)

    if logfile:
        with open(logfile, 'a') as f:
            f.write(fmsg + "\n")
