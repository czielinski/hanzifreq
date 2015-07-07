# Chinese Character Frequency Counter

These scripts allow the analysis of character frequencies in Chinese text corpora. This might be helpful for Chinese language learners to prioritize common characters when learning how to write.

## Usage

The scripts can take any form and number of non-binary text input files encoded in `UTF-8` (such as `txt`, `HTML`, `XML`, ...). All non-Chinese characters will be automatically removed (such as `HTML` tags) and the analysis will be done using the remaining characters.

All input files should be placed in a common directory such as `hanzifreq/input/`. It is recommended to split up larger files (i.e. a few 100 MB) with the `split.sh` utility, which can be called via `./split.sh path/to/large.file`. The resulting smaller files will be automatically placed in the `hanzifreq/input/` directory.

Then run `./calculate_freq.py input/` to analyze all files. The input files will be processed in parallel on multicore architectures. For each input file `input.file` the script generates a file `input.file.freq` with frequency information of Chinese characters.

Finally run `./combine_freq.py input/` to combine all frequency information into one summary table. You can find an HTML table of the most common Chinese characters of your corpus in the file `output/frequencies.html`.

You can change some settings by editing the `config.py` file.

### Chinese Wikipedia

One large language corpus is the Chinese Wikipedia, which you can download from https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2. After downloading, run `./split.sh zhwiki-latest-pages-articles.xml`. Due to its encyclopedic nature, the character frequencies in Wikipedia vary from other sources such as novels or classical poetry. For example characters such as `年` (year), `月` (month) and `日` (day) occur more frequent than in many other text corpora.

### Precomputed frequencies

Go to http://git.io/hanzifreq to see the calculated character frequencies for the Chinese Wikipedia corpus.

