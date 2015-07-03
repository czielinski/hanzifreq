# Chinese Character Frequency Counter

These script allows one to analyze character frequencies in Chinese texts. This might be helpful for Chinese language learners to prioritize on common characters.

### Download the Chinese Wikipedia

One good and large language corpus is the Chinese Wikipedia, which you can download from https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2.

### Split large input files into smaller ones

In the `script/` directory you can find the `split.sh` helper script. Use it to split a large input file into smaller ones, which can be analyzed in parallel. Run it via `./split.sh zhwiki-latest-pages-articles.xml`. You will find the smaller input files in the `input/` directory.

### Analyzing and combining

Finally run `./calculate_freq.py input/` to analyze all files and `./combine_freq.py input/` to combine everything and generate the output. You can find an HTML table of the 10000 most common Chinese characters of the corpus in the file `output/frequencies.html`.

