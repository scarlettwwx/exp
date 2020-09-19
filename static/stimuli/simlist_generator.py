import sys
import os
import io
from ipapy import UNICODE_TO_IPA
from ipapy import is_valid_ipa
from ipapy.ipachar import IPAConsonant
from ipapy.ipachar import IPAVowel
from ipapy.ipastring import IPAString
import codecs
import re
import operator
import json
# assume that the reference text's index name is the same as their file names
# in static file


# generate a JSON FILE: list of file names, and list of text string of display


reference_path = "ipa1000.csv"
simlist_path = "stimlist.js"

stimuli_dict={} #key: filepaths; value: the sounds_string
with codecs.open(reference_path, 'r', 'utf-8') as f:
    index_string = 0
    for line in f.readlines():
        ipa =line
        ipa = re.sub(r"/",'',ipa).strip("\n").rstrip()
        stimuli_dict["static/mp3s/top1000/" + str(index_string) + ".mp3"] =  ipa
        index_string = index_string + 1


with codecs.open(simlist_path, 'w+','utf-8') as f:
	f.write("var stimuli=")
	json.dump(stimuli_dict, f, ensure_ascii=False)