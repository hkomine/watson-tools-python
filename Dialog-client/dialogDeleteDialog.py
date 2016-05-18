'''
dialogListDialogs.py - (C) International Business Machines 2016
--------------------------------------------------------------
Delete Dialog account

Created on 2016/05/17

@author: hkomine
'''

import sys
import getopt
import json
import dialogConstants
from watson_developer_cloud import DialogV1 as Dialog

dialog_id=''
DEBUG=False
VERBOSE=False

def usage():
    print('dialogDeleteDialog.py -a <dialog_id> -d [enable debug output for script]')

try:
    opts, args = getopt.getopt(sys.argv[1:],"hda:",["dialog_id="])
except getopt.GetoptError as err:
    print(str(err))
    print(usage())
    sys.exit(2)
    
for opt, arg in opts:
    if opt == '-h':
        usage()
        sys.exit()
    elif opt in ("-a", "---dialog_id"):
        dialog_id = arg
    elif opt == '-d':
        DEBUG = True

if not dialog_id:
    print('dialog_id is missing.')
    usage()
    sys.exit(2)

try:
    # get dialog object 
    dialog = Dialog(username=dialogConstants.getUsername(), password=dialogConstants.getPassword())
    
    # delete the specified dialog
    sys.stdout.write('Deleting the dialog account %s ...\n' % dialog_id)
    res = dialog.delete_dialog(dialog_id)
    sys.stdout.write('Response: \n%s\n' % json.dumps(res, indent=2))


except Exception as e:
    sys.stdout.write(str(e))
    exit(1)