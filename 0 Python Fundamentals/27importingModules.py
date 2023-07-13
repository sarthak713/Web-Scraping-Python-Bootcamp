# Importing Modules
    # modules define variables, functions, classes that could be referenced by other programs
    # a lot of functionality comes with modules from Python Standard Library
    # we access modules using the 'import' keyword
    # to import specific functions from a module we use: from <module> import <function>
    # we could alias our imports using the 'as' keyword

# import entire module

import statistics

scores=[4,2,4,2]

print(scores)

print(statistics.mean(scores))

# import only the function needed from a module

from statistics import mean

print(mean(scores))     # now we can directly access it, without '.' dot notation

# alias

from statistics import mean as avg

print(avg(scores))