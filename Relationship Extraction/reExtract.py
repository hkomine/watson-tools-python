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
import reConstants
import codecs
from watson_developer_cloud import RelationshipExtractionV1Beta as RelationshipExtraction

sid=''
return_type='json'
DEBUG=False
VERBOSE=False

def usage():
    print('nlcGetClassifierInfo.py -s <dataset> -r <return type> -d [enable debug output for script]')
    print('\t Available datasets are:')
    print('\t\t ie-en-news for English')
    print('\t\t ie-es-news for Spanish')
    print('\t\t ie-ja-seg for Japanese (Dark feature)')

try:
    opts, args = getopt.getopt(sys.argv[1:],"hds:r:",["sid=","return_type="])
except getopt.GetoptError as err:
    print(str(err))
    print(usage())
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        usage()
        sys.exit()
    elif opt in ("-s", "---sid"):
        sid = arg
    elif opt in ("-r", "---return_type"):
        return_type = arg
    elif opt == '-d':
        DEBUG = True

if not sid:
    print('Required argument missing.')
    usage()
    sys.exit(2)
    
try:
    sys.stdout.write('Watson Relationship Extraction app. (Ctrl-z for terminating.)\n')
    
    # create classifiers with the training data
    relationship_extraction = RelationshipExtraction(username=reConstants.getUsername(), password=reConstants.getPassword())

    # set input encoding - change the encoding name according your platform
    sys.stdin  = codecs.getreader('shift_jis')(sys.stdin)
    
    # loop for classify texts
    sys.stdout.write('Your input> ')
    for line in iter(sys.stdin.readline, ''):
        line = line.rstrip()
        if line != "":
            # send input message - encoding will be done in the SDK
            res = relationship_extraction.extract(line, sid, return_type)
            sys.stdout.write('Response: \n%s\n' % json.dumps(res, indent=2))
                
        sys.stdout.write('Your input> ')

    # completed
    sys.stdout.write('Terminated.')
    
except Exception as e:
    sys.stdout.write(str(e))
    exit(1)
