'''
nlcCreateClassifier.py - (C) International Business Machines 2016
--------------------------------------------------------------
Create a Classifier with the specified training data

Created on 2016/05/18

@author: hkomine
'''

import sys
import getopt
import json
import nlcConstants
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier

trainingdata_filepath=''
name=''
language=''
DEBUG=False
VERBOSE=False

def usage():
    print('nlcCreateClassifier.py -t <training data file path> -n <classifier name> -l <ISO language code> -d [enable debug output for script]')

try:
    opts, args = getopt.getopt(sys.argv[1:],"hdt:n:l:",["trainingdata=","name=","language"])
except getopt.GetoptError as err:
    print(str(err))
    print(usage())
    sys.exit(2)
    
for opt, arg in opts:
    if opt == '-h':
        usage()
        sys.exit()
    elif opt in ("-t", "---trainingdata"):
        trainingdata_filepath = arg
    elif opt in ("-n", "---name"):
        name = arg
    elif opt in ("-l", "---language"):
        language = arg
    elif opt == '-d':
        DEBUG = True

if not trainingdata_filepath or not name or not language:
    print('Required argument missing.')
    usage()
    sys.exit(2)
    
try:   
    # create classifiers with the training data
    natural_language_classifier = NaturalLanguageClassifier(username=nlcConstants.getUsername(), password=nlcConstants.getPassword())
    with open(trainingdata_filepath, 'rb') as training_data:
        res = natural_language_classifier.create(training_data, name, language)
        sys.stdout.write('Response: \n%s\n' % json.dumps(res, indent=2))

except Exception as e:
    sys.stdout.write(str(e))
    exit(1)
