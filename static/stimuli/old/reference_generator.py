import codecs
import csv

with codecs.open('BLICK_reference.csv', 'r', 'utf8') as f:
    file_lines = [x.replace(',', '\t') for x in f.readlines()]

with codecs.open('BLICK_reference.txt', 'a+', 'utf8') as f:
    f.writelines(file_lines)
