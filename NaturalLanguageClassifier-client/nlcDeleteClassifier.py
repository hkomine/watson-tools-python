'''
dialogConversation.py - (C) International Business Machines 2016
--------------------------------------------------------------
Delete classifier
 
Created on 2016/05/17
@author: hkomine
'''

import sys
import getopt
import json
import nlcConstants
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
    # create classifiers with the training data
    natural_language_classifier = NaturalLanguageClassifier(url=nlcConstants.getUrl(), username=nlcConstants.getUsername(), password=nlcConstants.getPassword())

    # Delete the classifier
    sys.stdout.write('Deleting the classifier %s ...\n' % classifier_id)
    res = natural_language_classifier.remove(classifier_id)
    sys.stdout.write('Response: \n%s\n' % json.dumps(res, indent=2))

except Exception as e:
    sys.stdout.write(str(e))
    exit(1)
