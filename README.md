# Chinese Character Frequency Counter

These script allows one to analyze character frequencies in Chinese texts. This might be helpful for Chinese language learners to prioritize common characters when learning how to write.

### Download the Chinese Wikipedia

One large language corpus is the Chinese Wikipedia, which you can download from `https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2`. However, the scripts can be also used for other Chinese text corpora which are in plain text format and encoded as `UTF-8`. The scripts will remove all non-Chinese characters and then calculate their frequencies.

Due to its encyclopedic nature, the character frequencies in Wikipedia vary from other sources such as novels or classical poetry. For example characters such as `年` (year), `月` (month) and `日` (day) occur more frequent than in many other text corpora.

### Split large input files into smaller ones

In the `hanzifreq/` directory you can find the `split.sh` helper script. Use it to split a large input file into smaller ones, which can be analyzed in parallel. Run it via `./split.sh zhwiki-latest-pages-articles.xml`. You will find the smaller input files in the `input/` directory.

### Analyzing and combining

Then run `./calculate_freq.py input/` to analyze all files and `./combine_freq.py input/` to combine everything and generate the output. You can find an HTML table of the 10000 most common Chinese characters of the corpus in the file `output/frequencies.html`.

### Precomputed frequencies

Go to `http://git.io/hanzifreq` to see the calculated character frequencies for the Chinese Wikipedia corpus.

