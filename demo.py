# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [<arg4>]

Options:
<arg1>             Takes any value (this is a required positional argument)
--arg2=<arg2>      Takes any value (this is a required option)
[--arg3=<arg3>]    Takes any value (this is an optional option)
[<arg4>]           Takes any value (this is a optional positional argument)
""" 

from docopt import docopt
opt = docopt(__doc__)

# define main function
def main(opt):
  """
  This function prints out the docopt args datatypes and values, with value of arg4.
    
  Parameters
  ----------
  argument : arg
    Argument value
        
  Returns
  -------
  dict
    A dictionary of argument datatypes and values, with value of arg4. 
        
  Examples
  --------
  >>> main(1, --arg2=2))
  {'--arg2': '2',
 '--arg3': None,
 '<arg1>': '1',
 '<arg4>': 'final'}
 
  """
  print(opt)
  print(type(opt))
  print(opt["<arg4>"])

# call main function
if __name__ == "__main__":
    main(opt)

