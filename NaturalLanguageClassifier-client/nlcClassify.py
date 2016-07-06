'''
dialogConversation.py - (C) International Business Machines 2016
--------------------------------------------------------------
Classify input text with Natural Language Classifier
 
Created on 2016/05/17
@author: hkomine
'''

import sys
import getopt
import json
import nlcConstants
import codecs
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier

classifier_id=''
DEBUG=False
VERBOSE=False

def usage():
    print('nlcGetClassifierInfo.py -c <classifier id> -d [enable debug output for script]')

try:
    opts, args = getopt.getopt(sys.argv[1:],"hdc:",["classifier_id="])
except getopt.GetoptError as err:
    print(str(err))
    print(usage())
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        usage()
        sys.exit()
    elif opt in ("-c", "---classifier_id"):
        classifier_id = arg
    elif opt == '-d':
        DEBUG = True

if not classifier_id:
    print('Required argument missing.')
    usage()
    sys.exit(2)
    
try:
    sys.stdout.write('Watson Natural Language Classifier app. (Ctrl-z for terminating.)\n')
    
    # create classifiers with the training data
    natural_language_classifier = NaturalLanguageClassifier(url=nlcConstants.getUrl(), username=nlcConstants.getUsername(), password=nlcConstants.getPassword())

    # set input encoding - change the encoding name according your platform
    sys.stdin  = codecs.getreader('shift_jis')(sys.stdin)
    
    # loop for classify texts
    sys.stdout.write('Your input> ')
    for line in iter(sys.stdin.readline, ''):
        line = line.rstrip()
        if line != "":
            # send input message - encoding will be done in the SDK
            res = natural_language_classifier.classify(classifier_id, line)
            if DEBUG:
                sys.stdout.write('Response: \n%s\n' % json.dumps(res, indent=2))
                
            sys.stdout.write('Your input was %s\n' % res['text'])
            classes = res['classes']
            index = 0
            for oneclass in classes:
                index=index+1
                sys.stdout.write('%d : %s (%f)\n' % (index, oneclass['class_name'], oneclass['confidence']))
        sys.stdout.write('Your input> ')

    # completed
    sys.stdout.write('Terminated.')
    
except Exception as e:
    sys.stdout.write(str(e))
    exit(1)
