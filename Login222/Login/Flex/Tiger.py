#-*- coding: utf-8 -*-
from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
#from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
#from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#==============================================================================#

with open("token.txt","r") as z:
    jepangpunya = z.read()
maxgie = LINE(jepangpunya)
maxgie.log("Auth Token : " + str(maxgie.authToken))
maxgie.log("Timeline Token : " + str(maxgie.tl.channelAccessToken))

waitOpen = codecs.open("Max2.json","r","utf-8")
settingsOpen = codecs.open("max.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
wait = json.load(waitOpen)
images = json.load(imagesOpen)
settings = json.load(settingsOpen)
stickers = json.load(stickersOpen)
#==============================================================================#
maxgieMID = maxgie.profile.mid
maxgieProfile = maxgie.getProfile()
maxgieSettings = maxgie.getSettings()
#==============================================================================#
maxgiePoll = OEPoll(maxgie)
maxgieMID = maxgie.getProfile().mid
admin = [maxgieMID]
loop = asyncio.get_event_loop()
listToken = ['desktopmac','desktopwin','iosipad','chromeos','win10']
mc = {"wr":{}}
unsendchat = {}
msgdikirim = {}
msg_image={}
msg_video={}
msg_sticker={}
wbanlist = []
wblacklist = []
msg_dict = {}
Rapid2To = ""
temp_flood = {}
#==============================================================================#
maxs = {"tag":False,"tag1":False,"kick":False}
set = {"Contact":False}
set = {"autoRead":False}
invct = {
    "winvite":False
}
sets = {
    "pict": {},
    "checkPost": False, 
    "ilstpict": {},
    "tagsticker": False,
    "autoLeave": False,
    "Sticker": False,
    "autoJoinTicket": False,
    "changeGroupPicture": [],
    "changePictureProfile": False,
    "read":"แอบทำไมหว่า",
    "addSticker": {
        "name": "",
        "status": False,
    },
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "tag": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "lv": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "wc": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "add": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "join2": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
        }
    },
}
chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

anyun = {
    "addTikel": {
        "name": "",
        "status": False
        },
}
nissa = {
    "addTikel2": {
        "name": "",
        "status": False
        },
}
tagadd = {
    "tagss": False,
    "tags": False,
    "tag": "วิธีตั้งแทค \n- ตั้งแทค ข้อความที่ต้องการ",
    "add": "รับแอดละน้า >_<\nยินดีที่ได้รู้จักนะครับ😃\n🎀 ระบบรับแอดอัตโนมัติ 🎀\nเดียร์",
    "wctext": "เดียร์",
    "lv": "\nบ๊ายบาย ตัวเทอ!😘",
    "b": "ระบบได้บล็อคบัญชีคุณอัตโนมัติ\nกรุณารอเจ้าของบัญชีมาปลดบล็อคครับ!\n\nสนใจติดบอทกดลิ้งด้านล้างได้เลยครับ☺️\n http://line.me/ti/p/~zza503",
    "เดียร์": "🌸 สวัสดี เรามุดลิ้งมานะ สนใจระบบเชลบอท 🌸",
}
apalo = {
    "blacklist":{},
    "Talkblacklist": {},
    "talkban": True,
    "Talkwblacklist": False,
    "Talkdblacklist": False,
}
temp = {"te": "#EE1289","t": "#FFFFFF"}
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}
rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
ProfileMe = {
    "coverId": "",
    "statusMessage": "",
    "PictureMe": "",
    "NameMe": "",
}
peler = { 
    "receivercount": 0,
    "sendcount": 0
}
hoho = {
    "savefile": False,
    "namefile": "",
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

user1 = maxgieMID
user2 = ""

setTime = {}
setTime = rfuSet['setTime']

contact = maxgie.getProfile() 
backup = maxgie.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()
Start = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

settings["myProfile"]["displayName"] = maxgieProfile.displayName
settings["myProfile"]["statusMessage"] = maxgieProfile.statusMessage
settings["myProfile"]["pictureStatus"] = maxgieProfile.pictureStatus
cont = maxgie.getContact(maxgieMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = maxgie.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

ProfileMe["statusMessage"] = maxgieProfile.statusMessage
ProfileMe["pictureStatus"] = maxgieProfile.pictureStatus
coverId = maxgie.getProfileDetail()["result"]["objectId"]
ProfileMe["coverId"] = coverId
#=====================================================================
with open("max.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("Max2.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
#==============================================================================#
def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output video.mp3 {}'.format(link))
    try:
        maxgie.sendAudio(to, 'video.mp3')
        time.sleep(2)
        os.remove('video.mp3')
    except Exception as e:
        maxgie.sendMessage(to, "Error")

def fileYtMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output FileYoutube.mp4 {}'.format(link))
    try:
        maxgie.sendFile(to, "FileYoutube.mp4")
        time.sleep(2)
        os.remove('FileYoutube.mp4')
    except Exception as e:
        maxgie.sendMessage(to, ' 「 ERROR 」')
    
def fileYtMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output FileYoutube.mp3 {}'.format(link))
    try:
        maxgie.sendFile(to, 'FileYoutube.mp3')
        time.sleep(2)
        os.remove('FileYoutube.mp3')
    except Exception as e:
        maxgie.sendMessage(to, ' 「 ERROR 」')

def sendCarousel(to,col):
    col = json.dumps(col)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = maxgie.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=col, headers=headers)

def sendLiffMessage(to,t):
    data = {"messages":[{"type":"text","text":t}]}
    sendCarousel(to,data)

def Rapid2Say(mtosay):
    sendLiffMessage(Rapid2To,mtosay)
#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Ma '
        maxgie.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    maxgie.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    maxgie.sendMessage(to, '', annda, 13)
def cloneProfile(mid):
    contact = maxgie.getContact(mid)
    if contact.videoProfile == None:
        maxgie.cloneContactProfile(mid)
    else:
        profile = maxgie.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        maxgie.updateProfile(profile)
        pict = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = maxgie.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = maxgie.getProfileDetail(mid)['result']['objectId']
    maxgie.updateProfileCoverById(coverId)
def backupProfile():
    profile = maxgie.getContact(maxgieMID)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = maxgie.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def sendMention(to, mid, firstmessage='', lastmessage=''):
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
        maxgie.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
def restoreProfile():
    profile = maxgie.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        maxgie.updateProfileAttribute(8, profile.pictureStatus)
        maxgie.updateProfile(profile)
    else:
        maxgie.updateProfile(profile)
        pict = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = maxgie.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    maxgie.updateProfileCoverById(coverId)
def autoresponuy(to,msg,wait):
    to = msg.to
    if msg.to not in wait["GROUP"]['AR']['AP']:
        return
    if msg.to in wait["GROUP"]['AR']['S']:
        maxgie.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
    if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
        return
    if '@!' not in wait["GROUP"]['AR']['P'][msg.to]:
        wait["GROUP"]['AR']['P'][msg.to] = '@!'+wait["GROUP"]['AR']['P'][msg.to]
    nama = maxgie.getGroup(msg.to).name
    sd = maxgie.waktunjir()
    maxgie.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',nama),'',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@!'))
def ClonerV2(to):
    try:
        contact = maxgie.getContact(to)
        profile = maxgie.profile
        profileName = maxgie.profile
        profileStatus = maxgie.profile
        profileName.displayName = contact.displayName
        profileStatus.statusMessage = contact.statusMessage
        maxgie.updateProfile(profileName)
        maxgie.updateProfile(profileStatus)
        profile.pictureStatus = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus, 'path'))
        if maxgie.getProfileCoverId(to) is not None:
            maxgie.updateProfileCoverById(maxgie.getProfileCoverId(to))
        maxgie.updateProfilePicture(profile.pictureStatus)
        print("Success Clone Profile {}".format(contact.displayName))
        return maxgie.updateProfile(profile)
        if contact.videoProfile == None:
            return "Get Video Profile"
        path2 = "http://dl.profile.line-cdn.net/" + profile.pictureStatus
        maxgie.updateProfilePicture(path2, 'vp')
    except Exception as error:
        print(error)
        
def sendMentionFooter(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@LopeAgri"
        slen = str(len(text))
        elen = str(len(text) + len(mention))
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nama = "{}".format(maxgie.getContact(maxgieMID).displayName)
        img = "http://dl.profile.line-cdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus)
        ticket = "http://line.me/ti/p/~zza503"
        maxgie.sendMessage(to, text, {'AGENT_LINK': ticket, 'AGENT_ICON': img, 'AGENT_NAME': nama, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@maxgie  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    maxgie.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(maxgie.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + maxgie.getContact("ua053fcd4c52917706ae60c811e39d3ea").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = maxgie.genOBSParams({'oid': maxgieMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = maxgie.server.postContent('{}/talk/vp/upload.nhn'.format(str(maxgie.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        maxgie.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("FadhilvanHalen.mp4")
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = maxgie.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = maxgie.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def NOTIFIED_READ_MESSAGE(op):
    try:
        if read['readPoint'][op.param1]:
            if op.param2 in read['readMember'][op.param1]:
                pass
            else:
                read['readMember'][op.param1][op.param2] = True
                read['ROM'][op.param1] = op.param2
        else:
            pass
    except:
        pass
def logError(text):
    maxgie.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType,mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def sendMention(to, mid, firstmessage, lastmessage):
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
        maxgie.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentionMembers(to, mid):
    try:
        group = maxgie.getGroup(to)
        mids = [mem.mid for mem in group.members]
        jml = len(mids)
        arrData = ""
        if mid[0] == mids[0]:
            textx = ""
        else:
            textx = ""
        arr = []
        for i in mid:
            no = mids.index(i) + 1
            textx += "{}.".format(str(no))
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
        if no == jml:
            textx += ""
            textx += ""
        maxgie.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d เดือน" % (months)
    if weeks != 0: text += " %02d สัปดาห์" % (weeks)
    if days != 0: text += " %02d วัน" % (days)
    if hours !=  0: text +=  " %02d ชั่วโมง" % (hours)
    if mins != 0: text += " %02d นาที" % (mins)
    if secs != 0: text += " %02d วินาที" % (secs)
    if text[0] == " ":
            text = text[1:]
    return text
def restartBot():
    print ("RESETBOT..")
    python = sys.executable
    os.execl(python, python, *sys.argv)
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
def foro(to, text):
    data = {
    "type": "flex",
    "altText": text,
    "contents": {
    "type": "bubble",
    "styles": {
    "footer": {
    "backgroundColor": '#444444'
    }
    },
    "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
    {
    "type": "box",
    "layout": "baseline",
    "contents": [
    {
    "type": "icon",
    "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
    "size": "md"
    },
    {
    "type": "text",
    "text": text,
    "color": "#ffffff",
    "gravity": "center",
    "align":"center",
    "wrap": True,
    "size": "md"
    },
    {
    "type": "icon",
    "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
    "size": "md"
    }, 
    ]
    }
    ]
    }
    }
    }
    sendTemplate(to, data)
def sendStickers(to, sver, spkg, sid):
    contentMetadata = {
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    maxgie.sendMessage(to, '', contentMetadata, 7)
def sendSticker(to, mid, sver, spkg, sid):
    contentMetadata = {
        'MSG_SENDER_NAME': maxgie.getContact(mid).displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + maxgie.getContact(mid).pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    maxgie.sendMessage(to, '', contentMetadata, 7)
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            maxgie.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''  
    rmv = len(key + cmd) + 1
    return text[rmv:]

#=====================================================================
def backupData():
    try:
        backup = settings
        f = codecs.open('max.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('Max2.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#==============================================================================#
async def maxgieBot(op):
    try:
        if settings["restartPoint"] != None:
            maxgie.sendMessage(settings["restartPoint"], 'ล็อคอินแล้วเรียบร้อย ><')
            settings["restartPoint"] = None
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
              if op.param2 in admin:
                  return
              maxgie.findAndAddContactsByMid(op.param1)
              maxgie.sendMessage(op.param1,"{}".format(tagadd["a"]))
              msgSticker = sets["messageSticker"]["listSticker"]["a"]
              if msgSticker != None:
                  sid = msgSticker["STKID"]
                  spkg = msgSticker["STKPKGID"]
                  sver = msgSticker["STKVER"]
                  sendSticker(op.param1, sver, spkg, sid)
              print ("[ 5 ] AUTO ADD")
        if op.type == 5:
            if settings["autoblock"] == True:
              if op.param2 in admin:
                  return
              maxgie.sendMessage(op.param1,tagadd["block"])
              maxgie.blockContact(op.param1)
              print ("[ 5 ] AUTO BLOCK")
        if op.type == 13:
            if maxgieMID in op.param3:
                G = maxgie.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            maxgie.acceptGroupInvitation(op.param1)
                        else:
                            maxgie.leaveGroup(op.param1)
                    else:
                        maxgie.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        maxgie.acceptGroupInvitation(op.param1)
                        maxgie.leaveGroup(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in apalo["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    maxgie.acceptGroupInvitation(op.param1, matched_list)
                    maxgie.leaveGroup(op.param1, matched_list)
                    print ("[ 17 ] LEAVE GROUP")

        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = maxgie.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        contact = maxgie.getContact(op.param2)
                        coversider = maxgie.getProfileCoverURL(op.param2)
                        status = maxgie.getContact(op.param2)
                        true = True
                        data = {"styles":{"body":{"backgroundColor":"#FFCCFF"},"footer":{"backgroundColor":"#CCFFFF"}},"type":"bubble","body":{"contents":[{"contents":[{"url":"https://obs.line-scdn.net/{}".format(maxgie.getContact(op.param2).pictureStatus),"type":"image"},{"type":"separator","color":"#DC143C"},{"url":"{}".format(coversider),"type":"image"}],"type":"box","spacing":"md","layout":"horizontal"},{"type":"separator","color":"#6F4E37"},{"contents":[{"text":"แอบเก่งจังนะเราอะ😒","size":"md","align":"center","color":"#440000","wrap":true,"weight":"bold","type":"text"}],"type":"box","spacing":"md","layout":"vertical"},{"type":"separator","color":"#DC143C"},{"contents":[{"contents":[{"url":"https://img.live/images/2019/03/19/14337.png","type":"icon","size":"md"},{"text":"ชื่อ: {}".format(maxgie.getContact(op.param2).displayName),"size":"xs","margin":"none","color":"#440000","weight":"regular","type":"text"}],"type":"box","layout":"baseline"},{"type":"separator","color":"#DC143C"},{"contents":[{"url":"https://img.live/images/2019/03/19/14337.png","type":"icon","size":"md"},{"text":"รับติดเซลราคาถูก","size":"xs","margin":"none","color":"#440000","wrap":true,"weight":"regular","type":"text"}],"type":"box","layout":"baseline"}],"type":"box","layout":"vertical"}],"type":"box","spacing":"md","layout":"vertical"},"footer":{"type":"box","layout":"horizontal","contents":[{"contents":[{"contents":[{"url":"https://img.live/images/2019/03/19/14337.png","type":"icon","size":"md"},{"text":"เดียร์","size":"sm","action":{"uri":"http://line.me/ti/p/~zza503","type":"uri","label":"Add Creator"},"margin":"xl","align":"start","color":"#440000","weight":"bold","type":"text"}],"type":"box","layout":"baseline"}],"type":"box","layout":"horizontal"}]}}
                        data = {'type': 'flex','altText': 'ตรวจจับคนอ่าน','contents': data}
                        sendTemplate(op.param1, data)
        if op.type == 15:
          if settings["Leave"] == True:
            if op.param2 in admin:
                return
            ginfo = maxgie.getGroup(op.param1)
            contact = maxgie.getContact(op.param2)
            name = contact.displayName
            pp = contact.pictureStatus
            s = name + " " + tagadd["lv"]
            data = {
                "type": "flex",
                "altText": "คนออกกลุ่ม",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#FFFFCC'
                        },
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                 "type": "image",
                                 "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                 "size": "xxl"
                           },
                          {
                                "type": "text",
                                "text": "{}".format(s),
                                "wrap": True,
                                "color": "#EE1289",
                                "gravity": "center",
                                "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
            data = {
                "type": "flex",
                "altText": "คนออกกลุ่ม",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "http://line.me/ti/p/~zza503"
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)

        if op.type == 17:
          if settings["Welcome"] == True:
            if op.param2 in admin:
                return
            g = maxgie.getGroup(op.param1)
            true = True
            contact = maxgie.getContact(op.param2)
            gname = g.name
            name = contact.displayName
            pp = contact.pictureStatus
            data = {"footer":{"contents":[{"align":"center","size":"xs","text":"ติดต่อ","action":{"uri":"http://line.me/ti/p/~zza503","type":"uri"},"color":"#FF69B4","weight":"bold","type":"text","wrap":True},{"color":"#FF69B4","type":"separator"},{"align":"center","size":"xs","text":"สอบถาม","action":{"uri":"http://line.me/ti/p/~zza503","type":"uri"},"color":"#FF69B4","weight":"bold","type":"text","wrap":True}],"type":"box","layout":"horizontal"},"hero":{"url":"https://obs.line-scdn.net/{}".format(pp),"size":"full","aspectRatio":"1:1","aspectMode":"cover","type":"image","margin":"xxl"},"styles":{"footer":{"backgroundColor":"#FFFFCC"},"body":{"backgroundColor":"#CCFFFF"}},"type":"bubble","body":{"contents":[{"contents":[{"url":"https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"size":"sm","flex":0,"gravity":"bottom","aspectMode":"cover","type":"image","aspectRatio":"1:1"},{"align":"center","size":"md","text":"͜࿐้ོུ͜สวัสดีคุณได้เข้าสู่\n🇨🇽🇨🇽🇨🇽🇨🇽🇨🇽\n{}".format(gname),"color":"#0000FF","weight":"bold","type":"text","wrap":True}],"margin":"md","layout":"horizontal","type":"box"},{"align":"center","size":"md","text":"ทำตัวดีดีนะคุณ:  {}".format(name),"color":"#330000","weight":"bold","type":"text","wrap":True},{"contents":[{"color":"#333300","type":"separator"},{"align":"center","size":"lg","text":"{}".format(tagadd["wctext"]),"color":"#000000","type":"text","wrap":True}],"type":"box","layout":"vertical"},{"color":"#333300","type":"separator"},{"align":"center","size":"xs","flex":0,"text":"ช่องทางติดต่อBOT|แอพเคชั่น","color":"#000000","weight":"bold","type":"text","wrap":True,"margin":"md"},{"type":"box","contents":[{"url":"https://cdn3.iconfinder.com/data/icons/mobile-functions/154/phone-menu-512.png","size":"sm","aspectRatio":"1:1","action":{"uri":"line://app/1636169025-yQ7bGMVA?type=fotext&text=BOYBOTLINE","type":"uri"},"aspectMode":"cover","type":"image"},{"url":"https://i2.wp.com/www.vectorico.com/wp-content/uploads/2018/02/Facebook-Icon.png","size":"sm","aspectRatio":"1:1","action":{"uri":"line://app/1636169025-aVgXrzY6","type":"uri"},"aspectMode":"cover","type":"image"},{"url":"https://icon-icons.com/icons2/72/PNG/256/setting_14432.png","size":"sm","aspectRatio":"1:1","action":{"uri":"line://app/1636169025-yQ7bGMVA?type=fotext&text=set","type":"uri"},"aspectMode":"cover","type":"image"},{"url":"https://www.pacificspecialty.com/wp-content/themes/x-child/_img/icon-youtube.png","size":"sm","aspectRatio":"1:1","action":{"uri":"line://app/1636169025-m0Eex43Y","type":"uri"},"aspectMode":"cover","type":"image"},{"url":"https://www.edigitalagency.com.au/wp-content/uploads/new-instagram-logo-png-transparent.png","size":"sm","aspectRatio":"1:1","action":{"uri":"line://app/1636169025-JmQWEdvA","type":"uri"},"aspectMode":"cover","type":"image"}],"flex":2,"layout":"horizontal","spacing":"xs"}],"type":"box","layout":"vertical","spacing":"md"}}
            data = {'type': 'flex','altText': 'Welcome Message','contents': data}
            sendTemplate(op.param1, data)
#            s = "เดียร์\n"
#            s += "\n🇹🇭 สวัสดีคุณ 🇹🇭 \n🤟 {}\n\n".format(name)
#            s += "\n🇹🇭 ท่านได้เข้าสู่ห้อง 👉 {}".format(gname)
#            s += tagadd["wctext"]
#            data = {
#                "type": "flex",
#                "altText": "🙇ยินดีต้อนรับ..สมาชิกใหม่🙇",
#                "contents": {
#                    "type": "bubble",
#                    "styles": {
#                        "body": {
#                            "backgroundColor": '#FFFFCC'
#                        },
#                    },
#                    "body": {
#                        "type": "box",
#                        "layout": "vertical",
#                        "contents": [
#                           {
#                                 "type": "image",
#                                 "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
#                                 "size": "xxl"
#                           },
#                          {
#                                "type": "text",
##                                "text": "{}".format(s),
 #                               "wrap": True,
 #                               "color": "#EE1289",
# 
#                               "align": "center",
 #                               "gravity": "center",
 #                               "size": "md"
 #                           },
 #                       ]
 #                   }
 #               }
 #           }
 #           sendTemplate(op.param1, data)
 #           data = {
 #               "type": "flex",
 #               "altText": "🙇ยินดีต้อนรับคนมาใหม่🙇",
 #               "contents": {
 #                   "type": "bubble",
#                    "hero": {
#                         "type":"image",
#                         "url": "https://profile.line-scdn.net/" + str(pp),
#                         "size":"full",
 #                        "action": {
 #                            "type": "uri",
 #                            "uri": "http://line.me/ti/p/~zza503"
 #                        }
 #                   },
 #               }
 #           }
 #           sendTemplate(op.param1, data)


        if op.type == 26:
            msg = op.message
            sender = msg._from
            to = msg.to
            if msg.contentType == 6:
                    if settings["responGc"] == True and sender != maxgieMID:
                        contact = maxgie.getContact(sender)
                        if msg.toType == 0:
                            if msg.contentMetadata["GC_EVT_TYPE"] == "I":
                                sendMention(to, sender, "Nah",", พ่องไตพ่องไตรันคลอทำควยอะไร กูร้องเพลง😂$")
                                arg = "   [ Notify ] SpamCall"
                                arg += "\n   UserSpam: {}".format(str(contact.displayName))
                                print (arg)
                        elif msg.toType == 2:
                            group = maxgie.getGroup(to)
                            if msg.contentMetadata["GC_EVT_TYPE"] == "S":
                                arg = "   [ Notify ] เริ่มการคลอ"
                                arg += "\n   Group: {}".format(str(group.name))
                                arg += "\n   User Started: {}".format(str(contact.displayName))
                                print (arg)
                                sendMention(to, sender, "คุณ ", " \nฮันแน่ เหงาสิถ้า รู้นะคิดอะไรอยู่55😜")
                            elif msg.contentMetadata["GC_EVT_TYPE"] == "E":
                                sendMention(to, sender, "คุณ ", " \nแหม๋แหม๋ลงไวจิงเชียว มีคนเรียกอะดี้😝")
                                arg = "   [ Notify ] สิ้นสุดการคลอ"
                                arg += "\n   Group: {}".format(str(group.name))
                                arg += "\n   User Ended: {}".format(str(contact.displayName))
                                print (arg)

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if invct["winvite"] == True:
                     if msg._from in maxgieMID:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = maxgie.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 maxgie.sendMessage(msg.to,"-> " + _name + " \nทำการเชิญสำเร็จแล้วจ")
                                 break
                             elif invite in apalo["Talkblacklist"]:
                                 maxgie.sendMessage(msg.to,"ขออภัย, " + _name + " ไม่สามารถดึงได้")
                                 maxgie.sendMessage(msg.to,"กรุณาทำการล้างบัญชีดำ")
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     maxgie.findAndAddContactsByMid(target)
                                     maxgie.inviteIntoGroup(msg.to,[target])
                                     maxgie.sendMessage(msg.to,"ทำการเชิญ: " + _name + "สำเร็จแล้ว")
                                     invct["winvite"] = False
                                     break
                                 except:
                                     try:
                                         maxgie.findAndAddContactsByMid(invite)
                                         maxgie.inviteIntoGroup(op.param1,[invite])
                                         invct["winvite"] = False
                                     except:
                                         maxgie.sendMessage(msg.to,"เกิดข้อผิดพลาดติดต่อแอดมิน")
                                         invct["winvite"] = False
                                         break

        if op.type == 25:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 13:
              if msg._from in maxgieMID:
               if apalo["Talkwblacklist"] == True:
                 if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                     maxgie.sendMessage(msg.to,"เพิ่มบัญชีดำเรียบร้อย!")
                     apalo["Talkwblacklist"] == False
                 else:
                     apalo["Talkblacklist"][msg.contentMetadata["mid"]] = True
                     apalo["Talkwblacklist"] = False
                     maxgie.sendMessage(msg.to,"ผู้นี้คาดโทษอยู่แล้ว")

               if apalo["Talkdblacklist"] == True:
                 if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                     del apalo["Talkblacklist"][msg.contentMetadata["mid"]]
                     maxgie.sendMessage(msg.to,"ทำการปลดแบล็คลิสเรียบร้อย")
                     apalo["Talkdblacklist"] = False
                 else:
                     apalo["Talkdblacklist"] = False
                     maxgie.sendMessage(msg.to,"ผู้นี้บัญชีขาวอยู่แล้ว")

            if msg.to not in unsendchat:
                unsendchat[msg.to] = {}
            if msg_id not in unsendchat[msg.to]:
                unsendchat[msg.to][msg_id] = msg_id
            msgdikirim[msg_id] = {"text":text}
            to = msg.to
            isValid = True
            cmd = command(text)
            setkey = settings['keyCommand'].title()
            if settings['setKey'] == False: setkey = ''
            if isValid != False:
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    try:
                        if msg.to not in wait['Unsend']:
                            wait['Unsend'][msg.to] = {'B':[]}
                        if msg._from not in [maxgieMID]:
                            return
                        wait['Unsend'][msg.to]['B'].append(msg.id)
                    except:pass
        if op.type == 24:
            if sets["autoLeave"] == True:
                maxgie.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
                if msg._from not in maxgieMID:
                  if apalo["talkban"] == True:
                    if msg._from in apalo["Talkblacklist"]:
                        maxgie.sendMention(to, "ติดดำกูอยู่นะ @! :)","",[msg._from])
                        maxgie.kickoutFromGroup(msg.to, [msg._from])
#                if msg.contentType == 13:
#                  if apalo["Talkwblacklist"] == True:
#                    if msg._from in maxgieMID:
#                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
#                          foro(msg.to,"Sudah Ada")
#                          apalo["Talkwblacklist"] = False
#                      else:
#                          apalo["Talkblacklist"][msg.contentMetadata["mid"]] = True
#                          apalo["Talkwblacklist"] = False
#                          foro(msg.to,"เพิ่มบัญชีนี้ในรายการสีดำเรียบร้อยแล้ว")
#                  if apalo["Talkdblacklist"] == True:
#                    if msg._from in maxgieMID:
#                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
#                          del apalo["Talkblacklist"][msg.contentMetadata["mid"]]
#                          foro(msg.to,"เพิ่มบัญชีนี้ในรายการสีขาวเรียบร้อยแล้ว")
#                          apalo["Talkdblacklist"] = False
#                      else:
#                          apalo["Talkdblacklist"] = False
#                          foro(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
                if msg.contentType == 16:
                    if msg.toType in [2,1,0]:
                        print ("AutoLikeCommat")
                        try:
                            if settings["autolike"] == True:
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                if purl[1] not in wait['postId']:
                                    data = {"type":"bubble","styles":{"body":{"backgroundColor":"#CCFFFF"},"footer":{"backgroundColor":"#330000"}},"hero":{"type":"image","url":"https://img.live/images/2019/03/22/116694026.png","aspectMode":"cover","aspectRatio":"1:1","size":"full","margin":"xxl"},"body":{"type":"box","layout":"vertical","spacing":"md","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","url":"https://data.boteater.co/storage-1552507508582u6GYALrp.jpg","size":"xl"},{"type":"text","text":"AutoLike & Comment","weight":"bold","size":"md","align":"center","color":"#000055","action":{"type":"uri","uri":"line://app/1648257191-AQJRwmpk?type=profile"}}]},{"type":"separator","color":"#4B0082"},{"type":"box","layout":"vertical","spacing":"xs","flex":2,"contents":[{"type":"separator","color":"#4B0082"},{"type":"text","text":"Like ให้แล้วน๊าาา!!\nไลค์ไห้ฟรีคัฟไม่คิดตัง","wrap":True,"weight":"bold","align":"center","color":"#000055","size":"md"},{"type":"separator","color":"#4B0082"},{"type":"text","text":"AutoLike & Comment\n เดียร์","wrap":True,"weight":"bold","align":"center","color":"#000055","size":"xs"},{"type":"text","text":"เดียร์","wrap":True,"align":"center","size":"xs","color":"#000055"}]},{"type":"separator","color":"#4B0082"},{"type":"text","text":"Click Icon Di Bawah","wrap":True,"size":"xs","margin":"md","weight":"bold","align":"center","color":"#000055","flex":0},{"type":"box","layout":"horizontal","spacing":"xs","flex":2,"contents":[{"type":"image","url":"https://cdn.icon-icons.com/icons2/374/PNG/512/iPhone-WE-icon_37271.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/camera/"}},{"type":"image","url":"https://cdn4.iconfinder.com/data/icons/social-media-pro-icons/1080/Whatsapp-01-512.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"https://wa.me/?text=Im%20using%20VHBOTS"}},{"type":"image","url":"https://cdn.iconscout.com/icon/free/png-256/settings-409-461608.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/settings"}},{"type":"image","url":"https://i.downloadatoz.com/upload/android/icon/1/5/1/ef36baf8fac387f619c77fbaf613e735.jpg","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/cameraRoll/multi"}},{"type":"image","url":"https://support.apple.com/content/dam/edam/applecare/images/en_US/icloud/featured-content-messages-icon_2x.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"https://line.me/R/ti/p/%40137gcwpz"}}]}]},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"ติดบอท","wrap":True,"align":"center","weight":"bold","color":"#CCFF00","size":"xs","action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"}},{"type":"separator","color":"#FFFF99"},{"type":"text","text":"ติดเซล","wrap":True,"align":"center","weight":"bold","color":"#CCFF00","size":"xs","action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"}}]}}
                                    data = {'type': 'flex','altText': 'Share Like','contents': data}
                                    sendTemplate(to, data)
                                    maxgie.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                if settings["com"] == True:
                                    maxgie.createComment(purl[0], purl[1], settings["commet"])
                                    wait['postId'].append(purl[1])
                                else:
                                    pass
                        except Exception as e:
                                if settings["autolike"] == True:
                                    purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
                                    if purl[1] not in wait['postId']:
                                        maxgie.likePost(msg._from, purl[1], random.choice([1001,1002,1003,1004,1005]))
                                    if settings["com"] == True:
                                        maxgie.createComment(msg._from, purl[1], settings["commet"])
                                        wait['postId'].append(purl[1])
#                                        data = {"type":"bubble","styles":{"body":{"backgroundColor":"#CCFFFF"},"footer":{"backgroundColor":"#330000"}},"hero":{"type":"image","url":"https://data.boteater.co/storage-1552505056012u6GYALrp.jpg","aspectMode":"cover","aspectRatio":"1:1","size":"full","margin":"xxl"},"body":{"type":"box","layout":"vertical","spacing":"md","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","url":"https://data.boteater.co/storage-1552507508582u6GYALrp.jpg","size":"xl"},{"type":"text","text":"AutoLike & Comment","weight":"bold","size":"md","align":"center","color":"#000055","action":{"type":"uri","uri":"line://app/1648257191-AQJRwmpk?type=profile"}}]},{"type":"separator","color":"#4B0082"},{"type":"box","layout":"vertical","spacing":"xs","flex":2,"contents":[{"type":"separator","color":"#4B0082"},{"type":"text","text":"Like ให้แล้วน๊าาา!!\n💖รับติดเชลบอทภาพสีราคาถูก💖","wrap":True,"weight":"bold","align":"center","color":"#000055","size":"md"},{"type":"separator","color":"#4B0082"},{"type":"text","text":"AutoLike & Comment\─┅•●✫ざণざℓざื❍✫●•┅─","wrap":True,"weight":"bold","align":"center","color":"#000055","size":"xs"},{"type":"text","text":"เดียร์","wrap":True,"align":"center","size":"xs","color":"#000055"}]},{"type":"separator","color":"#4B0082"},{"type":"text","text":"Click Icon Di Bawah","wrap":True,"size":"xs","margin":"md","weight":"bold","align":"center","color":"#000055","flex":0},{"type":"box","layout":"horizontal","spacing":"xs","flex":2,"contents":[{"type":"image","url":"https://cdn.icon-icons.com/icons2/374/PNG/512/iPhone-WE-icon_37271.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/camera/"}},{"type":"image","url":"https://cdn4.iconfinder.com/data/icons/social-media-pro-icons/1080/Whatsapp-01-512.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"https://wa.me/?text=Im%20using%20VHBOTS"}},{"type":"image","url":"https://cdn.iconscout.com/icon/free/png-256/settings-409-461608.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/settings"}},{"type":"image","url":"https://i.downloadatoz.com/upload/android/icon/1/5/1/ef36baf8fac387f619c77fbaf613e735.jpg","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/cameraRoll/multi"}},{"type":"image","url":"https://support.apple.com/content/dam/edam/applecare/images/en_US/icloud/featured-content-messages-icon_2x.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"https://line.me/R/ti/p/%40137gcwpz"}}]}]},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"ติดบอท","wrap":True,"align":"center","weight":"bold","color":"#CCFF00","size":"xs","action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"}},{"type":"separator","color":"#FFFF99"},{"type":"text","text":"ติดบอท","wrap":True,"align":"center","weight":"bold","color":"#CCFF00","size":"xs","action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"}}]}}
#                                        data = {'type': 'flex','altText': 'Auto Like','contents': data}
#                                        sendTemplate(to, data)
                                    else:pass
#=====================================================================
#=====================================================================
        if op.type == 25:
            print("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == "ประกาศ":
                    sa="วิธีใช้ ประกาศกลุ่ม >\\<"
                    sa+="\n- ประกาศ ข้อความ/ไอดีไลน์"
                    sa+="\nตัวอย่าง >\\<"
                    sa+="\n- ประกาศ มอนิ่ง/mod......"
                    foro(to, str(sa))
                if text.lower() == "ตั้งapi":
                    sa = "วีธีใช้ api >\\<"
                    sa += "\n- ตั้งapi คีย์เวิร์ด;;ตอบกลับ"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- ตั้งapi เทส;;เทสทำไม"
                    foro(to, str(sa))
                if text.lower() == "stag":
                    sa = "วิธีใช้ stag >\\<"
                    sa += "\n- stag [เลขที่ต้องการ] @user"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- stag 1 @user"
                    foro(to, str(sa))
                if text.lower() == "สะกดจิต":
                    sa = "วิธีใช้ สะกดจิต >\\<"
                    sa += "\n- สะกดจิต [ข้อความ] @user"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- สะกดจิต Fc yeewa @user"
                    foro(to, str(sa))
                if text.lower() == "เชคค่า" or text.lower() == "set":
                    sas = "💜 ระบบ 💜"
                    if settings["autoAdd"] == True: sa = "\n💜 ออโต้แอด ( เปิด )"
                    else:sa = "\n💜 ออโต้แอด ( ปิด )"
                    if settings["autoblock"] == True: sa += "\n💜 ออโต้บล็อค ( เปิด )"
                    else:sa += "\n💜 ออโต้บล็อค ( ปิด )"
                    if settings["autoCancel"]["on"] == True: sa +="\n💜 ยกเชิญที่มีสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"])
                    else:sa += "\n💜 ปฏิเสธกลุ่มเชิญ ( ปิด )"
                    if tagadd["tags"] == True: sa += "\n💜 ตอบกลับคนแทค ( เปิด )"
                    else:sa += "\n💜 ตอบกลับคนแทค ( ปิด )"
                    if tagadd["tagss"] == True: sa += "\n?? ตอบกลับคนแทค2 ( เปิด )"
                    else:sa += "\n💜 ตอบกลับคนแทค2 ( ปิด )"
                    if sets["tagsticker"] == True: sa += "\n💜 แทคสติ๊กเกอร์ ( เปิด )"
                    else:sa += "\n💜 แทคสติ๊กเกอร์ ( ปิด )"
                    if maxs["tag"] == True: sa += "\n💜 ตอบกลับคนแทค3 ( เปิด )"
                    else:sa += "\n💜 ตอบกลับคนแทค3 ( ปิด )"
                    if maxs["tag1"] == True: sa += "\n💜 ตอบกลับคนแทค4 ( เปิด )"
                    else:sa += "\n💜 ตอบกลับคนแทค4 ( ปิด )"
                    if maxs["kick"] == True: sa += "\n💜 เตะคนแทค ( เปิด )"
                    else:sa += "\n💜 เตะคนแทค ( ปิด )"
                    if settings["autolike"] == True: sa += "\n💜 ออโต้ไลค์ ( เปิด )"
                    else:sa += "\n💜 ออโต้ไลค์ ( ปิด )"
                    if settings["com"] == True: sa += "\n💜 คอมเม้นโพส ( เปิด )"
                    else:sa += "\n💜 คอมเม้นโพส ( ปิด )"
                    if settings["Welcome"] == True: sa += "\n💜 ต้อนรับคนเข้ากลุ่ม ( เปิด )"
                    else:sa += "\n💜 ต้อนรับคนเข้ากลุ่ม ( ปิด )"
                    if settings["Wc"] == True: sa += "\n💜 ต้อนรับคนเข้ากลุ่ม2 ( เปิด )"
                    else:sa += "\n💜 ต้อนรับคนเข้ากลุ่ม2 ( ปิด )"
                    if settings["wcsti2"] == True: sa += "\n💜 ติ๊กคนเข้ากลุ่ม ( เปิด )"
                    else:sa += "\n💜 ติ๊กคนเข้ากลุ่ม ( ปิด )"
                    if settings["Leave"] == True: sa += "\n💜 คนออกกลุ่ม ( เปิด )"
                    else:sa += "\n💜 คนออกกลุ่ม ( ปิด )"
                    if settings["lv"] == True: sa += "\n💜 ติ๊กคนออกกลุ่ม ( เปิด )"
                    else:sa += "\n💜 ติ๊กคนออกกลุ่ม ( ปิด )"
                    if settings["unsendMessage"] == True: sa += "\n💜 ตรวจจับยกเลิก ( เปิด )"
                    else:sa += "\n💜 ตรวจจับยกเลิก ( ปิด )"
                    if settings["Sticker"] == True: sa += "\n💜 เชคติ๊กใหญ่ ( เปิด )"
                    else:sa += "\n💜 เชคติ๊กใหญ่ ( ปิด )"
                    if sets["Sticker"] == True: sa += "\n💜 เชคโค๊ดสติ๊กเกอร์ ( เปิด )"
                    else:sa += "\n💜 เชคโค๊ดสติ๊กเกอร์ ( ปิด )"
                    if sets["checkPost"] == True: sa += "\n💜 เชคโพส ( เปิด )"
                    else:sa += "\n?? เชคโพส ( ปิด )"
                    if set["autoRead"] == True: sa += "\n💜 อ่านออโต้ ( เปิด )"
                    else:sa += "\nอ่านออโต้ ( ปิด )"
                    data = {
                        "type": "flex",
                        "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                        "altText": "{}".format(sas),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#ffffff'
                                },
                            },
                            "hero": {
                                "type": "image",
                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                "size": "full",
                                "aspectRatio": "1:1",
                                "aspectMode": "cover",
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": sas,
                                        "color": "#CD1076",
                                        "align": "center",
                                        "weight": "bold",
                                        "size": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(sa),
                                        "wrap": True,
                                        "color": "#ee1289",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == "เปิดจับอ่าน":
                  try:
                      maxgie.sendMessage(msg.to,"ระบบเริ่มทำการจับอ่าน")
                      del cctv['point'][msg.to]
                      del cctv['sidermem'][msg.to]
                      del cctv['cyduk'][msg.to]
                  except:
                      pass
                  cctv['point'][msg.to] = msg.id
                  cctv['sidermem'][msg.to] = ""
                  cctv['cyduk'][msg.to]=True

                elif text.lower() == "ดึง":
                         invct["winvite"] = True
                         foro(to,"กรุณาลงคอนแทค")

                if text.lower() == "เชคคลอ เปิด":
                  if settings["responGc"] == False:
                      foro(to,"เปิดการเช็คคลอกลุ่มเรียบร้อย")
                      settings["responGc"] = True
                  else:
                      if settings["responGc"] == True:
                          foro(to,"เปิดการเช็คคลอกลุ่มเรียบร้อยอยู่แล้ว")

                if text.lower() == "เชคคลอ ปิด":
                  if settings["responGc"] == True:
                      foro(to,"ปิดการเช็คคลอกลุ่มเรียบร้อย")
                      settings["responGc"] = False
                  else:
                      if settings["responGc"] == False:
                          foro(to,"ปิดการเช็คคลอกลุ่มเรียบร้อยอยู่แล้ว")

                if "สแปม " in text.lower():
                  spl = re.split("สแปม ",msg.text,flags=re.IGNORECASE)
                  if spl[0] == "":
                      if msg._from in maxgieMID:
                          red = re.compile(re.escape('สแปม '),re.IGNORECASE)
                          mts = red.sub('',msg.text)
                          mtsl = mts.split()
                          mtsTimeArg = len(mtsl) - 1
                          mtsTime = mtsl[mtsTimeArg]
                          del mtsl[mtsTimeArg]
                          mtosay = " ".join(mtsl)
                          global Rapid2To
                          if msg.toType != 0:
                              Rapid2To = msg.to
                          else:
                              Rapid2To = msg._from
                          RapidTime = mtsTime
                          rmtosay = []
                          for count in range(0,int(RapidTime)):
                              rmtosay.insert(count,mtosay)
                          p = Pool(20)
                          p.map(Rapid2Say,rmtosay)
                          p.close()

                elif text.lower() == "ปิดจับอ่าน":
                  if msg.to in cctv['point']:
                      cctv['cyduk'][msg.to]=False
                      maxgie.sendMessage(msg.to,"ปิดระบบจับอ่านเรียบร้อย")
                  else:
                      maxgie.sendMessage(msg.to,"ปิดระบบจับอ่านเรียบร้อยอยู่แล้ว")

                elif text.lower() == 'clearban' or text.lower() == "ล้างดำ":
                      apalo["Talkblacklist"] = []
                      foro(to, "💜 สำเร็จ  💜")
                elif text.lower() == "ลบแชท":
                        if msg._from in maxgieMID:
                            try:
                                maxgie.removeAllMessages(op.param2)
                                foro(msg.to,"ลบทุกการแชทเรียบร้อย")
                            except:
                                pass
                elif text.lower() == "cancelall" or text.lower() == "/ยกเชิญ" and sender == maxgieMID:
                            if msg.toType == 2:
                                group = maxgie.getGroup(to)
                                if group.invitee is None or group.invitee == []:
                                    foro(to, "Nothing")
                                else:
                                    invitee = [contact.mid for contact in group.invitee]
                                    for inv in invitee:
                                        maxgie.cancelGroupInvitation(to, [inv])
                                        time.sleep(1)
                                    foro(to, "💜  ยกเชิญจำนวน「 {} 」คน  💜".format(str(len(invitee))))
                elif text.lower() == "คทดำ":
                    if msg._from in maxgieMID:
                        if apalo["Talkblacklist"] == []:
                            foro(to, "💜  ไม่มีคท.คนติดดำ  💜")
                        else:
                            for bl in apalo["Talkblacklist"]:
                                maxgie.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                elif msg.text.lower().startswith("ตั้งสีme "):
                            text_ = removeCmd("ตั้งสีme", text)
                            try:
                                temp["t"] = text_
                                foro(to,"💜 โค๊ดสี 💜\nคือ : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                elif msg.text.lower().startswith("สีอักษร "):
                            text_ = removeCmd("สีอักษร", text)
                            try:
                                temp["te"] = text_
                                foro(to,"💜 โค๊ดสี 💜\nคือ : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                elif msg.text.lower() == "รหัสสี":
                            c="https://i.pinimg.com/originals/d0/9c/8a/d09c8ad110eb44532825df454085a376.jpg"
                            p="https://i.pinimg.com/originals/7c/d3/aa/7cd3aa57150f8f6f18711ff22c9f6d4a.jpg"
                            m="**ตัวอย่างที่1**\nคำสั่งเปลี่ยนสี me\nพิม'ตั้งสีme #FFFFFF'\n**ตัวอย่างที่2**\nคำสั่งเปลี่ยนสี tag\nพิม'ตั้งสีแทค #FFFFFF'"
                            maxgie.sendImageWithURL(to,c)
                            maxgie.sendImageWithURL(to,p)
                            foro(to,m)
                elif msg.text.lower().startswith("ตั้งบล็อค "):
                            text_ = removeCmd("ตั้งบล็อค", text)
                            try:
                                tagadd["b"] = text_
                                foro(to,"💜 ตั้งบล็อคอัตโนมัติ 💜\nคือ : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                elif text.lower().startswith("ตั้งค้างเชิญ "):
                            text_ = removeCmd("ตั้งค้างเชิญ", text)
                            try:
                                settings["autoCancel"]["members"] = text_
                                foro(to,"💜 ตั้งยกค้างเชิญ 💜\nจำนวน : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                if text.lower() == "ดำ":
                  if msg._from in maxgieMID:
                      apalo["Talkwblacklist"] = True
                      foro(to,"💜  ส่งคท.มา  💜")

                if text.lower() == "ขาว":
                  if msg._from in maxgieMID:
                      apalo["Talkdblacklist"] = True
                      foro(to,"🐉  ส่งคท.มา  🐉")

                elif msg.text.lower().startswith("ตั้งแทค "):
                      text_ = removeCmd("ตั้งแทค", text)
                      try:
                          tagadd["tag"] = text_
                          sa = "🐉 ตั้งคำแทค 🐉\nคือ : " + text_
                          foro(to, str(sa))
                      except:
                          maxgie.sendMessage(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งแอบ "):
                      text_ = removeCmd("ตั้งแอบ", text)
                      try:
                          sets["read"] = text_
                          sa = "คือ : " + text_
                          foro(to, str(sa))
                      except:
                          maxgie.sendMessage(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งคนเข้า "):
                      text_ = removeCmd("ตั้งคนเข้า", text)
                      try:
                          tagadd["wctext"] = text_
                          sa = "「 ตั้งต้อนรับ 」\nคือ : " + text_
                          foro(to, str(sa)) 
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งคนออก "):
                            text_ = removeCmd("ตั้งคนออก", text)
                            try:
                                tagadd["lv"] = text_
                                foro(to,"「 ตั้งคนออก 」\nคือ : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                elif msg.text.lower().startswith("ตั้งคนแอด "):
                      text_ = removeCmd("ตั้งคนแอด", text)
                      try:
                          tagadd["add"] = text_
                          sa = "「 ตั้งแอด 」\nคือ : " + text_
                          foro(to, str(sa))
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งคอมเม้น "):
                      text_ = removeCmd("ตั้งคอมเม้น", text)
                      try:
                          settings["commet"] = text_
                          sa = "🐉 ตั้งคอมเม้น 🐉\nคือ : " + text_
                          foro(to, str(sa))
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                if text.lower() == "เชค":
                    add = tagadd["add"]
                    tag = tagadd["tag"]
                    like = settings["commet"]
                    wc = tagadd["wctext"]
                    lv = tagadd["lv"]
                    c = settings["autoCancel"]["members"]
                    b = tagadd["b"]
                    Re = settings["reply"]
                    foro(to, "ข้อความแอด :\n"+str(add)+"\n\nข้อความแทค :\n"+str(tag)+"\n\nข้อความเม้น :\n"+str(like)+"\n\nข้อความต้อนรับ :\n"+str(wc)+"\n\nข้อความคนออก :\n"+str(lv)+"\n\nจำนวนค้างเชิญ :\n"+str(c)+" จำนวน\n\nข้อความบล็อค :\n"+str(b)+"\n\nข้อความแทคแชท :\n"+str(Re))
                if text.lower() == "/คำสั่ง" or text.lower() == "/help":
                    sas = "💌ระบบเฟก💌\n"
                    sa = "• คท\n"
                    sa += "• ไอดีเรา\n"
                    sa += "• ชื่อเรา\n"
                    sa += "• ตัสเรา\n"
                    sa += "• รูปเรา\n"
                    sa += "• รูปวีดีโอเรา\n"
                    sa += "• ปกเรา\n"
                    sa += "──────────────\n"
                    sa += "• ข้อมูล\n"
                    sa += "• ออน\n"
                    sa += "• รีบอท\n"
                    sa += "• แทค\n"
                    sa += "• ยกเชิญ\n"
                    sa += "• /ลบรัน\n"
                    sa += "• ก็อป @user\n"
                    sa += "• กลับร่าง\n"
                    sa += "──────────────\n"
                    sa += "• สะกดกิต [พิม'สะกดกิต'เพื่อดูวิธี]\n"
                    sa += "• ตั้งapi [พิมเพื่อดูวิธี]\n"
                    sa += "• ล้างapi [คำที่จะลบ]\n"
                    sa += "• เชคapi\n"
                    sa += "• stag [พิม'stag'เพื่อดูวิธี]\n"
                    sa += "• แปรงคท [MID]\n"
                    sa += "• ยูทูป [ข้อความ]\n"
                    sa += "• image [text(ภาษาอังกฤษ)]\n"
                    sa += "• รูป [ข้อความ(ภาษาไทย)]\n"
                    sa += "• เพลสโต [ชื่อแอพ]\n"
                    sa += "• ตั้งรูปโปรไฟล์ [ลิ้งยูทูป]\n"
                    sa += "• ประกาศ [พิม'ประกาศ'เพื่อดูวิธี]\n"
                    sa += "• ยกเลิก [ใส่จำนวนที่จะยกเลิก]\n"
                    sa += "──────────────\n"
                    sa += "• ดำ ส่งคท.\n"
                    sa += "• ขาว ส่งคท.\n"
                    sa += "• ดำ @user\n"
                    sa += "• ล้าง @user\n"
                    sa += "• เชคดำ\n"
                    sa += "• คทดำ\n"
                    sa += "• ล้างดำ\n"
                    sa += "──────────────\n"
                    sa += "• ตั้งคนเข้า [ข้อความ]\n"
                    sa += "• ตั้งคนออก [ข้อความ]\n"
                    sa += "• ตั้งคนแอด [ข้อความ]\n"
                    sa += "• ตั้งคนแทค [ข้อความ]\n"
                    sa += "• ตั้งคอมเม้น [ข้อความ]\n"
                    sa += "──────────────\n"
                    sa += "• เปิดแทค/ปิดแทค\n"
                    sa += "• เปิดแทค2/ปิดแทค2\n"
                    sa += "• เปิดแทค3/ปิดแทค3\n"
                    sa += "• เปิดไลค์/ปิดไลค์\n"
                    sa += "• เปิดคอมเม้น/ปิดคอมเม้น\n"
                    sa += "• เปิดบล็อค/ปิดบล็อค\n"
                    sa += "• เปิดแอด/ปิดแอด\n"
                    sa += "• เปิดกันรัน/ปิดกันรัน\n"
                    sa += "• เปิดต้อนรับ/ปิดต้อนรับ\n"
                    sa += "• เปิดต้อนรับ2/ปิดต้อนรับ2\n"
                    sa += "• เปิดคนออก/ปิดคนออก\n"
                    sa += "• เปิดยกเลิก/ปิดยกเลิก\n"
                    sa += "• เปิดโค๊ดติ๊ก/ปิดโค๊ดติ๊ก\n"
                    sa += "• เปิดติ๊กใหญ่/ปิดติ๊กใหญ่"
                    helps = "{}".format(str(sa))
                    data = {
                        "type": "flex",
                        "altText": "{}".format(sas),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#6600CC'
                                 },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type":"text",
                                        "text": sas,
                                        "size":"xl",
                                        "weight":"bold",
                                        "color":"#FFFFCC",
                                        "align":"center"
                                    },
                                    {
                                        "type":"text",
                                        "text": " "
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(sa),
                                        "wrap": True,
                                        "color": "#FFFFCC",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": " "
                                    },
                                    {
                                        "type":"button",
                                        "style":"primary",
                                        "color":"#8B814C",
                                        "action": {
                                            "type":"uri",
                                            "label":"❈͜͡✯ติดต่อทีม✯͜͡❈",
                                            "uri":"http://line.me/ti/p/~zza503"
                                        },
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                if text.lower() == "ดูหนัง":
                    data = {"contents":[{"hero":{"aspectMode":"cover","url":"https://img.live/images/2019/03/13/6cc731eb-4e1e-4add-aff4-b75c2a68da55.png","action":{"uri":"https://www.movie2free.com/portal/","type":"uri"},"type":"image","size":"full"},"styles":{"body":{"backgroundColor":"#660000"},"footer":{"backgroundColor":"#666666"},"header":{"backgroundColor":"#333300"}},"type":"bubble","body":{"contents":[{"text":"หนังหน้าดูปี2019","color":"#FFFF66","wrap":True,"weight":"bold","type":"text","size":"lg","align":"center"},{"type":"separator","color":"#6F4E37"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://img.live/images/2019/03/12/51566.png"},{"text":"͜࿐้ོུ͜ หนังใหม่อัพเดททุกวัน","color":"#FFCC99","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"เดียร์","size":"xs","align":"end","color":"#00FFFF","wrap":True,"type":"text"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://img.live/images/2019/03/12/51566.png"},{"text":"͜࿐้ོུ͜หนัง2018","color":"#FFCC99","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"🇹🇭 ᴛᴇᴀᴍ ᴘʏᴛʜᴏɴ ᴛʜ �🇭","size":"xs","align":"end","color":"#00FFFF","wrap":True,"type":"text"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://img.live/images/2019/03/12/51566.png"},{"text":"࿐้ོུ͜คอหนังไม่ควรพลาด!","color":"#FFCC99","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"🇹🇭 ᴛᴇᴀᴍ ᴘʏᴛʜᴏɴ ᴛʜ 🇹🇭","size":"xs","align":"end","color":"#00FFFF","wrap":True,"type":"text"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://img.live/images/2019/03/12/51566.png"},{"text":"࿐้ོུ͜ที่นี่แน่นอน!","color":"#FFCC99","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"เดียร์","size":"xs","align":"end","color":"#00FFFF","wrap":True,"type":"text"}],"type":"box","spacing":"xs","layout":"vertical"},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"ติดต่อสอบถาม!","size":"xl","wrap":True,"weight":"bold","color":"#FFFFFF","action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"},"align":"center"}]},"header":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":" หนังใหม่ชนโรง","size":"xl","wrap":True,"weight":"bold","color":"#FFFFFF","action":{"type":"uri","uri":"https://www.movie2free.com/portal/"},"align":"center"}]}},{"hero":{"aspectMode":"cover","url":"https://img.live/images/2019/03/13/images28.jpg","action":{"uri":"https://www.movie2free.com/portal/","type":"uri"},"type":"image","size":"full"},"styles":{"body":{"backgroundColor":"#660000"},"footer":{"backgroundColor":"#666666"},"header":{"backgroundColor":"#333300"}},"type":"bubble","body":{"contents":[{"text":"หนังใหม่ชนโรงTH","color":"#FFFF66","wrap":True,"weight":"bold","type":"text","size":"lg","align":"center"},{"type":"separator","color":"#6F4E37"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://img.live/images/2019/03/12/51566.png"},{"text":"࿐้ོུ͜แอพที่ดีที่สุด","color":"#FFCC99","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"เดียร์","size":"xs","align":"end","color":"#00FFFF","wrap":True,"type":"text"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://img.live/images/2019/03/12/51566.png"},{"text":"࿐้ོུ͜มีหนังให้ชมเพียบ!","color":"#FFCC99","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"เดียร์","size":"xs","align":"end","color":"#00FFFF","wrap":True,"type":"text"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://img.live/images/2019/03/12/51566.png"},{"text":"࿐้ོུ͜ทั้งไทย - ฝรั่ง","color":"#FFCC99","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"เดียร์","size":"xs","align":"end","color":"#00FFFF","wrap":True,"type":"text"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://img.live/images/2019/03/12/51566.png"},{"text":"คมชัด100%","color":"#FFCC99","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"เดียร์","size":"xs","align":"end","color":"#00FFFF","wrap":True,"type":"text"}],"type":"box","spacing":"xs","layout":"vertical"},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"เพิ่มเติม","size":"xl","wrap":True,"weight":"bold","color":"#FFFFFF","action":{"type":"uri","uri":"https://line.me/ti/p/~-..-por"},"align":"center"}]},"header":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":" หนังใหม่","size":"xl","wrap":True,"weight":"bold","color":"#FFFFFF","action":{"type":"uri","uri":"https://garena.live/RoVTH"},"align":"center"}]}},{"body":{"contents":[{"text":"✨การแข่งขันROV TH 2019✨","color":"#FFFF66","wrap":True,"weight":"bold","type":"text","size":"lg","align":"center"},{"type":"separator","color":"#6F4E37"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://img.live/images/2019/03/13/garena-logo.png"},{"text":"࿐้ོུ͜เข้าชมง่าย","color":"#EE0000","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"เดียร์","size":"xs","align":"end","color":"#00FFFF","wrap":True,"type":"text"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://img.live/images/2019/03/13/garena-logo.png"},{"text":"࿐้ོུ͜ไม่ต้องพึ่งYoutube","color":"#EE0000","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"เดียร์","size":"xs","align":"end","color":"#00FFFF","wrap":True,"type":"text"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://img.live/images/2019/03/13/garena-logo.png"},{"text":"࿐้ོུ͜เอาใจสาวกคอROV","color":"#EE0000","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"เดียร์","size":"xs","align":"end","color":"#00FFFF","wrap":True,"type":"text"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://img.live/images/2019/03/12/51566.png"},{"text":"࿐้ོུ͜ภาพชัด100%(อยู่ที่เน็ต)","color":"#EE0000","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"เดียร์","size":"xs","align":"end","color":"#00FFFF","wrap":True,"type":"text"}],"type":"box","spacing":"xs","layout":"vertical"},"hero":{"aspectMode":"cover","url":"https://img.live/images/2019/03/13/maxresdefault.jpg","action":{"uri":"https://garena.live/RoVTH","type":"uri"},"type":"image","size":"full"},"styles":{"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#00008B"},"header":{"backgroundColor":"#00008B"}},"type":"bubble","footer":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"ตารางการแข่งขัน","size":"xl","wrap":True,"weight":"bold","color":"#FFFFFF","action":{"type":"uri","uri":"https://esports.rov.in.th/rtpl"},"align":"center"}]},"header":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":" ROV 2019","size":"xl","wrap":True,"weight":"bold","color":"#FFFFFF","action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"},"align":"center"}]}},{"hero":{"aspectMode":"cover","url":"https://i.ibb.co/fvJPwDd/87396.jpg","action":{"uri":"http://line.me/ti/p/~zza503","type":"uri"},"type":"image","size":"full"},"styles":{"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#00008B"},"header":{"backgroundColor":"#00008B"}},"type":"bubble","body":{"contents":[{"text":"เดียร์","color":"#00FFFF","wrap":True,"weight":"bold","type":"text","size":"lg","align":"center"},{"type":"separator","color":"#6F4E37"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://i.ibb.co/fvJPwDd/87396.jpg"},{"text":"❂➣ ʀᴏᴏᴍ / ɢᴄ sᴍᴜʟᴇ","color":"#FFFF00","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"150k/Bln","size":"xs","align":"end","color":"#00FF00","wrap":True,"type":"text"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://i.ibb.co/DGVnmTn/1533968430632.jpg"},{"text":"เดียร์","color":"#FFFF00","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"200k Sampai Selesai","size":"xs","align":"end","color":"#00FF00","wrap":True,"type":"text"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://i.ibb.co/DGVnmTn/1533968430632.jpg"},{"text":"เดียร์","color":"#FFFF00","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"180k/Bln","size":"xs","align":"end","color":"#00FF00","wrap":True,"type":"text"},{"contents":[{"contents":[{"size":"xl","type":"icon","url":"https://i.ibb.co/DGVnmTn/1533968430632.jpg"},{"text":"❂➣ DLL","color":"#FFFF00","flex":0,"weight":"bold","type":"text","margin":"none"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"text":"--","size":"xs","align":"end","color":"#00FF00","wrap":True,"type":"text"}],"type":"box","spacing":"xs","layout":"vertical"},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"ŦΔP Ħ€Ř€ ŦØ ØŘĐ€Ř","size":"xl","wrap":True,"weight":"bold","color":"#FFFFFF","action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"},"align":"center"}]},"header":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":" ØP€Ň ØŘĐ€Ř","size":"xl","wrap":True,"weight":"bold","color":"#FFFFFF","action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"},"align":"center"}]}}],"type":"carousel"}
                    data = {'type': 'flex','altText': 'Me4N','contents': data}
                    sendTemplate(to, data)
                if text.lower() == "ข้อมูล3":
                    data = {"type":"bubble","styles":{"body":{"backgroundColor":"#E6E6FA"},"footer":{"backgroundColor":"#BA55D3"}},"hero":{"type":"image","url":"https://obs.line-scdn.net/0hGHqhxQ2MGGdMETKGeUdnMHBUFgo7Px4vNCBRAj0XRlRkIVdkeHJQUzwWQAVpdQwycXdfCW0SRlIy","aspectMode":"cover","aspectRatio":"1:1","size":"full","margin":"xxl"},"body":{"type":"box","layout":"vertical","spacing":"md","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","url":"https://i.ibb.co/GWGVd45/20181202-004453.png","size":"xl"},{"type":"text","text":"Used VH_LittleBot LINE","weight":"bold","size":"md","align":"center","color":"#4B0082","action":{"type":"uri","uri":"line://app/1636169025-bgap47xO?type=fotext&text=me"}}]},{"type":"separator","color":"#4B0082"},{"type":"box","layout":"vertical","spacing":"xs","flex":2,"contents":[{"type":"separator","color":"#4B0082"},{"type":"text","text":"Chall","wrap":True,"weight":"bold","align":"center","color":"#4B0082","size":"md"},{"type":"separator","color":"#4B0082"},{"type":"text","text":"MY STATUS PROFILE","wrap":True,"weight":"bold","align":"center","color":"#4B0082","size":"xs"},{"type":"text","text":"Tuman","wrap":True,"align":"center","size":"xxs","color":"#4B0082"}]},{"type":"separator","color":"#4B0082"},{"type":"text","text":"Click Icon Di Bawah","wrap":True,"size":"xs","margin":"md","weight":"bold","align":"center","color":"#4B0082","flex":0},{"type":"box","layout":"horizontal","spacing":"xs","flex":2,"contents":[{"type":"image","url":"https://cdn.icon-icons.com/icons2/374/PNG/512/iPhone-WE-icon_37271.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/camera/"}},{"type":"image","url":"https://cdn4.iconfinder.com/data/icons/social-media-pro-icons/1080/Whatsapp-01-512.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"https://wa.me/?text=Im%20using%20VHBOTS"}},{"type":"image","url":"https://cdn.iconscout.com/icon/free/png-256/settings-409-461608.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/settings"}},{"type":"image","url":"https://i.downloadatoz.com/upload/android/icon/1/5/1/ef36baf8fac387f619c77fbaf613e735.jpg","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/cameraRoll/multi"}},{"type":"image","url":"https://support.apple.com/content/dam/edam/applecare/images/en_US/icloud/featured-content-messages-icon_2x.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"http://line.me/ti/p/qFG-c-gytC"}}]}]},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"My Pict","wrap":True,"align":"center","weight":"bold","color":"#ffffff","size":"xs","action":{"type":"uri","uri":"line://app/1636169025-bgap47xO?type=foimage&img=https://obs.line-scdn.net/0hGHqhxQ2MGGdMETKGeUdnMHBUFgo7Px4vNCBRAj0XRlRkIVdkeHJQUzwWQAVpdQwycXdfCW0SRlIy"}},{"type":"separator","color":"#ffffff"},{"type":"text","text":"My Video","wrap":True,"align":"center","weight":"bold","color":"#ffffff","size":"xs","action":{"type":"uri","uri":"line://app/1636169025-bgap47xO?type=video&ocu=https://obs.line-scdn.net//0hGHqhxQ2MGGdMETKGeUdnMHBUFgo7Px4vNCBRAj0XRlRkIVdkeHJQUzwWQAVpdQwycXdfCW0SRlIy/vp&piu=https://obs.line-scdn.net/0hGHqhxQ2MGGdMETKGeUdnMHBUFgo7Px4vNCBRAj0XRlRkIVdkeHJQUzwWQAVpdQwycXdfCW0SRlIy"}}]}}
                    data = {'type': 'flex','altText': 'ข้อมูล3','contents': data}
                    sendTemplate(to, data)
                if text.lower() == "me":
                    contact = maxgie.getContact(sender)
                    sendTemplate(to,{"type":"flex","altText": "❈͜͡✯ติดต่อ✯͜͡❈","contents":{"type":"bubble","footer":{"type":"box","layout":"horizontal","contents":[{"color":"#FFFFFF","size":"md","wrap":True,"action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"},"type":"text","text":"❈͜͡✯ติดต่อ✯͜͡❈","align":"center","weight":"bold"},{"type":"separator","color":"#ff99cc"},{"color":"#FFFFCC","size":"md","wrap":True,"action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"},"type":"text","text":"เดียร์","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#ee1289"},"body":{"backgroundColor":"#FFFFCC"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#ff99cc"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"xxl","type":"image","url":"https://img.live/images/2019/03/12/14319.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/14346.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/14337.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/14320.png"},{"type":"separator","color":"#ee1289"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#FF69B4"},{"type":"box","contents":[{"type":"separator","color":"#ee1289"},{"color":"#cd1076","size":"md","wrap":True,"type":"text","text":"❈͜͡✯ติดต่อ✯͜͡❈","weight":"bold"},{"type":"separator","color":"#ff99cc"},{"color":"#ee1289","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#ff99cc"},{"color":"#ee1289","size":"xs","wrap":True,"type":"text","text":"Status Profile:","weight":"bold"},{"type":"text","text":"{}".format(contact.statusMessage),"size":"xxs","wrap":True,"color":"#ee1289"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"},"hero":{"aspectMode":"cover","margin":"xxl","aspectRatio":"1:1","size":"full","type":"image","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)}}})
                if text.lower() == "คำสั่ง":
                    s = "🇨🇽 me\n"
                    s += "🇨🇽 แอพ\n"
                    s += "🇨🇽 ดูหนัง\n"
                    s += "🇨🇽 เพลง [ลิ้งyoutube]\n"
                    s += "🇨🇽 หารูป [ข้อความ]\n"
                    s += "🇨🇽 ยูทูป [ข้อความ]\n"
                    s += "🇨🇽 Google [ข้อความ]\n"
                    s += "🇨🇽 cvp [ลิ้งyoutube]\n"
                    s += "🇨🇽 คลิป [ข้อความ]\n"
                    s += "🇨🇽 เตะดึง [@คนที่จะเตะ]\n"
                    s += "🇨🇽 คำสั่ง2\n"
                    s += "🇨🇽 เปิดจับอ่าน\n"
                    s += "🇨🇽 ปิดจับอ่าน\n"
                    s += "🇨🇽 คำ + คท\n"
                    s += "🇨🇽 ขาว + คท\n"
                    s += "🇨🇽 สแปม [ข้อความ] [จำนวน]\n"
                    s += "🇨🇽 ดึง [ค.ท ที่จะดึง]\n"
                    s += "🇨🇽 คท @"
                    se = "🇵🇳 เปิดแทค/ปิดแทค\n"
                    se += "🇵🇳 เปิดแทค2/ปิดแทค2\n"
                    se += "🇵🇳 เปิดแทค3/ปิดแทค3\n"
                    se += "🇵🇳 เปิดแทค4/ปิดแทค4\n"
                    se += "🇵🇳 เปิดแทค5/ปิดแทค5\n"
                    se += "🇵🇳 เชคคลอ เปิด ปิด\n"
                    se += "🇵🇳 เปิดคอมเม้น/ปิดคอมเม้น\n"
                    se += "🇵🇳 เปิดบล็อค/ปิดบล็อค\n"
                    se += "🇵🇳 เปิดแอด/ปิดแอด\n"
                    se += "🇵🇳 เปิดกันรัน/ปิดกันรัน\n"
                    se += "🇵🇳 เปิดต้อนรับ/ปิดต้อนรับ\n"
                    se += "🇵🇳 เปิดต้อนรับ2/ปิดต้อนรับ2\n"
                    se += "🇵🇳 เปิดคนออก/ปิดคนออก\n"
                    se += "🇵🇳 เปิดยกเลิก/ปิดยกเลิก\n"
                    se += "🇵🇳 เปิดติ๊กคนเข้า/ปิดติ๊กคนเข้า\n"
                    se += "🇵🇳 เปิดติ๊กคนออก/ปิดติ๊กคนออก\n"
                    se += "🇵🇳 เปิดติ๊กใหญ่/ปิดติ๊กใหญ่\n"
                    se += "🇵🇳 เปิดเตะแทค/ปิดเตะแทค\n"
                    se += "🇵🇳 เปิดมุดลิ้ง/ปิดมุดลิ้ง\n"
                    se += "🇵🇳 เปิดเชคโพส/ปิดเชคโพส"
                    sti = "🇳🇫 ตั้งติ๊กคนแอด\n"
                    sti += "🇳🇫 ลบติ๊กคนแอด\n"
                    sti += "🇳🇫 ตั้งติ๊กคนแทค\n"
                    sti += "🇳🇫 ลบติ๊กคนแทค\n"
                    sti += "🇳🇫 ตั้งติ๊กคนเข้า\n"
                    sti += "🇳🇫 ลบติ๊กคนเข้า\n"
                    sti += "🇳🇫 ตั้งติ๊กคนออก\n"
                    sti += "🇳🇫 ลบติ๊กคนออก\n"
                    sti += "🇳🇫 เขียน [ข้อความ]\n"
                    sti += "🇳🇫 ไอดีไลน์ [idline]\n"
                    sti += "🇳🇫 ดึง @user\n"
                    sti += "🇳🇫 บล็อค @user\n"
                    sti += "🇳🇫 เพิ่มเพื่อน @user\n"
                    sti += "🇳🇫 ลบเพื่อน @user\n"
                    sti += "🇳🇫 ตั้งรูปโปรไฟล์ [ลิ้งยูทูป]\n"
                    sti += "🇳🇫 ประกาศ [พิม'ประกาศ'เพื่อดูวิธี]\n"
                    sti += "🇳🇫 ประกาศ2 [พิม'ประกาศ2'เพื่อดู]\n"
                    sti += "🇳🇫 คำห้ามพิม [ใส่คำที่ห้ามพิม]\n"
                    sti += "🇳🇫 ล้างคำห้ามพิม [ใส่คำที่จะล้าง]\n"
                    sti += "🇳🇫 เชคคำห้ามพิม\n"
                    sti += "🇳🇫 spam on/off [เลข] [คำ]\n"
                    sti += "🇳🇫 โทร [ จำนวน ]"
                    contact = maxgie.getContact(sender)
                    sendTemplate(to,{"type":"flex","altText": "Help Message","contents":{"type":"carousel","contents":[{"type":"bubble","footer":{"type":"box","layout":"baseline","contents":[{"color":"#FFFF99","size":"md","wrap":True,"action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"},"type":"text","text":"ติดบอทกดที่นี่!","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#EE1289"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#7FFFD4"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)},{"type":"separator","color":"#FFFF99"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/51566.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/51555.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/51564.png"},{"type":"separator","color":"#FF69B4"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#FF69B4"},{"type":"box","contents":[{"type":"separator","color":"#ff99cc"},{"color":"#cd1076","size":"md","wrap":True,"type":"text","text":"❈͜͡✯เดียร์✯͜͡❈","weight":"bold"},{"type":"separator","color":"#FF69B4"},{"color":"#EE1289","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#FF69B4"},{"color":"#EE1289","size":"xs","wrap":True,"type":"text","text":"มุมบันเทิง🎧","weight":"bold"},{"type":"text","text":s,"size":"xxs","wrap":True,"color":"#EE1289"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"}},{"type":"bubble","footer":{"type":"box","layout":"baseline","contents":[{"color":"#FFFF99","size":"md","wrap":True,"action":{"type":"uri","uri":"https://line.me/R/ti/p/%40137gcwpz"},"type":"text","text":"❈͜͡✯สนใจติดต่อ✯͜͡❈","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#EE1289"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#FF69B4"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://img.live/images/2019/03/12/14657.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/14658.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/14674.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/11905.png"},{"type":"separator","color":"#FF69B4"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#FF69B4"},{"type":"box","contents":[{"type":"separator","color":"#FF69B4"},{"color":"#cd1076","size":"md","wrap":True,"type":"text","text":"❈͜͡✯สนใจติดต่อ✯͜͡❈","weight":"bold"},{"type":"separator","color":"#FF69B4"},{"color":"#EE1289","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#EE1289"},{"color":"#EE1289","size":"xs","wrap":True,"type":"text","text":"Menu Media2:","weight":"bold"},{"type":"text","text":se,"size":"xxs","wrap":True,"color":"#EE1289"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"}},{"type":"bubble","footer":{"type":"box","layout":"baseline","contents":[{"color":"#ffffff","size":"md","wrap":True,"action":{"type":"uri","uri":"https://line.me/R/ti/p/%40137gcwpz"},"type":"text","text":"❈͜͡✯สนใจติดต่อ✯͜͡❈","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#EE1289"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#FF99CC"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://img.live/images/2019/03/12/12456.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/12469.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/12467.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/12458.png"},{"type":"separator","color":"#FF69B4"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#FF69B4"},{"type":"box","contents":[{"type":"separator","color":"#ff99cc"},{"color":"#cd1076","size":"md","wrap":True,"type":"text","text":"{ เดียร์ }","weight":"bold"},{"type":"separator","color":"#FF99CC"},{"color":"#EE1289","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#003366"},{"color":"#EE1289","size":"xs","wrap":True,"type":"text","text":"Menu media3:","weight":"bold"},{"type":"text","text":sti,"size":"xxs","wrap":True,"color":"#EE1289"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"}}]}})
                if text.lower() == "!help" or text.lower() == "คำสั่ง2":
                            s = "#EE1289"
                            sa = "🐉 me\n"
                            sa += "🐉 /me\n"
                            sa += "🐉 คท\n"
                            sa += "🐉 ไอดีเรา\n"
                            sa += "🐉 ชื่อเรา\n"
                            sa += "🐉 ตัสเรา\n"
                            sa += "🐉 รูปเรา\n"
                            sa += "🐉 รูปวีดีโอเรา\n"
                            sa += "🐉 ปกเรา\n"
                            sa += "🐉 ข้อมูล\n"
                            sa += "🐉 รีบอท\n"
                            sa += "🐉 ออน\n"
                            sa += "🐉 /ลบรัน\n"
                            sa += "🐉 เชค\n"
                            ss = "🐉แทค\n"
                            sa += "🐉 ยกเชิญ"
                            ss += "🐉 ก็อป @user\n"
                            ss += "🐉 กลับร่าง\n"
                            ss += "🐉 ตั้งapi [พิมเพื่อดูวิธี]\n"
                            ss += "🐉 ล้างapi [คำที่จะลบ]\n"
                            ss += "🐉 เชคapi\n"
                            ss += "🐉 stag [พิม'stag'เพื่อดูวิธี]\n"
                            ss += "🐉 เชค [MID]\n"
                            ss += "🐉 ยูทูป [ข้อความ]\n"
                            ss += "🐉 image [text(ภาษาอังกฤษ)]\n"
                            ss += "🐉 รูป [ข้อความ(ภาษาไทย)]\n"
                            ss += "🐉 playstore [ชื่อแอพ]\n"
                            ss += "🐉 ตั้งรูปโปรไฟล์ [ลิ้งยูทูป]\n"
                            ss += "🐉 ประกาศ [พิม'ประกาศ'เพื่อดูวิธี]\n"
                            ss += "🐉 ยกเลิก [ใส่จำนวนที่จะยกเลิก]"
                            sd = "🐉 ดำ ส่งคท.\n"
                            sd += "🐉 ขาว ส่งคท.\n"
                            sd += "🐉 ดำ @user\n"
                            sd += "🐉 ล้าง @user\n"
                            sd += "🐉 เชคดำ\n"
                            sd += "🐉 คทดำ\n"
                            sd += "🐉 ล้างดำ\n"
                            sd += "🐉 ตั้งต้อนรับ [ข้อความ]\n"
                            sd += "🐉 ตั้งคนออก [ข้อความ]\n"
                            sd += "🐉 ตั้งแอด [ข้อความ]\n"
                            sd += "🐉 ตั้งแทค [ข้อความ]\n"
                            sd += "🐉 ตั้งคอมเม้น [ข้อความ]\n"
                            sd += "🐉 ตั้งค้างเชิญ [จำนวน]\n"
                            sd += "🐉 ตั้งมุดลิ้ง [ข้อความ]\n"
                            sd += "🐉 ตั้งคนบล็อค [ข้อความ]"
                            se = "🐉 เปิดแทค/ปิดแทค\n"
                            se += "🐉 เปิดแทค2/ปิดแทค2\n"
                            se += "🐉 เปิดแทค3/ปิดแทค3\n"
                            se += "🐉 เปิดไลค์/ปิดไลค์\n"
                            se += "🐉 เปิดคอมเม้น/ปิดคอมเม้น\n"
                            se += "🐉 เปิดบล็อค/ปิดบล็อค\n"
                            se += "🐉 เปิดแอด/ปิดแอด\n"
                            se += "🐉 เปิดกันรัน/ปิดกันรัน\n"
                            se += "🐉 เปิดต้อนรับ/ปิดต้อนรับ\n"
                            se += "🐉 เปิดต้อนรับ2/ปิดต้อนรับ2\n"
                            se += "🐉 เปิดคนออก/ปิดคนออก\n"
                            se += "🐉 เปิดยกเลิก/ปิดยกเลิก\n"
                            se += "🐉 เปิดติ๊กคนเข้า/ปิดติ๊กคนเข้า\n"
                            se += "🐉 เปิดติ๊กคนออก/ปิดติ๊กคนออก\n"
                            se += "🐉 เปิดติ๊กใหญ่/ปิดติ๊กใหญ่"
                            sti = "🐉 เปิดมุดลิ้ง/ปิดมุดลิ้ง\n"
                            sti += "🐉 ตั้งติ๊กคนแอด\n"
                            sti += "🐉 ลบติ๊กคนแอด\n"
                            sti += "🐉 ตั้งติ๊กคนแทค\n"
                            sti += "🐉 ลบติ๊กคนแทค\n"
                            sti += "🐉 ตั้งติ๊กคนเข้า\n"
                            sti += "🐉 ลบติ๊กคนเข้า\n"
                            sti += "🐉 ตั้งติ๊กคนออก\n"
                            sti += "🐉 ลบติ๊กคนออก\n"
                            sti += "🐉 เขียน [ข้อความ]\n"
                            sti += "🐉 ไอดีไลน์ [idline]\n"
                            sti += "🐉 ดึง @user\n"
                            sti += "🐉 บล็อค @user\n"
                            sti += "🐉 เพิ่มเพื่อน @user\n"
                            sti += "🐉 ลบเพื่อน @user"
                            g = "🐉 แอด\n"
                            g += "🐉 ไอดีกลุ่ม\n"
                            g += "🐉 ชื่อกลุ่ม\n"
                            g += "🐉 รูปกลุ่ม\n"
                            g += "🐉 ข้อมูลกลุ่ม\n"
                            g += "🐉 คนในห้อง\n"
                            g += "🐉 กลุ่มทั้งหมด\n"
                            g += "🐉 ลิ้ง\n"
                            g += "🐉 เปิดลิ้ง\n"
                            g += "🐉 ปิดลิ้ง\n"
                            g += "🐉 เพื่อน\n"
                            g += "🐉 อัพชื่อ [ข้อความ]\n"
                            g += "🐉 อัพตัส [ข้อความ]\n"
                            g += "🐉 อัพรูปโปร\n"
                            g += "🐉 อัพรูปกลุ่ม"
                            st = "🐉  จุด [ตั้งคนอ่าน]\n"
                            st += "🐉 อ่าน [เช็คคนอ่าน]\n"
                            st += "🐉 เปิดอ่านออโต้/ปิดอ่านออโต้\n"
                            st += "🐉 เปิดเชคโพส/ปิดเชคโพส\n"
                            st += "🐉 โทร  [จำนวน]\n"
                            st += "🐉 !me/!Me\n"
                            st += "🐉 Help\n"
                            st += "🐉 Spsm on  [จำนวน ข้อความ]\n"
                            st += "🐉 เปิดแอบ/ปิดแอบ\n"
                            st += "🐉 ตั้งคนแอบ  [ข้อความ]\n"
                            st += "🐉 คำห้ามพิม  [ข้อความ]\n"
                            st += "🐉 เชคคำห้ามพิม\n"
                            st += "🐉 ล้างคำห้ามพิม  [ใส่คำห้าม]\n"
                            st += "🐉 เปิดเตะแทค/ปิดเตะแทค\n"
                            st += "🐉__"
                            sx = "🐉 เปิดออกแชท/ปิดออกแชท\n"
                            sx += "?? เปิดอ่านคท/ปิดอ่านคท"
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#FFFFCC"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#669900"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                                "size": "xxl"
                                            },
                                            {
                                                "type": "text",
                                                "text": "💃มุมบันเทิง",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CD1076"
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sa,
                                                "color": s, 
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#EE1289",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"❈͜͡✯สนใจติดต่อ✯͜͡❈",
                                                     "uri":"https://line.me/R/ti/p/%40137gcwpz"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#FFFFCC"},
                                        "hero": {"backgroundColor": "#000000"}, 
                                        "footer": {"backgroundColor": "#669900"}, 
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                                "size": "xxl"
                                            },
                                            {
                                                "type": "text",
                                                "text": "🐉 คำสั่งพิเศษ 🐉",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CD1076"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": ss, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#EE1289",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"❈͜͡✯สนใจติดต่อ✯͜͡❈",
                                                     "uri":"https://line.me/R/ti/p/%40137gcwpz"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#FFFFCC"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#669900"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                                "size": "xxl"
                                            },
                                            {
                                                "type": "text",
                                                "text": "🐉 คำสั่งเปิด/ปิด 🐉",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CD1076"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": se, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#EE1289",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"࿐้ོུ͜สนใจติดต่อ",
                                                     "uri":"https://line.me/R/ti/p/%40137gcwpz"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#FFFFCC"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#669900"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                                "size": "xxl"
                                            },
                                            {
                                                "type": "text",
                                                "text": "🐉 คำสั่งตั้งค่า/ติดดำ 🐉",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CD1076"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sd, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#EE1289",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"࿐้ོུ͜สนใจติดต่อ",
                                                     "uri":"https://line.me/R/ti/p/%40137gcwpz"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#FFFFCC"},
                                        "hero": {"backgroundColor": "#000000"}, 
                                        "footer": {"backgroundColor": "#669900"}, 
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                                "size": "xxl"
                                            },
                                            {
                                                "type": "text",
                                                "text": "🐉 คำสั่งทั่วไป 🐉",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CD1076"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sti, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#EE1289",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"❈͜͡✯สนใจติดต่อ✯͜͡❈",
                                                     "uri":"https://line.me/R/ti/p/%40137gcwpz"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#FFFFCC"},
                                        "hero": {"backgroundColor": "#000000"}, 
                                        "footer": {"backgroundColor": "#669900"}, 
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                                "size": "xxl"
                                            },
                                            {
                                                "type": "text",
                                                "text": "🐉 คำสั่งกลุ่ม 🐉",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CD1076"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": g, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#EE1289",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"࿐้ོུ͜สนใจติดต่อ",
                                                     "uri":"https://line.me/R/ti/p/%40137gcwpz"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#FFFFCC"},
                                        "hero": {"backgroundColor": "#000000"}, 
                                        "footer": {"backgroundColor": "#669900"}, 
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                                "size": "xxl"
                                            },
                                            {
                                                "type": "text",
                                                "text": "🐉 คำสั่งทั่วไป 🐉",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CD1076"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": st, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#EE1289",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"࿐้ོུ͜สนใจติดต่อ",
                                                     "uri":"https://line.me/R/ti/p/%40137gcwpz"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#FFFFCC"},
                                        "hero": {"backgroundColor": "#000000"}, 
                                        "footer": {"backgroundColor": "#669900"}, 
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                                "size": "xxl"
                                            },
                                            {
                                                "type": "text",
                                                "text": "🐉 คำสั่งทั่วไป 🐉",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CD1076"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sx, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#EE1289",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"❈͜͡✯สนใจติดต่อ✯͜͡❈",
                                                     "uri":"https://line.me/R/ti/p/%40137gcwpz"
                                                 },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "เดียร์",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
#=====================================================================
                elif msg.text.lower().startswith("ไอดี "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n" + ls
                        maxgie.sendMessage(msg.to, str(ret_))
#=====================================================================
                elif msg.text.lower().startswith("คท "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = maxgie.getContact(ls)
                            mi_d = contact.mid
                            maxgie.sendContact(msg.to, mi_d)
#=====================================================================
                elif "ขำๆนะ " in msg.text:
                    Ri0 = text.replace("ขำๆนะ ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = maxgie.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    maxgie.kickoutFromGroup(to,[target])
                                    maxgie.findAndAddContactsByMid(target)
                                    maxgie.inviteIntoGroup(to,[target])
                                except:
                                    pass
#=====================================================================
                elif cmd.startswith("นับ "):
                           number = removeCmd("นับ", text)
                           if len(number) > 0:
                               if number.isdigit():
                                   number = int(number)
                                   if number > 50000:                                             
                                       client.sendMessage(to,"ว่างๆไม่มีอะรัยทำ")
                                   else:
                                       for i in range(0,number):
                                           maxgie.sendMessage(to,str(i+1))
                                           i += 1+1
                                           time.sleep(0.009)
                               else:
                                  client.sendMessage(to,"โปรดระบุหมายเลขที่ถูกต้อง")
#=====================================================================
                elif 'ไปนอนนะ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               maxgie.kickoutFromGroup(msg.to,[target])      
                               print ("Rfu kick User")
                           except:
                               maxgie.sendMessage(msg.to,"บัคแล้วลูกเพ้ 😫")
#=====================================================================
                elif cmd.startswith("เพลง "):
                    link = removeCmd("เพลง", text)
                    youtubeMp3(to, link)
                elif cmd.startswith("วีดีโอ "):
                    link = removeCmd("วีดีโอ", text)
                    youtubeMp4(to, link)
#=====================================================================
                
#=====================================================================
                elif cmd.startswith("google "):
                            spl = re.split("google ",msg.text,flags=re.IGNORECASE)
                            if spl[0] == "":
                                if spl[1] != "":
                                    try:
                                        if msg.toType != 0:
                                            maxgie.sendMessage(msg.to,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                        else:
                                            maxgie.sendMessage(msg.from_,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                        resp = BeautifulSoup(requests.get("https://www.google.co.th/search",params={"q":spl[1],"gl":"th"}).content,"html.parser")
                                        text = "ผลการค้นหาจาก Google:\n\n"
                                        for el in resp.findAll("h3",attrs={"class":"r"}):
                                            try:
                                                tmp = el.a["class"]
                                                continue
                                            except:
                                                pass
                                            try:
                                                if el.a["href"].startswith("/search?q="):
                                                    continue
                                            except:
                                                continue
                                            text += el.a.text+"\n"
                                            text += str(el.a["href"][7:]).split("&sa=U")[0]+"\n\n"
                                        text = text[:-2]
                                        if msg.toType != 0:
                                            maxgie.sendMessage(msg.to,str(text))
                                        else:
                                            maxgie.sendMessage(msg.from_,str(text))
                                    except Exception as e:
                                        print(e) 
#=====================================================================
                elif cmd.startswith("cvp"):
                            link = removeCmd("cvp", text)
                            contact = maxgie.getContact(sender)
                            maxgie.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Download...")
                            print("Sedang Mendownload Data ~")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output video.mp4 {}'.format(link))
                            pict = maxgie.downloadFileURL(pic)
                            vids = "video.mp4"
                            time.sleep(2)
                            changeVideoAndPictureProfile(pict, vids)
                            maxgie.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Succes")
                            os.remove("video.mp4")
#=====================================================================
                elif cmd.startswith("คลิป "):
                            try:
                                sep = msg.text.split("คลิป ")
                                textToSearch = text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                dl=("https://www.youtube.com" + results['href'])
                                vid = pafy.new(dl)
                                stream = vid.streams
                                for s in stream:
                                    vin = s.url
                                    hasil = "Youtube - Video :\n"
                                    hasil += "\nTitle : {}".format(str(vid.title))
                                    hasil += "\nSubscriber From : {}".format(str(vid.author))
                                maxgie.generateReplyMessage(msg.id)
                                maxgie.sendReplyMessage(msg.id, to,hasil)
                                maxgie.sendVideoWithURL(msg.to,vin)
                                print("[YOUTUBE]MP4 Succes")
                            except Exception as e:
                                maxgie.generateReplyMessage(msg.id)
                                maxgie.sendReplyMessage(msg.id, to,str(e))
#=====================================================================
                if text.lower() == "แอพ":
                    pp = maxgie.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = maxgie.getProfile().displayName
                    status = maxgie.getProfile().statusMessage
                    true = True
                    data={"type":"carousel","contents":[{"hero":{"size":"full","type":"image","action":{"uri":"line://app/1648257191-AQJRwmpk?type=profile","type":"uri"},"aspectMode":"cover","url":"https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"aspectRatio":"1:1"},"styles":{"header":{"backgroundColor":"#1C1C1C"},"body":{"backgroundColor":"#1C1C1C"}},"type":"bubble","body":{"type":"box","spacing":"xs","contents":[{"type":"box","margin":"md","layout":"baseline","contents":[{"size":"sm","type":"icon","url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"},{"size":"sm","type":"icon","url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"},{"size":"sm","type":"icon","url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"},{"size":"sm","type":"icon","url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"},{"size":"sm","type":"icon","url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"},{"size":"xxs","type":"text","text":"© 2019","color":"#F8F8FF","align":"end"}]},{"type":"box","spacing":"xs","contents":[{"type":"box","flex":1,"layout":"horizontal","contents":[{"size":"xxs","type":"image","url":"https://i.ibb.co/Gpd4gYq/CC-20190226-120445.png","action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"}},{"size":"xxs","type":"image","url":"https://i.ibb.co/TLMzHYM/CC-20190226-120353.png","action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"}},{"size":"xxs","type":"image","url":"https://i.ibb.co/b1Rgjgf/CC-20190226-120232.png","action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"}},{"size":"xxs","type":"image","url":"https://i.ibb.co/R3zr1X0/CC-20190226-121428.png","action":{"type":"uri","uri":"http://line.me/ti/p/~zza503"}}]},{"contents":[{"size":"xs","type":"text","text":"เดียร์","color":"#4EE7FF","align":"center"},{"size":"xs","type":"text","text":"ᵐᵉⁿᵘ","color":"#4EE7FF","align":"center"},{"size":"xs","type":"text","text":"เดียร์","color":"#4EE7FF","align":"center"},{"size":"xs","type":"text","text":"เดียร์","color":"#4EE7FF"}],"type":"box","layout":"horizontal","spacing":"xxl"}],"layout":"vertical"}],"layout":"vertical"}},{"styles":{"header":{"backgroundColor":"#1C1C1C"},"body":{"backgroundColor":"#1C1C1C"}},"type":"bubble","body":{"type":"box","spacing":"xs","contents":[{"type":"box","layout":"baseline","contents":[{"size":"md","type":"icon","url":"https://i.ibb.co/Scv2SyN/battery-Phones.png"},{"size":"md","type":"icon","url":"https://i.ibb.co/TrLWWVH/signal-icons-53578.png"},{"size":"xxs","flex":0,"type":"text","text":"4G","color":"#66FF66"},{"size":"xxs","type":"text","text":"16:18:03 wib","align":"end","color":"#66FF66"}]},{"type":"box","spacing":"xs","contents":[{"type":"box","flex":1,"layout":"horizontal","contents":[{"size":"xs","type":"image","url":"https://img.live/images/2019/02/28/images.png","action":{"type":"uri","uri":"https://line.me/th/"}},{"size":"xs","type":"image","url":"https://img.live/images/2019/02/28/fb_icon_325x325.png","action":{"type":"uri","uri":"https://m.facebook.com/?stype=lo&jlou=Afe2B6KSMcEhWu3Fh-ZNW0u4WOxhvkD_FUemDw84NtNwxlTCi7Rj45Y7oc1PO0EJppO6jXI_iV6to83e87Ap2fdA9zj5SIjdJm7OXnOOuw_XEg&smuh=5787&lh=Ac-NqKmrimS3g8Y7&_rdr"}},{"size":"xs","type":"image","url":"https://img.live/images/2019/02/28/images11.jpg","action":{"type":"uri","uri":"https://www.instagram.com/?hl=th"}}]},{"contents":[{"size":"xs","type":"text","text":"เดียร์","color":"#4EE7FF","align":"center"},{"size":"xs","type":"text","text":"เดียร์","color":"#4EE7FF","align":"center"},{"size":"xs","type":"text","text":"เดียร์","color":"#4EE7FF","align":"center"}],"type":"box","layout":"horizontal","spacing":"xxl"}],"layout":"vertical"},{"type":"box","spacing":"xs","contents":[{"type":"box","flex":1,"layout":"horizontal","contents":[{"size":"xs","type":"image","url":"https://img.live/images/2019/02/28/images12.jpg","action":{"type":"uri","uri":"https://www.google.com/url?sa=t&source=web&rct=j&url=https://mobile.twitter.com/session/new&ved=2ahUKEwiO8Kf6u9zgAhVKAXIKHYw3ATwQjjgwAHoECAEQAQ&usg=AOvVaw3wYBGNtMzTYLt1ywf0Q-Dx"}},{"size":"xs","type":"image","url":"https://img.live/images/2019/02/28/02f667e51b18cc5d97c96106a7ae067a.jpg","action":{"type":"uri","uri":"https://www.kfc.co.th/menu"}},{"size":"xs","type":"image","url":"https://img.live/images/2019/02/28/images13.jpg","action":{"type":"uri","uri":"https://www.mcdonalds.co.th/?lang=th"}}]},{"contents":[{"size":"xs","type":"text","text":"ᴛᴡɪᴛᴛᴇʀ","color":"#4EE7FF","align":"center"},{"size":"xs","type":"text","text":"เดียร์","color":"#4EE7FF","align":"center"},{"size":"xs","type":"text","text":"เดียร์","color":"#4EE7FF","align":"center"}],"type":"box","layout":"horizontal","spacing":"xxl"}],"layout":"vertical"},{"type":"box","spacing":"xs","contents":[{"type":"box","flex":1,"layout":"horizontal","contents":[{"size":"xs","type":"image","url":"https://img.live/images/2019/02/28/images14.jpg","action":{"type":"uri","uri":"https://www.1112.com"}},{"size":"xs","type":"image","url":"https://img.live/images/2019/02/28/kerry-track.png","action":{"type":"uri","uri":"https://th.kerryexpress.com/th/track/"}},{"size":"xs","type":"image","url":"https://img.live/images/2019/02/28/20140819_3_1408417995_16107.jpg","action":{"type":"uri","uri":"https://www.chesters.co.th"}}]},{"contents":[{"size":"xs","type":"text","text":"เดียร์","color":"#4EE7FF","align":"center"},{"size":"xs","type":"text","text":"ᴋᴇʀʀʏ","color":"#4EE7FF","align":"center"},{"size":"xs","type":"text","text":"เดียร์","color":"#4EE7FF","align":"center"}],"type":"box","layout":"horizontal","spacing":"xxl"}],"layout":"vertical"},{"type":"box","spacing":"xs","contents":[{"type":"box","flex":1,"layout":"horizontal","contents":[{"size":"xs","type":"image","url":"https://img.live/images/2019/02/28/Sizzler-logo.jpg","action":{"type":"uri","uri":"https://www.sizzler.co.th/th"}},{"size":"xs","type":"image","url":"https://img.live/images/2019/02/28/images15.jpg","action":{"type":"uri","uri":"https://termgame.com/new/app"}},{"size":"xs","type":"image","url":"https://img.live/images/2019/02/28/appmajorb4582.jpg","action":{"type":"uri","uri":"http://www.majorcineplex.com/th/main"}}]},{"contents":[{"size":"xs","type":"text","text":"เดียร์","color":"#4EE7FF","align":"center"},{"size":"xs","type":"text","text":"เดียร์","color":"#4EE7FF","align":"center"},{"size":"xs","type":"text","text":"รอบหนังmajor","color":"#4EE7FF","align":"center"}],"type":"box","layout":"horizontal","spacing":"xxl"},{"contents":[{"size":"xs","type":"text","text":"- - -","color":"#F8F8FF","wrap":true,"weight":"bold","align":"center"}],"type":"box","layout":"horizontal","spacing":"md"}],"layout":"vertical"}],"layout":"vertical"}}]}
                    data = {'type': 'flex','altText': 'เดียร์','contents': data}
                    sendTemplate(to, data)
#=====================================================================
                elif msg.text.lower().startswith("ก็อป "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                clone = ast.literal_eval(msg.contentMetadata['MENTION'])
                                clones = clone['MENTIONEES']
                                target = []
                                for clone in clones:
                                    if clone["M"] not in target:
                                        target.append(clone["M"])
                                for she in target:
                                    BackupProfile = maxgie.getContact(sender)
                                    Save1 = "http://dl.profile.line-cdn.net/{}".format(BackupProfile.pictureStatus);Save2 = "{}".format(BackupProfile.displayName);ProfileMe["PictureMe"] = Save1;ProfileMe["NameMe"] = Save2
                                    contact = maxgie.getContact(she);ClonerV2(she)
                                    sendMention(to, contact.mid, "🌸 คุณกำลังก็อปปี้ 🌸", "🌸 สำเร็จแล้ว 🌸");maxgie.sendContact(to, str(BackupProfile.mid));maxgie.sendContact(to, str(contact.mid))
                elif text.lower() == "กลับร่าง":
                            try:
                                maxgiestatus = maxgie.getProfile()
                                maxgieName = maxgie.getProfile()
                                maxgieName.statusMessage = ProfileMe["statusMessage"]
                                maxgieName.pictureStatus = str(ProfileMe["pictureStatus"])
                                maxgie.updateProfile(maxgiestatus)
                                maxgieName.displayName = ProfileMe["NameMe"]
                                maxgie.updateProfile(maxgieName)
                                path = maxgie.downloadFileURL(ProfileMe["PictureMe"])
                                maxgie.updateProfilePicture(path)
                                coverId = ProfileMe["coverId"]
                                maxgie.updateProfileCoverById(coverId)
                                BackupProfile = maxgie.getContact(sender)
                                sendMention(to, BackupProfile.mid, "🌸 กลับบัญชีเดิมเรียบร้อย 🌸", "by~เดียร์");maxgie.sendContact(to, str(BackupProfile.mid))
                            except Exception as error:
                                maxgie.sendMessage(to,"🌸 คุณยังไม่ได้ก็อปปี้ 🌸")
                if text.lower() == "คท":
                    maxgie.generateReplyMessage(msg.id) 
                    maxgie.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': maxgieMID}, contentType=13)
                if text.lower() == "mid" or text.lower() == "ไอดีเรา":
                    maxgie.generateReplyMessage(msg.id)
                    maxgie.sendReplyMessage(msg.id, to,maxgieMID)
                elif text.lower() == "myname" or text.lower() == "ชื่อเรา":
                            h = maxgie.getContact(maxgieMID)
                            foro(to, "🌸 ชื่อของคุณ 🌸\n"+str(h.displayName))
                elif text.lower() == "mybio" or text.lower() == "ตัสเรา":
                            h = maxgie.getContact(maxgieMID)
                            foro(to, "🌸 ตัสของคุณ 🌸\n"+str(h.statusMessage))
                elif text.lower() == "mypicture" or text.lower() == "รูปเรา":
                            h = maxgie.getContact(maxgieMID)
                            image = "http://dl.profile.line-cdn.net/" + h.pictureStatus
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyImageWithURL(msg.id, to, image)
                elif text.lower() == "myvideo" or text.lower() == "รูปวีดีโอเรา":
                            h = maxgie.getContact(maxgieMID)
                            if h.videoProfile == None:
                            	return maxgie.sendMessage(to, "🌸 คุณไม่ได้ใส่รูปวีดีโอ 🌸")
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyVideoWithURL(msg.id, to,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                elif text.lower() == "mycover" or text.lower() == "ปกเรา":
                            h = maxgie.getContact(maxgieMID)
                            cu = maxgie.getProfileCoverURL(maxgieMID)
                            image = str(cu)
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyImageWithURL(msg.id, to, image)
                if text.lower() == "!me":
                    cover = maxgie.getProfileCoverURL(maxgie.profile.mid)
                    pp = maxgie.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = maxgie.getProfile().displayName
                    status = maxgie.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={"type":"flex","altText":"{} sendFlex".format(name),"contents":{"type":"bubble",'styles': {"body":{"backgroundColor":a}},"hero":{"type":"image","url":cover,"size":"full","aspectRatio":"20:13","aspectMode":"cover"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":" "},{"type":"image","url":profile,"size":"lg"},{"type":"text","text":" "},{"type":"text","text":name,"size":"xl","weight":"bold","color":s,"align":"center"},{"type":"text","text":" "},{"type":"text","text":status,"align":"center","size":"xs","color":s,"wrap":True},{"type":"text","text":" "},{"type":"button","style":"primary","color":"#EE1289","action":{"type":"uri","label":"❈͜͡✯สนใจติดต่อ✯͜͡❈","uri":"https://line.me/R/ti/p/%40137gcwpz"}}]}}}
                    sendTemplate(to, data)
                elif text.lower() == "/me":
                            s = temp["te"]
                            a = temp["t"]
                            contact = maxgie.getContact(maxgieMID)
                            cover = maxgie.getProfileCoverURL(maxgieMID)
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit",
                                    },
                                    "body": {
                                       "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "weight": "bold",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1
                                            },
                                            {
                                                "type": "text",
                                                "text": "🌸 รูปโปรไฟล์ 🌸",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
                                       ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "❈͜͡✯สนใจติดต่อ✯͜͡❈",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(cover),
                                        "size": "full",
                                        "aspectRatio":"20:13",
                                        "aspectMode":"cover"
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.mid),
                                                "align": "center",
                                                "color": s,
                                                "size": "sm",
                                                "flex": 1,
                                            },
                                            {
                                                "type": "text",
                                                "text": "🌸 รูปปกพื้นหลัง 🌸",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "❈͜͡✯สนใจติดต่อ✯͜͡❈",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "🌷 ชื่อของคุณ 🌷",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "color": s,
                                                "size": "md"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "align": "center",
                                                "color": a,
                                                "size": "sm",
                                            },
                                            {
                                                "type": "text",
                                                "text": "🌷 สเตตัสของคุณ 🌷",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.statusMessage),
                                                "align": "center",
                                                "color": s,
                                                "wrap": True,
                                                "size": "md"
                                           },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "❈͜͡✯สนใจติดต่อ✯͜͡❈",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(contact.displayName),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "/runtime" or text.lower() == "/ออน":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "🌸 เวลาออน 🌸\n"
                    run += runtime
                    helps = "{}".format(str(run))
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "{}".format(maxgie.getContact(maxgieMID).displayName),
                             "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=uaa47cda3f5823bdeaaa88e57835bb7ba"
                        }
                    }
                    sendTemplate(to, data)
                if text.lower() == "ออน" or text.lower() == "runtime":
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    timeNows = time.time() - Start
                    runtime = timeChange(timeNows)
                    run = "🤡 ผลที่ได้ 🤡\n" + runtime + "\n" + hasil + "ที่" + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n" + "เวลา: " + timeNow.strftime('%H:%M:%S')
                    data = {
                        "type": "flex",
                        "altText": "{}".format(run),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#CC33CC'
                                 },
                            },
                            "hero": {
                                "type": "image",
                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                "size": "full",
                                "aspectRatio": "1:1",
                                "aspectMode": "fit",
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(run),
                                        "wrap": True,
                                        "color": "#FFFF99",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "xl"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == "/รีบอท" or text.lower() == "reset":
                    gifnya = ["https://img.live/images/2019/03/12/12456.png"]
                    data = {
                        "type": "template",
                        "altText": "กำลังรีบอท...",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "full",
                                     "action": {
                                         "type": "uri",
                                          "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                     }
                                }
                            ]
                        }
                    }
                    sendTemplate(to, data)
                    time.sleep(1)
                    ga = "🤡 สำเร็จแล้ว 🤡"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(ga)),
                        "sentBy": {
                             "label": "รีบอทสำเร็จ...",
                             "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=uf12790edd709ff32f99941f922cba7e8"
                        }
                    }
                    sendTemplate(to, data)
                    restartBot()
                if text.lower() == "/speed" or text.lower() == "/sp" or text.lower() == "/สปีด":
                    start = time.time()
                    maxgie.sendMessage("u7117c2d956015d8cd118f15754164354","speed...")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = "ความเร็ว :\n- เชิร์ฟเวอร์ : %.3f วินาที" % (took)
                    data = {"type": "text","text": "{}".format(a),"sentBy": {"label": "%.10f" % (elapsed_time), "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=uaa47cda3f5823bdeaaa88e57835bb7ba"}}
                    #
                    sendTemplate(to,data)
                if text.lower() == "sp" or text.lower() == "speed":
                    start = time.time()
                    maxgie.sendMessage("u7117c2d956015d8cd118f15754164354","❈~ เดียร์ ~❈")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = "🤡 ความเร็ว : %.3f วินาที 🤡" % (took)
                    data = {
                        "type": "flex",
                        "altText": "BotSpeed",
                        "contents": {
                            "type": "bubble",
                            "hero": {
                                "type":"image",
                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                "size": "full",
                                "aspectRatio": "1:1",
                                "aspectMode": "fit"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": a,
                                        "wrap": True,
                                        "color":"#EE1289",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'ข้อมูล' or text.lower() == "/about":
                    try:
                        arr = []
                        owner = "ube7e5b15dbea0cc92f2067c04d25b1fc"
                        creator = maxgie.getContact(owner)
                        contact = maxgie.getContact(maxgieMID)
                        cover = maxgie.getProfileCoverURL(maxgieMID)
                        grouplist = maxgie.getGroupIdsJoined()
                        contactlist = maxgie.getAllContactIds()
                        blockedlist = maxgie.getBlockedContactIds()
                        IdsInvit = maxgie.getGroupIdsInvited()
                        times = time.time() - Start
                        runtime = timeChange(times)
                        sendTemplate(to,{'type':'flex','altText':"about me",'contents':{"type":"bubble","footer":{"type":"box","contents":[{"type":"box","contents":[{"type":"box","contents":[{"align":"center","color":"#ffffff","action":{"type":"uri","uri":"https://line.me/ti/p/~" + str(maxgie.profile.userid)},"weight":"bold","text":"ติดต่อผู้ใช้","type":"text","margin":"xl","size":"sm"}],"layout":"baseline"}],"layout":"horizontal"},{"type":"separator","color":"#ffffff"},{"type":"box","contents":[{"type":"box","contents":[{"align":"center","color":"#ffffff","action":{"type":"uri","uri":"https://line.me/R/ti/p/%40137gcwpz"},"weight":"bold","text":"ติดต่อผู้สร้าง","type":"text","margin":"xl","size":"sm"}],"layout":"baseline"}],"layout":"horizontal"}],"layout":"vertical"},"body":{"type":"box","spacing":"md","contents":[{"type":"box","spacing":"md","contents":[{"type":"image","url":"https://obs.line-scdn.net/{}".format(str(contact.pictureStatus))},{"type":"separator","color":"#EE1289"},{"type":"image","url":str(cover)}],"layout":"horizontal"},{"type":"separator","color":"#ff99cc"},{"type":"box","spacing":"md","contents":[{"align":"center","wrap":True,"weight":"bold","color":"#cd1076","text":"🌸 ❈͜͡✯สนใจติดต่อ✯͜͡❈ 🌸","type":"text","size":"md"}],"layout":"vertical"},{"type":"separator","color":"#ff99cc"},{"type":"box","contents":[{"type":"box","contents":[{"type":"icon","url":"https://i.pinimg.com/originals/89/9f/2c/899f2c29200cae10c0fa04980fadb5ea.png","size":"md"},{"type":"text","color":"#EE1289","weight":"regular","text":"ชื่อผู้ใช้ : "+str(contact.displayName),"margin":"none","size":"xs"}],"layout":"baseline"},{"type":"box","contents":[{"type":"icon","url":"https://i.pinimg.com/originals/89/9f/2c/899f2c29200cae10c0fa04980fadb5ea.png","size":"md"},{"type":"text","color":"#ee1289","weight":"regular","wrap":True,"text":"บอททำงาน : "+str(runtime),"margin":"none","size":"xs"}],"layout":"baseline"},{"type":"box","contents":[{"type":"icon","url":"https://i.pinimg.com/originals/89/9f/2c/899f2c29200cae10c0fa04980fadb5ea.png","size":"md"},{"type":"text","color":"#ee1289","weight":"regular","wrap":True,"text":"ข้อความที่ส่ง : 55","margin":"none","size":"xs"}],"layout":"baseline"},{"type":"box","contents":[{"type":"icon","url":"https://i.pinimg.com/originals/89/9f/2c/899f2c29200cae10c0fa04980fadb5ea.png","size":"md"},{"type":"text","color":"#ee1289","weight":"regular","wrap":True,"text":"ข้อความที่ได้รับ : 999","margin":"none","size":"xs"}],"layout":"baseline"},{"type":"box","contents":[{"type":"icon","url":"https://i.pinimg.com/originals/89/9f/2c/899f2c29200cae10c0fa04980fadb5ea.png","size":"md"},{"type":"text","color":"#ee1289","weight":"regular","wrap":True,"text":"กลุ่ม : "+(str(len(grouplist))),"margin":"none","size":"xs"}],"layout":"baseline"},{"type":"box","contents":[{"type":"icon","url":"https://i.pinimg.com/originals/89/9f/2c/899f2c29200cae10c0fa04980fadb5ea.png","size":"md"},{"type":"text","color":"#ee1289","weight":"regular","wrap":True,"text":"เพื่อน : "+(str(len(contactlist))),"margin":"none","size":"xs"}],"layout":"baseline"},{"type":"box","contents":[{"type":"icon","url":"https://i.pinimg.com/originals/89/9f/2c/899f2c29200cae10c0fa04980fadb5ea.png","size":"md"},{"type":"text","color":"#ee1289","weight":"regular","wrap":True,"text":"การบล็อค : "+(str(len(blockedlist))),"margin":"none","size":"xs"}],"layout":"baseline"},{"type":"box","contents":[{"type":"icon","url":"https://i.pinimg.com/originals/89/9f/2c/899f2c29200cae10c0fa04980fadb5ea.png","size":"md"},{"type":"text","color":"#ee1289","weight":"regular","wrap":True,"text":"ค้างเชิญ : "+(str(len(IdsInvit))),"margin":"none","size":"xs"}],"layout":"baseline"},{"type":"box","contents":[{"type":"icon","url":"https://i.pinimg.com/originals/89/9f/2c/899f2c29200cae10c0fa04980fadb5ea.png","size":"md"},{"type":"text","color":"#ee1289","weight":"regular","wrap":True,"text":"เวอร์ชั่น : 4.4.2","margin":"none","size":"xs"}],"layout":"baseline"},{"type":"box","contents":[{"type":"icon","url":"https://i.pinimg.com/originals/89/9f/2c/899f2c29200cae10c0fa04980fadb5ea.png","size":"md"},{"type":"text","color":"#ee1289","weight":"regular","wrap":True,"text":"ผู้สร้าง : "+str(creator.displayName),"margin":"none","size":"xs"}],"layout":"baseline"}],"layout":"vertical"}],"layout":"vertical"},"styles":{"footer":{"backgroundColor":"#Ee1289"},"body":{"backgroundColor":"#ffffff"}}}})
                    except Exception as e:
                        maxgie.sendMessage(msg.to, str(e))
                elif text.lower() == 'ข้อมูล2' or text.lower() == "about":
                    try:
                        arr = []
                        owner = "ube7e5b15dbea0cc92f2067c04d25b1fc"
                        creator = maxgie.getContact(owner)
                        contact = maxgie.getContact(maxgieMID)
                        grouplist = maxgie.getGroupIdsJoined()
                        contactlist = maxgie.getAllContactIds()
                        blockedlist = maxgie.getBlockedContactIds()
                        IdsInvit = maxgie.getGroupIdsInvited()
                        times = time.time() - Start
                        runtime = timeChange(times)
                        ret_ = "╭───「 About Your 」"
                        ret_ += "\n├🌸 ชื่อ : {}".format(contact.displayName)
                        ret_ += "\n├🌸 กลุ่ม : {}".format(str(len(grouplist)))
                        ret_ += "\n├🌸 เพื่อน : {}".format(str(len(contactlist)))
                        ret_ += "\n├🌸 บล็อค : {}".format(str(len(blockedlist)))
                        ret_ += "\n├🌸 ค้างเชิญ : {}".format(str(len(IdsInvit)))
                        ret_ += "\n├────────────"
                        ret_ += "\n├🌸 เวลาออนบอท :"
                        ret_ += "\n├🌸 {}".format(str(runtime))
                        ret_ += "\n├────────────"
                        ret_ += "\n├🌸 ผู้สร้าง : {}".format(str(creator.displayName))
                        ret_ += "\n╰───「 About Your 」"
                        feds = "{}".format(str(ret_))
                        data = {
                            "type": "text",
                            "text": "{}".format(str(ret_)),
                            "sentBy": {
                                 "label": "{}".format(maxgie.getContact(maxgieMID).displayName),
                                 "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                 "linkUrl": "https://line.me/R/ti/p/%40137gcwpz"
                            }
                        }
                        sendTemplate(to, data)
                        maxgie.sendContact(msg.to, creator.mid)
                    except Exception as e:
                        maxgie.sendMessage(msg.to, str(e))
                elif text.lower() == "/อาหารเสริม" or text.lower() == "/สุขภาพ":
                            gifnya = ['https://img.live/images/2019/03/04/GIF-190304_220733.gif']
                            data = {
                                "type": "template",
                                "altText": "🌼มีผู้กล่าวถึงคุณ🌼",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "อาหารเสริม" or text.lower() == "ผิวขาว":
                            gifnya = ['https://img.live/images/2019/03/06/1551809496104.gif']
                            data = {
                                "type": "template",
                                "altText": "🌼มีผู้กล่าวถึงคุณ🌼",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "ถั่งเฉ่า" or text.lower() == "สุขภาพ":
                            gifnya = ['https://img.live/images/2019/03/06/1551809485707.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "/ทีม" or text.lower() == "ผู้สร้าง":
                            gifnya = ['https://img.live/images/2019/03/06/GIF-190304_12033905334.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "คาสิโน" or text.lower() == "/คาสิโน":
                            gifnya = ['https://img.live/images/2019/03/08/1552057418670.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://bit.ly/2VIisOT"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "คอลลาเจน" or text.lower() == "/คอลลาเจน":
                            gifnya = ['https://img.live/images/2019/03/08/1552057743212.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://line.me/R/ti/p/%40137gcwpz"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif msg.text.lower().startswith("คำห้ามพิม "):
                    wban = msg.text.lower().split()[1:]
                    wban = " ".join(wban)
                    wbanlist.append(wban)
                    foro(to,"%s พิมคำนี้อาจมีจุกนะ5555."%wban)
                elif msg.text.lower().startswith("ล้างคำห้ามพิม "):
                    wunban = msg.text.lower().split()[1:]
                    wunban = " ".join(wunban)
                    if wunban in wbanlist:
                        wbanlist.remove(wunban)
                        foro(to,"%s ล้างออกจากคำสั่งห้ามพิมแล้ว."%wunban)
                    else:
                        foro(to,"%s is not blacklisted."%wunban)
                elif msg.text.lower() == 'เชคคำห้ามพิม':
                    tst = "คำห้ามพิม:\n"
                    if len(wbanlist) > 0:
                        for word in wbanlist:
                            tst += "- %s"%word
                        foro(msg.to,tst)
                    else:
                        foro(msg.to,"คำที่ห้ามพิมทั้งหมด")
                elif msg.text.lower().startswith("ตั้งรูปโปรไฟล์"):
                            link = removeCmd("ตั้งรูปโปรไฟล์", text)
                            contact = maxgie.getContact(sender)
                            foro(to, "Type: Profile\n • Detail: Change video url\n • Status: Download...")
                            print("Sedang Mendownload Data ~")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            pict = maxgie.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            changeVideoAndPictureProfile(pict, vids)
                            foro(to, "Type: Profile\n • Detail: Change video url\n • Status: Succes")
                            os.remove("TeamAnuBot.mp4")
#=====================================================================
#=====================================================================
                elif msg.text.lower().startswith("ดำ "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        apalo["Talkblacklist"][ls] = True
                                        foro(to, '🌸 เพิ่มลงในบัญชีดำเรียบร้อย 🌸')
                                    except:
                                        pass
                elif msg.text.lower().startswith("ล้าง "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del apalo["Talkblacklist"][ls]
                                        foro(to, '🌸 ลบออกจากบัญชีดำเรียบร้อย 🌸')
                                    except:
                                        pass
                elif text.lower() == "เชคดำ":
                            if apalo["Talkblacklist"] == {}:
                              foro(to,"🌸 ไม่พบคนที่เรายัดดำ 🌸")
                            else:
                              ma = ""
                              a = 0
                              for m_id in apalo["Talkblacklist"]:
                                  a = a + 1
                                  end = '\n'
                                  ma += str(a) + ". " +maxgie.getContact(m_id).displayName + "\n"
                              foro(to,"🌸 รายชื่อคนติดดำ 🌸\n\n"+ma+"\nจำนวน %s คนติดดำ" %(str(len(apalo["Talkblacklist"]))))
#=====================================================================                
                if text.lower() == "เปิดบล็อค":
                  if msg._from in admin:
                      settings["autoblock"] = True
                      sa = "🌸 เปิดแล้ว 🌸"
                  else:
                      sa = "เปิดอยู่แล้ว (｀・ω・´)"
                  foro(to, sa)
                if text.lower() == "ปิดบล็อค":
                  if msg._from in admin:
                      settings["autoblock"] = False
                      foro(msg.to,"🌸 ปิดแล้ว 🌸")
                  else:
                      foro(msg.to,"ปิดอยู่แล้ว (｀・ω・´)")
                if text.lower() == "เปิดแทค":
                    tagadd["tags"] = True
                    sa = "🤡 เปิดแล้วว 🤡"
                    foro(to,str(sa))
                if text.lower() == "ปิดแทค":
                    tagadd["tags"] = False
                    sa = "🤡 ปิดแล้ว 🤡"
                    foro(to,str(sa))
                if text.lower() == "เปิดกันรัน":
                    settings["autoCancel"]["on"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดกันรัน":
                    settings["autoCancel"]["on"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดแอด":
                    settings["autoAdd"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดแอด":
                    settings["autoAdd"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดไลค์":
                    settings["autolike"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดไลค์":
                    settings["autolike"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดแทค2":
                    tagadd["tagss"] = True
                    foro(to, "🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดแทค2":
                    tagadd["tagss"] = False
                    foro(to, "🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดคอมเม้น":
                    settings["com"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดคอมเม้น":
                    settings["com"] = False
                    foro(to, "🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดต้อนรับ":
                    settings["Welcome"] = True
                    foro(to, "🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดต้อนรับ":
                    settings["Welcome"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดต้อนรับ2":
                    settings["Wc"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดต้อนรับ2":
                    settings["Wc"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดคนออก":
                    settings["Leave"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดคนออก":
                    settings["Leave"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดยกเลิก":
                    settings["unsendMessage"] = True
                    foro(to, "🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดยกเลิก":
                    settings["unsendMessage"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดติ๊กใหญ่":
                    settings["Sticker"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดติ๊กใหญ่":
                    settings["Sticker"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดโค๊ดติ๊ก":
                    sets["Sticker"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดโค๊ดติ๊ก":
                    sets["Sticker"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดแทค3":
                    sets["tagsticker"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดแทค3":
                    sets["tagsticker"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดติ๊กคนออก":
                    settings["lv"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดติ๊กคนออก":
                    settings["lv"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดติ๊กคนเข้า":
                    settings["wcsti2"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดติ๊กคนเข้า":
                    settings["wcsti2"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดมุดลิ้ง":
                    sets["autoJoinTicket"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดมุดลิ้ง":
                    sets["autoJoinTicket"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดแทค4":
                    maxs["tag"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดแทค4":
                    maxs["tag"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดแทค5":
                    maxs["tag1"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดแทค5":
                    maxs["tag1"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดเตะแทค":
                    maxs["kick"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดเตะแทค":
                    maxs["kick"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                if text.lower() == "เปิดเชคโพส":
                    sets["checkPost"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดเชคโพส":
                    sets["checkPost"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
                elif text.lower() == 'เปิดออกแชท':
                    sets["autoLeave"] = True
                    foro(to, "เปิดระบบออกแชทรวมอัตโนมัติ")
                elif text.lower() == 'ปิดออกแชท':
                    sets["autoLeave"] = False
                    foro(to, "ปิดระบบออกแชทรวมอัตโนมัติ")
                if text.lower() == "เปิดอ่านคท":
                    set["Contact"] = True
                    foro(to, "เปิดแล้วว ><")
                if text.lower() == "ปิดอ่านคท":
                    set["Contact"] = False
                    foro(to, "ปิดแล้วว ><")
                if text.lower() == "เปิดอ่านออโต้":
                    set["autoRead"] = True
                    foro(to,"🤡 เปิดแล้ว 🤡")
                if text.lower() == "ปิดอ่านออโต้":
                    set["autoRead"] = False
                    foro(to,"🤡 ปิดแล้ว 🤡")
#==============================================================================#
                if text.lower() == "ประกาศ":
                    s="**วิธีใช้ =°=\n1.พิม'ตั้งรูปประกาศ'ก่อน\n2.พิม'เชครูปประกาศ'เพื่อดูรูป\n3.กรอกคำที่จะประกาศ + idline"
                    foro(to,s)
                if text.lower() == "ตั้งรูปประกาศ":
                    sets["pict"] = True
                    foro(to,"Send Pict...")
                if text.lower() == "เชครูปประกาศ":
                    path = sets["listpict"]
                    maxgie.sendImage(to, path)
                elif msg.text.lower().startswith("ประกาศ "):
                            delcmd = msg.text.split(" ")
                            get = msg.text.replace(delcmd[0]+" ","").split("/")
                            kw = get[0]
                            ans = get[1]
                            groups = maxgie.getGroupIdsJoined()
                            path = sets["listpict"]
                            for group in groups:
                                sa = "🤡 ประกาศ 🤡\n\n{}".format(str(kw))
                                data = {"type": "flex","altText": "มาอ่านเอาสิ","contents": {"type": "bubble","body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": sa,"wrap": True,"align": "center","size": "md"},{  "type":"text","text":" "},{"type":"button","style":"primary","color":"#ee1289","action": {"type": "uri","label": "✫ ติดต่อเรา ✫","uri": "line://ti/p/~{}".format(ans),}}]}}}
                                sendTemplate(group, data)
                                maxgie.sendImage(group, str(path))
                            maxgie.sendMessage(to, "ส่งคำประกาศเสร็จแล้ว จำนวน {} กลุ่ม".format(str(len(groups))))
                elif msg.text.lower().startswith("ประกาศ "):
                            text = msg.text.replace("ประกาศ ", "")
                            groups = maxgie.getGroupIdsJoined()
                            for group in groups:
                                sa = "─┅•●✫ざণざℓざื❍✫●•┅─\n\n{}".format(str(text))
                                data = {
                                    "type": "flex",
                                    "altText": "ถูกจริง",
                                    "contents": {
                                        "type": "bubble",
                                        "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                        },
                                        "body": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                   "type": "text",
                                                   "text": sa,
                                                   "wrap": True,
                                                   "align": "center",
                                                   "gravity": "center",
                                                   "size": "md"
                                               },
                                               {  
                                                   "type":"text",
                                                   "text":" "
                                               },
                                               {
                                                   "type":"button",
                                                   "style":"primary",
                                                   "color":"#EE1289",
                                                   "action": {
                                                       "type": "uri",
                                                       "label": "🎀 ติดต่อเรา 🎀",
                                                       "uri": "line://ti/p/~{}".format(ans),
                                                   }
                                               }
                                           ]
                                        }
                                    }
                                }
                                sendTemplate(group, data)
                                time.sleep(1)
                            foro(to, "🤡 ส่งคำประกาศจำนวน  {} กลุ่ม เรียบร้อย 🤡".format(str(len(groups))))
#==============================================================================#
                elif text.lower() == "แทค":
                        group = maxgie.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(maxgie.getProfile().mid)
                        maxgie.datamention(to,'แทคทุกคน',nama)
                elif text.lower() == "แทค" or text.lower() == "tagall":
                    if msg._from in maxgieMID:
                        group = maxgie.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
                        nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, jml = [], [], [], [], [], [], [], [], [], len(nama)
                        if jml <= 20:
                          mentionMembers(msg.to, nama)
                        if jml > 20 and jml < 40:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, len(nama)):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                        if jml > 40 and jml < 60:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, len(nama)):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                        if jml > 60 and jml < 80:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, len(nama)):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                        if jml > 80 and jml < 100:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for m in range (80, len(nama)):
                              nm5 += [nama[m]]
                          mentionMembers(msg.to, nm5)
                        if jml > 100 and jml < 120:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, len(nama)):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                        if jml > 120 and jml < 140:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for v in range (120, len(nama)):
                              nm7 += [nama[v]]
                          mentionMembers(msg.to, nm7)
                        if jml > 140 and jml < 160:
                          for i in range (0, 19):
                               nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [nama[q]]
                          mentionMembers(msg.to, nm7)
                          for r in range (140, len(nama)):
                              nm8 += [nama[r]]
                          mentionMembers(msg.to, nm8)
                        if jml > 160 and jml < 180:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [nama[q]]
                          mentionMembers(msg.to, nm7)
                          for z in range (140, 159):
                              nm8 += [nama[z]]
                          mentionMembers(msg.to, nm8)
                          for f in range (160, len(nama)):
                              nm9 += [nama[f]]
                          mentionMembers(msg.to, nm9)
#==============================================================================#
                elif "โทร" in msg.text.lower():
                    if msg.toType == 2:
                        sep = msg.text.split(" ")
                        resp = msg.text.replace(sep[0] + " ","")
                        num = int(resp)
                        try:
                            foro(msg.to,"กำลังดำเนินการ...")
                        except:
                            pass
                        for var in range(num):
                            group = maxgie.getGroup(msg.to)
                            members = [mem.mid for mem in group.members]
                            maxgie.acquireGroupCallRoute(msg.to)
                            maxgie.inviteIntoGroupCall(msg.to, contactIds=members)
                        foro(msg.to,"เชิญคอลสำเร็จแล้ว(｀・ω・´)")
                elif "สแปมแชท " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("สแปมแชท "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               maxgie.sendMessage(msg.to, teks)
                        else:
                           foro(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            foro(msg.to, tulisan)
                        else:
                            foro(msg.to, "Out Of Range!")
                elif msg.text.lower().startswith("เขียน "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=ee1289,70&chf=bg,s,ff99cc"
                    maxgie.sendImageWithURL(msg.to, urlnya)
                elif msg.text.lower().startswith("ดึง "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                       maxgie.findAndAddContactsByMid(ls)
                                       maxgie.inviteIntoGroup(to, [ls])
                                    except:
                                       foro(to, "Limited !")
                elif msg.text.lower().startswith("สะกดจิต"):
                  if msg.toType == 2:
                    data = text.replace("สะกดจิต ","")
                    yud = data.split(' ')
                    yud = yud[0].replace(' ','_')
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            maxgie.unsendMessage(msg_id)
                            maxgie.sendMessage(to, yud,contentMetadata={"MSG_SENDER_NAME": str(maxgie.getContact(ls).displayName),"MSG_SENDER_ICON":"http://dl.profile.line-cdn.net/%s" % maxgie.getContact(ls).pictureStatus})
                elif msg.text.lower().startswith("ยูทูป"):
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["items"] != []:
                                ret_ = []
                                yt = []
                                for music in a["items"]:
                                    ret_.append({
                                        "type": "bubble",
                                        "styles": {
                                            "header": {
                                                "backgroundColor": "#CCFF33"
                                            },
                                            "body": {
                                               "backgroundColor": "#66FFFF",
                                               "separator": True,
                                               "separatorColor": "#EE1289"
                                            },
                                            "footer": {
                                                "backgroundColor": "#CCFF33",
                                                "separator": True,
                                               "separatorColor": "#EE1289"
                                           }
                                        },
                                        "header": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                               {
                                                    "type": "text",
                                                    "text": "Youtube",
                                                    "weight": "bold",
                                                    "color": "#FF00FF",
                                                    "size": "sm"
                                                }
                                            ]
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=ub90fee136a68d4602aa10f734f24ff42"
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "horizontal",
                                            "contents": [{
                                                "type": "box",
                                                "spacing": "none",
                                                "flex": 1,
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "image",
                                                    "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                    "aspectMode": "cover",
                                                    "gravity": "bottom",
                                                    "size": "sm",
                                                    "aspectRatio": "1:1",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                    }
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#111111"
                                            }, {
                                                "type": "box",
                                                "contents": [{
                                                    "type": "text",
                                                    "text": "รับชมกดที่รูป",
                                                    "color": "#0000EE",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "flex": 1,
                                                    "gravity": "top"
                                                }, {
                                                    "type": "text",
                                                    "text": "%s" % music['snippet']['title'],
                                                    "color": "#005500",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
                                                }],
                                                "flex": 2,
                                                "layout": "vertical"
                                            }]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [{
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "button",
                                                    "flex": 2,
                                                    "style": "primary",
                                                    "color": "#3333FF",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Page",
                                                        "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }, {
                                                    "flex": 3,
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#111111",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp3",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }, {
                                                "type": "button",
                                                "margin": "sm",
                                                "style": "primary",
                                                "color": "#111111",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Mp4",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                }
                                            }]
                                        }
                                    }
                                )
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {
                                        "type": "flex",
                                        "altText": "Youtube",
                                        "contents": {
                                            "type": "carousel",
                                            "contents": ret_[aa*10 : (aa+1)*10]
                                        }
                                    }
                                    sendTemplate(to, data)
                elif msg.text.lower().startswith("image "):
                                query = removeCmd("image", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "sendImage",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif msg.text.lower().startswith("playstore "):
                                query = removeCmd("playstore", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.farzain.com/playstore.php?id={}&apikey=KJaOT94NCD1bP1veQoJ7uXc9M".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data != []:
                                    ret_ = []
                                    for music in data:
                                        if 'http://' in music["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(music["icon"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Download",
                                                        "uri": "{}".format(str(music["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Searching App",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif msg.text.lower().startswith("รูป "):
                                query = removeCmd("รูป", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("https://api.boteater.co/googleimg?search={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                        if 'http://' in fn["img"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["img"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(fn["img"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Google_Image",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif msg.text.lower().startswith("ยกเลิก "):
                    mes = 0
                    try:
                        mes = int(args[1])
                    except:
                        mes = 100
                        M = line.getRecentMessagesV2(to, 100)
                        MId = []
                        for ind,i in enumerate(M):
                            if ind == 0:
                                pass
                            else:
                                if i._from == line.profile.mid:
                                    MId.append(i.id)
                                    if len(MId) == mes:
                                        break
                        def unsMes(id):
                            line.unsendMessage(id)
                        for i in MId:
                            thread1 = threading.Thread(target=unsMes, args=(i,))
                            thread1.start()
                            thread1.join()
                        line.sendMessage(to, ' 「 กำลังยกเลิก 」\nยกเลิกทั้งหมด {} ข้อความ'.format(len(MId)))        
                elif msg.text.lower().startswith("เพิ่มเพื่อน "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    maxgie.findAndAddContactsByMid(ls)
                                foro(to, "🌸 เพิ่มเพื่อนสำเร็จ 🌸" + str(contact.displayName) + " to Friendlist")
                elif msg.text.lower().startswith("ลบเพื่อน "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    n = len(maxgie.getAllContactIds())
                                    try:
                                        maxgie.deleteContact(ls)
                                    except:pass
                                    t = len(maxgie.getAllContactIds())
                                    foro(to, "🌸 ❈͜͡✯สนใจติดต่อ✯͜͡❈ 🌸\n • Detail: Delete friend\n • Status: Succes..\n • Before: %s Friendlist\n • After: %s Friendlist"%(n,t))
                elif msg.text.lower().startswith("บล็อค "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    maxgie.blockContact(ls)
                                foro(to, "🌸 บล็อคเพื่อนสำเร็จ 🌸" + str(contact.displayName) + " to Blocklist")
                elif msg.text.lower().startswith("ไอดีไลน์ "):
                            a = removeCmd("ไอดีไลน์", text)
                            b = maxgie.findContactsByUserid(a)
                            line = b.mid
                            maxgie.sendMessage(msg.to,"line://ti/p/~" + a)
                            maxgie.sendContact(to, line)                                                                                           
                elif msg.text.lower().startswith("stag "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = maxgie.getContact(receiver)
                                RhyN_(to, contact.mid)
                elif "/ลบรัน" in msg.text.lower():
                    spl = re.split("/ลบรัน",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = maxgie.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        foro(to, str(txt))
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                maxgie.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    maxgie.sendMessage(gr,spl[1])
                                maxgie.leaveGroup(gr)
                            except:
                                pass
                        sis = "สำเร็จแล้ว (｀・ω・´)"
                        foro(to, str(sis))
#==============================================================================#
                elif text.lower() == 'คนสร้างกลุ่ม' or text.lower() == "แอด":
                    group = maxgie.getGroup(to)
                    cg = group.creator
                    c = cg.mid
                    name = cg.displayName
                    pp = cg.pictureStatus
                    data = {
                        "type": "flex",
                        "altText": "แอดกลุ่ม",
                        "contents": {
                            "type": "bubble",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type":"text",
                                        "text": "─┅•●✫ざণざℓざื❍✫●•┅─ ",
                                        "size":"md",
                                        "color":"#CD1076",
                                        "align":"center"
                                    },
                                    {
                                        "type": "text",
                                        "text": " "
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://profile.line-scdn.net/" + str(pp),
                                        "size": "lg"
                                    },
                                    {
                                        "type":"text",
                                        "text":" "
                                    },
                                    {
                                       "type":"text",
                                       "text": name,
                                       "color":"#CD1076",
                                       "align":"center",
                                       "size":"xl",
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                    maxgie.sendContact(to, c)
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = maxgie.getGroup(to)
                    foro(to, "{ Group ID }\n" + gid.id)
                    maxgie.sendMessage(to, maxgie.getGroup(to).name, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+maxgie.getGroup(to).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~', 'type': 'mt', 'subText': "Yeewa Bots", 'a-installUrl': 'https://line.me/ti/p/~', 'a-installUrl': ' https://line.me/ti/p/~', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~', 'i-linkUri': 'https://line.me/ti/p/~', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~'}, contentType=19)
                elif text.lower() == 'รูปกลุ่ม':
                    group = maxgie.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    maxgie.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = maxgie.getGroup(to)
                    foro(to, "ชื่อกลุ่ม -> \n" + gid.name)   
                elif text.lower() == 'ลิ้ง':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = maxgie.reissueGroupTicket(to)
                            maxgie.sendMessage(to, "ลิ้งของกลุ่ม : "+group.name+"\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == 'เปิดลิ้ง':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            foro(to, "เปิดลิ้งเรียบร้อย")
                        else:
                            group.preventedJoinByTicket = False
                            maxgie.updateGroup(group)
                            foro(to, "เปิดลิ้งเรียบร้อย")
                elif text.lower() == 'ปิดลิ้ง':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            foro(to, "ปิดลิ้งเรียบร้อย")
                        else:
                            group.preventedJoinByTicket = True
                            maxgie.updateGroup(group)
                            foro(to, "ปิดลิ้งเรียบร้อย")
                elif text.lower() == 'ข้อมูลกลุ่ม':
                    group = maxgie.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "ผู้สร้างกลุ่มนี้ลบชี"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ไม่สมารถแสดงลิ้งได้"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(maxgie.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลของกลุ่มนี้ ]"
                    ret_ += "\n╠ ชื่อของกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ไอดีของกลุ่ม : {}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ จำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ จำนวนค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ ลิ้งของกลุ่ม : {}".format(gQr)
                    ret_ += "\n╠ ลิ้งกลุ่ม👉 : {}".format(gTicket)
                    ret_ += "\n╚══─┅•●✫ざণざℓざื❍✫●•┅─"
                    data = {
                        "type": "flex",
                        "altText": "กลุ่ม",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#ffffff'
                                 },
                            },
                            "hero": {
                                "type": "image",
                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                "size": "full",
                                "aspectRatio": "1:1",
                                "aspectMode": "fit",
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": ret_,
                                        "color": "#ee1298",
                                        "wrap": True,
                                        "size": "md",
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
                    maxgie.sendImageWithURL(to, path)
                elif text.lower() == 'คนในห้อง':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        ret_ = "รายชื่อสามชิกในกลุ่มนี้\n"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n\nจำนวน {} คน".format(str(len(group.members)))
                        data = {
                            "type": "flex",
                            "altText": "กลุ่ม",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                        "backgroundColor": '#ffffff'
                                    },
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit",
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": ret_,
                                            "color": "#ee1298",
                                            "wrap": True,
                                            "size": "md"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)
                elif text.lower() == 'กลุ่มทั้งหมด':
                        groups = maxgie.groups
                        ret_ = "รายชื่อกลุ่มทั้งหมด :\n"
                        no = 0 + 1
                        for gid in groups:
                            group = maxgie.getGroup(gid)
                            ret_ += "\n{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n\nจำนวน {} กลุ่ม".format(str(len(groups)))
                        data = {
                            "type": "flex",
                            "altText": "Group list",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                         "backgroundColor": '#ffffff'
                                    },
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit",
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type":"text",
                                            "text": ret_,
                                            "color": "#ee1298",
                                            "wrap": True,
                                            "size": "md"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)
                elif "อัพชื่อ " in text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = maxgie.getProfile()
                        profile_A.displayName = string
                        maxgie.updateProfile(profile_A)
                        foro(msg.to,"Update to :\n" + string)
                        print ("Update Name")

                elif "อัพตัส " in msg.text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = maxgie.getProfile()
                        profile_A.statusMessage = string
                        maxgie.updateProfile(profile_A)
                        foro(msg.to,"Succes Update :\n" + string)
                        print ("Update Bio Succes")
                        
                elif text.lower() == "อัพรูปโปร":
                    sets["changePictureProfile"] = True
                    foro(to, "ส่งรูปภาพลงมาได้เลยครับผม")
                elif text.lower() == "อัพรูปกลุ่ม":
                    if msg.toType == 2:
                        if to not in sets["changeGroupPicture"]:
                            sets["changeGroupPicture"].append(to)
                        foro(to, "ส่งรูปภาพลงมาได้เลยครับผม")
            
                elif text.lower() == 'เพื่อน':
                    contactlist = maxgie.getAllContactIds()
                    kontak = maxgie.getContacts(contactlist)
                    num=1
                    msgs="🎎รายชื่อเพื่อนทั้งหมด🎎"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n🎎รายชื่อเพื่อนทั้งหมด🎎\n\nมีดังต่อไปนี้ : %i" % len(kontak)
                    foro(msg.to, msgs)
                    
                elif msg.text in ["เปิดแอบ"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    foro(msg.to,"เปิดระบบตรวจคนอ่านอัตโนมัติ")
                elif msg.text in ["ปิดแอบ"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        foro(msg.to, "ปิดระบบแอบคนอ่านแล้ว")
#=====================================================================
                elif text.lower()== "ตั้งติ๊กคนแทค":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "tag"
                    foro(to, "🌸 ส่งสติกเกอรที่จะใช่ลงมา 🌸")
                elif msg.text.lower() == "ลบติ๊กคนแทค":
                    sets["messageSticker"]["listSticker"]["tag"] = None
                    foro(to, "🌸 ลบสติกเกอรคนแทคแล้ว 🌸")
                elif msg.text.lower()== "ตั้งติ๊กคนเข้า":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "wc"
                    foro(to, "🌸 ส่งสติกเกอรที่จะใช่ลงมา 🌸")
                elif msg.text.lower() == "ลบติ๊กคนเข้า":
                    sets["messageSticker"]["listSticker"]["wc"] = None
                    foro(to, "🌸 ลบสติกเกอรคนเข้าแล้ว 🌸")
                elif msg.text.lower()== "ตั้งติ๊กคนออก":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "lv"
                    foro(to, "🌸 ส่งสติกเกอรที่จะใช่ลงมา 🌸")
                elif msg.text.lower() == "ลบติ๊กคนออก":
                    sets["messageSticker"]["listSticker"]["lv"] = None
                    foro(to, "🌸 ลบสติกเกอรคนออกแล้ว 🌸")
                elif msg.text.lower()== "ตั้งติ๊กคนแอด":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "add"
                    foro(to, "🌸 ส่งสติกเกอรที่จะใช่ลงมา 🌸")
                elif msg.text.lower() == "ลบติ๊กคนแอด":
                    sets["messageSticker"]["listSticker"]["add"] = None
                    foro(to, "🌸 ลบสติกเกอรคนแอดแล้ว 🌸")
                elif msg.text.lower() == "ตั้งติ๊กมุดลิ้ง":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "join2"
                    foro(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติ๊กมุดลิ้ง":
                    sets["messageSticker"]["listSticker"]["join2"] = None
                    foro(to, "ลบสติกเกอรแล้ว")
#=====================================================================
            elif msg.contentType == 1:
                if sets["pict"] == True:
                    path = maxgie.downloadObjectMsg(msg_id)
                    sets["pict"] = False
                    sets["listpict"] = str(path)
                    foro(to, "Done...")
            elif msg.contentType == 1:
                if sets["changePictureProfile"] == True:
                    path = maxgie.downloadObjectMsg(msg_id)
                    sets["changePictureProfile"] = False
                    maxgie.updateProfilePicture(path)
                    foro(to, "ทำการแปลงโฉมเสร็จเรียบร้อย")
                if msg.toType == 2:
                    if to in sets["changeGroupPicture"]:
                        path = maxgie.downloadObjectMsg(msg_id)
                        sets["changeGroupPicture"].remove(to)
                        maxgie.updateGroupPicture(to, path)
                        foro(to, "เปลี่ยนรูปภาพกลุ่มเรียบร้อยแล้ว")
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                elif msg.contentType == 7:
                    if sets["Sticker"] == True:
                        try:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "「 Check Sticker 」\n"
                            ret_ += "\nSTKID : {}".format(stk_id)
                            ret_ += "\nSTKPKGID : {}".format(pkg_id)
                            ret_ += "\nSTKVER : {}".format(stk_ver)
                            ret_ += "\nLINK : line://shop/detail/{}".format(pkg_id)
                            print(msg)
                            maxgie.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            foro(to, str(ret_))
                        except Exception as error:
                            maxgie.sendMessage(to, str(error))
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in maxgieMID:
                            try:
                                maxgie.kickoutFromGroup(msg.to,[sender])
                                foro("บอกแล้อย่าพิมไม่เชื่อจุกไปสิ55555")
                            except Exception as e:
                                print(e)
                    if "/ti/g/" in msg.text.lower():
                        if sets["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = maxgie.findGroupByTicket(ticket_id)
                                maxgie.acceptGroupInvitationByTicket(group.id,ticket_id)
                                foro(group.id,str(tagadd["m"]))
                                foro(to, "เข้าไปสิงในห้องชื่อ %s 👈 เรียบร้อยแล้ว" % str(group.name))
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            foro(to, "Success Added " + name)
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        foro(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
            elif msg.contentType == 7:
                if sets["Sticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    foro(to, str(ret_))
#=====================================================================
#========================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == "//////แทค":
                    foro(to,"\nสนใจติดบอท\nทำเซลบอทไห้กลายเปนภาพสี(เฟค)\nติดต่อ!\n🇹🇭 ᴛᴇᴀᴍ ᴘʏᴛʜᴏɴ ᴛʜ 🇹🇭\n \nline://ti/p/~zamo15\nhttp://line.me/ti/p/~-..-por")
#========================================================================
            elif msg.contentType == 7: # Content type is sticker
                if settings['Sticker']:
                    if 'STKOPT' in msg.contentMetadata:
                        contact = maxgie.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
                    else:
                        contact = maxgie.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if "MENTION" in msg.contentMetadata.keys() != None:
        	             if maxs['kick'] == True:
        		             contact = maxgie.getContact(msg._from)
        		             cName = contact.displayName
        		             balas = ["เนื่องจากตอนนี้ผมเปิดระบบเตะคนแทคไว้ " + "\n👉" + cName + "\n🙏ต้องขออภัยด้วยจริงๆ🙏Bye!!!"]
        		             ret_ = "" + random.choice(balas)                     
        		             name = re.findall(r'@(\w+)', msg.text)
        		             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
        		             mentionees = mention["MENTIONEES"]
        		             for mention in mentionees:
        			               if mention['M'] in admin:
        				                  foro(msg.to,ret_)
        				                  maxgie.kickoutFromGroup(msg.to,[msg._from])
        				                  break                                  
        			               if mention['M'] in maxgieMID:
        				                  foro(msg.to,ret_)
        				                  maxgie.kickoutFromGroup(msg.to,[msg._from])
        				                  break
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if maxs["tag1"] == True:
                            contact = maxgie.getContact(msg._from) 
                            maxgie.reissueUserTicket()
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if maxgieMID in mention["M"]:
                                     sendTemplate(to,{"type":"flex","altText": "BOTS","contents":{"type":"carousel","contents":[{"type":"bubble","body":{"type":"box","contents":[{"type":"text","wrap":True,"size":"xl","text":"{}".format(str(contact.displayName)),"weight":"bold"},{"type":"box","contents":[{"weight":"bold","text":"Picture ","size":"xl","type":"text","wrap":True,"flex":0},{"weight":"bold","text":"Status","size":"xs","type":"text","wrap":True,"flex":0}],"layout":"baseline"},{"margin":"md","text":"❈͜͡✯สนใจติดต่อ✯͜͡❈","size":"xxs","type":"text","wrap":True,"color":"#ee1289","flex":0}],"spacing":"xs","layout":"vertical"},"footer":{"type":"box","contents":[{"size":"md","action":{"type":"uri","uri":"https://line.me/ti/p/~" + str(maxgie.profile.userid)},"text":"ติดต่อ","weight":"bold","type":"text","wrap":True,"align":"center","color":"#ffffff"}],"layout":"baseline"},"hero":{"margin":"xxl","url":"https://obs.line-scdn.net/{}".format(str(contact.pictureStatus)),"aspectMode":"cover","aspectRatio":"1:1","type":"image","size":"full"},"styles":{"footer":{"backgroundColor":"#ee1289"},"body":{"backgroundColor":"#ffffff"}}},{"type":"bubble","body":{"type":"box","contents":[{"type":"text","wrap":True,"size":"xl","text":"{}".format(str(contact.displayName)),"weight":"bold"},{"type":"box","contents":[{"weight":"bold","text":"Cover","size":"xl","type":"text","wrap":True,"flex":0},{"weight":"bold","text":" Status","size":"xs","type":"text","wrap":True,"flex":0}],"flex":1,"layout":"baseline"},{"margin":"md","text":"❈͜͡✯สนใจติดต่อ✯͜͡❈S","size":"xxs","type":"text","wrap":True,"color":"#ee1289","flex":0}],"spacing":"xs","layout":"vertical"},"footer":{"type":"box","contents":[{"size":"md","action":{"type":"uri","uri":"https://line.me/R/ti/p/%40137gcwpz"},"text":"❈͜͡✯สนใจติดต่อ✯͜͡❈B","weight":"bold","type":"text","wrap":True,"align":"center","color":"#ffffff"}],"layout":"baseline"},"hero":{"margin":"xxl","url":str(maxgie.getProfileCoverURL(msg._from)),"aspectMode":"cover","aspectRatio":"1:1","type":"image","size":"full"},"styles":{"footer":{"backgroundColor":"#ee1289"},"body":{"backgroundColor":"#ffffff"}}},{"type":"bubble","footer":{"type":"box","contents":[{"size":"md","action":{"type":"uri","uri":"https://line.me/R/ti/p/%40137gcwpz"},"text":"❈͜͡✯สนใจติดต่อ✯͜͡❈","weight":"bold","type":"text","wrap":True,"align":"center","color":"#ffffff"}],"layout":"baseline"},"body":{"type":"box","contents":[{"size":"lg","text":"STATUS PROFILE","weight":"bold","type":"text","wrap":True,"color":"#cd1076"},{"type":"box","contents":[{"weight":"bold","text":"{}".format(str(contact.statusMessage)),"size":"sm","type":"text","wrap":True,"flex":0}],"flex":1,"layout":"baseline"},{"margin":"md","text":"❈͜͡✯สนใจติดต่อ✯͜͡❈S","size":"xxs","type":"text","wrap":True,"color":"#ee1289","flex":0}],"spacing":"xs","layout":"vertical"},"styles":{"footer":{"backgroundColor":"#ee1289"},"body":{"backgroundColor":"#ffffff"}}}]}})
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if "MENTION" in msg.contentMetadata.keys() != None:
                        if maxs["tag"] == True:
                            contact = maxgie.getContact(msg._from) 
                            names = contact.displayName
                            pp = contact.pictureStatus
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if maxgieMID in mention["M"]:
                                     sendTemplate(to,{"type":"flex","altText": "auto reply","contents":{"type":"bubble","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"AUTO REPLY","size":"xxl","color":"#CD1076","weight":"bold"},{"type":"text","text":"|","color":"#ffffff"},{"type":"separator","color":"#4b4b4b"}]},"body":{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"image","aspectRatio":"1:1","size":"xl","url": "https://profile.line-scdn.net/" + str(pp)},{"type":"separator","color":"#ffffff","margin":"lg"},{"type":"text","text":names,"size":"lg","margin":"md","color":"#EE1289","gravity":"center","flex":2,"wrap":True}]},{"type":"box","layout":"vertical","contents":[{"type":"spacer","size":"xxl"},{"type":"text","text":tagadd["tag"],"size":"xl","color":"#EE1289","align":"center","wrap":True}]}]},"footer":{"type":"box","layout":"vertical","spacing":"xxl","contents":[{"type":"separator","margin":"xxl","color":"#4b4b4b"},{"type":"button","style":"primary","color":"#EE1289","action":{"type":"uri","label":"ติดต่อ","uri":"https://line.me/R/ti/p/%40137gcwpz"}}]}}})
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if tagadd["tags"] == True:
                            contact = maxgie.getContact(msg._from) 
                            pict = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if maxgieMID in mention["M"]:
                                     data = {
                                         "type": "flex",
                                         "altText": "{}".format(tagadd["tag"]),
                                         "contents": {
                                             "type": "bubble",
                                             "styles": {
                                                 "body": {
                                                     "backgroundColor": '#FFFFFF'
                                                  },
                                             },
                                             "body": {
                                                 "type": "box",
                                                 "layout": "vertical",
                                                 "contents": [
                                                     {
                                                         "type": "text",
                                                         "text": "{}".format(tagadd["tag"]),
                                                         "wrap": True,
                                                         "color": "#EE1289",
                                                         "align": "start",
                                                         "gravity": "center",
                                                         "size": "md"
                                                     },
                                                 ]
                                             }
                                         }
                                     }
                                     sendTemplate(to, data)
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if tagadd["tagss"] == True:
                            contact = maxgie.getContact(sender)
                            cover = maxgie.getProfileCoverURL(sender)
                            names = contact.displayName
                            status = contact.statusMessage
                            pp = contact.pictureStatus
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if maxgieMID in mention["M"]:
                                     data = {
                                         "type": "flex",
                                         "altText": "tagall",
                                         "contents": {
                                             "type": "bubble",
                                             'styles': {
                                                 "body": {
                                                     "backgroundColor": '#FFFFFF'
                                                 },
                                             },
                                             "hero": {
                                                 "type":"image",
                                                 "url": cover,
                                                 "size":"full",
                                                 "aspectRatio":"20:13",
                                                 "aspectMode":"cover"
                                             },
                                             "body": {
                                                 "type": "box",
                                                 "layout": "vertical",
                                                 "contents": [
                                                     {
                                                         "type": "image",
                                                         "url": "https://profile.line-scdn.net/" + str(pp),
                                                         "size": "lg"
                                                     },
                                                     {
                                                          "type":"text",
                                                          "text":" "
                                                     },
                                                     {
                                                         "type":"text",
                                                         "text":"{}".format(names),
                                                         "size":"xl",
                                                         "weight":"bold",
                                                         "color":"#CD1076",
                                                         "align":"center"
                                                     },
                                                     {
                                                         "type": "text",
                                                         "text": status,
                                                         "wrap": True,
                                                         "align": "center",
                                                         "gravity": "center",
                                                         "color": "#EE1289",
                                                         "size": "md"
                                                     },
                                                 ]
                                             }
                                         }
                                     }
                                     sendTemplate(to, data)
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if sets["tagsticker"] == True:
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if maxgieMID in mention["M"]:
                                      msg = sets["messageSticker"]["listSticker"]["tag"]
                                      if msg != None:
                                          contact = maxgie.getContact(maxgieMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
                                      else:
                                          contact = maxgie.getContact(maxgieMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+'ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
#==============================================================================#
        if op.type == 19:
            if maxgieMID in op.param3:
                apalo["Talkblacklist"][op.param2] = True
        if op.type == 26 or op.type == 25:
            msg = op.message
            sender = msg._from
            try:
               if mc["wr"][str(msg.text)]:
                   foro(msg.to,mc["wr"][str(msg.text)])
            except:
              pass
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if msg.text.lower() == "จุด":
                  group = maxgie.getGroup(msg.to)
                  groupMemberMids = [i.mid for i in group.members if i.mid in admin]
                  b=  "พิมว่า อ่าน เพื่อดูสมาชิกที่อ่านข้อความ (｀・ω・´)"
                  if maxgieMID in groupMemberMids:
                      foro(to, b)
                  else:
                      foro(to,b)
                  try:
                      del read['readPoint'][msg.to]
                      del read['readMember'][msg.to]
                  except:
                      pass
                  read['readPoint'][msg.to] = True
                  read['readMember'][msg.to] = {}
                  read['ROM'][msg.to] = {}
                  
                if msg.text.lower() == "อ่าน" or text.lower() == "#reader":
                  group = maxgie.getGroup(msg.to)
                  groupMemberMids = [i.mid for i in group.members if i.mid in admin]
                  if msg.to in read['readPoint']:
                      if read["ROM"][msg.to] == {}:
                          ed = "\nNone"
                          lread = "None"
                      else:
                          ed = ""
                          for i in read["readMember"][msg.to]:
                              ed += "\n- " + maxgie.getContact(i).displayName
                          lr = read["ROM"][msg.to]
                          lread = "- " + maxgie.getContact(lr).displayName

                      b="รายชื่อสมาชิกที่อ่านทั้งหมด\n\nสมาชิกที่อ่าน" + ed + "\n\nสมาชิกที่อ่านล่าสุด\n"+lread+"\n\nพิมพ์ จุด เพื่อตั้งนับอ่านใหม่ (｀・ω・´)"

                      if maxgieMID in groupMemberMids:
                          foro(to, b)
                      else:
                         foro(to,b)
                  else:
                      b="คุณยังไม่ได้ตั้งนับอ่าน พิมพ์ จุด เพื่อตั้งจุดอ่าน (｀・ω・´)"
                      if maxgieMID in groupMemberMids:
                          foro(to, b)
                      else:
                         foro(to,b)
                if msg.text.lower().startswith("เชค "):
                    delcmd = msg.text.split(" ")
                    getx = msg.text.replace(delcmd[0] + " ","")
                    maxgie.sendContact(msg.to,str(getx))
                if msg.text.startswith("ตั้งapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(";;")
                        kw = get[0]
                        ans = get[1]
                        mc["wr"][kw] = ans
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                        foro(msg.to,"คีย์เวิร์ด: " + str(kw) + "\nตอบกลับ: "+ str(ans))
                    except Exception as Error:
                        print(Error)
                if msg.text.startswith("ล้างapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        getx = msg.text.replace(delcmd[0] + " ","")
                        del mc["wr"][getx]
                        maxgie.sendMessage(msg.to, "คำ " + str(getx) + " ล้างแล้ว")
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
                if msg.text.lower() == "เชคapi":
                    lisk = "[ คำตอบโต้ทั้งหมด ]\n"
                    for i in mc["wr"]:
                        lisk+="\nคีย์เวิร์ด: "+str(i)+"\nตอบโต้: "+str(mc["wr"][i])+"\n"
                    lisk+="\nวิธีล้างapi >\\<\nล้างapi ตามด้วยคำที่จะล้าง"
                    foro(to, str(lisk))
            elif msg.contentType == 13:
                if set["Contact"] == True:
                    try:
                        contact = maxgie.getContact(msg.contentMetadata["mid"])
                        if maxgie != None:
                            cover = maxgie.getProfileCoverURL(msg.contentMetadata["mid"])
                        else:
                            cover = "Tidak dapat masuk di line channel"
                        n = "{}".format(str(contact.displayName))
                        m = "{}".format(str(msg.contentMetadata["mid"]))
                        s = "{}".format(str(contact.statusMessage))
                        pict = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        covers = "{}".format(str(cover))
                        data = {
                "type": "flex",
                "altText": "{} Contact".format(n),
                "contents": {
                    "type": "bubble",
                    'styles': {
                        "body": {
                            "backgroundColor": '#FFFFFF'
                        },
                     },
                     "body": {
                         "type": "box",
                         "layout": "vertical",
                         "contents": [
                             {
                                        "type": "text",
                                        "text": "-★ Contact ★-",
                                        "color": "#ee1289",
                                        "align": "center",
                                        "weight":"bold",
                                        "size":"xxl"
                             },
                             {"type": "separator","color": "#ffffff"},
                             {
                                        "type": "text",
                                        "text": "{}".format(n),
                                        "color": "#4b4b4b",
                                        "align": "center",
                                        "weight":"bold",
                                        "size":"md"
                             },
                             {
                                        "type": "text",
                                        "text": "{}".format(s),
                                        "color": "#4b4b4b",
                                        "align": "center",
                                        "wrap": True,
                                        "size":"sm"
                             },
                             {
                                  "type":"button",
                                  "style": "primary",
                                  "color": "#ee1289",
                                  "action": {
                                       "type": "uri",
                                       "label": "• Cover URL •",
                                       "uri": "line://app/1644992891-KOnapywG?type=text&text={}".format(covers)
                                  },
                            },
                            {"type": "separator","color": "#ffffff"},
                            {
                                  "type":"button",
                                  "style": "primary",
                                  "color": "#ee1289",
                                  "action": {
                                       "type": "uri",
                                       "label": "• Pict URL •",
                                       "uri": "line://app/1644992891-KOnapywG?type=text&text={}".format(pict)
                                  },
                            },
                            {"type": "separator","color": "#ffffff"},
                            {
                                  "type":"button",
                                  "style": "primary",
                                  "color": "#ee1289",
                                  "action": {
                                       "type": "uri",
                                       "label": "• MID •",
                                       "uri": "line://app/1644992891-KOnapywG?type=text&text={}".format(m)
                                  },
                            },
                        ]
                    }
                }
            }
                        sendTemplate(to, data)
                    except:
                        foro(to, "เกิดข้อผิดพลาดในการสำรวจ")
#==============================================================================#
#==============================================================================#
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != maxgie.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#========================================================================
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            foro(to, "Success Added " + name)
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        foro(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
                        
        if op.type in [25,26]:
            msg = op.message
            if msg.contentType == 16:
                if sets["checkPost"] == True:
                        try:
                            ret_ = "[ ข้อมูลของโพสนี้ ]"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = maxgie.getContact(msg._from)
                                auth = "\n  ผู้เขียนโพส : {}".format(str(contact.displayName))
                            else:
                                auth = "\n  ผู้เขียนโพส : {}".format(str(msg.contentMetadata["serviceName"]))
                            purl = "\n  ลิ้งโพส : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                            ret_ += auth
                            ret_ += purl
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n  Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "text" in msg.contentMetadata:
                                text = "\n ข้อความโดยย่อ : {}".format(str(msg.contentMetadata["text"]))
                                ret_ += text
                            ret_ += "\n[ สิ้นสุดการเช็คโพส ]"
                            maxgie.sendMessage(to, str(ret_))
                        except:
                            maxgie.sendMessage(to, "เกิดข้อผิดะลาดในการเช็คโพสนี้")
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if set["autoRead"] == True:
                        maxgie.sendChatChecked(to, msg_id)
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
                if msg.contentType == 0 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"location":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                if msg.contentType == 1 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
        if op.type == 65:
            if op.param1 not in chatbot["botMute"]:
                if settings["unsendMessage"] == True:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        ah = time.time()
                        ikkeh = maxgie.getContact(msg_dict[msg_id]["from"])
                        if "text" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                            rat_ += "\nText :\n{}".format(msg_dict[msg_id]["text"])
                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                            del msg_dict[msg_id]
                        else:
                            if "image" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                rat_ += "\nImage :\nBelow"
                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                maxgie.sendImage(at, msg_dict[msg_id]["image"])
                                del msg_dict[msg_id]
                            else:
                                if "video" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    rat_ += "\nVideo :\nBelow"
                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                    maxgie.sendVideo(at, msg_dict[msg_id]["video"])
                                    del msg_dict[msg_id]
                                else:
                                    if "audio" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nAudio :\nBelow"
                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                        maxgie.sendAudio(at, msg_dict[msg_id]["audio"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "sticker" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                            rat_ += "\nSticker :\nBelow"
                                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                            maxgie.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "mid" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nContact :\nBelow"
                                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                maxgie.sendContact(at, msg_dict[msg_id]["mid"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "location" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nLocation :\nBelow"
                                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                    maxgie.sendLocation(at, msg_dict[msg_id]["location"])
                                                    del msg_dict[msg_id]
                                                else:
                                                    if "file" in msg_dict[msg_id]:
                                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                        waktumsg = format_timespan(waktumsg)
                                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                        rat_ += "\nFile :\nBelow"
                                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                        maxgie.sendFile(at, msg_dict[msg_id]["file"])
                                                        del msg_dict[msg_id]
                else:
                    print ("[ ERROR ] Terjadi Error Karena Tidak Ada Data Chat Tersebut~")
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            NOTIFIED_READ_MESSAGE(op)
    except Exception as error:
        logError(error)
#==============================================================================#
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

def run():
    while True:
        try:
            ops = maxgiePoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(maxgieBot(op))
                   maxgiePoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
if __name__ == "__main__":
      run()
