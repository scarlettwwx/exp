import codecs
import csv
with codecs.open('ipa1000.csv', 'r', 'utf8') as f:
    file_lines = ['<phoneme alphabet="ipa" ph="' + x.rstrip('\n').rstrip('\r') + '"></phoneme>'
    + '\n' for x in f.readlines()]

with codecs.open('1000_Polly.txt', 'w', 'utf8') as f:
    f.writelines(file_lines)
