# Chinese Character Frequency Counter

These scripts allow the analysis of character frequencies in Chinese text corpora. This might be helpful for Chinese language learners to prioritize common characters when learning how to write.

## Usage

The scripts can take _any form and number of non-binary text input files_ (such as `txt`, `HTML`, `XML`, ...) encoded in `UTF-8`. All non-Chinese characters will be automatically removed (such as `HTML` tags) and the analysis will be done using the remaining characters. One example for a large text corpus is the [Chinese Wikipedia](https://zh.wikipedia.org/), but the scripts can also process other kinds of text corpora.

All input files should be placed in a common directory such as `hanzifreq/input/`. It is recommended to split up larger files (i.e. above 100 MB) with the `split.sh` utility, which can be called via `./split.sh path/to/large.file`. The resulting smaller files will be automatically placed in the `hanzifreq/input/` directory.

Then run `./calculate_freq.py input/` to analyze all files in the input directory. The input files will be processed in parallel on multicore architectures. For each input file `input.file` the script generates a file `input.file.freq` with frequency information of Chinese characters.

Finally run `./combine_freq.py input/` to combine all frequency information into one summary table. You can find the resulting table of the most common Chinese characters of your text corpus in the file `output/frequencies.html`. The `HTML` template file for that table is `template/template.html` and can be modified.

You can also change some settings by editing the `config.py` file.

### Chinese Wikipedia

One large language corpus is the Chinese Wikipedia, which you can download from:

* https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2

After downloading and unpacking, run `./split.sh zhwiki-latest-pages-articles.xml` to create smaller input files. Due to its encyclopedic nature, the character frequencies in Wikipedia vary from other sources such as novels or classical poetry. For example characters such as `年` (year), `月` (month) and `日` (day) occur more frequent than in many other text corpora.

### Precomputed frequencies

Go to http://git.io/hanzifreq to see the calculated character frequencies for the Chinese Wikipedia corpus.

