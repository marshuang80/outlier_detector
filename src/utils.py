import inspect
import builtins 
import argparse

from collections.abc import Callable


def add_func_params(
        parser:argparse.ArgumentParser, func: Callable
    ) -> argparse.ArgumentParser:
    """
    Add function parameters to argumenter parser. 

    args: 
        parser (argparse.ArgumentParser): parser to add arguments
        func (Callable): function with parameters to be added to parser

    returns: 
        updated parser with arguments from function parameters
    """

    # retrieve function signature
    sig = inspect.signature(func)

    # loop over function parameters
    for param, info in sig.parameters.items(): 
        
        # dataframe input will be parsed from csv file (args.csv_path)
        if param in ['df', 'col']: continue

        # get param type and defaults
        p_name, p_val = str(info).split(':')
        p_val = p_val.split('=')
        p_type = getattr(builtins, p_val[0].strip(' '))
        p_default = p_val[1].strip(' ')

        # cast default type 
        if p_default == "None": 
            p_default = None
        else: 
            p_default = p_type(p_default)

        parser.add_argument(
            f"--{p_name}",
            default=p_default,
            type=p_type,
            required=False,
        )
    return parser