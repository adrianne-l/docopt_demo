# author: Tiffany Timbers
# date: 2020-01-15

"This script prints out docopt args.
Usage: demo.R <arg1> --arg2=<arg2> [--arg3=<arg3>] [<arg4>]

Options:
<arg1>            Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
<arg4>            Takes any value (this is an optional positional argument)
" -> doc

library(docopt)
opt <- docopt(doc)

main <- function(opt){
  # print docopt argument values and data types
  print(opt)
  print(typeof(opt))
  print(opt$arg4)
}

# call main function
main(opt)
