'''
nlcListClassifier.py - (C) International Business Machines 2016
--------------------------------------------------------------
Get Classifiers list

Created on 2016/05/17

@author: hkomine
'''

import sys
import getopt
import json
import nlcConstants
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier

DEBUG=False
VERBOSE=False

def usage():
    print('nlcListClassifiers.py -d [enable debug output for script] -v [enable verbose output for curl]')

try:
    opts, args = getopt.getopt(sys.argv[1:],"hdv",[])
except getopt.GetoptError as err:
    print(str(err))
    print(usage())
    sys.exit(2)
    
for opt, arg in opts:
    if opt == '-h':
        usage()
        sys.exit()
    elif opt == '-d':
        DEBUG = True

try:
    # list classifiers to get classifier_id
    natural_language_classifier = NaturalLanguageClassifier(url=nlcConstants.getUrl(), username=nlcConstants.getUsername(), password=nlcConstants.getPassword())
    res = natural_language_classifier.list()
    sys.stdout.write('Response: \n%s\n' % json.dumps(res, indent=2))

#    sys.stdout.write('Classifiers:\n')
#    sys.stdout.write('classifier_id,\tname,\tlanguage,\tcreated,\turl')
#    classifiers = res['classifiers']
#    for classifier in classifiers:
#        sys.stdout.write('%s,\t%s,\t%s,\t%s,\t%s\n' % (classifier['classifier_id'], classifier['name'], classifier['language'], classifier['created'], classifier['url']))

except Exception as e:
    sys.stdout.write(str(e))
    exit(1)