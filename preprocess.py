from __future__ import print_function
from gensim.corpora import WikiCorpus
import logging
from gensim import utils


def tokenize_tr(content, token_min_len=2, token_max_len=50, lower=True):
    if lower:
        lowerMap = {ord(u'A'): u'a', ord(u'A'): u'a', ord(u'B'): u'b', ord(u'C'): u'c', ord(u'Ç'): u'ç',
                    ord(u'D'): u'd', ord(u'E'): u'e', ord(u'F'): u'f', ord(u'G'): u'g', ord(u'Ğ'): u'ğ',
                    ord(u'H'): u'h', ord(u'I'): u'ı', ord(u'İ'): u'i', ord(u'J'): u'j', ord(u'K'): u'k',
                    ord(u'L'): u'l', ord(u'M'): u'm', ord(u'N'): u'n', ord(u'O'): u'o', ord(u'Ö'): u'ö',
                    ord(u'P'): u'p', ord(u'R'): u'r', ord(u'S'): u's', ord(u'Ş'): u'ş', ord(u'T'): u't',
                    ord(u'U'): u'u', ord(u'Ü'): u'ü', ord(u'V'): u'v', ord(u'Y'): u'y', ord(u'Z'): u'z'}
        content = content.translate(lowerMap)
    return [
        utils.to_unicode(token) for token in utils.tokenize(content, lower=False, errors='ignore')
        if token_min_len <= len(token) <= token_max_len and not token.startswith('_')
    ]


if __name__ == '__main__':
    inputFile = "/home/oguzhan/PycharmProjects/OguzModel/trwiki-20200620-pages-articles-multistream.xml.bz2"
    outputFile = "wiki.tr.txt"
    wiki = WikiCorpus(inputFile, lemmatize=False, tokenizer_func=tokenize_tr)
    output = open(outputFile, "w", encoding="utf-8")
    i = 0
    for text in wiki.get_texts():
        output.write(" ".join(text) + "\n")
        i += 1
        if i % 10000 == 0:
            logging.info("Saved " + str(i) + " articles.")
    output.close()
