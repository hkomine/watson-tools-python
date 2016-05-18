'''
dialogConversation.py - (C) International Business Machines 2016
--------------------------------------------------------------
Start and execute conversation with the a Dialog instance
 
Created on 2016/05/17
@author: hkomine
'''

import sys
import getopt
import json
import dialogConstants
import codecs
from watson_developer_cloud import DialogV1 as Dialog

dialog_id=''
client_id=''
conversation_id=''
DEBUG=False
VERBOSE=False

def usage():
    print('dialogConversation.py -a <dialog_id> -l <client id> -o <conversation id> -d [enable debug output for script]')

try:
    opts, args = getopt.getopt(sys.argv[1:],"hda:l:o:",["dialog_id=","client_id=","conversation_id="])
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
    elif opt in ("-l", "--client_id"):
        client_id = arg
    elif opt in ("-o", "--conversatin_id"):
        conversation_id = arg
    elif opt == '-d':
        DEBUG = True

if not dialog_id:
    print('dialog_id is missing.')
    usage()
    sys.exit(2)
    
try:
    sys.stdout.write('Watson Dialog conversation app. (Ctrl-z for terminating.)\n')
    
    # get dialog object 
    dialog = Dialog(username=dialogConstants.getUsername(), password=dialogConstants.getPassword())   
    
    # check dialog_id and get from constant
    if dialog_id =='':
        dialog_id = dialogConstants.getDialogId()
    
    # start conversation to get client_id and conversation_id
    res = dialog.conversation(dialog_id, '', client_id, conversation_id)
    if DEBUG:
        sys.stdout.write('Response: \n%s\n' % json.dumps(res, indent=2))

    client_id = res['client_id']
    sys.stdout.write('client_id = %s\n' % (client_id))
    conversation_id = res['conversation_id']
    sys.stdout.write('conversation_id = %s\n' % (conversation_id))

    messages = res['response']
    for message in messages:
        sys.stdout.write('Dialog> %s\n' % (message))

    # set input encoding - change the encoding name according your platform
    sys.stdin  = codecs.getreader('shift_jis')(sys.stdin)
    
    # conversation loop
    sys.stdout.write('You> ')
    for line in iter(sys.stdin.readline, ''):
        line = line.rstrip()
        if line != "":
            # send input message - encoding will be done in the SDK
            res = dialog.conversation(dialog_id, line, client_id, conversation_id)
            if DEBUG:
                sys.stdout.write('Response: \n%s\n' % json.dumps(res, indent=2))
                sys.stdout.write('Your input was %s\n' % res['input'])
                
            messages = res['response']
            for message in messages:
                sys.stdout.write('Dialog> %s\n' % (message))
        sys.stdout.write('You> ')

    # completed
    sys.stdout.write('Terminated.')
    
except Exception as e:
    sys.stdout.write(str(e))
    exit(1)
