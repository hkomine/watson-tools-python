""" dialogConstants.py - (C) International Business Machines 2016
 --------------------------------------------------------------
 constants and corresponding utility routines for the Watson Dialog Service
 --------------------------------------------------------------
 @author hkomine@jp.ibm.com
"""

import common
import dialogConstants

################################################################
def startConversation(dialog_id, client_id, conversation_id, debug, verbose):
    """  get client_id and conversation_id to start new conversation
    """
    data = "\"client_id=%s&conversation_id=%s&input=\"" % (client_id, conversation_id)
    cmd = "%s %s -X POST --header \"Accept: application/json\" -d %s %s" % (common.getCurlCommand(verbose),
                           dialogConstants.getUsernameAndPW(),
                           data,
                           dialogConstants.getUrlAndCommand(dialog_id, 'conversation'))
    if debug:
        print 'cURL command: %s' % cmd
    return common.issueCmd(cmd)

################################################################
def converse(dialog_id, client_id, conversation_id, message, debug, verbose):
    """  get client_id and conversation_id to start new conversation
    """
    data = "\"client_id=%s&conversation_id=%s&input=%s\"" % (client_id, conversation_id, message)
    cmd = "%s %s -X POST --header \"Accept: application/json\" -d %s %s" % (common.getCurlCommand(verbose),
                           dialogConstants.getUsernameAndPW(),
                           data,
                           dialogConstants.getUrlAndCommand(dialog_id, 'conversation'))
    if debug:
        print 'cURL command: %s' % cmd
    return common.issueCmd(cmd)

################################################################
def listDialogs(debug, verbose):
    """  get client_id and conversation_id to start new conversation
    """
    cmd = "%s %s -X GET --header \"Accept: application/json\" %s" % (common.getCurlCommand(verbose),
                           dialogConstants.getUsernameAndPW(),
                           dialogConstants.getUrl())
    if debug:
        print 'cURL command: %s' % cmd
    return common.issueCmd(cmd)
