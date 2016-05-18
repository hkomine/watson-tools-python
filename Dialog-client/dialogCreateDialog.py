'''
dialogListDialogs.py - (C) International Business Machines 2016
--------------------------------------------------------------
Create Dialog account

Created on 2016/05/17

@author: hkomine
'''

import sys
import getopt
import json
import dialogConstants
from watson_developer_cloud import DialogV1 as Dialog

dialog_filepath=''
name=''
DEBUG=False
VERBOSE=False

def usage():
    print('dialogListDialog.py -f <dialog filepath> -n <dialog name> -d [enable debug output for script]')

try:
    opts, args = getopt.getopt(sys.argv[1:],"hdf:n:",["dialogfile=", "name="])
except getopt.GetoptError as err:
    print(str(err))
    print(usage())
    sys.exit(2)
    
for opt, arg in opts:
    if opt == '-h':
        usage()
        sys.exit()
    elif opt in ("-f", "---dialogfile"):
        dialog_filepath = arg
    elif opt in ("-n", "---name"):
        name = arg
    elif opt == '-d':
        DEBUG = True

if not dialog_filepath or not name:
    print('Required argument missing.')
    usage()
    sys.exit(2)

try:
    # get dialog object 
    dialog = Dialog(username=dialogConstants.getUsername(), password=dialogConstants.getPassword())
    
    # create a dialog
    sys.stdout.write('Creating dialog %s\n' % name)
    with open(dialog_filepath, 'rb') as dialog_file:
        res = dialog.create_dialog(dialog_file, name)
        sys.stdout.write('Response: \n%s\n' % json.dumps(res, indent=2))


except Exception as e:
    sys.stdout.write(str(e))
    exit(1)