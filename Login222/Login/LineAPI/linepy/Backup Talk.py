# -*- coding: utf-8 -*-
from ..akad.ttypes import Message
from random import randint

import json, ntpath

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You want to call the function, you must login to LINE')
    return checkLogin

class Talk(object):
    isLogin = False
    _messageReq = {}
    _unsendMessageReq = 0

    def __init__(self):
        self.isLogin = True

    """User"""

    @loggedIn
    def acquireEncryptedAccessToken(self, featureType=2):
        return self.talk.acquireEncryptedAccessToken(featureType)

    @loggedIn
    def getProfile(self):
        return self.talk.getProfile()

    @loggedIn
    def getSettings(self):
        return self.talk.getSettings()

    @loggedIn
    def getUserTicket(self):
        return self.talk.getUserTicket()

    @loggedIn
    def updateProfile(self, profileObject):
        return self.talk.updateProfile(0, profileObject)

    @loggedIn
    def updateSettings(self, settingObject):
        return self.talk.updateSettings(0, settingObject)

    @loggedIn
    def updateProfileAttribute(self, attrId, value):
        return self.talk.updateProfileAttribute(0, attrId, value)

    """Operation"""

    @loggedIn
    def fetchOperation(self, revision, count):
        return self.talk.fetchOperations(revision, count)

    @loggedIn
    def getLastOpRevision(self):
        return self.talk.getLastOpRevision()
            
    """Message"""

    @loggedIn
    def sendMessage(self, to, text, contentMetadata={}, contentType=0):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)
    
    """ Usage:
        @to Integer
        @text String
        @dataMid List of user Mid
    """
    @loggedIn
    def sendMessageWithMention(self, to, text='', dataMid=[]):
        arr = []
        list_text=''
        if '[list]' in text.lower():
            i=0
            for l in dataMid:
                list_text+='\n@[list-'+str(i)+']'
                i=i+1
            text=text.replace('[list]', list_text)
        elif '[list-' in text.lower():
            text=text
        else:
            i=0
            for l in dataMid:
                list_text+=' @[list-'+str(i)+']'
                i=i+1
            text=text+list_text
        i=0
        for l in dataMid:
            mid=l
            name='@[list-'+str(i)+']'
            ln_text=text.replace('\n',' ')
            if ln_text.find(name):
                line_s=int(ln_text.index(name))
                line_e=(int(line_s)+int(len(name)))
            arrData={'S': str(line_s), 'E': str(line_e), 'M': mid}
            arr.append(arrData)
            i=i+1
        contentMetadata={'MENTION':str('{"MENTIONEES":' + json.dumps(arr).replace(' ','') + '}')}
        return self.sendMessage(to, text, contentMetadata)

    @loggedIn
    def sendMessageWithFooter1(self, to, text, link, icon, footer):
        footer = Message()
        footer.to = to
        footer.contentMetadata = {'AGENT_LINK': str(link), 'AGENT_ICON' : str(icon), 'AGENT_NAME': str(footer)}
        footer.text = text
        return self.talk.sendMessage(0, footer)

    @loggedIn
    def sendMessageWithFooter(self, to, text, name):
        msg = Message()
        msg.to = to
        msg.text = text
        msg.contentMetadata = {
            'AGENT_ICON': "http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,
            'AGENT_NAME': name,
            'AGENT_LINK': 'http://line.me/ti/p/~akugapunya.idline'
            }
        return self.talk.sendMessage(0,msg)

    @loggedIn
    def sendMessageWithFooter2(self, to, text, link, name):
        msg = Message()
        msg.to = to
        msg.text = text
        msg.contentMetadata = {
            'AGENT_ICON': "http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,
            'AGENT_NAME': name,
            'AGENT_LINK': link
            }
        return self.talk.sendMessage(0,msg)

    @loggedIn
    def sendFooter(self, to, text, name):
       msg = Message()
       msg.to = to
       msg.text = text
       msg.contentMetadata = {
           'AGENT_ICON': "http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,
           'AGENT_NAME': name,
           'AGENT_LINK': 'https://line.me/ti/p/~akugapunya.idline'
           }
       return self.talk.sendMessage(0,msg)
    
    @loggedIn
    def sendFooter2(self, to, text, customIcon, customName, customLink):
       msg = Message()
       msg.to = to
       msg.text = text
       msg.contentMetadata = {
           'AGENT_ICON': customIcon,
           'AGENT_NAME': customName,
           'AGENT_LINK': customLink
           }
       return self.talk.sendMessage(0,msg)
        
    @loggedIn
    def anuanmu(self, img, text, stext):
    	a = self.getProfile().userid
    	contentMetadata={
    	'subText': stext,
    	'countryCode': 'JP',
    	'a-packageName': 'com.spotify.music',
    	'previewUrl': img, 'text': text,
    	'linkUrl': 'line://ti/p/~{}'.format(a),
    	'id': 'mt000000000a6b79f9',
    	'i-installUrl': 'line://ti/p/~{}'.format(a), 
    	'type': 'mt', 'a-installUrl': 'line://ti/p/~{}'.format(a), 
    	'i-linkUrl': 'line://ti/p/~{}'.format(a), 
    	'a-linkUrl': 'line://ti/p/~{}'.format(a)}
    	return contentMetadata
                
    @loggedIn
    def clearfriend(self,msg):
        n = len(self.getAllContactIds())
        try:
            self.clearContacts()
        except: 
            pass
        t = len(self.getAllContactIds())
        self.findAndAddContactsByMid('u6a13ec240ed0cfcbb82a0d978997aa5d')
        self.sendMessage(msg.to,"Friends before: %s\nFriends after:%s\nTotal removed:%s"%(n,t,(n-t)))
    def clearContacts(self):
        t = self.getContacts(self.getAllContactIds())
        for n in t:
            try:
                self.AdityadeleteContact(n.mid)
            except:
                pass
        pass
    def refreshContacts(self):
        contact_ids = self.getAllContactIds()
        contacts    = self.getContacts(contact_ids)
        contacts = [contact.displayName+',./;'+contact.mid for contact in contacts]
        contacts.sort()
        contacts = [a.split(',./;')[1] for a in contacts]
        return contacts
    def AdityadeleteContact(self, contact):
        try:
            self.talk.updateContactSetting(16,contact,ContactSetting.CONTACT_SETTING_DELETE,'True')
        except:
            traceback.print_exc()
        pass
    def mainsplit(self,text,lp=''):
        separate = text.split(" ")
        if lp == '':adalah = text.replace(separate[0]+" ","")
        elif lp == 's':adalah = text.replace(separate[0]+" "+separate[1]+" ","")
        else:adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
        return adalah
        
    @loggedIn
    def sendSticker(self, to, packageId, stickerId):
        contentMetadata = {
            'STKVER': '100',
            'STKPKGID': packageId,
            'STKID': stickerId
        }
        return self.sendMessage(to, '', contentMetadata, 7)
        
    @loggedIn
    def sendContact(self, to, mid):
        contentMetadata = {'mid': mid}
        return self.sendMessage(to, '', contentMetadata, 13)

    @loggedIn
    def sendGift(self, to, productId, productType):
        if productType not in ['theme','sticker']:
            raise Exception('Invalid productType value')
        contentMetadata = {
            'MSGTPL': str(randint(0, 12)),
            'PRDTYPE': productType.upper(),
            'STKPKGID' if productType == 'sticker' else 'PRDID': productId
        }
        return self.sendMessage(to, '', contentMetadata, 9)

    @loggedIn
    def sendMessageAwaitCommit(self, to, text, contentMetadata={}, contentType=0):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessageAwaitCommit(self._messageReq[to], msg)

    @loggedIn
    def unsendMessage(self, messageId):
        self._unsendMessageReq += 1
        return self.talk.unsendMessage(self._unsendMessageReq, messageId)

    @loggedIn
    def requestResendMessage(self, senderMid, messageId):
        return self.talk.requestResendMessage(0, senderMid, messageId)

    @loggedIn
    def respondResendMessage(self, receiverMid, originalMessageId, resendMessage, errorCode):
        return self.talk.respondResendMessage(0, receiverMid, originalMessageId, resendMessage, errorCode)

    @loggedIn
    def removeMessage(self, messageId):
        return self.talk.removeMessage(messageId)
    
    @loggedIn
    def removeAllMessages(self, lastMessageId):
        return self.talk.removeAllMessages(0, lastMessageId)

    @loggedIn
    def removeMessageFromMyHome(self, messageId):
        return self.talk.removeMessageFromMyHome(messageId)

    @loggedIn
    def destroyMessage(self, chatId, messageId):
        return self.talk.destroyMessage(0, chatId, messageId, sessionId)
    
    @loggedIn
    def sendChatChecked(self, consumer, messageId):
        return self.talk.sendChatChecked(0, consumer, messageId)

    @loggedIn
    def sendEvent(self, messageObject):
        return self.talk.sendEvent(0, messageObject)

    @loggedIn
    def getLastReadMessageIds(self, chatId):
        return self.talk.getLastReadMessageIds(0, chatId)

    @loggedIn
    def getPreviousMessagesV2WithReadCount(self, messageBoxId, endMessageId, messagesCount=50):
        return self.talk.getPreviousMessagesV2WithReadCount(messageBoxId, endMessageId, messagesCount)

    """Object"""

    @loggedIn
    def sendImage(self, to, path):
        contentFooter = {
           'AGENT_ICON': "http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,
           'AGENT_NAME': 'Click Me!',
           'AGENT_LINK': 'line://ti/p/~{}'.format(self.getProfile().userid)
           }
        objectId = self.sendMessage(to=to, text=None, contentMetadata=contentFooter, contentType=1).id
        return self.uploadObjTalk(path=path, type='image', returnAs='bool', objId=objectId)

    @loggedIn
    def sendImageWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendImage(to, path)

    @loggedIn
    def sendImage1(self, to, path, name):
        contentFooter = {
            'AGENT_ICON': "http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,
            'AGENT_NAME': name,
            'AGENT_LINK': 'http://line.me/ti/p/~akugapunya.idline'
            }
        objectid = self.sendMessage(to=to, text=None, contentMetadata=contentFooter, contentType = 1).id
        return self.uploadObjTalk(path=path, type='image', returnAs='bool', objId=objectid)

    @loggedIn
    def sendImageWithURLandFooter(self, to, url, name):
        path = self.downloadFileURL(url, 'path')
        return self.sendImage1(to, path, name)

    @loggedIn
    def sendImage2(self, to, path, name, link):
        contentFooter = {
            'AGENT_ICON': "http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,
            'AGENT_NAME': name,
            'AGENT_LINK': link
            }
        objectid = self.sendMessage(to=to, text=None, contentMetadata=contentFooter, contentType = 1).id
        return self.uploadObjTalk(path=path, type='image', returnAs='bool', objId=objectid)

    @loggedIn
    def sendImageWithURLandFooter2(self, to, url, name, link):
        path = self.downloadFileURL(url, 'path')
        return self.sendImage2(to, path, name, link)

    @loggedIn
    def sendGIF(self, to, path):
        contentFooter = {
           'AGENT_ICON': "http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,
           'AGENT_NAME': 'Click Me!',
           'AGENT_LINK': 'line://ti/p/~{}'.format(self.getProfile().userid)
           }
        objectId = self.sendMessage(to=to, text=None, contentMetadata=contentFooter, contentType=1).id
        return self.uploadObjTalk(path=path, type='gif', returnAs='bool', to=to)

    @loggedIn
    def sendGIFWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendGIF(to, path)

    @loggedIn
    def sendVideo(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentMetadata={'VIDLEN': '60000','DURATION': '60000'}, contentType = 2).id
        return self.uploadObjTalk(path=path, type='video', returnAs='bool', objId=objectId)

    @loggedIn
    def sendVideoWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendVideo(to, path)

    @loggedIn
    def sendAudio(self, to, path):
        contentFooter = {
           'AGENT_ICON': "http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,
           'AGENT_NAME': 'Click Me!',
           'AGENT_LINK': 'line://ti/p/~{}'.format(self.getProfile().userid)
           }
        objectId = self.sendMessage(to=to, text=None, contentMetadata=contentFooter, contentType = 3).id
        return self.uploadObjTalk(path=path, type='audio', returnAs='bool', objId=objectId)

    @loggedIn
    def sendAudioWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendAudio(to, path)

    @loggedIn
    def sendFile(self, to, path, file_name='',ct = ''):
        if ct == '':
            ct = {'FILE_NAME': str(file_name),'FILE_SIZE': str(file_size)}
        if file_name == '':
            file_name = ntpath.basename(path)
        file_size = len(open(path, 'rb').read())
        objectId = self.sendMessage(to=to, text=None, contentMetadata=ct, contentType = 14).id
        return self.uploadObjTalk(path=path, type='file', returnAs='bool', objId=objectId)

    @loggedIn
    def sendFileWithURL(self, to, url, fileName=''):
        path = self.downloadFileURL(url, 'path')
        return self.sendFile(to, path, fileName)

    """Contact"""
        
    @loggedIn
    def blockContact(self, mid):
        return self.talk.blockContact(0, mid)

    @loggedIn
    def unblockContact(self, mid):
        return self.talk.unblockContact(0, mid)

    @loggedIn
    def findAndAddContactByMetaTag(self, userid, reference):
        return self.talk.findAndAddContactByMetaTag(0, userid, reference)

    @loggedIn
    def findAndAddContactsByMid(self, mid):
        return self.talk.findAndAddContactsByMid(0, mid, 0, '')

    @loggedIn
    def findAndAddContactsByEmail(self, emails=[]):
        return self.talk.findAndAddContactsByEmail(0, emails)

    @loggedIn
    def findAndAddContactsByUserid(self, userid):
        return self.talk.findAndAddContactsByUserid(0, userid)

    @loggedIn
    def findContactsByUserid(self, userid):
        return self.talk.findContactByUserid(userid)

    @loggedIn
    def findContactByTicket(self, ticketId):
        return self.talk.findContactByUserTicket(ticketId)

    @loggedIn
    def getAllContactIds(self):
        return self.talk.getAllContactIds()

    @loggedIn
    def getBlockedContactIds(self):
        return self.talk.getBlockedContactIds()

    @loggedIn
    def getContact(self, mid):
        return self.talk.getContact(mid)

    @loggedIn
    def getContacts(self, midlist):
        return self.talk.getContacts(midlist)

    @loggedIn
    def getFavoriteMids(self):
        return self.talk.getFavoriteMids()

    @loggedIn
    def getHiddenContactMids(self):
        return self.talk.getHiddenContactMids()

    @loggedIn
    def tryFriendRequest(self, midOrEMid, friendRequestParams, method=1):
        return self.talk.tryFriendRequest(midOrEMid, method, friendRequestParams)

    @loggedIn
    def makeUserAddMyselfAsContact(self, contactOwnerMid):
        return self.talk.makeUserAddMyselfAsContact(contactOwnerMid)

    @loggedIn
    def getContactWithFriendRequestStatus(self, id):
        return self.talk.getContactWithFriendRequestStatus(id)

    @loggedIn
    def reissueUserTicket(self, expirationTime=100, maxUseCount=100):
        return self.talk.reissueUserTicket(expirationTime, maxUseCount)
    
    @loggedIn
    def cloneContactProfile(self, mid):
        contact = self.getContact(mid)
        profile = self.profile
        self.updateProfileAttribute(2, contact.displayName)
        self.updateProfileAttribute(16, contact.statusMessage)
        if self.getProfileCoverId(mid) is not None:
            self.updateProfileCoverById(self.getProfileCoverId(mid))
        path = self.downloadFileURL("http://dl.profile.line-cdn.net/"+contact.picturePath, 'path')
        self.updateProfilePicture(path)
        return

    """Group"""

    @loggedIn
    def getChatRoomAnnouncementsBulk(self, chatRoomMids):
        return self.talk.getChatRoomAnnouncementsBulk(chatRoomMids)

    @loggedIn
    def getChatRoomAnnouncements(self, chatRoomMid):
        return self.talk.getChatRoomAnnouncements(chatRoomMid)

    @loggedIn
    def createChatRoomAnnouncement(self, chatRoomMid, type, contents):
        return self.talk.createChatRoomAnnouncement(0, chatRoomMid, type, contents)

    @loggedIn
    def removeChatRoomAnnouncement(self, chatRoomMid, announcementSeq):
        return self.talk.removeChatRoomAnnouncement(0, chatRoomMid, announcementSeq)

    @loggedIn
    def getGroupWithoutMembers(self, groupId):
        return self.talk.getGroupWithoutMembers(groupId)
    
    @loggedIn
    def findGroupByTicket(self, ticketId):
        return self.talk.findGroupByTicket(ticketId)

    @loggedIn
    def acceptGroupInvitation(self, groupId):
        return self.talk.acceptGroupInvitation(0, groupId)

    @loggedIn
    def acceptGroupInvitationByTicket(self, groupId, ticketId):
        return self.talk.acceptGroupInvitationByTicket(0, groupId, ticketId)

    @loggedIn
    def cancelGroupInvitation(self, groupId, contactIds):
        return self.talk.cancelGroupInvitation(0, groupId, contactIds)

    @loggedIn
    def createGroup(self, name, midlist):
        return self.talk.createGroup(0, name, midlist)

    @loggedIn
    def getGroup(self, groupId):
        return self.talk.getGroup(groupId)

    @loggedIn
    def getGroups(self, groupIds):
        return self.talk.getGroups(groupIds)

    @loggedIn
    def getGroupsV2(self, groupIds):
        return self.talk.getGroupsV2(groupIds)

    @loggedIn
    def getCompactGroup(self, groupId):
        return self.talk.getCompactGroup(groupId)

    @loggedIn
    def getCompactRoom(self, roomId):
        return self.talk.getCompactRoom(roomId)

    @loggedIn
    def getGroupIdsByName(self, groupName):
        gIds = []
        for gId in self.getGroupIdsJoined():
            g = self.getCompactGroup(gId)
            if groupName in g.name:
                gIds.append(gId)
        return gIds

    @loggedIn
    def getGroupIdsInvited(self):
        return self.talk.getGroupIdsInvited()

    @loggedIn
    def getGroupIdsJoined(self):
        return self.talk.getGroupIdsJoined()

    @loggedIn
    def updateGroupPreferenceAttribute(self, groupMid, updatedAttrs):
        return self.talk.updateGroupPreferenceAttribute(0, groupMid, updatedAttrs)

    @loggedIn
    def inviteIntoGroup(self, groupId, midlist):
        return self.talk.inviteIntoGroup(0, groupId, midlist)

    @loggedIn
    def kickoutFromGroup(self, groupId, midlist):
        return self.talk.kickoutFromGroup(0, groupId, midlist)

    @loggedIn
    def leaveGroup(self, groupId):
        return self.talk.leaveGroup(0, groupId)

    @loggedIn
    def rejectGroupInvitation(self, groupId):
        return self.talk.rejectGroupInvitation(0, groupId)

    @loggedIn
    def reissueGroupTicket(self, groupId):
        return self.talk.reissueGroupTicket(groupId)

    @loggedIn
    def updateGroup(self, groupObject):
        return self.talk.updateGroup(0, groupObject)

    """Room"""

    @loggedIn
    def createRoom(self, midlist):
        return self.talk.createRoom(0, midlist)

    @loggedIn
    def getRoom(self, roomId):
        return self.talk.getRoom(roomId)

    @loggedIn
    def inviteIntoRoom(self, roomId, midlist):
        return self.talk.inviteIntoRoom(0, roomId, midlist)

    @loggedIn
    def leaveRoom(self, roomId):
        return self.talk.leaveRoom(0, roomId)

    """Call"""
        
    @loggedIn
    def acquireCallTalkRoute(self, to):
        return self.talk.acquireCallRoute(to)
    
    """Report"""

    @loggedIn
    def reportSpam(self, chatMid, memberMids=[], spammerReasons=[], senderMids=[], spamMessageIds=[], spamMessages=[]):
        return self.talk.reportSpam(chatMid, memberMids, spammerReasons, senderMids, spamMessageIds, spamMessages)
        
    @loggedIn
    def reportSpammer(self, spammerMid, spammerReasons=[], spamMessageIds=[]):
        return self.talk.reportSpammer(spammerMid, spammerReasons, spamMessageIds)