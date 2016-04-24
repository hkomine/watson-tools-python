#!/usr/bin/env python
""" dialogConversation.py - (C) International Business Machines 2016
 --------------------------------------------------------------
 Start and execute conversation with the a Dialog instance
 @author hkomine@jp.ibm.com
"""
import sys
import getopt
import dialogAPI

DEBUG=False
VERBOSE=False

def usage():
    print('dialogConversation.py -d [enable debug output for script] -v [enable verbose output for curl]')

try:
    opts, args = getopt.getopt(sys.argv[1:],"hdv",[])
except getopt.GetoptError as err:
    print str(err)
    print usage()
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        usage()
        sys.exit()
    elif opt == '-d':
        DEBUG = True
    elif opt == '-v':
        VERBOSE = True

try:
    # start conversation to get client_id and conversation_id
    res = dialogAPI.listDialogs(DEBUG, VERBOSE)
    if DEBUG:
        print('Response: %s\n' % res)

    sys.stdout.write('Dialog accounts:\n')
    dialogs = res['dialogs']
    for dialog in dialogs:
        sys.stdout.write('\t%s : %s\n' % (dialog['name'], dialog['dialog_id']))

    sys.stdout.write('\n')
    sys.stdout.write('Language packs accounts:\n')
    language_packs = res['language_packs']
    for language_pack in language_packs:
        sys.stdout.write('\t%s : %s\n' % (language_pack['name'], language_pack['dialog_id']))

except Exception as e:
    print str(e)
    exit(1)
