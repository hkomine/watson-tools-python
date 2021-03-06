'''
dialogListDialogs.py - (C) International Business Machines 2016
--------------------------------------------------------------
Get Dialog accounts list

Created on 2016/05/17

@author: hkomine
'''

import sys
import getopt
import json
import dialogConstants
from watson_developer_cloud import DialogV1 as Dialog

DEBUG=False
VERBOSE=False

def usage():
    print('dialogListDialogs.py -d [enable debug output for script]')

try:
    opts, args = getopt.getopt(sys.argv[1:],"hd",[])
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
    # get dialog object 
    dialog = Dialog(username=dialogConstants.getUsername(), password=dialogConstants.getPassword())
    
    # list dialogs to get client_id and conversation_id
    res = dialog.get_dialogs()
    if DEBUG:
        sys.stdout.write('Response: \n%s\n' % json.dumps(res, indent=2))
    
    sys.stdout.write('Dialog accounts:\n')
    sys.stdout.write('\tdialog_id,\tname\n')
    dialogs = res['dialogs']
    for dialog in dialogs:
        sys.stdout.write('\t%s : %s\n' % (dialog['dialog_id'], dialog['name']))

    sys.stdout.write('\n')
    sys.stdout.write('Language packs accounts:\n')
    sys.stdout.write('\tdialog_id,\tname\n')
    language_packs = res['language_packs']
    for language_pack in language_packs:
        sys.stdout.write('\t%s : %s\n' % (language_pack['dialog_id'], language_pack['name']))

except Exception as e:
    sys.stdout.write(str(e))
    exit(1)