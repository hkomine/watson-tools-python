#!/usr/bin/env python
""" dialogConversation.py - (C) International Business Machines 2016
 --------------------------------------------------------------
 Start and execute conversation with the a Dialog instance
 @author hkomine@jp.ibm.com
"""
import sys
import getopt
import dialogAPI
import dialogConstants
import urllib
import codecs

dialog_id=''
client_id=''
conversation_id=''
DEBUG=False
VERBOSE=False

def usage():
    print('dialogConversation.py -a <dialog_id> -l <client id> -o <conversation id> -d [enable debug output for script] -v [enable verbose output for curl]')

try:
    opts, args = getopt.getopt(sys.argv[1:],"hdva:l:o:",["dialog_id=","client_id=","conversation_id="])
except getopt.GetoptError as err:
    print str(err)
    print usage()
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
    elif opt == '-v':
        VERBOSE = True

try:
    sys.stdout.write('Watson Dialog conversation app. (Ctrl-z for terminating.)\n')
    
    # check dialog_id and get from constant
    if dialog_id =='':
        dialog_id = dialogConstants.getDialogId()
    
    # start conversation to get client_id and conversation_id
    res = dialogAPI.startConversation(dialog_id, client_id, conversation_id, DEBUG, VERBOSE)
    if DEBUG:
        print('Response: %s\n' % res)

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
            enc_line = urllib.quote(line.encode('utf-8'))
            res = dialogAPI.converse(dialog_id, client_id, conversation_id, enc_line, DEBUG, VERBOSE)
            if DEBUG:
                print('Response: %s' % res)
            messages = res['response']
            for message in messages:
                sys.stdout.write('Dialog> %s\n' % (message))
        sys.stdout.write('You> ')

    # completed
    sys.stdout.write('Terminated.')
    
except Exception as e:
    print str(e)
    exit(1)
