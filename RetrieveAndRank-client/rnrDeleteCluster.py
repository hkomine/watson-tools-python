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
import rnrConstants
from watson_developer_cloud import RetrieveAndRankV1 as RetrieveAndRank

cluster_id=''
DEBUG=False
VERBOSE=False

def usage():
    print('rnrListCollections.py -i [cluster id] -d [enable debug output for script] -v [enable verbose output for curl]')

try:
    opts, args = getopt.getopt(sys.argv[1:],'hdi:',['cluster_id='])
except getopt.GetoptError as err:
    print(str(err))
    print(usage())
    sys.exit(2)
    
for opt, arg in opts:
    if opt == '-h':
        usage()
        sys.exit()
    elif opt in ('-i', '---cluster_id'):
        cluster_id = arg
    elif opt == '-d':
        DEBUG = True

if not cluster_id:
    print('Required argument missing.')
    usage()
    sys.exit(2)

try:
    # list Solr config
    retrieve_and_rank = RetrieveAndRank(url=rnrConstants.getUrl(), username=rnrConstants.getUsername(), password=rnrConstants.getPassword())
    res = retrieve_and_rank.list_collections(cluster_id)
    sys.stdout.write('Response: \n%s\n' % json.dumps(res, indent=2))

except Exception as e:
    sys.stdout.write(str(e))
    exit(1)