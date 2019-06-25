# -*- coding: utf-8 -*-
from LineAPI.akad.ttypes import Message, Location
from LineAPI.akad.ttypes import *
from random import randint
from mencode import *
import json, ntpath, requests, shutil, tempfile,os, urllib,time,asyncio,base64

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
    def sendMention(self,to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@Arfinee Meka "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        self.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~{}'.format(self.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,'AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    """ Usage:
        @to Integer
        @text String
        @dataMid List of user Mid
    """
    @loggedIn
    def generateReplyMessage(self, relatedMessageId):
        msg = Message()
        msg.relatedMessageServiceCode = 1
        msg.messageRelationType = 3
        msg.relatedMessageId = str(relatedMessageId)
        return msg

    @loggedIn
    def sendReplyMessage(self, relatedMessageId, to, text, contentMetadata={}, contentType=0):
        msg = self.generateReplyMessage(relatedMessageId)
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType = contentType
        msg.contentMetadata = contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)
        
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
    def sendMessageWithMention3(self, to, mid, firstmessage, lastmessage):
        try:
            arrData = ""
            text = "%s " %(str(firstmessage))
            arr = []
            mention = "@x "
            slen = str(len(text))
            elen = str(len(text) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':mid}
            arr.append(arrData)
            text += mention + str(lastmessage)
            self.sendMessage(to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as error:
            print(error)

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
    def deleteContact(self, contact):
        return self.talk.updateContactSetting(16,contact,ContactSetting.CONTACT_SETTING_DELETE,'True')
        
    @loggedIn
    def clearContacts(self):
        t = self.getContacts(self.getAllContactIds())
        for n in t:
            try:
                self.deleteContact(n.mid)
            except:
                pass
        pass
        
    @loggedIn
    def clearfriend(self,msg):
        n = len(self.getAllContactIds())
        try:
            self.clearContacts()
        except: 
            pass
        t = len(self.getAllContactIds())
        self.findAndAddContactsByMid('u60e46c914992f5acb02f1fa618a0f630')
        self.sendMessage(msg.to,"Friends before: %s\nFriends after:%s\nTotal removed:%s"%(n,t,(n-t)))
        
    @loggedIn
    def anuanmu(self,img,text,stext):
        contentMetadata={'previewUrl': img, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': str(stext), 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': str(text), 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.line.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1'}
        return contentMetadata
                
    @loggedIn
    def sendCarousel(self, col):
        col = json.dumps(col)
        r = requests.session().post('https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage',headers={'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.1; ASUS_X00ID Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/7.11.2','Content-Type':'application/json','Connection':'keep-alive','Accept':'*/*','Accept-Encoding':'gzip, deflate'},data=col)
        return r.text
    def adityaarchi(self,sd,dd,ss,split,msg,tex,nama=[]):
        selection = mencode(split,range(1,len(nama)+1))
        k = len(nama)//100
        for a in range(k+1):
            if a == 0:eto='「 '+sd+' 」'
            else:eto=''
            text = ''
            mids = []
            no = a
            for i in selection.parse()[a*100 : (a+1)*100]:
                mids.append(nama[i-1])
                if dd == 'kick':self.kickoutFromGroup(ss,[nama[i-1]]);hh = ''
                if dd == 'delfriend':
                    try:self.deleteContact(nama[i-1]);hh = 'Del Friend'
                    except:hh = 'Not Friend User'
                if dd == '':hh = ''
                if dd == 'tag':hh = ''
                no+= 1
                if no == len(selection.parse()):text+= "\n{}. @! {}".format(i,hh)
                else:text+= "\n{}. @! {}".format(i,hh)
            if dd == 'tag':self.sendMention(ss,eto+text,sd,mids)
            else:self.sendMention(msg.to,eto+text,sd,mids)
        if dd == 'tag':self.sendMessage(msg.to,'Status: Success tag {} mem'.format(tex,len(nama)-(len(nama)-len(selection.parse()))))
    def datamention(self,msg,text,data,ps=''):
        if(data == [] or data == {}):return self.sendMention(msg.to," 「 {} 」\nSorry @! I can't found maybe empty".format(text),text,[msg._from])
        k = len(data)//20
        for aa in range(k+1):
            if aa == 0:dd = '「 {} 」{}'.format(text,ps);no=aa
            else:dd = '';no=aa*20
            msgas = dd
            for i in data[aa*20 : (aa+1)*20]:
                no+=1
                if no == len(data):msgas+='\n{}. @!'.format(no)
                else:msgas+='\n{}. @!'.format(no)
            self.sendMention(msg.to, msgas,' 「 {} 」'.format(text), data[aa*20 : (aa+1)*20])
    def getinformation(self,to,mid,data):
        try:
            h = self.getContact(mid).statusMessage
            if h == '':hh = '\n'
            else:hh = "Status:\n" + h + "\n\n"
            zxc = " 「 ID 」\nName: @!\n" + hh + "User ID:\n" + mid + "\n"+a+" "+b
            self.sendMention(to, zxc, '',[mid])
            self.sendContact(to,mid)
        except:
            ginfo = self.getCompactGroup(mid)
            try:
                gCreators = ginfo.creator.mid;gtime = ginfo.createdTime
            except:
                gCreators = ginfo.members[0].mid;gtime = ginfo.createdTime
            if ginfo.invitee is None:
                sinvitee = "0"
            else:
                sinvitee = str(len(ginfo.invitee))
            if ginfo.preventedJoinByTicket == True:u = "Disable"
            else:u = "line://ti/g/" + self.reissueGroupTicket(mid)
            zxc = " 「 ID 」\nGroup Name:\n{}\n\nGroup ID:\n{}\n\nAnggota: {}\nInvitation: {}\nTicket:{}\n\nCreated at:\n{}\nby @!".format(ginfo.name,mid,len(ginfo.members),sinvitee,u,humanize.naturaltime(datetime.fromtimestamp(gtime/1000)))
            self.sendMention(to,zxc,'',[gCreators])
            self.sendContact(to,gCreators)
    def lsgroup(self,msg,cmd):
        to = msg.to
        gid = self.getGroupIdsJoined()
        group = self.getGroup(gid[int(cmd.split(' ')[1])-1])
        nama = [a.mid for a in group.members]
        if len(cmd.split(" ")) == 2:
            total = "Local ID: {}".format(int(cmd.split(' ')[1]))
            self.datamention(msg,'List Member',nama)
        if len(cmd.split(" ")) == 4:
            if cmd.startswith('grouplist '+cmd.split(' ')[1]+' mem '):self.getinformation(to,nama[int(cmd.split(' ')[3])-1])
            if cmd.startswith('grouplist '+cmd.split(' ')[1]+' tag'):self.adityaarchi('Mention','tag',gid[int(cmd.split(' ')[1])-1],cmd.split(' ')[3],msg,"Group: {}\nLocal ID: {}".format(group.name[:20],int(cmd.split(' ')[1])),nama=nama)
            if cmd.startswith('grouplist '+cmd.split(' ')[1]+' kick'):self.adityaarchi('Kick Member','kick',gid[int(cmd.split(' ')[1])-1],cmd.split(' ')[3],msg,"Group: {}\nLocal ID: {}".format(group.name[:20],int(cmd.split(' ')[1])),nama=nama)
    def delgroups(self,to,cmd):
        gid = self.getGroupIdsJoined()
        if len(cmd.split(" ")) == 3:
            selection = mencode(cmd.split(' ')[2],range(1,len(gid)+1))
            k = len(gid)//100
            for a in range(k+1):
                if a == 0:eto='╭「 Leave Group 」─'
                else:eto=''
                text = ''
                no = 0
                for i in selection.parse()[a*100 : (a+1)*100]:
                    self.leaveGroup(gid[i - 1])
                    no+=1
                    if no == len(selection.parse()):text+= "\n╰{}. {}".format(i,self.getGroup(gid[i - 1]).name)
                    else:text+= "\n│{}. {}".format(i,self.getGroup(gid[i - 1]).name)
                self.sendMessage(to,eto+text)
    def openqr(self,to,cmd):
        gid = self.getGroupIdsJoined()
        if len(cmd.split(" ")) == 3:
            selection = mencode(cmd.split(' ')[2],range(1,len(gid)+1))
            k = len(gid)//100
            for a in range(k+1):
                if a == 0:eto='╭「 QR Group 」─'
                else:eto=''
                text = ''
                no = 0
                for i in selection.parse()[a*100 : (a+1)*100]:
                    group = self.getGroup(gid[i - 1])
                    if group.preventedJoinByTicket == True:
                        group.preventedJoinByTicket = False
                        self.updateGroup(group)
                    no+=1
                    if no == len(selection.parse()):text+= "\n│{}. {}\n╰   line://ti/g/{}".format(i,self.getGroup(gid[i - 1]).name,self.reissueGroupTicket(gid[i - 1]))
                    else:text+= "\n│{}. {}\n│   line://ti/g/{}".format(i,self.getGroup(gid[i - 1]).name,self.reissueGroupTicket(gid[i - 1]))
                self.sendMessage(to,eto+text)
    def mainsplit(self,text,lp=''):
        separate = text.split(" ")
        if lp == '':adalah = text.replace(separate[0]+" ","")
        elif lp == 's':adalah = text.replace(separate[0]+" "+separate[1]+" ","")
        else:adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
        return adalah
        
    def surahlist(self, msg):
        if msg.text.lower() == "alquran":data = self.requestsin("http://api.alquran.cloud/surah")
        if msg.text.lower().startswith("alqur'an "):data = self.requestsin("http://api.alquran.cloud/surah/{}".format(self.mainsplit(msg.text)))
        if len(msg.text.split(' ')) == 1:
            if data["data"] != []:
                no = 0
                ret_ = "「 Al Qur'an 」\n"
                for music in data["data"]:
                    no += 1
                    if no == len(data['data']):ret_ += "\n{}. {}".format(no,music['englishName'])
                    else:ret_ += "\n{}. {}".format(no,music['englishName'])
                return self.sendMessage(msg.to, ret_)
        if len(msg.text.split(' ')) == 2:
            try:
                no = 0
                ret_ = " 「 Al Qur'an 」\nSurah: {}".format(data['data']['englishName'])
                for music in data["data"]["ayahs"]:
                    no += 1
                    ret_ += "\n{}. {}".format(no,music['text'])
                k = len(ret_)//9999
                for aa in range(k+1):
                    self.sendMessage(msg.to,'{}'.format(ret_[aa*9999 : (aa+1)*9999]))
            except:pass
        if len(msg.text.split(' ')) == 3:
            try:
                nama = data["data"]["ayahs"]
                selection = mencode(self.mainsplit(msg.text.lower(),'s'),range(1,len(nama)+1))
                k = len(nama)//100
                text = " 「 Al Qur'an 」\nSurah: {}".format(data['data']['englishName'])
                no = 0
                for i in selection.parse():
                    no+= 1
                    text+= "\n{}. {}".format(i,nama[i-1]['text'])
                k = len(text)//10000
                for aa in range(k+1):
                    self.sendMessage(to,'{}'.format(text[aa*10000 : (aa+1)*10000]))
            except:pass
    def requestsin(self,url):
        r = requests.get("{}".format(url))
        data = r.text
        data = json.loads(data)
        return data
            
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
    def sendLocation(self, to, latitude, longitude, address, title):
        msg = Message()
        msg.to = to
        msg.contentMetadata = {}
        msg.location = Location(latitude=latitude, longitude=longitude, address=address, title=title, phone=None)
        return self.talk.sendMessage(0,msg)
        
    @loggedIn
    def renameContact(self, contact, text):
    	return self.talk.updateContactSetting(0,contact,ContactSetting.CONTACT_SETTING_DISPLAY_NAME_OVERRIDE,text)
    
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

    @loggedIn
    def getRecentMessagesV2(self, messageBoxId, messagesCount=50):
        return self.talk.getRecentMessagesV2(messageBoxId, messagesCount)
    """Object"""

    @loggedIn
    def sendImage(self, to, path, name):
        contentFooter = {
           'AGENT_ICON': "http://dl.profile.line-cdn.net/"+self.getProfile().picturePath,
           'AGENT_NAME': name,
           'AGENT_LINK': 'line://ti/p/~{}'.format(self.getProfile().userid)
           }
        objectId = self.sendMessage(to=to, text=None, contentMetadata=contentFooter, contentType=1).id
        return self.uploadObjTalk(path=path, type='image', returnAs='bool', objId=objectId)

    @loggedIn
    def sendImageWithURL(self, to, url, name):
        path = self.downloadFileURL(url, 'path')
        return self.sendImage(to, path, name)
        
    @loggedIn
    def sendImageMimic(self, to, path, icon, name):
        contentMimic = {
           'MSG_SENDER_ICON': icon,
           'MSG_SENDER_NAME': name
           }
        objectId = self.sendMessage(to=to, text=None, contentMetadata=contentMimic, contentType=1).id
        return self.uploadObjTalk(path=path, type='image', returnAs='bool', objId=objectId)

    @loggedIn
    def sendImageWithMimic(self, to, url, icon, name):
        path = self.downloadFileURL(url, 'path')
        return self.sendImageMimic(to, path, icon, name)

    @loggedIn
    def sendImage1(self, to, path, name):
        contentFooter = {
            'AGENT_ICON': "http://dl.profile.line-cdn.net/"+self.getProfile().picturePath,
            'AGENT_NAME': name,
            'AGENT_LINK': 'line://ti/p/~{}'.format(self.getProfile().userid)
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
            'AGENT_ICON': "http://dl.profile.line-cdn.net/"+self.getProfile().picturePath,
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
    def sendVideoMimic(self, to, path, icon, name):
        objectId = self.sendMessage(to=to, text=None, contentMetadata={'VIDLEN': '60000','DURATION': '60000','MSG_SENDER_ICON': icon,'MSG_SENDER_NAME': name}, contentType = 2).id
        return self.uploadObjTalk(path=path, type='video', returnAs='bool', objId=objectId)

    @loggedIn
    def sendVideoWithMimic(self, to, url, icon, name):
        path = self.downloadFileURL(url, 'path')
        return self.sendVideoMimic(to, path, icon, name)

    @loggedIn
    def sendVideo(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentMetadata={'VIDLEN': '60000','DURATION': '60000'}, contentType = 2).id
        return self.uploadObjTalk(path=path, type='video', returnAs='bool', objId=objectId)

    @loggedIn
    def sendVideoWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendVideo(to, path)

    @loggedIn
    def sendAudioMimic(self, to, path, icon, name):
        objectId = self.sendMessage(to=to, text=None, contentMetadata={'MSG_SENDER_ICON': icon,'MSG_SENDER_NAME': name}, contentType = 3).id
        return self.uploadObjTalk(path=path, type='audio', returnAs='bool', objId=objectId)

    @loggedIn
    def sendAudioWithMimic(self, to, url, icon, name):
        path = self.downloadFileURL(url, 'path')
        return self.sendAudioMimic(to, path, icon, name)

    @loggedIn
    def sendAudio(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 3).id
        return self.uploadObjTalk(path=path, type='audio', returnAs='bool', objId=objectId)

    @loggedIn
    def sendAudioWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendAudio(to, path)

    @loggedIn
    def sendFMc(self, to, path, ic, nm, file_name=''):
        if file_name == '':
            file_name = ntpath.basename(path)
        file_size = len(open(path, 'rb').read())
        objectId = self.sendMessage(to=to, text=None, contentMetadata={'FILE_NAME': str(file_name),'FILE_SIZE': str(file_size),'MSG_SENDER_ICON': ic,'MSG_SENDER_NAME': nm}, contentType = 14).id
        return self.uploadObjTalk(path=path, type='file', returnAs='bool', objId=objectId)

    @loggedIn
    def sendFileWithMimic(self, to, url, ic, nm, fileName=''):
        path = self.downloadFileURL(url, 'path')
        return self.sendFMc(to, path, fileName, ic, nm)
        return self.deleteFile(path)

    @loggedIn
    def sendFile(self, to, path, file_name=''):
        if file_name == '':
            file_name = ntpath.basename(path)
        file_size = len(open(path, 'rb').read())
        objectId = self.sendMessage(to=to, text=None, contentMetadata={'FILE_NAME': str(file_name),'FILE_SIZE': str(file_size)}, contentType = 14).id
        return self.uploadObjTalk(path=path, type='file', returnAs='bool', objId=objectId)

    @loggedIn
    def sendFileWithURL(self, to, url, fileName=''):
        path = self.downloadFileURL(url, 'path')
        return self.sendFile(to, path, fileName)
        return self.deleteFile(path)

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
    def getBlockedRecommendationIds(self):
        return self.talk.getBlockedRecommendationIds()
        
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
        if contact.videoProfile == None:
            return self.updateProfilePicture(path)
        else:
            path_vid = self.downloadFileURL("http://dl.profile.line.naver.jp"+ contact.picturePath + "/vp", 'path')
            files = {'file': open(path_vid, 'rb')}
            obs_params = self.genOBSParams({'oid': self.profile.mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
            data = {'params': obs_params}
            r_vp = self.server.postContent('{}/talk/vp/upload.nhn'.format(str(self.server.LINE_OBS_DOMAIN)), data=data, files=files)
            if r_vp.status_code != 201:return "Failed"
            path_pic = path
            self.updateProfilePicture(path_pic, 'vp')
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