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

import sys
import re

# File ending for frequency information
freq_file = '.freq'

# Number of characters to output
num_output_chars = 10000

# HTML template file
template_file = 'template/template.html'

# Definition of Chinese characters
hanzi = '\u3007\u4E00-\u9FFF\u3400-\u4DBF\uF900-\uFAFF'

if sys.maxunicode > 0xFFFF:
    hanzi += '\U00020000-\U0002A6DF\U0002A700-\U0002B73F'
    hanzi += '\U0002B740-\U0002B81F\U0002F800-\U0002FA1F'

re_hanzi = re.compile('[{}]'.format(hanzi))
