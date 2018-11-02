"""
Choir is a test program used for demonstrating Github collaboration.

Step 1: Add a file to the `/lyrics` folder and create 2 functions:
sing(): Return a line of lyrics
credit(): Return a line crediting yourself for participation

Step 2: Add your file name (without the .py extension) the to MODULES array
"""
from time import sleep
import importdir
importdir.do("lyrics", globals())

"""
ADD YOUR FILE NAME HERE (without the .py extension):
"""
# pylint: disable=undefined-variable
#
MODULES = [
    first_example,
    second,
    husciicoder_lyrics_add
]
#
# pylint: enable=undefined-variable
"""
And that's all! We disable undefined variables since the modules
are loaded dynamically and aren't available before run-time and thus
will appear as an error
"""


def main():
    for module in MODULES:
        print(module.sing() + ' - ' + module.credit())
        sleep(0.500)
    print('\n\n')

if __name__ == '__main__':
    main()
