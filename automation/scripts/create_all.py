#!/usr/bin/env python
import os
import sys
import glob
import re
from commands import getoutput
import config


def main():
    # create home page
    op = getoutput('home_page_create.py')
    print op

    # create aboutus page
    op = getoutput('aboutus_create.py')
    print op

    # create contactus page
    op = getoutput('contact_us_create.py')
    print op

    # create all product pages
    schema_files = glob.glob('*.schema')

    for f in schema_files:
        if (f == config.SITE_NAVIGATION_MENU_SCHEMA or
                f == 'readme.prod.schema'):
            continue
        print getoutput('./product_create.py -i ' + f)



    print "Done"



if __name__ == "__main__":
    sys.exit(main())    # pylint: disable=E1120
