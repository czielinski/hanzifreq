#!/usr/bin/python3

# The MIT License (MIT)
#
# Copyright (c) 2015 Christian Zielinski
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULtAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import multiprocessing
import collections
import pickle
import sys
import os
import re

import config


def count_characters(input_file):
    """
    Calculates Chinese character frequencies in a given file.
    """
    if not os.path.exists(input_file):
        print("ERROR: File <{}> does not exist".format(input_file))
        return 0

    output_file = input_file + config.freq_file

    if os.path.exists(output_file):
        print("Skipping <{}> ...".format(input_file))
        return 0

    print("Processing file <{}> ...".format(input_file))
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Count hanzi 
    chars = ''.join(re.findall(config.re_hanzi, content))
    chars_count = collections.Counter(chars)
    chars_total = sum(chars_count.values())

    with open(output_file, 'wb') as f:
        pickle.dump(chars_count, f, pickle.HIGHEST_PROTOCOL)

    print("Processed {} characters ...".format(chars_total))
    return chars_total


def main():
    if len(sys.argv) != 2:
        print("Usage:\n> python3 {} input_directory/".format(sys.argv[0]))
        return 1

    input_dir = sys.argv[1]
    if not os.path.isdir(input_dir):
        print("ERROR: <{}> is not a valid input directory".format(input_dir))
        return 2

    input_files = os.listdir(input_dir)
    input_files = [f for f in input_files if not f.startswith('.')]
    input_files = [f for f in input_files if not f.endswith(config.freq_file)]
    input_files = [os.path.join(input_dir, f) for f in input_files]

    pool = multiprocessing.Pool()
    pool.map(count_characters, input_files)

    print("Done.")


if __name__ == "__main__":
    main()
