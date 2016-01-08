#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Nandaja Varma <nvarma@redhat.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#

import argparse
import sys
import os
import time
import shutil
from collections import OrderedDict

from lib import *


@logfunction
def parse_arguments(args=None):
    '''
    This method uses argparser to parse the command line inputs
    to the gdeploy script
    '''
    usage = 'gdeploy [-h] [-v] [-vv] [-c CONFIG_FILE] ' \
        '[-k]'
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s 1.0')
    parser.add_argument('-c', dest='config_file',
                        help="Configuration file",
                        nargs='+',
                        type=argparse.FileType('rt'))
    parser.add_argument('-k', dest='keep',
                        action='store_true',
                        help="Keep the generated ansible utility files")
    parser.add_argument('-vv', dest='verbose',
                        action='store_true',
                        help="verbose mode")
    try:
        args = parser.parse_args(args=args)
    except IOError as msg:
        raise IOError
        parser.error(str(msg))
    if not args.config_file:
        parser.print_help()
        try:
            Global.logger.error("Invalid usage")
        except:
            pass
        return None
    return args


if __name__ == '__main__':
    '''
    This script just reads in the command line arguments and gets the
    config file.

    Here gdeploy starts!
    Drum roll!
    '''
    '''
    and it initialises a global var to keep track of the logs
    '''
    log_event()
    args = parse_arguments(sys.argv[1:])


