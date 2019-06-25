#ＦＡＲＩＳＢＯＴＬＩＮＥ#
from linepy import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, pafy, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,antolib, subprocess, unicodedata
_session = requests.session()
from gtts import gTTS
from googletrans import Translator
import youtube_dl
#from LineAPI.linepy import *
#from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
#from LineAPI.akad import ChannelService,TalkService
#from LineAPI.akad.ttypes import Message, Location, LoginRequest, ChatRoomAnnouncementContents, ContentType as Type
from thrift.protocol import TCompactProtocol, TBinaryProtocol, TProtocol
from thrift.transport import THttpClient, TTransport
from thrift.Thrift import TProcessor
from multiprocessing import Pool, Process
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread, activeCount
from time import sleep
from datetime import datetime, timedelta
from humanfriendly import format_timespan, format_size, format_number, format_length
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#import time, random, sys, json, codecs, glob, urllib, pytz, ast, os, multiprocessing, subprocess, tempfile, string, six, urllib.parse, traceback, atexit, html5lib, re, wikipedia, ntpath, threading, base64, shutil, humanize, service, os.path, youtube_dl, requests
#import urllib3
#urllib3.disable_warnings()
#import urllib3
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#==============================================================================#
botStart = time.time()
#===============================================================================#
print ("\n\n『✮ のิՁυิπ⇴ℂℝỦҾⱢ ✮』\n")
with open("token.txt","r") as z:
    jepangpunya = z.read()
line = LINE(jepangpunya)
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))


lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()
zxcv = lineMID

oepoll = OEPoll(line)

Rfu = [line]
Exc = [line]
lineMID = line.getProfile().mid
bot1 = line.getProfile().mid
RfuBot=[lineMID]
Family=["ua77ed9dfe7882bfa33f8cea4df61667f",lineMID]
admin=['ua77ed9dfe7882bfa33f8cea4df61667f',lineMID]
adminMID="ua77ed9dfe7882bfa33f8cea4df61667f"
RfuFamily = RfuBot + Family
Bot = RfuBot + Family
welcome = []
leave = []
msg_dict = {}
msg_image={}
msg_video={}
msg_sticker={}
unsendchat = {}
temp_flood = {}
wbanlist = []
wblacklist = []
protectcancel =[]
protectJoin = []
protectInvite = []
protectKick = []
protectQr = []
protectkick = []
protectqr = []
protectjoin = []
protectinvite = []
autocancel = {}
sended = {}
autoinvite = []
autoleaveroom = []
targets = []
pson = {}
pson = {"kw":{}}
#==============================================================================#
settings = {
    "anu": "แอบทมาย",
    "anu2": "เดะจิ้มตาบอด",
    "autoAdd":False,
    "autoBlock":True,
    "autoJoin": False,
    'autoCancel':{"on":True,"members":10},
    "autoLeave": False,
    "autoRead": False,
    "autoReply": False,
    "autoJoinTicket": False,
    "bc":{},
    "blacklist":{},
    "checkContact": False,
    "leaveRoom": False,
    "lang":"JP",
    "W": False,
    "L": False,
    "Nk": False,
    "Api": True,
    "Aip": False,
    "Siri": True,
    "detectMention": False,
    "detectMentionPM": False,
    "delayMention": False,
    "potoMention": False,
    "kickMention": False,
    "protect": False,
    "checkSticker": False,
    "checkContact": False,
    "checkPost": False,
    "server":"VPS",
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "commentBlack":{}, 
    "wblack": False,
    "dblack": False,
    "unsend": False,
    "prankRespon": False,
    "unsendMessage":"",
    "changeGroupPicture": [],
    "changePictureProfile": False,
    "Respontag":"🍞✯มด✯🍞",
    "ResponPM":"🍞✯มด✯🍞",
    "replyPesan": "Sorry , i'm busy right now.",
    "message":"🍞✯มด✯🍞",
    "comment":"🍞✯มด✯🍞",
    "Wc":"กรุณาตั้งคนเข้า",
    "bye":"กรุณาตั้งคนออก",
    "pro":"กรุณาตั้งข้อความ",
    "add":"🍞✯มด✯🍞",
    "kick":"ยังไม่ได้ตั้งคำทักเตะ",
    "c":"🍞✯มด✯🍞",
    "s":"",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "addSticker": {
        "name": "",
        "status": False,
    },  
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {            
            "คนแทค": {
                "STKID": "9469754",
                "STKPKGID": "1233337",
                "STKVER": "1"
            }          
        }
    },
    "mimic": {
       "copy": False,
       "status": False,
       "target": {}
    } 
}
RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": False,
    "autoBlock": False,
}
Setmain = {
    "foto": {},
}
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": False,
}

lgncall = ""
def logincall(this):
    line.sendMessage(lgncall,"login url: " + this)

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

user1 = lineMID
user2 = ""
	
setTime = {}
setTime = rfuSet['setTime']

contact = line.getProfile() 
backup = line.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
squareChatMid='mdbd283c4f8e1840fbcecf1e0e0fd9288'

mulai = time.time() 

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Rh'
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
#==============================================================================================================
#==============================================================================================================
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
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))                                               
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 0*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        userid = "https://line.me/ti/p/~" + line.profile.userid
                    #    line.sendFooter(tmp, "Spam is over , Now Bots Actived !", str(userid), "http://dl.profile.line-cdn.net/"+line.getContact(lineMID).pictureStatus, line.getContact(lineMID).displayName)
                    except Exception as error:
                        logError(error)
                        
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
        
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    line.sendMessage(to, '', contentMetadata, 7)

def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            line.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
        
def Rapid1Say(mtosay):
    line.sendText(Rapid1To,mtosay)

def waktu(secs):
	mins, secs = divmod(secs,60)
	hours, mins = divmod(mins,60)
	days,hours = divmod(hours,24)
	return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)

def delete_log():
    ndt = datetime.datetime.now()
    for data in msg_dict:
        if (datetime.datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = line.genOBSParams({'oid': lineMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = line.server.postContent('{}/talk/vp/upload.nhn'.format(str(line.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        line.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "「{}」\nสวัสดี  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = line.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["Wc"]+"\nชื่อห้อง "+str(ginfo.name)+"\n"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(phusui.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "「{}」\nโชคดีนะ ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = line.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["bye"]+"\nชื่อห้อง "+str(ginfo.name)+"\n"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(phusui.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentionMembers(to, mid):
    try:
        group = line.getGroup(to)
        mids = [mem.mid for mem in group.members]
        jml = len(mids)
        arrData = ""
        if mid[0] == mids[0]:
            textx = "สมาชิก {} คน\n\n".format(str(jml))
        else:
            textx = ""
        arr = []
        for i in mid:
            no = mids.index(i) + 1
            textx += "{}. ".format(str(no))
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
        if no == jml:
            textx += ""
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))
#==============================================================================#
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)
def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessageWithMention(to, lineMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(lineMID)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def sendCarousel(data):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/SendMessage"
    data = data
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.10.1'
    headers['Content-Type'] = 'application/json'
    return requests.Session().post(url,data=json.dumps(data),headers=headers)
#==============================================================================================================
def command(text):
    pesan = text.lower()
    if pesan.startswith(settings["keyCommand"]):
        cmd = pesan.replace(settings["keyCommand"],"")
    else:
        cmd = "Undefined command"
    return cmd        
#==============================================================================================================
def myhelp():
    key = settings["s"]
    key = key.title()  
    myHelp = """╭━━━━━━━━━━━━━━━╮
┃🇬🇧✯มด✯🇬🇧 
┣━━━━━━━━━━━━━━━
┃🇬🇧✒ คิมมี่
┃🇬🇧✒ คิมมี่2
┃🇬🇧✒ คิมมี่3
┃🇬🇧✒ คิมมี่4
┃🇬🇧✒ คิมมี่5
┃🇬🇧✒ คิมมี่6
┣━━━━━━━━━━━━━━━
┃🇬🇧✒ กู
┃🇬🇧✒ คท
┃🇬🇧✒ แปลงคท: (Midเป็น คท.)
┃🇬🇧✒ เชคค่า
┃🇬🇧✒ sp {เช็คความเร็วบอท
┃🇬🇧✒ กูออกนะ {สั่งตัวเองออกกลุ่ม}
┃🇬🇧✒ เวลออน
┣━━━━━━━━━━━━━━━
┃🇬🇧✒ ข้อมูล
┃🇬🇧✒ ไอดี
┃🇬🇧✒ ชื่อ
┃🇬🇧✒ ตัส
┃🇬🇧✒ ดิส
┃🇬🇧✒ ปก
┃🇬🇧✒ วีดีโอ
┃🇬🇧✒ ยกรัน [ข้อความ]
┃🇬🇧✒ อัพดิส
┃🇬🇧✒ อัพดิสกลุ่ม
┃🇬🇧✒ ล้างแชท
┃🇬🇧✒ อัพชื่อ [ข้อความ]
┃🇬🇧✒ อัพตัส [ข้อความ]
┃🇬🇧✒ คอล [ข้อความ]
┃🇬🇧✒ พูด [ข้อความ]
┣━━━━━━━━━━━━━━━
┃🇬🇧✒ สแปม on/off[เลข][ข้อความ]
┃🇬🇧✒ สมาชิกกลุ่ม
┃🇬🇧✒ เชคกลุ่ม
┃🇬🇧✒ ปฏิทิน
┃🇬🇧✒ แทคล่อง
┃🇬🇧✒ ไอดีล่อง
┃🇬🇧✒ คทล่อง
┃🇬🇧✒ คำห้ามพิม [ข้อความ]
┃🇬🇧✒ ล้างคำห้ามพิม [ข้อความ]
┃🇬🇧✒ เชคคำห้ามพิม
┃🇬🇧✒ ยกเลิก [เลข]
┃🇬🇧✒ ยกเชิญ [ใส่จุดข้างหน้าด้วย]
┣━━━━━━━━━━━━━━━
┃🇬🇧✒ ไอดีไลน์ [ไอดีไลน์]
┃🇬🇧✒ เขียน [ข้อความ]
┃🇬🇧✒ เพลสโต [ข้อความ]
┃🇬🇧✒ ประกาศ [ข้อความ]
┃🇬🇧✒ ค้นหา [ข้อความ]
┃🇬🇧✒ ยูทูป [ข้อความ]
┃🇬🇧✒ ดึงวีดีโอ [ใส่เพลงที่จะดึง]
┣━━━━━━━━━━━━━━━
╰━━{ 🇬🇧✯เดียร์✯🇬🇧 }
    """
    return myHelp
def listgrup():
    key = settings["s"]
    key = key.title()    
    listGrup = """╭━━{ 🇬🇧✯เดียร์✯🇬🇧 }
┣━━━━━━━━━━━━━━━
┃🇬🇧✯มด✯🇬🇧
┣━━━━━━━━━━━━━━━
┃🇬🇧✒ แทค
┃🇬🇧✒ แทค2
┃🇬🇧✒ คท @
┃🇬🇧✒ ไอดี @
┃🇬🇧✒ ชื่อ @
┃🇬🇧✒ ตัส @
┃🇬🇧✒ รูป @
┃🇬🇧✒ วีดีโอ @
┃🇬🇧✒ เพิ่มเพื่อน @
┃🇬🇧✒ ลบเพื่อน @
┃🇬🇧✒ ปก @
┃🇬🇧✒ ดึงหมด @
┃🇬🇧✒ แทคล่อง
┃🇬🇧✒ เห่ย [เลข] @
┃🇬🇧✒ ทัก [เลข] @ สต.
┃🇬🇧✒ ดึงหมด สต.
┃🇬🇧✒ เตะเหี้ย
┣━━━━━━━━━━━━━━━
╰━━{ 🇬🇧✯เดียร์✯🇬🇧 }
"""
    return listGrup
def socmedia():
    key = settings["s"]
    key = key.title()  
    socMedia = """╭━━{ 🇬🇧✯เดียร์✯🇬🇧 }
┣━━━━━━━━━━━━━━━━━
┃🇬🇧✯มด✯🇬🇧
┣━━━━━━━━━━━━━━━━━
┃🇬🇧✒ Bmw 
┃🇬🇧✒ ผู้ดูแล
┃🇬🇧✒ โคลนนิ่ง {กอป}
┃🇬🇧✒ ปีโป้อร่อยจัง {ไวรัส}
┃🇬🇧✒ คำสั่ง
┃🇬🇧✒ สีชมพู {ไวรัส}
┃🇬🇧✒ ของขวัญ
┃🇬🇧✒ Kitty  {ไวรัส}
┃🇬🇧✒ ของขวัญ {ของขวัญปลอม}
┃🇬🇧✒ เหี้ย
┃🇬🇧✒ ไม่เหี้ย
┃🇬🇧✒ เชคเหี้ย
┃🇬🇧✒ คทเหี้ย
┃🇬🇧✒ ล้างเหี้ย
┃🇬🇧✒ เตะเหี้ย
┃🇬🇧✒ ไปเส้
┃🇬🇧✒ เตะ @ 
┃🇬🇧✒ ล้อเล่น @
┃🇬🇧✒ Kick @
┃🇬🇧✒ คำห้ามพิม [ข้อความ]
┃🇬🇧✒ ล้างคำห้ามพิม [ข้อความ]
┃🇬🇧✒ เชคคำห้ามพิม
┣━━━━━━━━━━━━━━━━━
╰━━{ 🇬🇧✯เดียร์✯🇬🇧 }
"""
    return socMedia
def helpset():
    key = settings["s"]
    key = key.title()    
    helpSet = """╭━━{ 🇬🇧✯เดียร์✯🇬🇧}
┣━━━━━━━━━━━━━━━━━
┃🇬🇧✒ เปิดแอด/ปิดแอด
┃🇬🇧✒ เปิดคนเข้า/ปิดคนเข้า
┃🇬🇧✒ เปิดคนออก/ปิดคนออก
┃🇬🇧✒ เปิดแทค/ปิดแทค
┃🇬🇧✒ เปิดแทค2/ปิดแทค2
┃🇬🇧✒ เปิดแทค3/ปิดแทค3
┃🇬🇧✒ เปิดบล็อค/ปิดบล็อค
┃🇬🇧✒ เปิดเข้า/ปิดเข้า
┃🇬🇧✒ เปิด/ปิดแทคแชท
┃🇬🇧✒ เปิดออก/ปิดออก
┃🇬🇧✒ เปิดอ่าน/ปิดอ่าน
┃🇬🇧✒ เปิดคท./ปิดคท.
┃🇬🇧✒ เปิด/ปิดอ่านคท
┃🇬🇧✒ เปิดโพส/ปิดโพส
┃🇬🇧✒ เปิดยกเลิก/ปิดยกเลิก
┃🇬🇧✒ เปิดตอบโต้/ปิดตอบโต้
┃🇬🇧✒ เปิดแชท/ปิดแชท
┃🇬🇧✒ เปิด/ปิดพูด
┃🇬🇧✒ เปิด/ปิดตรวจสอบ
┃🇬🇧✒ เปิด/ปิดสีริ
┃🇬🇧✒ เปิด/ปิดทักเตะ
┣━━━━━━━━━━━━━━━━━
┃🇬🇧✒ คนเข้า [เช็คห้องที่ตั้งไว้]
┃🇬🇧✒ คนออก [เช็คห้องที่ตั้งไว้]
┃🇬🇧✒ คนเข้า on
┃🇬🇧✒ คนเข้า off
┃🇬🇧✒ คนออก on
┃🇬🇧✒ คนออก off
┣━━━━━━━━━━━━━━━━━
┃🇬🇧✒ กันลิ้ง on/off
┃🇬🇧✒ กันเชิญ on/off
┃🇬🇧✒ กันคนเข้า on/off
┃🇬🇧✒ กันเตะ on/off
┣━━━━━━━━━━━━━━━━━
┃🇬🇧✒ ตั้งแชท [ข้อความ]
┃🇬🇧✒ ตั้งเข้า [ข้อความ]
┃🇬🇧✒ ตั้งออก [ข้อความ]
┃🇬🇧✒ ตั้งคนแทค [ข้อความ]
┃🇬🇧✒ ตั้ง [ใบคำสั่ง]
┃🇬🇧✒ ตั้งผส [ข้อความ]
┣━━━━━━━━━━━━━━━━━
┃🇬🇧✒ ตั้งติ๊กแทค
┃🇬🇧✒ ลบติ๊กแทค
┣━━━━━━━━━━━━━━━━━
┃🇬🇧✒ ตั้งapi [คีย์เวิร์ด];;[ตอบกลับ]
┃🇬🇧✒ ล้างapi [คีย์เวร์ด]
┃🇬🇧✒ เชคapi
┣━━━━━━━━━━━━━━━━━
┃🇬🇧✒ เชคข้อความแทคแชท
┃🇬🇧✒ เชคข้อความแทค
┃🇬🇧✒ เชคข้อความแอด
┃🇬🇧✒ เชคตั้งผส
┃🇬🇧✒ เชคตั้ง
┃🇬🇧✒ เชคทักออก
┃🇬🇧✒ เชคทักเข้า
┣━━━━━━━━━━━━━━━━━
┃🇬🇧✒ รีเช็ต
┃🇬🇧✒ ประกาศ: 
┃🇬🇧✒ ประกาศ 
┃🇬🇧✒ ประกาศแชท: 
┣━━━━━━━━━━━━━━━━━
╰━━{ 🇬🇧✯เดียร์✯🇬🇧 }
 """
    return helpSet

def helpsetting():
    key = settings["s"]
    key = key.title()   
    helpSetting = """╭━━{ 🇬🇧✯เดียร์✯🇬🇧 }
┣━━━━━━━━━━━━━━━━━
┃🇬🇧✒ แอด
┃🇬🇧✒ ไอดีกลุ่ม
┃🇬🇧✒ รูปกลุ่ม
┃🇬🇧✒ ชื่อกลุ่ม
┃🇬🇧✒ ลิ้ง
┃🇬🇧✒ ดึง
┃🇬🇧✒ เปิดร่าน/ปิดร่าน
┃🇬🇧✒ ข้อมูลกลุ่ม
┃🇬🇧✒ อัพดิสกลุ่ม
┃🇬🇧✒ สมาชิกกลุ่ม
┃🇬🇧✒ เชคกลุ่ม
┣━━━━━━━━━━━━━━━━━
┃🇬🇧✒ mimic no/off เปิด/ปิด
┃🇬🇧✒ mimicadd @แทรค เพิ่ม@
┃🇬🇧✒ mimicdel @แทรค ลบ@
┣━━━━━━━━━━━━━━━━━
┃🇬🇧✒ เปิด/ปิดมุด [ข้องห้องด้วยลิ้งค์]
┃🇬🇧✒ sh (เช็ค tmux)
┃🇬🇧✒ เทส  (เทสระบบ)
┃🇬🇧✒ ยกเชิญ  (ลบค้างเชิญ)
┃🇬🇧✒ ไอดีไลน์  (ขอไอดีไลน์เรา)
┃🇬🇧✒ รักนะ [จำนวล]+[@แทรก]
┃🇬🇧✒ ส่งความรัก [จำนวล]+[@แทรก]
┣━━━━━━━━━━━━━━━━━
┃🇬🇧✒ เปิดแอบอ่าน [ตั้งเวลาดูคนอ่าน]
┃🇬🇧✒ ปิดแอบอ่าน [ปิดการเช็คคนอ่าน]
┃🇬🇧✒ อ่านคนแอบ [ดูคนแอบอ่าน]
┃🇬🇧✒ แอบอ่านใหม่ [ดูคนแอบอ่านใหม่]
┃🇬🇧✒ เปิดแสกน[เปิดดูคนอ่าน]
┃🇬🇧✒ ปิดแสกน [ปิดดูคนอ่าน]
┣━━━━━━━━━━━━━━━━━
╰━━{ 🇬🇧✯เดียร์✯🇬🇧 }

"""
    return helpSetting 
  
def helpsiri():
    #key = settings["s"]
    #key = key.title() 
    helpSiri = """╭━━━{ 🇬🇧✯เดียร์✯🇬🇧 }
┣━━━━━━━━━━━━━━━━
┃      คำสั่งใช้งานบอทสิริ 
┃╭━━━━━━━━━━━━━━━
┃┝🇬🇧✒ /แอด 
┃┝🇬🇧✒ /แอดรอง
┃┝🇬🇧✒ /ตั่งค่า
┃┝🇬🇧✒ /ตั้งแอดรอง
┃┝🇬🇧✒ /สลับ
┃┝🇬🇧✒ /ปลดแอด
┃┝🇬🇧✒ /ทวิทเต้อ
┃┝🇬🇧✒ /ย้ายตั๋ว
┃┝🇬🇧✒ /บอทกลับ
┃┝🇬🇧✒ /ชุดล็อคen
┃┝🇬🇧✒ /ชุดล็อคjp
┃┝🇬🇧✒ /เพิ่มดำ
┃┝🇬🇧✒ /แก้ดำ
┃┝🇬🇧✒ /ลบค้างเชิญ
┃┝🇬🇧✒ /เปลี่ยนอด
┃┝🇬🇧✒ /ปิดลิ้ง
┃┝🇬🇧✒ /เปิดลิ้ง
┃┝🇬🇧✒ /ตั้งอ่าน
┃┝🇬🇧✒ /คนแอบ
┃┝🇬🇧✒ /ปิดการเชิญ
┃┝🇬🇧✒ /เปิดเชิญ
┃┝🇬🇧✒ /ปิดพูด
┃┝🇬🇧✒ /เปิดพูด
┃┝🇬🇧✒ /รันติก
┃┝🇬🇧✒ /ล็อคแอด
┃┝🇬🇧✒ /ล็อคชื่อ
┃┝🇬🇧✒ /ล็อครูป
┃┝🇬🇧✒ /ล็อคเชิญ
┃╰━━━━━━━━━━━━━━━
┃ { คำสั่งใช้ในบอทสิริเท่านั้น }
┣━━━━━━━━━━━━━━━━
╰━━━{ 🇬🇧✯เดียร์✯🇬🇧 }
"""
    return helpSiri
    
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                line.sendMessage(op.param1,(str(settings["add"])))  
            if settings["autoBlock"] == True:
                line.blockContact(op.param1)
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if line.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bot:
                            line.reissueGroupTicket(op.param1)
                            X = line.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            line.updateGroup(X)
                            line.kickoutFromGroup(op.param1,[op.param2])
                            line.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    pass
#        if op.type == 11:    
#        	if line.getGroup(op.param1).preventedJoinByTicket == False:
#        	   line.sendMessage(op.param1,"🍯มีคนทำการเปิดลิ้งกลุ่ม🍯")
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bot:
                    try:
                        group = line.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            line.cancelGroupInvitation(op.param1,[_mid])
                            line.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass  
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bot:
                    settings["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in settings["blacklist"]:
                            line.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return   
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bot:
                    settings["blacklist"][op.param2] = True
                    line.kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass                
        if op.type == 15:
            if op.param1 in leave:
                if op.param2 in Bot:
                    pass
                leaveMe = pson["lv"]
                user = line.getContact(op.param2)
                group = line.getGroup(op.param1)
                get = leaveMe.replace("(ชื่อ)",user.displayName)
                get = get.replace("(ชื่อกลุ่ม)",group.name)               
                if "(แทค)" in get:
                    sendMessageWithMention(op.param1, user.mid)
                get = get.replace("(แทค)","")
                if "(คท)" in get:
                    line.sendContact(op.param1,op.param2)
                get = get.replace("(คท)","")
                if "(รูป)" in get:
                    line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(user.picturePath))
                get = get.replace("(รูป)","")	
                line.sendMessage(op.param1,str(get))
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bot:
                   pass
                welcomemessage = pson["wc"]
                user = line.getContact(op.param2)
                group = line.getGroup(op.param1)
                get = welcomemessage.replace("(ชื่อ)",user.displayName)
                get = get.replace("(ชื่อกลุ่ม)",group.name)               
                if "(แทค)" in get:
                    sendMessageWithMention(op.param1, user.mid)
                get = get.replace("(แทค)","")
                if "(คท)" in get:
                    line.sendContact(op.param1,op.param2)
                get = get.replace("(คท)","")
                if "(รูป)" in get:
                    line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(user.picturePath))
                get = get.replace("(รูป)","")	
                line.sendMessage(op.param1,str(get))                
        if op.type == 13:
            print ("[ 13 ] มีคนเชิญคุณเข้ากลุ่ม")
            group = line.getGroup(op.param1)
            contact = line.getContact(op.param2)
            if settings["autoJoin"] and lineMID in op.param3:
                line.acceptGroupInvitation(op.param1)
                #line.sendMessage(op.param1, op.param2, "สวัสดีครับ", "ขอบคุณที่เชิญผมเข้ากลุ่มนะ")
        if op.type == 13:            
            line.sendMessage(to,"มีคนได้ทำการเชิญเพื่อนเข้ากลุ่ม")    
        if op.type == 13:
            if lineMID in op.param3:
                G = line.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 24:
            if settings["autoLeave"] == True:
                line.leaveRoom(op.param1)                      
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if settings["winvite"] == True:
                     if msg._from in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = line.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 line.sendMessage(msg.to,"-> " + _name + " ทำการเชิญสำเร็จ")
                                 break
                             elif invite in settings["blacklist"]:
                                 line.sendMessage(msg.to,"ขออภัย, " + _name + " บุคคนนี้อยู่ในรายการบัญชีดำ")
                                 line.sendMessage(msg.to,"ใช้คำสั่ง!,ล้างดำ,ดึง" )
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     line.findAndAddContactsByMid(target)
                                     line.inviteIntoGroup(msg.to,[target])
                                     line.sendMessage(msg.to,"เชิญ :" + _name + "เรียบร้อย")
                                     settings["winvite"] = False
                                     break
                                 except:
                                     try:
                                         line.findAndAddContactsByMid(invite)
                                         line.inviteIntoGroup(op.param1,[invite])
                                         settings["winvite"] = False
                                     except:
                                         line.sendMessage(msg.to,"😧ตรวจพบข้อผิดพลาดที่ไม่ทราบสาเหตุ😩อาจเป็นได้ว่าบัญชีของคุณถูกแบนเชิญ😨")
                                         settings["winvite"] = False
                                         break
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        line.sendMessage(msg.to,"รับทราบ")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        line.sendMessage(msg.to,"decided not to comment")

               elif settings["dblack"] == True:
                   if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        line.sendMessage(msg.to,"ลบจากรายการที่ถูกแบนแล้ว [ Done ]")
                        settings["dblack"] = False

                   else:
                        settings["dblack"] = False
                        line.sendMessage(msg.to,"Tidak Ada Dalam Daftar Blacklist")
               elif settings["wblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        line.sendMessage(msg.to,"Sudah Ada")
                        settings["wblacklist"] = False
                   else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        line.sendMessage(msg.to,"เพิ่มบัญชีนี้ในรายการสีดำเรียบร้อยแล้ว")

               elif settings["dblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        line.sendMessage(msg.to,"เพิ่มบัญชีนี้ในรายการสีขาวเรียบร้อยแล้ว [ Done ]")
                        settings["dblacklist"] = False

                   else:
                        settings["dblacklist"] = False
                        line.sendMessage(msg.to,"Tidak Ada Dalam Da ftar Blacklist")    
#==============================================================================================================                       
        if op.type == 26:
            msg = op.message
            if settings["prankRespon"] == True:
                if msg.toType == 0:
                    try:
                        if sended[msg._from] == True:
                            return
                    except:
                        sended[msg._from] = False
                    sended[msg._from] = True
                    contact = line.getContact(msg._from)
                    cName = contact.displayName
                    balas = [str(settings["pro"])]
                    ret_ = random.choice(balas)
                    line.sendMessage(msg._from,ret_)
                else:
                    pass                           
#==============================================================================================================
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sam = squareChatMid
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                elif msg.text.lower().startswith("ตั้งอ่าน1 "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    settings["anu"] = str(say).lower()
                    line.sendMessage(msg.to, "ข้อความคนอ่าน 「 " + str(settings["anu"]) + " 」")
                elif msg.text.lower().startswith("ตั้งอ่าน2 "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    settings["anu2"] = str(say).lower()
                    line.sendMessage(msg.to, "ข้อความคนอ่าน 「 " + str(settings["anu2"]) + " 」")
                elif msg.text.lower().startswith("say "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    line.sendMessage(to, (say))                    
#======================================              
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
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
#==============================================================================#
                if text.lower() == 'คิมมี่':
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))
                    line.sendContact(to, lineMID)         
                elif text.lower() == 'คิมมี่6':                    
                    helpSiri = helpsiri()
                    line.sendMessage(to, str(helpSiri))
                elif text.lower() == 'คิมมี่2':
                    listGrup = listgrup()
                    line.sendMessage(to, str(listGrup))
                elif text.lower() == 'คิมมี่3':
                    socMedia = socmedia()
                    line.sendMessage(to, str(socMedia))
                elif text.lower() == 'คิมมี่4':
                    helpSet = helpset()
                    line.sendMessage(to, str(helpSet))   
                elif text.lower() == 'คิมมี่5':
                    helpSetting = helpsetting()
                    line.sendMessage(to, str(helpSetting))               
                elif text.lower() == 'me':
                    line.sendMentionFooter(to, '「ผู้ใช้งานบอท」\n', sender, "https://line.me/ti/p/~faris_bot", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~faris_bot', 'type': 'mt', 'subText': settings["c"], 'a-installUrl': 'https://line.me/ti/p/~gu.11', 'a-installUrl': ' https://line.me/ti/p/~faris_bot', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~faris_bot', 'i-linkUri': 'https://line.me/ti/p/~faris_bot', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~faris_bot'}, contentType=19)
                elif text.lower() == "คท":
                    me = line.getContact(lineMID)
                    sendMessageWithMention(to, lineMID)                 
                    line.sendContact(to, lineMID)
                    #line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)                      
                elif text.lower() == 'speed':
                    start = time.time()
                    line.sendMessage(to, "กรุณารอสักครู่ค่ะ")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == 'sp':
                    start = time.time()
                    line.sendMessage(to, "ความเร็วบอทคงที่")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")                    
                if text.lower() == 'เวลออน':
                    eltime = time.time() - mulai
                    van = "ระยะเวลาการทำงานของบอท🍯 :\n"+waktu(eltime)
                    line.sendMessage(receiver,van)
                elif msg.text in ["4g","Hk"]:
                    line.sendMessage(msg.to, " Tëst : Prëmium Spëed™\n✧•••••••••❂✧✯✧❂••••••••••✧")
                    line.sendMessage(msg.to, " S.p.ë.e.d")
                    start = time.time()
                    time.sleep(0.02)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time))   
#                elif msg.text in ["หำออน"]:
#                    line.sendMessage(msg.to,"ระยะเวลาการทำงานของบอท⏰")
#                    line.sendMessage(msg.to,"\n📆20วัน🕛5ชั่วโมง🕒5นาที🕘38วินาที")    
                elif msg.text in ["9g",".22"]:
                    line.sendMessage(msg.to, "Hî Speëd:•➣➣➣➣➣➣➣➣")
                    line.sendMessage(msg.to, "")
                    start = time.time()
                    time.sleep(0.03)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time))
#------------------------------------------------------------------------------------------------------------
                elif msg.text in ["รถเต่า","Bmx","Bmw","Benz","ปอร์เช่","เบ้นซ์","จากัวร์","เฟอร์รารี่"]:
                    line.sendMessage(msg.to, "■•■•■• 3500cc •■•■•■")
                    line.sendMessage(msg.to, "●•➤➤➤➤➤➤➤➤➤➤")
                    line.sendMessage(msg.to, "●•➤➤➤➤➤➤➤➤➤➤➤➤")
                    start = time.time()
                    time.sleep(0.05)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time))                
#-------------------------------------------------------------------------------------------------------------
                elif msg.text in ["fc",".45"]:
                    line.sendMessage(msg.to, "")
                    line.sendMessage(msg.to, "❂•➣➣➣ S.p.ë.e.d ➣➣➣➣")
                    start = time.time()
                    time.sleep(0.03)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time))
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
                elif msg.text in ["6g","M16"]:
                    line.sendMessage(msg.to, "✧•••••••••❂✧✯✧❂••••••••••✧\n     ♡♡ HELLO KITTY ♡♡\n✧•••••••••❂✧✯✧❂••••••••••✧")
                    line.sendMessage(msg.to, "❂•➣➣➣ S.p.ë.e.d ➣➣➣➣")
                    start = time.time()
                    time.sleep(0.04)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time))
                elif msg.text in ["กูออกนะ"]:
                    line.leaveGroup(msg.to)                    
                elif msg.text in ".ต้อนรับ":
                   line.sendReplyMessage(msg.id, to,"วิธีการใช้งานตัวอย่างเช่น\nตั้งเข้า ดีครับ (ชื่อ) สู่กลุ่ม (ชื่อกลุ่ม) (แทค) (คท) (รูป)\nชื่อ = ชื่อคนที่เข้า\nชื่อกลุ่ม = ชื่อกลุ่มที่เข้ามา\nแทค = แทคคนที่เข้า\nคท = ส่งคทคนที่เข้า\nรูป = ส่งรูปคนเข้า")
                elif msg.text in ".อำลา":
                   line.sendReplyMessage(msg.id, to,"วิธีการใช้งานตัวอย่างเช่น\nตั้งออก บาย (ชื่อ) สู่กลุ่ม (ชื่อกลุ่ม) (แทค) (คท) (รูป)\nชื่อ = ชื่อคนที่เข้า\nชื่อกลุ่ม = ชื่อกลุ่มที่ออก\nแทค = แทคคนที่ออก\nคท = ส่งคทคนที่ออก\nรูป = ส่งรูปคนออก")
                elif 'กันลิ้ง ' in msg.text:
                      spl = msg.text.replace('กันลิ้ง ','')
                      if spl == 'on':
                          if msg.to in protectqr:
                              msgs = "เปิดระบบกันลิ้ง"
                          else:
                              protectqr.append(msg.to)
                              ginfo = line.getGroup(msg.to)
                              msgs = "เปิดระบบกันลิ้ง\n ประจำกลุ่ม : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「พร้อมใช้งานแล้ว」\n" + msgs)                          
                      elif spl == 'off':
                           if msg.to in protectqr:
                               protectqr.remove(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "ปิดระบบกันลิ้ง\n ประจำกลุ่ม : " +str(ginfo.name)
                           else:
                               msgs = "ปิดระบบกันลิ้ง"
                           line.sendMessage(msg.to, "「ไม่พร้อมใช้งาน」\n" + msgs)
                elif 'กันเชิญ ' in msg.text:
                      spl = msg.text.replace('กันเชิญ ','')
                      if spl == 'on':
                          if msg.to in protectinvite:
                              msgs = "เปิดระบบกันคนเชิญ"
                          else:
                              protectinvite.append(msg.to)
                              ginfo = line.getGroup(msg.to)
                              msgs = "เปิดระบบกันคนเชิญ\n ประจำกลุ่ม : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「พร้อมใช้งานแล้ว」\n" + msgs)                          
                      elif spl == 'off':
                           if msg.to in protectinvite:
                               protectinvite.remove(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "ปิดระบบกันคนเชิญ\n ประจำกลุ่ม : " +str(ginfo.name)
                           else:
                               msgs = "ปิดระบบกันคนเชิญ"
                           line.sendMessage(msg.to, "「ไม่พร้อมใช้งาน」\n" + msgs)
                elif 'กันคนเข้า ' in msg.text:
                      spl = msg.text.replace('กันคนเข้า ','')
                      if spl == 'on':
                          if msg.to in protectjoin:
                              msgs = "เปิดระบบกันคนเข้า"
                          else:
                              protectjoin.append(msg.to)
                              ginfo = line.getGroup(msg.to)
                              msgs = "เปิดระบบกันคนเข้า\n ประจำกลุ่ม : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「พร้อมใช้งานแล้ว」\n" + msgs)                          
                      elif spl == 'off':
                           if msg.to in protectjoin:
                               protectjoin.remove(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "ปิดระบบกันคนเข้า\n ประจำกลุ่ม : " +str(ginfo.name)
                           else:
                               msgs = "ปิดระบบกันคนเข้า"
                           line.sendMessage(msg.to, "「ไม่พร้อมใช้งาน」\n" + msgs)
                elif 'กันเตะ ' in msg.text:
                      spl = msg.text.replace('กันเตะ ','')
                      if spl == 'on':
                          if msg.to in protectkick:
                              msgs = "เปิดระบบกันคนเตะ"
                          else:
                              protectkick.append(msg.to)
                              ginfo = line.getGroup(msg.to)
                              msgs = "เปิดระบบกันคนเตะ\n ประจำกลุ่ม : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「พร้อมใช้งานแล้ว」\n" + msgs)                          
                      elif spl == 'off':
                           if msg.to in protectkick:
                               protectkick.remove(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "ปิดระบบกันคนเตะ\n ประจำกลุ่ม : " +str(ginfo.name)
                           else:
                               msgs = "ปิดระบบกันคนเตะ"
                           line.sendMessage(msg.to, "「ไม่พร้อมใช้งาน」\n" + msgs)
#-------------------------------------------------------------------------------------------------------------
                elif msg.text in ["7g","Hk"]:
                    line.sendMessage(msg.to, "✧•••••••••❂✧✯✧❂••••••••••✧\n     Tëst : Prëmium Spëed™\n✧•••••••••❂✧✯✧❂••••••••••✧")
                    line.sendMessage(msg.to, "❂•➣➣➣ S.p.ë.e.d ➣➣➣➣")
                    start = time.time()
                    time.sleep(0.02)
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "%sseconds" % (elapsed_time))
                elif msg.text == "คนเข้า":
                     ma = ""
                     a = 0
                     for group in welcome:
                       a = a + 1
                       end = '\n'
                       ma += str(a) + ". " +line.getGroup(group).name + "\n"
                     line.sendReplyMessage(msg.id, msg.to,"➢ ต้อนรับแยก\n\n➢ ชื่อกลุ่ม :\n"+ma+"\nจำนวน「%s」กลุ่ม" %(str(len(welcome))))
                elif msg.text == "คนออก":
                     ma = ""
                     a = 0
                     for group in leave:
                       a = a + 1
                       end = '\n'
                       ma += str(a) + ". " +line.getGroup(group).name + "\n"
                     line.sendReplyMessage(msg.id, msg.to,"➢ อำลาแยก\n\n➢ ชื่อกลุ่ม :\n"+ma+"\nจำนวน「%s」กลุ่ม" %(str(len(leave))))    
                elif msg.text.lower().startswith("ตั้งเข้า") and "ตั้งเข้า" in msg.text.lower():
                   if msg._from in admin:
                        try:
                            delcmd = msg.text.split(" ")
                            replacecmd = msg.text.replace(delcmd[0] + " ","")
                            pson["wc"] = replacecmd
                            line.sendReplyMessage(msg.id, to,"สำเร็จแล้ว")
                            f=codecs.open('sb.json','w','utf-8')
                            json.dump(pson, f, sort_keys=True, indent=4, ensure_ascii=False)
                        except Exception as Error:
                            print(Error)    
                elif msg.text.lower().startswith("ตั้งออก") and "ตั้งออก" in msg.text.lower():
                   if msg._from in admin:
                        try:
                            delcmd = msg.text.split(" ")
                            replacecmd = msg.text.replace(delcmd[0] + " ","")
                            pson["lv"] = replacecmd
                            line.sendReplyMessage(msg.id, to,"สำเร็จแล้ว")
                            f=codecs.open('sb.json','w','utf-8')
                            json.dump(pson, f, sort_keys=True, indent=4, ensure_ascii=False)
                        except Exception as Error:
                            print(Error)   
                elif msg.text.startswith("โทร"):
                    dan = text.split(" ")
                    num = int(dan[1])             
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            for var in range(0,num):
                                group = line.getGroup(to)
                                members = [ls]
                                line.acquireGroupCallRoute(to)
                                line.inviteIntoGroupCall(to, contactIds=members)     
                elif msg.text.lower().startswith("คอล "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        members = [mem.mid for mem in group.members]
                        line.acquireGroupCallRoute(to)
                        line.inviteIntoGroupCall(to, contactIds=members)
                    else:
                        line.sendMessage(to, "มาเล่นกันเถอะค่ะ ^_^🍯".format(str(jml)))
                elif text.lower() == 'เทส':
                    line.sendMessage(to, "กำลังโหลด:▒...0%")
                    line.sendMessage(to, "█▒... 10.0%")
                    line.sendMessage(to, "██▒... 20.0%")
                    line.sendMessage(to, "███▒... 30.0%")
                    line.sendMessage(to, "████▒... 40.0%")
                    line.sendMessage(to, "█████▒... 50.0%")
                    line.sendMessage(to, "██████▒... 60.0%")
                    line.sendMessage(to, "███████▒... 70.0%")
                    line.sendMessage(to, "████████▒... 80.0%")
                    line.sendMessage(to, "█████████▒... 90.0%")
                    line.sendMessage(to, "███████████..100.0%")
                    line.sendMessage(to, "🍯〘บอทยังอยู่จะท่านผู้ชม〙🍯")
                elif 'คนเข้า ' in msg.text:
                      spl = msg.text.replace('คนเข้า ','')
                      if spl == 'on':
                          if msg.to in welcome:
                              msgs = "เปิดระบบต้อนรับเฉพาะกลุ่ม"
                          else:
                              welcome.append(msg.to)
                              ginfo = line.getGroup(msg.to)
                              msgs = "เปิดระบบต้อนรับเฉพาะกลุ่ม\n GM ผู้ดูแลประจำกลุ่ม : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「พร้อมต้อนรับเฉพาะกลุ่มนี้ให้แล้ว」\n" + msgs)
                      elif spl == 'off':
                           if msg.to in welcome:
                               welcome.remove(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "ปิดระบบต้อนรับเฉพาะกลุ่ม\n GM ผู้ดูแลประจำกลุ่ม : " +str(ginfo.name)
                           else:
                               msgs = "ปิดระบบต้อนรับเฉพาะกลุ่ม"
                           line.sendMessage(msg.to, "「ไม่พร้อมต้อนรับในกลุ่มนี้」\n" + msgs)
                elif 'คนออก ' in msg.text:
                      spl = msg.text.replace('คนออก ','')
                      if spl == 'on':
                          if msg.to in leave:
                              msgs = "เปิดระบบต้อนรับคนออกเฉพาะกลุ่ม"
                          else:
                              leave.append(msg.to)
                              ginfo = line.getGroup(msg.to)
                              msgs = "เปิดระบบต้อนรับคนออกเฉพาะกลุ่ม\n GM ผู้ดูแลประจำกลุ่ม : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「พร้อมต้อนรับคนออกให้แล้ว」\n" + msgs)
                      elif spl == 'off':
                           if msg.to in leave:
                               leave.remove(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "ปิดระบบต้อนรับคนออกเฉพาะกลุ่ม\n GM ผู้ดูแลประจำกลุ่ม : " +str(ginfo.name)
                           else:
                               msgs = "ปิดระบบต้อนรับคนออกเฉพาะกลุ่ม"
                           line.sendMessage(msg.to, "「ไม่พร้อมต้อนรับคนออกในกลุ่มนี้」\n" + msgs)
                elif text.lower() == 'รีบอท':
                    line.sendMessage(to, "กำลังนับถอยหลัง 3 ถึง 1")
                    time.sleep(1)
                    line.sendMessage(to, "3")
                    time.sleep(1)
                    line.sendMessage(to, "2")
                    time.sleep(1)
                    line.sendMessage(to, "1")
                    line.sendMessage(to, "บอทรีสตาร์ทเรีบร้อยแล้ว^_^ ")
                    restartBot()
                elif text.lower() == 'ข้อมูล':
                    try:
                        arr = []
                        owner = adminMID
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╭━━{ ✯のิՁυิπ⇴ℂℝỦҾⱢ✯ }"
                        ret_ += "\n┣◉➣ ชื่อ ═ {}".format(contact.displayName)
                        ret_ += "\n┣◉➣ กลุ่ม ═ {}".format(str(len(grouplist)))
                        ret_ += "\n┣◉➣ เพื่อน ═ {}".format(str(len(contactlist)))
                        ret_ += "\n┣◉➣ บล็อค ═ {}".format(str(len(blockedlist)))
                        ret_ += "\n┣◉➣ สถานะ ═ {}".format(contact.statusMessage)
                        ret_ += "\n┣◉➣ ผู้สร้าง ═ {}".format(creator.displayName)
                        ret_ += "\n╰━━『✯のิՁυิπ⇴ℂℝỦҾⱢ✯ 』"
                        line.sendMessage(to, str(ret_))
                        line.sendContact(to, lineMID)
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'เชคค่า':
                    try:
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        ret_ = "╭━━{🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯}\n┣━━━━━━━━━━━━━━━━━\n┃       [ ◉STATUS START◉ ]\n┣━━━━━━━━━━━━━━━━━"
                        if settings["autoAdd"] == True: ret_ += "\n┣◉➣🍊✔ ออโต้แอด [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ ออโต้แอด [ off ] "
                        if settings["autoBlock"] == True: ret_ += "\n┣◉➣🍊✔ ออโต้บล็อค [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ ออโต้บล็อค [ off ]"
                        if settings["autoCancel"]["on"] == True:ret_+="\n┣◉➣🍊✔ ยกเชิญที่มีสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"])
                        else: ret_ += "\n┣◉➣🍓✖ ปฏิเสธกลุ่มเชิญ [ off ]"  
                        if settings["autoJoin"] == True: ret_ += "\n┣◉➣🍊✔ เข้าห้องออโต้ [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ เข้าห้องออโต้ [ off ]"       
                        if settings["autoJoinTicket"] == True: ret_ += "\n┣◉➣🍊✔ มุดลิ้งค์เข้าห้อง [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ มุดลิ้งค์เข้าห้อง [ off ]"
                        if settings["autoLeave"] == True: ret_ += "\n┣◉➣🍊✔ ออกแชทรวม [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ ออกแชทรวม [ off ] "
                        if settings["checkSticker"] == True: ret_ += "\n┣◉➣🍊✔ Sticker [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ Sticker [ off ]" 
                        if settings["checkContact"] == True: ret_ += "\n┣◉➣🍊✔ เช็คคอนแท๊ค [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ เช็คคอนแท๊ค [ off ]" 
                        if settings["autoRead"] == True: ret_ += "\n┣◉➣🍊✔ อ่านออโต้ [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ อ่านออโต้ [ off ]"				
                        if settings["checkContact"] == True: ret_ += "\n┣◉➣🍊✔ อ่านคท [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ อ่านคท [ off ]"
                        if settings["Api"] == True: ret_ += "\n┣◉➣🍊✔ อ่านApi [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ อ่านApi [ off ]"
                        if settings["Aip"] == True: ret_ += "\n┣◉➣🍊✔ ตรวจคำหยาบ [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ ตรวจคำหยาบ [ off ]"
                        if settings["Siri"] == True: ret_ += "\n┣◉➣🍊✔ คำสั่งบอทสิริ [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ คำสั่งบอทสิริ [ off ]"
                        if settings["checkPost"] == True: ret_ += "\n┣◉➣🍊✔ เชคโพส [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ เชคโพส [ off ]"                          
                        if settings["kickMention"] == True: ret_ += "\n┣◉➣🍊✔ เตะคนแทค [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ เตะคนแทค [ off ]"                                                
                        if settings["detectMention"] == True: ret_ += "\n┣◉➣🍊✔ ตอบกลับคนแทค [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ ตอบกลับคนแทค [ off ]"
                        if settings["detectMentionPM"] == True: ret_ += "\n┣◉➣🍊✔ ตอบกลับแทคแชท [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ ตอบกลับแทคแชท [ off ]"
                        if settings["potoMention"] == True: ret_ += "\n┣◉➣🍊✔ ส่งคอนแทครูปคนแทค [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ ส่งคอนแทครูปคนแทค [ off ]"   
                        if settings["delayMention"] == True: ret_ += "\n┣◉➣🍊✔ แทคกลับคนแทค [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ แทคกลับคนแทค [ off ]"   
                        if settings["unsend"] == True: ret_ += "\n┣◉➣🍊✔ เชคยกเลิกข้อความ [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ เชคยกเลิกข้อความ [ off ]"
                        if settings["unsend"] == True: ret_ += "\n┣◉➣🍊✔ ตอบแชท [ on ]"
                        else: ret_ += "\n┣◉➣🍓✖ ตอบแชท [ off ]"                          
                        ret_ += "\n┣━━━━━━━━━━━━━━━━━\n"
                        line.sendMessage(to, ret_+"┃   ◐📆วันที่ : "+ datetime.strftime(timeNow,'%d-%m-%Y')+"\n┃   ◐⏰เวลา [ "+ datetime.strftime(timeNow,'%H:%M:%S')+"\n┣━━━━━━━━━━━━━━━━━\n╰━━{🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯}")
                        line.sendContact(to, lineMID)
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                elif text.lower() == 'เปิดแอด':
                    settings["autoAdd"] = True
                    line.sendMessage(to, "ออโต้แอด (เปิด) ใช้งาน🍯")
                elif text.lower() == 'ปิดแอด':
                    settings["autoAdd"] = False
                    line.sendMessage(to, "ออโต้แอด (ปิด) ใช้งาน🍭")
                elif text.lower() == 'เปิดบล็อค':
                    settings["autoBlock"] = True
                    line.sendMessage(to, "ออโต้บล็อค (เปิด) ใช้งาน🍯")
                elif text.lower() == 'ปิดบล็อค':
                    settings["autoBlock"] = False
                    line.sendMessage(to, "ออโต้บล็อค (ปิด) ใช้งาน🍭")
                elif text.lower() == 'เปิดเข้า':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "เข้ากลุ่ม (เปิด) ใช้งาน🍯")
                elif text.lower() == 'ปิดเข้า':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "เข้ากลุ่ม (ปิด) ใช้งาน🍭")
                elif text.lower() == 'เปิดออก':
                    settings["autoLeave"] = True
                    line.sendMessage(to, "ออกแชทรวมอัตโนมัติ (เปิด) ใช้งาน🍯")
                elif text.lower() == 'ปิดออก':
                    settings["autoLeave"] = False
                    line.sendMessage(to, "ออกแชทรวมอัตโนมัติ (ปิด) ใช้งาน🍭")
                elif text.lower() == 'เปิดติ๊ก':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "อ่านโค๊ดติ๊ก (เปิด) ใช้งาน🍯")
                elif text.lower() == 'ปิดติ๊ก':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "อ่านโค๊ดติ๊ก (ปิด) ใช้งาน🍭")    
                elif text.lower() == 'เปิดพูด':
                    settings["Api"] = True
                    line.sendMessage(to, "อ่านโค๊ดApi (เปิด) ใช้งาน🍯")
                elif text.lower() == 'ปิดพูด':
                    settings["Api"] = False
                    line.sendMessage(to, "อ่านโค๊ดApi (ปิด) ใช้งาน🍭")  
                elif text.lower() == 'เปิดตรวจสอบ':
                    settings["Aip"] = True
                    line.sendMessage(to, "ตรวจสอบคำหยาบ (เปิด) ใช้งาน🍯")
                elif text.lower() == 'ปิดตรวจสอบ':
                    settings["Aip"] = False
                    line.sendMessage(to, "ตรวจสอบคำหยาบ (ปิด) ใช้งาน🍭") 
                elif text.lower() == 'เปิดสิริ':
                    settings["Siri"] = True
                    line.sendMessage(to, "คำสั่งบอทสิริ (เปิด) ใช้งาน🍯")
                elif text.lower() == 'ปิดสิริ':
                    settings["Siri"] = False
                    line.sendMessage(to, "คำสั่งบอทสิริ (ปิด) ใช้งาน🍭") 
                elif text.lower() == 'เปิดคท.':
                    settings["checkContact"] = True
                    line.sendMessage(to, "อ่านคท. (เปิด) ใช้งาน🍯")
                elif text.lower() == 'ปิดคท.':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "อ่านคท. (ปิด) ใช้งาน🍭")  
                elif text.lower() == 'เปิดแชท':
                    settings["prankRespon"] = True
                    line.sendMessage(to, "ตอบแชท. (เปิด) ใช้งาน🍯")
                elif text.lower() == 'ปิดแชท':
                    settings["prankRespon"] = False
                    line.sendMessage(to, "ตอบแชท. (ปิด) ใช้งาน🍭")  
                #elif text.lower() == 'เปิดเชคคนเตะ':
                #    settings["kickContact"] = True
                #    line.sendMessage(to, "เปิดเช็คคนลบส่งContact ✔")
                #elif text.lower() == 'ปิดเชคคนเตะ':
                #    settings["kickContact"] = False
                #    line.sendMessage(to, "ปิดเช็คคนลบส่งContact ✘")
                elif text.lower() == 'เปิดอ่าน':
                    settings["autoRead"] = True
                    line.sendMessage(to, "อ่านทุกห้อง (เปิด) ใช้งาน🍯")
                elif text.lower() == 'ปิดอ่าน':
                    settings["autoRead"] = False
                    line.sendMessage(to, "อ่านทุกห้อง (ปิด) ใช้งาน🍭")      
                elif text.lower() == 'เปิดโพส':
                    settings["checkPost"] = True
                    line.sendMessage(to, "เชคโพส (เปิด) ใช้งาน🍯")
                elif text.lower() == 'ปิดโพส':
                    settings["checkPost"] = False
                    line.sendMessage(to, "เชคโพส (ปิด) ใช้งาน🍭")    
                elif text.lower() == 'เปิดร่าน':
                    settings["autoJoinTicket"] = True
                    line.sendMessage(to, "เปิดออโต้เข้าห้องด้วยลิ้งค์เรียบร้อยแล้ว🍯")
                elif text.lower() == 'ปิดร่าน':
                    settings["autoJoinTicket"] = False
                    line.sendMessage(to, "ปิดออโต้เข้าห้องด้วยลิ้งค์เรียบร้อยแล้ว🍭")
                elif text.lower() == 'เปิดยกเลิก':
                    settings["unsend"] = True
                    line.sendMessage(to, "เชคยกเลิกข้อความ (เปิด) ใช้งาน🍯")
                elif text.lower() == 'ปิดยกเลิก':
                    settings["unsend"] = False
                    line.sendMessage(to, "เชคยกเลิกข้อความ (ปิด) ใช้งาน🍭") 
                elif msg.text in ["เปิดเตะแทค"]:
                    settings["kickMention"] = False
                    line.sendMessage(msg.to,"เปิดระบบเตะคนแทค🍯")                    
                elif msg.text in ["ปิดแทคเตะ"]:
                    settings['kickMention'] = True
                    line.sendMessage(msg.to,"ปิดระบบเตะคนแทค🍭")                    
                        #line.sendMessage(msg.to,"Respon enabled.\n\n『✮ ғc.ᴘ'ʟɪкɪнт тᴇѕт ✮』")
                
#==============================================================================#
                elif text.lower() == 'ไอดี':
                    line.sendMessage(msg.to,"[🍯ไอดีมึง🍯]\n" +  lineMID)
                elif text.lower() == 'ชื่อ':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[🍯ชื่อมึง🍯]\n" + me.displayName)
                elif text.lower() == 'ตัส':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[🍯สเตตัสมึง🍯]\n" + me.statusMessage)
                elif text.lower() == 'ดิส':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'วีดีโอ':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'ปก':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                elif text.lower() == 'เชคตั้ง':
                    line.sendMessage(msg.to,str(settings["s"]))
                    #line.sendMessage(msg.to, None, contentMetadata={"STKID":"52114123","STKPKGID":"11539","STKVER":"1"}, contentType=7)
                elif text.lower() == 'เชคทักเข้า':
                    line.sendMessage(msg.to, str(settings["Wc"]))
                elif text.lower() == 'เชคทักออก':
                    line.sendMessage(msg.to, str(settings["bye"]))
                elif text.lower() == 'เชคตั้งผส':
                    line.sendMessage(msg.to, str(settings["c"]))
                elif text.lower() == 'เชคข้อความแอด':
                    line.sendMessage(msg.to, str(settings["add"]))
                elif text.lower() == 'เชคข้อความแทค':
                    line.sendMessage(msg.to, str(settings["Respontag"]))
                elif text.lower() == 'เชคข้อความแทคแชท':
                    line.sendMessage(msg.to, str(settings["ResponPM"]))
                elif text.lower() == 'ดึงหมด':
                    if line != None:
                        me = line.getContact(to)
                        path = line.getProfileCoverURL(to)
                        path = str(path)
                        if settings["server"] == "VPS":
                            line.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                            line.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                            line.sendMessage(msg.to,"「 MID 」\n" +  to)
                            line.sendMessage(to, text=None, contentMetadata={'mid': to}, contentType=13)
                            line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                            line.sendImageWithURL(to, str(path))
                            line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                        else:
                            line.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                            line.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                            line.sendMessage(msg.to,"「 MID 」\n" +  to)
                            line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                            line.sendImageWithURL(to, str(path))
                    else:
                        line.sendMessaged(to, "Talk Exception")
#==============================================================================#
                elif text.lower() == 'แอด':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    line.sendMessage(to, "☝คนนี้แหล่ะคนสร้างกลุ่มนี้🍯")
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ไอดีกลุ่ม \n" + gid.id)
                elif text.lower() == 'รูปกลุ่ม':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ชื่อกลุ่ม -> \n" + gid.name)
                elif text.lower() == 'ลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "ลิ้งของกลุ่ม\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == 'เปิดลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "เปิดลิ้งเรียบร้อย🍯")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "เปิดลิ้งเรียบร้อย🍯")
                elif text.lower() == 'ปิดลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "ปิดลิ้งเรียบร้อย🍭")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "ปิดลิ้งเรียบร้อย🍭")
                elif text.lower() == 'ข้อมูลกลุ่ม':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                        GS = group.creator.mid
                    except:
                        gCreator = "ผู้สร้างลบชี"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ไม่สมารถแสดงลิ้งได้"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ 🍉 ข้อมูลของกลุ่มนี้🍉 ]"
                    ret_ += "\n╠🍯 ชื่อของกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠🍯 ไอดีของกลุ่ม : {}".format(group.id)
                    ret_ += "\n╠🍯 ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠🍯 จำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠🍯 จำนวนค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠🍯 ลิ้งของกลุ่ม : {}".format(gQr)
                    ret_ += "\n╠🍯 ลิ้งกลุ่ม : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
                    line.sendContact(to, GS)
                elif text.lower() == 'สมาชิกกลุ่ม':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ สมาชิกในกลุ่ม ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} คน ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == 'เชคกลุ่ม':
                        groups = line.groups
                        ret_ = "╔══[ กลุ่ม ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} กลุ่ม ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))
                        
                elif "โคลนนิ่ง " in msg.text:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = line.getContact(target)
                            X = contact.displayName
                            profile = line.getProfile()
                            profile.displayName = X
                            line.updateProfile(profile)
                            line.sendMessage(msg.to, "✯เริ่มทำการโคลนนิ่ง®🍰")
                        #---------------------------------------
                            Y = contact.statusMessage
                            lol = line.getProfile()
                            lol.statusMessage = Y
                            line.updateProfile(lol)
                        #---------------------------------------
                            settings["changePictureProfile"] = True
                            me = line.getContact(target)     
                            line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                        except Exception as e:
                            line.sendMessage(msg.to, "Failed!")
                            print (e)
                            print (e)
                            

#==============================================================================#
                elif text.lower() == 'แจ๊ะ':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//1
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*1 : (a+1)*1]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        line.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
              #          line.sendMessage(to, "จำนวน {} คน".format(str(len(nama))))
                elif text.lower() == 'แทค2':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        line.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)                       
#===========BOT UPDATE BY NOXTIAN============#
                elif msg.text.lower().startswith("แทค"):
                  if msg._from in admin:						
                    data = msg.text[len("แทค"):].strip()
                    if data == "":
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                        cb = ""
                        cb2 = ""
                        count = 1
                        strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 20:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == "<":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                        cb = ""
                        cb2 = ""
                        count = 1
                        strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count > mentargs:
                                break
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 20:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == ">":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                        cb = ""
                        cb2 = ""
                        count = 1
                        if mentargs >= 0:
                            strt = len(str(mentargs)) + 2
                        else:
                            strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count < mentargs:
                                count += 1
                                continue
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 20:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == "=":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                        cb = ""
                        cb2 = ""
                        count = 1
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count != mentargs:
                                count += 1
                                continue
                            akh = akh + len(str(count)) + 2 + 5
                            strt = len(str(count)) + 2
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 20:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
#=====================================================================================#                        
                elif text.lower() == 'ปฏิทิน':
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
                    readTime = "📆ปฏิทิน📆\n\n📅" + "\n🍓" + hasil + "\n🍓 ที่ " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y')  + "\n⏰ เวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]" + "📆⏰📆⏰" + "\n\n🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯 }"
                    line.sendMessage(msg.to, readTime)                    
                elif "sh " in msg.text.lower():
                    spl = re.split("sh ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,subprocess.getoutput(spl[1]))
                        except:
                            pass 
                elif "โทเค่น" in msg.text.lower():
                  #if wait["selfbot"] == True:
                   if msg._from in admin:
                       line.sendMessage(msg.to,"[ LINE ]\n"+line.authToken)
                elif text.lower() == 'แทคล่อง':
                    gs = line.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        line.sendMessage(to, "ไม่มีคนใส่ร่องหนในกลุ่มนี้😂")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        line.sendMessage(to, mc)
                elif text.lower() == 'ไอดีล่อง':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีmidคนใส่ร่องหน🤗")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        line.sendMessage(to,mc)
                elif text.lower() == 'คทล่อง':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีคนใส่ร่องหนในกลุ่มนี้😂")
                    else:
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(to, mi_d)
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
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
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
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("ชื่อ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("ตัส "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
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
                             line.deleteContact(ls)
                         line.sendMessage(to, "ลบออกจากการเป็นเพื่อนแล้ว")
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
                            contact = line.getContact(ls)
                            line.findAndAddContactsByMid(ls)
                        line.sendMessage(to, "เพิ่ม " + str(contact.displayName) + " เป็นเพื่อนสำเร็จแล้ว")
                elif msg.text.lower().startswith("รูป "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("วีดีโอ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("ปก "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                elif msg.text.startswith("ดึงหมด "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                                for ls in lists:
                                    me = line.getContact(ls)
                                    path = line.getProfileCoverURL(ls)
                                    path = str(path)
                                    if settings["server"] == "VPS":
                                        line.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                                        line.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                                        line.sendMessage(msg.to,"「 MID 」\n" +  to)
                                        line.sendMessage(to, text=None, contentMetadata={'mid': ls}, contentType=13)
                                        line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                                        line.sendImageWithURL(to, str(path))
                                        line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                    else:
                                        line.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                                        line.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                                        line.sendMessage(msg.to,"「 MID 」\n" + ls)
                                        line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                        line.sendImageWithURL(to, str(path))
                                else:
                                    line.sendMessage(to, "Talk Exception You are not Related to LineChannel")
                        else:
                            line.sendMessage(to, "Talk Exception You are not Related to LineChannel")  
                elif "แปลงคท: " in msg.text:
                    mmid = msg.text.replace("แปลงคท: ","")
                    line.sendMessage(to, text=None, contentMetadata={'mid': mmid}, contentType=13)
                elif "สแปม " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("สแปม "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               line.sendMessage(msg.to, teks)
                        else:
                           line.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "Out Of Range!")
                elif msg.text.lower().startswith("อัพชื่อ "):
                    string = msg.text.lower().replace("อัพชื่อ", "")
                    if len(string) <= 10000000000:
                        pname =  line.getContact(sender).displayName
                        profile = line.getProfile()
                        profile.displayName = string
                        line.updateProfile(profile)
                        userid = "https://line.me/ti/p/~" + line.profile.userid
                        line.sendFooter(to, "Update Name\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                elif msg.text.lower().startswith("อัพตัส "):
                    string = msg.text.lower().replace("อัพตัส", "")
                    if len(string) <= 10000000000:
                        pname = line.getContact(sender).statusMessage
                        profile = line.getProfile()
                        profile.statusMessage = string
                        line.updateProfile(profile)
                        userid = "https://line.me/ti/p/~" + line.profile.userid
                        line.sendFooter(to, "Update Status\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)        
                elif msg.text.lower().startswith("เห่ย "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
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
                                contact = line.getContact(receiver)
                                RhyN_(to, contact.mid)
               
                elif msg.text.lower().startswith("ไอดีไลน์"):
                    line.reissueUserTicket()
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendFooter(to, "「🍯ไอดีไลน์ของเรา🍯」\n"+str(userid), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
 
                elif msg.text.lower().startswith("แจก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
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
                                line.sendMessage(receiver, text=None, contentMetadata=None, contentType=9)
                                line.sendMessage(to, "ส่งของขวัญใน ส.ต แล้ว".format(str(jml)))
                elif msg.text in ["สีชมพู"]:
                    line.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                    line.sendContact(to, "u1f41296217e740650e0448b96851a3e2',") 
                    line.sendMessage(msg.to, "💗•💗•💗•Virus Pink•💗•💗•💗")       

                #----------------------------------------------------------------------------------------------------------------------------------------
#                elif msg.text in ["ปีโป้อร่อยจัง"]:
#                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.ด.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
#                    line.sendMessage(msg.to, "ไ.ว.รั.ส.ด.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังค่ะ")
#                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.ด.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
#                    line.sendMessage(msg.to, "ไวรัสเอจังฟรุ้งฟรุ้งมุ้งมิ้ง~☆😍💜💛💚💙💗💖.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.ฟรุ้งฟริ้ง by.เอจัง~☆🤗")
#                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.ด.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
#                    line.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
#                    line.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
#                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.ด.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
#                    line.sendMessage(msg.to, "💔.ไ.ว.รั.ส.ด.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.ค่.ะ.💚.💟.💛1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.ฟ.รุ้.ง.ฟ.ริ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.💓.💗.💖.")
#                    line.sendMessage(msg.to, "ไ.ว.รั.ส.ด.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังค่ะ")
#                    line.sendMessage(msg.to, "💛💜??ีี💜💛💜💛💜💛💜💛\n  ❂••• ปีโป้อร่อยที่สุดเลย •••❂\n💛💜💛💜💛💜💛💜💛💜💛")
#--------------------------------------------------------------------------------------------------------------
                elif msg.text in ["Kitty"]:
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.ด.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.ด.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังค่ะ")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.ด.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.ด.อ.จั.ง.น่.า.รั๊.ก.ไ.ล.น์.เ.ขี.ย.ว.~.☆. 🤗.🕸.💙.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.")
                    line.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.ด.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังค่ะ")
                    line.sendMessage(msg.to, "ไวรัสเอจังฟรุ้งฟรุ้งมุ้งมิ้ง~☆😍💜💛💚💙💗💖.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.ฟรุ้งฟริ้ง by.เอจัง~☆🤗")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.ด.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.ด.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "💗.ไ.ว.รั.ส.ด.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    line.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.ด.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    line.sendMessage(msg.to, "✧•••••••••❂✧✯✧❂••••••••••✧\n   💖💖 HELLO KITTY 💖💖\n✧•••••••••❂✧✯✧❂••••••••••✧")
#-------------------------------------------------------------------------------------------------------------
                   
                elif msg.text.lower().startswith("ส่งความรัก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
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
                                line.sendMessage(to, "🎁•รับทางแชทสต.นะ•🎁".format(str(jml)))
                               # line.sendMessage(receiver, ".God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                line.sendMessage(to, "ไปดู ส.ต ด้วย".format(str(jml)))
                            else:
                                pass                                
                elif text.lower() == "/me":
                	_session = requests.session()
                	contact = line.getContact(lineMID)
                	url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                	headers = {
                		"Host": "game.linefriends.com",
                		"Content-Type": "application/json",
                		"User-Agent": "Mozilla/5.0",
                		"Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                	}
                	data = {
                		"cc": channelToken.token,
                		"to": to,
                		"messages": [
                	        {
                	            "type": "template",
                	            "altText": "Check Bot",
                	            "template": {
                	                "type": "buttons",
                	                "thumbnailImageUrl": "https://obs.line-scdn.net/{}".format(contact.picturePath),
                	                "title": "-** MAX TEST BOT **-",
                	                "text": "MaxGie",
                	                "actions": [
                	                    {
                	                "type": "uri",
                	                "label": "Add",
                	                "uri": "line://ti/p/~gu.11"
                	                    },
                	                    {
                	                "type": "uri",
                	                "label": "Anime",
                	                "uri": "https://i.pinimg.com/originals/13/05/a7/1305a7f3726f49515f914ce7caede5c7.gif"               	                													
                	                    }
                	                ],
                	                "imageAspectRatio": "square",
                	                "imageSize": "cover"
                	            }
                	        }
                	    ]
                	}
                	data = json.dumps(data)
                	sendPost = _session.post(url, data=data, headers=headers)

                elif text.lower() == "text":
                	_session = requests.session()
                	url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                	headers = {
                		"Host": "game.linefriends.com",
                		"Content-Type": "application/json",
                		"User-Agent": "Mozilla/5.0",
                		"Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                	}
                	data = {
                		"cc": channelToken.token,
                		"to": to,
                		"messages": [
	                    {
	                      "type": "template",
	                      "altText": "this is a buttons template",
	                      "template": {
	                          "type": "buttons",
	                          "actions": [
	                            {
	                              "type": "uri",
	                              "label": "Add",
	                              "uri": "line://ti/p/~gu.11",
	                            }
	                          ],
                            "thumbnailImageUrl": "https://i.pinimg.com/originals/13/05/a7/1305a7f3726f49515f914ce7caede5c7.gif",
                    	      "title": "MAX TEST BOT",
	                          "text": "@MAXGIE"
                        }
                      }
                    ]
	                }
                	data = json.dumps(data)
                	sendPost = _session.post(url, data=data, headers=headers)

                elif text.lower() == "test":
                	_session = requests.session()
                	contact = line.getContact(lineMID)
                	url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                	headers = {
                		"Host": "game.linefriends.com",
                		"Content-Type": "application/json",
                		"User-Agent": "Mozilla/5.0",
                		"Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                	}
                	data = {
                		"cc": channelToken.token,
                		"to": to,
                		"messages": [
	                    {
										    "type": "template",
										    "altText": "this is a carousel template",
										    "template": {
											    "type": "carousel",
											    "actions": [],
											    "columns": [
												    {
													    "thumbnailImageUrl": "https://steamusercontent-a.akamaihd.net/ugc/97230215087482034/3694E72D5E5CA1EAB5F4E2746A1C264FED589FCE/",
													    "title": "Title",
													    "text": "Text",
													    "actions": [
														    {
															    "type": "uri",
															    "label": "Action 1",
															    "uri": "https://steamusercontent-a.akamaihd.net/ugc/97230215087482034/3694E72D5E5CA1EAB5F4E2746A1C264FED589FCE/"
														    }
													    ]
												    },
												    {
													    "thumbnailImageUrl": "https://steamusercontent-a.akamaihd.net/ugc/97230215087482034/3694E72D5E5CA1EAB5F4E2746A1C264FED589FCE/",
													    "title": "Title",
													    "text": "Text",
													    "actions": [
														    {
															    "type": "uri",
															    "label": "Action 1",
															    "uri": "https://steamusercontent-a.akamaihd.net/ugc/97230215087482034/3694E72D5E5CA1EAB5F4E2746A1C264FED589FCE/"
														    }
													    ]
												    }
											    ]
										    }
									    }
								    ]
							    }
                	data = json.dumps(data)
                	sendPost = _session.post(url, data=data, headers=headers)
                  
                elif text.lower() == "555":
                	_session = requests.session()
                	contact = line.getContact(lineMID)
                	url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                	headers = {
                		"Host": "game.linefriends.com",
                		"Content-Type": "application/json",
                		"User-Agent": "Mozilla/5.0",
                		"Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                	}
                	data = {
                		"cc": channelToken.token,
                		"to": to,
                		"messages": [
									      {
											    "type": "template",
											    "altText": "",
											    "template": {
												      "type": "image_carousel",
												      "columns": [
													      {
														      "imageUrl": "https://i.pinimg.com/originals/00/73/06/007306aeb5a6283f11956ffe4397ff57.gif",
														      "action": {
															      "type": "uri",
															      "uri": "line://ti/p/~gu.11"
														      }
													      }
												      ]
											    }
										    }
								    ]
							    }
                	data = json.dumps(data)
                	sendPost = _session.post(url, data=data, headers=headers)
                  
                elif text.lower() == "เขิล":
                	_session = requests.session()
                	contact = line.getContact(lineMID)
                	url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                	headers = {
                		"Host": "game.linefriends.com",
                		"Content-Type": "application/json",
                		"User-Agent": "Mozilla/5.0",
                		"Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                	}
                	data = {
                		"cc": channelToken.token,
                		"to": to,
                		"messages": [
									      {
											    "type": "template",
											    "altText": "",
											    "template": {
												      "type": "image_carousel",
												      "columns": [
													      {
														      "imageUrl": "https://i.pinimg.com/originals/d5/fb/83/d5fb83e26bfd4ec440abaec15bdc0f21.gif",
														      "action": {
															      "type": "uri",
															      "uri": "line://ti/p/~gu.11"
														      }
													      }
												      ]
											    }
										    }
								    ]
							    }
                	data = json.dumps(data)
                	sendPost = _session.post(url, data=data, headers=headers)
                  
                elif text.lower() == "ขำ":
                	_session = requests.session()
                	contact = line.getContact(lineMID)
                	url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                	headers = {
                		"Host": "game.linefriends.com",
                		"Content-Type": "application/json",
                		"User-Agent": "Mozilla/5.0",
                		"Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                	}
                	data = {
                		"cc": channelToken.token,
                		"to": to,
                		"messages": [
									      {
											    "type": "template",
											    "altText": "",
											    "template": {
												      "type": "image_carousel",
												      "columns": [
													      {
														      "imageUrl": "https://i.pinimg.com/originals/95/5d/e1/955de1d227f25654b3df115be5f08b18.gif",
														      "action": {
															      "type": "uri",
															      "uri": "line://ti/p/~gu.11"
														      }
													      }
												      ]
											    }
										    }
								    ]
							    }
                	data = json.dumps(data)
                	sendPost = _session.post(url, data=data, headers=headers)
                elif msg.text.lower().startswith("รักนะ "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
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
                                line.sendContact(receiver, 'u1f41296217e740650e0448b96851a3e2')
                                line.sendMessage(to, "ไปดู ส.ต ด้วย".format(str(jml)))
                            else:
                                pass
                elif msg.text.lower().startswith("ทัก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    for x in range(jml):
                        name = line.getContact(to)
                        RhyN_(to, name.mid)                    
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif text.lower().startswith("ขอเพลง "):
                    if msg._from in admin:
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["items"] != []:
                                ret_ = []
                                yt = []
                                for music in a["items"]:
                                    ret_.append({"thumbnailImageUrl": 'https://i.ytimg.com/vi/{}/maxresdefault.jpg'.format(music['id']['videoId']),"imageSize": "contain","imageAspectRatio": "square","title": '{}'.format(str(music['snippet']['title'][:40])),"text": '{}'.format(str(music['snippet']['channelTitle'][:15])),"actions": [{"type": "uri","label": "Go Page","uri": 'https://www.youtube.com/watch?v=' +music['id']['videoId']}]})
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {"cc":carousel,"to": to,"messages": [{"type": "template","altText": "Youtube","template": {"type": "carousel","columns": ret_[aa*10 : (aa+1)*10]}}]}
                                    sendCarousel(data)
                               
                elif msg.text in ["นับไทย"]:
                    line.sendMessage(msg.to,"✍✯のิՁυิπ⇴ℂℝỦҾⱢ✯ ")
                    line.sendMessage(msg.to,"❂➣-รอสักครู่...........")
                    line.sendMessage(msg.to,"💖:::⭐ ๑ ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ ๒ ⭐:::💚")
                    line.sendMessage(msg.to,"💙:::⭐ ๓ ⭐:::💙")
                    line.sendMessage(msg.to,"💔:::⭐ ๔ ⭐:::💔")                     
                    line.sendMessage(msg.to,"💖:::⭐ ๕ ⭐:::💖")       
                    line.sendMessage(msg.to,"💚:::⭐ ๖ ⭐:::💚")
                    line.sendMessage(msg.to,"💙:::⭐ ๗ ⭐:::💙")     
                    line.sendMessage(msg.to,"💔:::⭐ ๘ ⭐:::💔")
                    line.sendMessage(msg.to,"💖:::⭐ ๙ ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 0 ⭐:::💚")
                    line.sendMessage(msg.to,"「✯のิՁυิπ⇴ℂℝỦҾⱢ✯ 」")                    
                                    
                elif msg.text in ["นับสเปน"]:
                    line.sendMessage(msg.to,"✍「✯のิՁυิπ⇴ℂℝỦҾⱢ✯ 」")
                    line.sendMessage(msg.to,"❂➣-รอสักครู่...........")
                    line.sendMessage(msg.to,"1.❂•••  รีลมาดริด")
                    line.sendMessage(msg.to,"2.❂••• บาเซโลน่า")
                    line.sendMessage(msg.to,"3.❂••• บาเลนเซีย")
                    line.sendMessage(msg.to,"4.❂•• แอตมาดริด")
                    line.sendMessage(msg.to,"5.❂•• ลาคอรุนญ่า")
                    line.sendMessage(msg.to,"6.❂••เอสปันญ่อล")
                    line.sendMessage(msg.to,"7.❂•••  โอซาซูน่า")
                    line.sendMessage(msg.to,"8.❂••• ซาราโกซ่า")
                    line.sendMessage(msg.to,"9.❂•••• บียาร์รีลล์")
                    line.sendMessage(msg.to,"0.❂••• เรอัลเบติส")
                    line.sendMessage(msg.to,"⚽ •🏆🏆🏆🏆• ⚽")                    
                                    
                elif msg.text in ["ด่า"]:
                    line.sendMessage(msg.to,"🍍•สักครู่ระบบกำลังประมวลผล•🍍\n 「」™")
                    line.sendMessage(msg.to,"Now Loding...........................")
                    line.sendMessage(msg.to,"ไอ้ผีฉีกเรียน")
                    line.sendMessage(msg.to,"อีคางคกเห็นผี")
                    line.sendMessage(msg.to,"อีจระเข้เดินห้าง")
                    line.sendMessage(msg.to,"ไอ้แกงบูด")
                    line.sendMessage(msg.to,"อีสุวรรณมาลี")
                    line.sendMessage(msg.to,"ไอ้ไก่ดุดพรก")
                    line.sendMessage(msg.to,"ไอ้แตดสีรุ้ง")
                    line.sendMessage(msg.to,"ไอ้ขี้มูกเขียว")
                    line.sendMessage(msg.to,"ไอ้ผีขบส้ม")
                    line.sendMessage(msg.to,"ไอ้หัวล้านใส่เยล")
                    line.sendMessage(msg.to,"อีหนังหน้าปลาจวด")
                    line.sendMessage(msg.to,"อีโกดังเก็บศพ")
                    line.sendMessage(msg.to,"อีแย้แดกแห้ว")
                    line.sendMessage(msg.to,"อีหลุมดำจักรวาล")
                    line.sendMessage(msg.to,"ไอ้สะตอโปรตุเกส")
                    line.sendMessage(msg.to,"อีดาวเทียมไทคม\nแม่งเสือกทุกสถานี🍰\nจบข่าว สนับสนุนการด่าโดย\n\n✯のิՁυิπ⇴ℂℝỦҾⱢ✯ ")                    
                                    
                elif msg.text in ["นับอังกฤษ"]:
                    line.sendMessage(msg.to,"✯のิՁυิπ⇴ℂℝỦҾⱢ✯ ")
                    line.sendMessage(msg.to,"❂➣-รอสักครู่...........")
                    line.sendMessage(msg.to,"💖⭐ ••One•• ⭐💖")
                    line.sendMessage(msg.to,"💚⭐ ••Two•• ⭐💚")
                    line.sendMessage(msg.to,"💙⭐ •Three• ⭐💙")
                    line.sendMessage(msg.to,"💔⭐  •Four•  ⭐💔")
                    line.sendMessage(msg.to,"💖⭐ ••Five•• ⭐💖")
                    line.sendMessage(msg.to,"💚⭐ •••Six••• ⭐💚")
                    line.sendMessage(msg.to,"💙⭐ •Seven• ⭐💙")
                    line.sendMessage(msg.to,"💔⭐  •Eight•  ⭐💔")
                    line.sendMessage(msg.to,"💖⭐ ••Nine•• ⭐💖")
                    line.sendMessage(msg.to,"💚⭐ ••Zero•• ⭐💚")
                    line.sendMessage(msg.to,"✯のิՁυิπ⇴ℂℝỦҾⱢ✯ ")
#-----------------------------------------------------------------------------------------------------------
                elif msg.text in ["นับ"]:
                    line.sendMessage(msg.to,"✯のิՁυิπ⇴ℂℝỦҾⱢ✯ ")
                    line.sendMessage(msg.to,"❂➣-รอสักครู่...........")
                    line.sendMessage(msg.to,"💖:::⭐ 1 ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 2 ⭐:::💚")
                    line.sendMessage(msg.to,"💙:::⭐ 3 ⭐:::💙")
                    line.sendMessage(msg.to,"💔:::⭐ 4 ⭐:::💔")
                    line.sendMessage(msg.to,"💖:::⭐ 5 ⭐:::💖")
                    line.sendMessage(msg.to,"💚:::⭐ 6 ⭐:::💚")
                    line.sendMessage(msg.to,"💙:::⭐ 7 ⭐:::💙")
                    line.sendMessage(msg.to,"💔:::⭐ 8 ⭐:::💔")
                    line.sendMessage(msg.to,"💖:::⭐ 9 ⭐:::💖")                                   

                elif msg.text in ["เอจังนับอินโด","นับอินโด"]:
                    line.sendMessage(msg.to,"✯のิՁυิπ⇴ℂℝỦҾⱢ✯ ")
                    line.sendMessage(msg.to,"❂➣-รอสักครู่..................")
                    line.sendMessage(msg.to,"💖⭐1 •••Satu••• 1⭐💖")
                    line.sendMessage(msg.to,"💚⭐2••••Dua••••2⭐💚")
                    line.sendMessage(msg.to,"💙⭐3 •••Tiga••• 3⭐💙")
                    line.sendMessage(msg.to,"💔⭐4 ••Empat••4⭐💔")
                    line.sendMessage(msg.to,"💖⭐5  ••Lima••  5⭐💖")
                    line.sendMessage(msg.to,"💚⭐6•••Enam•••6⭐💚")
                    line.sendMessage(msg.to,"💙⭐7  ••Tujuh•• 7⭐💙")
                    line.sendMessage(msg.to,"💔⭐8 •Delapan•8⭐💔")
                    line.sendMessage(msg.to,"💖⭐9 Sembilan 9⭐💖")
                    line.sendMessage(msg.to,"💚⭐0 ••••Nol•••• 0⭐💚")
                    line.sendMessage(msg.to,"✯のิՁυิπ⇴ℂℝỦҾⱢ✯ " +datetime.today().strftime('%H:%M:%S')+ "™") 
                    
                elif msg.text in ["เอจังนับไฮโซ","นับไฮโซ"]:
                    line.sendMessage(msg.to,"✯のิՁυิπ⇴ℂℝỦҾⱢ✯ \n     ♡♡ HELLO KITTY ♡♡\n✧•••••••••❂✧✯✧❂••••••••••✧")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💖💖[[[[[ 1 ]]]]]💖💖\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💚💚[[[[[ 2 ]]]]]💚💚\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💙💙[[[[[ 3 ]]]]]💙💙\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💔💔[[[[[ 4 ]]]]]💔💔\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💖💖[[[[[ 5 ]]]]]💖💖\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💚💚[[[[[ 6 ]]]]]💚💚\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💙💙[[[[[ 7 ]]]]]💙💙\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💔💔[[[[[ 8 ]]]]]💔์💔\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💖ั💖[[[[[ 9 ]]]]]💖💖\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    line.sendMessage(msg.to,"✧••••••❂✯❂••••••✧\n💚💚[[[[[ 0 ]]]]]💚💚\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")   
#--------------------------------------------------------------------------------------------------------------------------    
                elif msg.text in ["คำสั่ง"]:
                    line.sendMessage(msg.to, " 🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯 \n🍭 กรุณาพิมคิมมี่ 🍭")                   
#==============================================================================#
                elif text.lower() == 'เปิดแอบอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                line.sendMessage(msg.to,"Lurking enabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            line.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'ปิดแอบอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        line.sendMessage(msg.to,"Lurking disabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        line.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'แอบอ่านใหม่':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        line.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        line.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'อ่านคนแอบ':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if list(read["ROM"][receiver].items()) == []:
                            line.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in list(read["ROM"][receiver].items()):
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ *** LurkDetector *** ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        line.sendMessage(receiver,"Lurking has not been set.")
#==============================================================================#
                elif msg.text.lower().startswith("ประกาศ "):  
                    bc = msg.text.replace("ประกาศ ","")
                    gid = line.getGroupIdsJoined()
                    for i in gid:
                        line.sendMessage(i,"[ 🍰ประกาศกลุ่ม🍰 ]\n\n"+bc+"")
                                         
                elif msg.text.lower().startswith("ประกาศ: "):
                    sep = text.split(" ")
                    txt = text.replace(sep[0] + " ","")
                    groups = line.groups
                    for group in groups:
                        line.sendMessage(group, "「 ประกาศ 🍰」\n{}".format(str(txt)))
                    line.sendMessage(to, "ส่งข้อความ ปะกาศ ทั้งหมด {} กลุ่ม".format(str(len(groups))))
                    
                elif msg.text.lower().startswith("ประกาศแชท: "):
                    sep = text.split(" ")
                    txt = text.replace(sep[0] + " ","")
                    friends = line.friends
                    for friend in friends:
                        line.sendMessage(friend, "「ข้อความอัตโนมัติ ประกาศแชท」\n{}".format(str(txt)))
                    line.sendMessage(to, "ส่งข้อความถึงเพื่อน {} คน".format(str(len(friends))))
#=============================================================================
                elif msg.text in ["เหี้ย"]:
                  if msg._from in admin: 
                    settings["wblacklist"] = True
                    line.sendMessage(msg.to,"กรุณาส่งคอทแทค")
                elif msg.text in ["ไม่เหี้ย"]:
                  if msg._from in admin: 
                    settings["dblacklist"] = True
                    line.sendMessage(msg.to,"กรุณาส่งคอทแทค")
                elif msg.text in ["ล้างเหี้ย"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"ทำการลบบัญชีเหี้ยทั้งหมดเรียร้อย")
                    print ("Clear Ban")
                    
               
              
                elif msg.text.lower() == "คทเหี้ย":
                    if msg._from in lineMID:
                        if settings["blacklist"] == []:
                            line.sendMessage(to, "Nothing boss")
                        else:
                            for bl in settings["blacklist"]:
                                line.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                elif msg.text in ["เตะเหี้ย"]:
                	if msg.toType == 2:
                         group = line.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             line.sendMessage(receiver,"ไม่มีตัวเหี้ยในห้องนี้")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[line]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     line.sendMessage(receiver,"sorry bl ke cyduk")
                                     print ("Blacklist di Kick")
                elif msg.text in ["เชคเหี้ย"]:
                  if msg._from in Family:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"ไม่พบ") 
                    else:
                        line.sendMessage(msg.to,"รายชื่อผู้เหี้ย")
                        mc = "Blacklist User\n"
                        for mi_d in settings["blacklist"]:
                            mc += "[√] " + line.getContact(mi_d).displayName + " \n"
                        line.sendMessage(msg.to, mc + "")
                elif 'ไปเส้' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])      
                               print ("Rfu kick User")
                           except:
                               line.sendMessage(msg.to,"555555555555")
                              
                
                elif "Kick " in msg.text:
                    Ri0 = text.replace("kick ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = line.getGroup(msg.to)
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
                                    line.kickoutFromGroup(to,[target])
                                except:
                                    pass                              
                              
                elif "ล้อเล่น " in msg.text:
                    Ri0 = text.replace("ล้อเล่น ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = line.getGroup(msg.to)
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
                                    line.kickoutFromGroup(to,[target])
                                    line.findAndAddContactsByMid(target)
                                    line.inviteIntoGroup(to,[target])
                                except:
                                    pass
                
                elif "เตะ " in msg.text:
                        vkick0 = msg.text.replace("เตะ ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = line.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    line.kickoutFromGroup(msg.to,[target])
                                    line.findAndAddContactsByMid(target)
                                    line.inviteIntoGroup(msg.to,[target])
                                    line.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass
                                  
                elif "ยกรัน" in msg.text.lower():
                    spl = re.split("ยกรัน",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = line.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        line.sendText(msg.to,txt)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                line.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    line.sendText(gr,spl[1])
                                line.leaveGroup(gr)
                            except:
                                pass
                        line.sendText(msg.to,"สำเร็จแล้ว(⊙_⊙)")
#==============================================================================#
#==============================================================================#
                elif msg.text.lower().startswith("เขียน "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    line.sendImageWithURL(msg.to, urlnya)
                elif msg.text.lower().startswith("ดึงวีดีโอ "):
                  #if wait["selfbot"] == True:
                    if msg._from in admin:
                    #try:
                        sep = msg.text.split(" ")
                        textToSearch = msg.text.replace(sep[0] + " ","")
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
                            hasil = "「 Youtube - Video 」"
                            hasil += "\nTitle : {}".format(str(vid.title))
                            hasil += "\nSubscriber From : {}".format(str(vid.author))
                            hasil += "\nPlease wait for the videos"
                            hasil += "\n"
                        line.sendMessage(msg.to,hasil)
                        line.sendVideoWithURL(msg.to,vin)
                        print("[YOUTUBE]MP4 Succes")
            
                elif msg.text.lower().startswith("ไอดีไลน์ "):
                    id = msg.text.lower().replace("ไอดีไลน์ ","")
                    conn = line.findContactsByUserid(id)
                    if True:                                      
                        line.sendMessage(to,"http://line.me/ti/p/~" + id)
                        line.sendContact(to,conn.mid)
                elif msg.text.lower().startswith("ยกเลิก "):
                    args = msg.text.lower().replace("ยกเลิก ","")
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
                elif msg.text in ["ดึง"]:
                        settings["winvite"] = True
                        line.sendMessage(msg.to,"send a contact to invite user")                           
                #if text.lower() == 'ยกเชิญ':
                #elif msg.text.lower() == "ยกเชิญ":
                elif msg.text.lower().startswith(".ยกเชิญ"):
                                if msg._from in bot1:                                
                                    if msg.toType == 2:
                                        group = line.getGroup(receiver)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        k = len(gMembMids)//15
                                        line.sendMessage(msg.to,"[ ยกค้างเชิญ จำนวน {} คน]".format(str(len(gMembMids))))
                                        num=1
                                        for i in range(k+1):
                                            for j in gMembMids[i*15 : (i+1)*15]:
                                                time.sleep(random.uniform(0.5,0.4))
                                                line.cancelGroupInvitation(msg.to,[j])
                                                print ("[Command] "+str(num)+" => "+str(len(gMembMids))+" cancel members")
                                                num = num+1
                                            #line.sendMessage(receiver,"รอสักครู่🕛เดียวยกต่อ 30 คน\n🇹🇭🄵🄰🅁🄸🅂🄱🄾🅃🄻🄸🄽🄴🇹🇭 ")
                                            time.sleep(random.uniform(15,10))
                                        line.sendMessage(receiver,"[ ยกค้างเชิญ จำนวน {} คน เรียบร้อยแล้ว👏]".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        #line.sendMessage(receiver, None, contentMetadata={"STKID": "52002735","STKPKGID": "11537","STKVER": "1" }, contentType=7)
                                        gname = line.getGroup(receiver).name
                                        line.sendMessage(Notify,"[ ยกค้างเชิญ >> "+gname+"  <<] \n จำนวน {} คน เรียบร้อยแล้ว👏\n🇹🇭🄵🄰🅁🄸🅂🄱🄾🅃🄻🄸🄽🄴🇹🇭 ".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        line.leaveGroup(receiver)
                                								
                                    line.sendMessage(receiver,"[ไม่มีค้างเชิญ แล้วนะ😁]")
                                    line.sendMessage(receiver, None, contentMetadata={"STKID": "52114123","STKPKGID": "11539","STKVER": "1" }, contentType=7)
                                    line.leaveGroup(receiver)
                                    
                elif msg.text.lower() == ".":
                    if msg.toType == 0:
                        sendMention(to, to, "", "")
                    elif msg.toType == 2:
                        group = line.getGroup(to)
                        contact = [mem.mid for mem in group.members]
                        mentionMembers(to, contact)
                                    
                elif msg.text.lower().startswith("คำห้ามพิม "):
                    wban = msg.text.lower().split()[1:]
                    wban = " ".join(wban)
                    wbanlist.append(wban)
                    line.sendMessage(to,"%s พิมคำนี้อาจมีปลิวนะ."%wban)
                elif msg.text.lower().startswith("ล้างคำห้ามพิม "):
                    wunban = msg.text.lower().split()[1:]
                    wunban = " ".join(wunban)
                    if wunban in wbanlist:
                        wbanlist.remove(wunban)
                        line.sendMessage(to,"%s ล้างออกจากคำสั่งห้ามพิมแล้ว."%wunban)
                    else:
                        line.sendMessage(to,"%s is not blacklisted."%wunban)
                elif msg.text.lower() == 'เชคคำห้ามพิม':
                    tst = "คำห้ามพิม:\n"
                    if len(wbanlist) > 0:
                        for word in wbanlist:
                            tst += "- %s \n"%word
                        line.sendMessage(msg.to,tst)
                    else:
                        line.sendMessage(msg.to,"คำที่ห้ามพิมทั้งหมด")                   

                elif msg.text.lower().startswith("เพลสโต "):  
                        tob = msg.text.lower().replace('เพลสโต ',"")
                        line.sendMessage(msg.to,"กรุณารอสักครู่...")
                        line.sendMessage(msg.to,"ผลจากการค้นหา : "+tob+"\nจาก : Google Play\nลิ้งโหลด : https://play.google.com/store/search?q=" + tob)
                        line.sendMessage(msg.to,"👆กรุณากดลิ้งเพื่อทำการโหลดแอพ👆")
            
                elif msg.text.lower().startswith("รูป "):  
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("การ์ตูน "):  
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(msg.to, str(path))
                            
                elif text.lower() == "อัพดิส":
                    settings["changePictureProfile"] = True
                    line.sendMessage(to, "ส่งรูปภาพลงมาได้เลยครับผม(○ﾟεﾟ○)")
                elif text.lower() == "อัพดิสกลุ่ม":
                    if msg.toType == 2:
                        if to not in settings["changeGroupPicture"]:
                            settings["changeGroupPicture"].append(to)
                        line.sendMessage(to, "ส่งรูปภาพลงมาไดเเลยครับผม(○ﾟεﾟ○)")
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Mimic has been added as")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Mimic deleting succes...")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Mimic enabled.")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Mimic disabled.")
#=================================================================================#                    
                elif msg.text.lower().startswith("ยูทูป "):  
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif "ค้นหา " in msg.text.lower():
                    spl = re.split("ค้นหา ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        if spl[1] != "":
                                try:
                                    if msg.toType != 0:
                                        line.sendMessage(msg.to,"กำลังรับข้อมูล กรุณารอสักครู่..")                                  
                                    else:
                                        line.sendMessage(msg.from_,"กำลังรับข้อมูล กรุณารอสักครู่..")
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
                                        line.sendMessage(msg.to,str(text))
                                    else:
                                        line.sendMessage(msg.from_,str(text))
                                except Exception as e:
                                    print(e)
#==============================================================================#
                elif msg.text in ["เปิดแสกน"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"เปิดระบบแสกนคนอ่านอัตโนมัติ ")
                elif msg.text in ["ปิดแสกน"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        line.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    else:
                        line.sendMessage(msg.to, "ปิดระบบแสกนคนอ่านแล้ว")
                        
                elif text.lower() == "ผู้ดูแล":
                        line.sendContact(to,"ua77ed9dfe7882bfa33f8cea4df61667f") 
                    
                elif text.lower() == 'ของขวัญ':
                        line.sendGift(msg.to,'2','sticker')
                        line.sendGift(msg.to,'11537','sticker')
                        line.sendGift(msg.to,'11539','sticker')
                        line.sendGift(msg.to,'1','sticker')
                        line.sendGift(msg.to,'3','sticker')
                        line.sendGift(msg.to,'4','sticker')
                        
                if "gift " in msg.text.lower():
                    red = re.compile(re.escape('gift '),re.IGNORECASE)
                    themeid = red.sub('',msg.text)
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': themeid,
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    line.sendMessage(msg)                        
                elif msg.text.lower() == "เชคติ๊กแทค":
                        msgSticker = settings["messageSticker"]["listSticker"]["คนแทค"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "ตั้งติ๊กแทค":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "คนแทค"
                    line.sendMessage(to, "ส่งสติ๊กเกอร์มา🍯")
                elif msg.text.lower() == "ลบติ๊กแทค":
                    settings["messageSticker"]["listSticker"]["คนแทค"] = None
                    line.sendMessage(to, "ลบสติ๊กเกอร์คนแทคแล้ว🍭")                    
                elif msg.text.lower() == "รีเช็ต":
                    settings["s"] = ""
                    settings["c"] = "🍯のิՁυิπ⇴ℂℝỦҾⱢ🍯 "
                    line.sendMessage(to, "[ Done ]")                       
#==============================================================================#                    
                elif msg.text.startswith("ตั้งแอด "):
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งแอด ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["add"] = spl
                         line.sendMessage(msg.to, "🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯\nตั้งข้อความตอบโต้เมื่อมีคนแอดแล้ว\n\n[ {} ]".format(str(spl)))
                elif msg.text.startswith("ตั้งแชท "):
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งแชท ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["pro"] = spl
                         line.sendMessage(msg.to, "🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯\nตั้งข้อความตอบแชทแล้ว\n\n[ {} ]".format(str(spl)))
                elif msg.text.startswith("ตั้งคนเข้า "):
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งคนเข้า ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["Wc"] = spl
                         line.sendMessage(msg.to, "🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯\nตั้งข้อความตอบโต้เมื่อมีคนเข้ากลุ่ม\n\n[ {} ]".format(str(spl)))  
                elif msg.text.startswith("ตั้งคนออก "):
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งคนออก ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["bye"] = spl
                         line.sendMessage(msg.to, "🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯\nตั้งข้อความตอบโต้เมื่อมีคนเข้ากลุ่ม\n\n[ {} ]".format(str(spl)))  
                elif msg.text.startswith("ตั้งคนแทค "):
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งคนแทค ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["Respontag"] = spl
                         line.sendMessage(msg.to, "🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯\nตั้งข้อความตอบโต้เมื่อมีคนแทคคุณในกลุ่ม\n\n[ {} ]".format(str(spl)))
                elif msg.text.startswith("ตั้งแทคแชท "):
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งแทคแชท ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["ResponPM"] = spl
                         line.sendMessage(msg.to, "🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯\nตั้งข้อความตอบโต้แทคแชทแล้ว\n\n[ {} ]".format(str(spl)))
                elif msg.text.startswith("ตั้ง "):
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้ง ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["s"] = spl
                         line.sendMessage(msg.to, "🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯\n[ {} ]".format(str(spl)))       
                elif msg.text.startswith("ตั้งผส "):
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งผส ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["c"] = spl
                         line.sendMessage(msg.to, "🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯\n[ {} ]".format(str(spl)))                       
                          
                elif "บอกหมุด: " in msg.text.lower():
                    bctxt = msg.text.replace("บอกหมุด: ", "")
                    a = line.getGroupIdsJoined()
                    for manusia in settings["bc"]:
                        if manusia in a:
                            line.sendText(manusia,(bctxt))
                            time.sleep(0.1)
                    line.sendText(receiver,"「 ส่งกลุ่มที่ปักหมุดแล้ว 」")
								
#==============FINNISHING PROTECT========================#
								
                elif msg.text in ["ลิสหมุด"]:
                    a = line.getGroupIdsJoined()
                    ret_ = " ══[รายชื่อกลุ่ม]══"
                    num = 1
                    for manusia in settings["bc"]:
                        if manusia in a:
                            group = line.getGroup(manusia)
                            ret_ += "\n {}. {} | {}".format(str(num), str(group.name), str(len(group.members)))
                            num=(num+1)					
                    line.sendMessage(to, str(ret_))

                elif msg.text in ["ปักหมุด"]:
                    settings["bc"][receiver] = True
                    line.sendText(receiver,"「 ปักหมุดกลุ่มนี้เรียบร้อย 」")
								
                elif msg.text in ["ลบหมุด"]:
                    try:
                        del settings["bc"][receiver]
                        line.sendText(receiver,"「 ลบหมุดออกเรียบร้อย 」")
                    except:
                        line.sendText(receiver,"「 ลบหมุดออกเรียบร้อย 」")

#=====================================================================================#                
                elif msg.text.lower() == 'เปิดแทค':
                        if settings["detectMention"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความคนแทคเมื่อมีคนแทคคุณ🍯")
                        else:
                            settings["detectMention"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความคนแทคเมื่อมีคนแทคคุณ🍯")
                elif msg.text.lower() == 'ปิดแทค':
                        if settings["detectMention"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความคนแทคเมื่อมีคนแทคคุณ🍭")
                        else:
                            settings["detectMention"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความคนแทคเมื่อมีคนแทคคุณ🍭") 
                elif msg.text.lower() == 'เปิดแทคแชท':
                        if settings["detectMentionPM"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความคนแทคแชทอยู่แล้ว🍯")
                        else:
                            settings["detectMentionPM"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความคนแทคแชทแล้ว🍯")
                elif msg.text.lower() == 'ปิดแทคแชท':
                        if settings["detectMentionPM"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความคนแทคแชทอยู่แล้ว🍭")
                        else:
                            settings["detectMentionPM"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความคนแทคแชทแล้ว🍭")
                elif msg.text.lower() == 'เปิดแทค2':
                        if settings["potoMention"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดส่งคทและรูปคนแทคเมื่อมีคนแทคคุณ🍯")
                        else:
                            settings["potoMention"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดส่งคทและรูปคนแทคเมื่อมีคนแทคคุณ🍯")
                elif msg.text.lower() == 'ปิดแทค2':
                        if settings["potoMention"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดส่งคทและรูปคนแทคเมื่อมีคนแทคคุณ🍭")
                        else:
                            settings["potoMention"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดส่งคทและรูปคนแทคเมื่อมีคนแทคคุณ🍭") 
                elif msg.text.lower() == 'เปิดทักเตะ':
                        if settings["Nk"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่ม...\n\n🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯")
                        else:
                            settings["Nk"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่ม...\n\n🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯")
                                
                elif msg.text.lower() == 'ปิดทักเตะ':
                        if settings["Nk"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่มแล้ว..\n\n🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯")
                        else:
                            settings["Nk"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่มแล้ว...\n\n🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯")

                elif msg.text.lower() == 'เปิดอ่านคท':
                        if settings["checkContact"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดอ่านข้อความคอนแทคภายในห้อง...\n\n🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            settings["checkContact"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดอ่านข้อความคอนแทคภายในห้อง....\n\n🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                                
                elif msg.text.lower() == 'ปิดอ่านคท':
                        if settings["checkContact"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดอ่านข้อความคอนแทคภายในห้อง...\n\n🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            settings["checkContact"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดอ่านข้อความคอนแทคภายในห้อง....\n\n🍯 のิՁυิπ⇴ℂℝỦҾⱢ 🍯", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text.lower() == 'เปิดแทค3':
                        if settings["delayMention"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดแทคกลับไปแล้ว🍯")
                        else:
                            settings["delayMention"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดแทคกลับแล้ว🍯")
                elif msg.text.lower() == 'ปิดแทค3':
                        if settings["delayMention"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดแทคกลับไปแล้ว🍭")
                        else:
                            settings["delayMention"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดแทคกลับแล้ว🍭") 

#========================================================================
                elif text.lower() == "ล้างแชท":
                        if msg._from in Family:
                            try:
                                line.removeAllMessages(op.param2)
                                kk.removeAllMessages(op.param2)
                                kc.removeAllMessages(op.param2)
                                ke.removeAllMessages(op.param2)                                
                                line.sendMessage(msg.to,"ลบทุกการแชทเรียบร้อย")
                            except:
                                pass
                                print ("ลบแชท")
#========================================================================                            
            elif msg.contentType == 13:
                if settings["checkContact"] == True:
                    try:
                        contact = line.getContact(msg.contentMetadata["mid"])
                        if line != None:
                            cover = line.getProfileCoverURL(msg.contentMetadata["mid"])
                        else:
                            cover = "Tidak dapat masuk di line channel"
                        path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        try:
                            line.sendImageWithURL(to, str(path))
                        except:
                            pass
                        ret_ = "[ รายการทั้งหมดจากการสำรวจด้วย คท ]"
                        ret_ += "\n ชื่อ : {}".format(str(contact.displayName))
                        ret_ += "\n ไอดี : {}".format(str(msg.contentMetadata["mid"]))
                        ret_ += "\n ตัส : {}".format(str(contact.statusMessage))
                        ret_ += "\n รูปโปรไฟล : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        ret_ += "\n  รูปปก : {}".format(str(cover))
                        ret_ += "\n[ สิ้นสุดการสำรวจ ]"
                        line.sendMessage(to, str(ret_))
                    except:
                        line.sendMessage(to, "เกิดข้อผิดพลาดในการสำรวจ")
            elif msg.contentType == 1:
                if settings["changePictureProfile"] == True:
                    path = line.downloadObjectMsg(msg_id)
                    settings["changePictureProfile"] = False
                    line.updateProfilePicture(path)
                    line.sendMessage(to, "ทำการแปลงโฉมเสร็จเรียบร้อย")
                if msg.toType == 2:
                    if to in settings["changeGroupPicture"]:
                        path = line.downloadObjectMsg(msg_id)
                        settings["changeGroupPicture"].remove(to)
                        line.updateGroupPicture(to, path)
                        line.sendMessage(to, "เปลี่ยนรูปภาพกลุ่มเรียบร้อยแล้ว")
                if msg.contentType == 7:
                    if settings["messageSticker"]["addStatus"] == True:
                        name = settings["messageSticker"]["addName"]
                        if name != None and name in settings["messageSticker"]["listSticker"]:
                            settings["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            line.sendMessage(to, "ได้ทำการตั้งสติ๊กเกอร์ " + name)
                        settings["messageSticker"]["addStatus"] = False
                        settings["messageSticker"]["addName"] = None
                    if settings["addSticker"]["status"] == True:
                        stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "Success Added sticker {}".format(str(settings["addSticker"]["name"])))
                        settings["addSticker"]["status"] = False
                        settings["addSticker"]["name"] = ""
                   
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
              
#==============================================================================#
        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)              
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)             
#==============================================================================#
#==============================================================================#
        if op.type == 17:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
            if RfuProtect["protect"] == True:
                if settings["blacklist"][op.param2] == True:
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            G = line.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["protect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Rfu).inviteIntoGroup(op.param1,[op.param2])
        
        if op.type == 13:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["inviteprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Family:
                        if op.param2 in Family:
                            pass
                        elif RfuProtect["inviteprotect"] == True:
                            settings ["blacklist"][op.param2] = True
                            random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 not in Family:
                                if op.param2 in Family:
                                    pass
                                elif RfuProtect["cancelprotect"] == True:
                                    settings ["blacklist"][op.param2] = True
                                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 11:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 11:
            if RfuProtect["linkprotect"] == True:
                if op.param2 not in Family:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param3])

        if op.type == 5:
            if RfuProtect["autoBlock"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))
        if op.type == 5:
            if RfuProtect["autoAdd"] == True:
                if (settings["comment"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["comment"]))
        if op.type == 13:
           if RfuProtect["Protectguest"] == True:
               if op.param2 not in Family:
                  random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 17:
            if op.param2 in settings["blacklist"] == {}:
                line.kickoutFromGroup(op.param1,[op.param2])
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                line.sendText(op.param1,"สมาชิกที่ถูกแบนไม่ได้รับอนุญาตให้เข้าร่วมกลุ่ม （´・ω・｀）"+tm)
        if op.type == 17:
           if RfuProtect["Protectjoin"] == True:
               if op.param2 not in Family:
                   random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    
        if op.type == 1:
            if sender in Setmain["foto"]:
                path = line.downloadObjectMsg(msg_id)
                del Setmain["foto"][sender]
                line.updateProfilePicture(path)
                line.sendMessage(to,"Foto berhasil dirubah")
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#========================================================================
                if msg.contentType == 7:
                    if settings["messageSticker"]["addStatus"] == True:
                        name = settings["messageSticker"]["addName"]
                        if name != None and name in settings["messageSticker"]["listSticker"]:
                            settings["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            line.sendMessage(to, "ได้ทำการตั้งสติ๊กเกอร์ " + name)
                        settings["messageSticker"]["addStatus"] = False
                        settings["messageSticker"]["addName"] = None
                    if settings["addSticker"]["status"] == True:
                        stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "Success Added sticker {}".format(str(settings["addSticker"]["name"])))
                        settings["addSticker"]["status"] = False
                        settings["addSticker"]["name"] = ""
                        
        if op.type in [25,26]:
            msg = op.message
            if msg.contentType == 16:
                if settings["checkPost"] == True:
                        try:
                            ret_ = "[ ข้อมูลของโพสนี้ ]"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = line.getContact(msg._from)
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
                            ret_ += "\n✯のิՁυิπ⇴ℂℝỦҾⱢ✯ "
                            line.sendMessage(msg.to, (str(ret_)))
                        except:
                            line.sendMessage(msg.to, "เกิดข้อผิดะลาดในการเช็คโพสนี้")  
        if op.type == 26 or op.type == 25:
            msg = op.message
            sender = msg._from
            try:
              
               if pson["kw"][str(msg.text)]:
             #      user = line.Contact(msg._from)
                   line.sendMessage(msg.to,pson["kw"][str(msg.text)])
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
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.text is None:
                    return
                if msg.text.lower() == "เชคapi":
                    lisk = "[ 🐯คำตอบโต้ทั้งหมด🐯 ]\n"
                    for i in pson["kw"]:
                        lisk+="\nคีย์เวิร์ด: "+str(i)+"\nตอบโต้: "+str(pson["kw"][i])+"\n"
                    line.sendMessage(msg.to,lisk)
                if msg.text.startswith("ล้างapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        getx = msg.text.replace(delcmd[0] + " ","")
                        del pson["kw"][getx]
                        line.sendMessage(msg.to, "คำตอบโต้ " + str(getx) + " ล้างแล้ว")
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(pson, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
                if msg.text.startswith("ตั้งapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(";;")
                        kw = get[0]
                        ans = get[1]
                        pson["kw"][kw] = ans
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(pson, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(msg.to,"คีย์เวิร์ด: " + str(kw) + "\nตอบกลับ: " +str(ans))
                    except Exception as Error:
                        print(Error)
                if msg.text.lower() == "/wc":
                    try:
                        welcomemessage = pson["wc"]
                        user = line.getContact(msg._from)
                        group = line.getGroup(msg.to)
                        get = welcomemessage.replace("{NAME}",user.displayName)
                        get = get.replace("{GNAME}",group.name)
                        get = get.replace("{GID}",group.id)
                        if "{MEN}" in welcomemessage:
                            sendMessageWithMention(msg.to, user.mid)
                        get = get.replace("{MEN}","")
                        if "{CONTACT}" in get:
                            line.sendContact(msg.to,msg._from)
                        get = get.replace("{CONTACT}","")
                        line.sendMessage(msg.to,get)
                        line.sendImageWithURL(msg.to, "http://dl.profile.line.naver.jp/" + user.pictureStatus)
                        
                    except Exception as Error:
                        print(Error)
                elif "/wc" in msg.text.lower():
                    try:
                        delcmd = msg.text.split(" ")
                        replacecmd = msg.text.replace(delcmd[0] + " ","")
                        pson["wc"] = replacecmd
                        line.sendMessage(msg.to,"/wc")
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(pson, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
                if msg.text.lower() == "/lv":
                    try:
                        lvmessage = pson["lv"]
                        user = line.getContact(msg._from)
                        group = line.getGroup(msg.to)
                        get = lvmessage.replace("{NAME}",user.displayName)
                        get = get.replace("{GNAME}",group.name)
                        get = get.replace("{GID}",group.id)
                        if "{MEN}" in lvmessage:
                            sendMessageWithMention(msg.to, user.mid)
                        get = get.replace("{MEN}","")
                        if "{CONTACT}" in get:
                            line.sendContact(msg.to,msg._from)
                        get = get.replace("{CONTACT}","")
                        line.sendMessage(msg.to,get)
                        line.sendImageWithURL(msg.to, "http://dl.profile.line.naver.jp/" + user.pictureStatus)
                    except Exception as Error:
                        print(Error)
                elif "/lv" in msg.text.lower():
                    try:
                        delcmd = msg.text.split(" ")
                        replacecmd = msg.text.replace(delcmd[0] + " ","")
                        pson["lv"] = replacecmd
                        line.sendMessage(msg.to,"/lv")
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(pson, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
#==============================================================================#
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                elif text.lower() in "รีส":
                    if msg.toType == 2: 
                        phusui.sendMessage(msg.to,"ครับผม")
                    else: 
                        phusui.sendMessage(msg._from,"ครับผม")
#==============================================================================#
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.text in ["ฟารีส"]:
                    user = line.getContact(msg._from)
                    sendMessageWithMention(msg.to, user.mid)
                    line.sendMessage(msg.to, None, contentMetadata={"STKID":"36441425","STKPKGID":"11100","STKVER":"1"}, contentType=7)
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)
                if settings["unsendMessage"] == True:
                    try:
                        msg = op.message
                        if msg.toType == 0:
                            line.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                        else:
                            line.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                            msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    except Exception as error:
                        logError(error)
                if msg.contentType == 0:
                    if text is None:
                        return
                if settings["autoRead"] == True:
                        line.sendChatChecked(to, msg_id)				
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    if msg.contentType == 7:
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        ret_ = "Sticker Info"
                        ret_ += "\nSTICKER ID : {}".format(stk_id)
                        ret_ += "\nSTICKER PACKAGES ID : {}".format(pkg_id)
                        ret_ += "\nSTICKER VERSION : {}".format(stk_ver)
                        line.sendMessage(to, text=None, contentMetadata={'STKID':'107', 'STKVER':'100', 'STKPKGID':'1'}, contentType=7)
                    elif msg.contentType == 1:
                        line.sendMessage(to, text=None, contentMetadata={"STKID": "190", "STKVER": "100", "STKPKGID": "3"}, contentType=7)
                    else:
                        if text is not None:
                            txt = text
                            line.sendMessage(msg.to,txt)
                elif msg.contentType == 7:
                    if settings["checkSticker"] == True:
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
                            line.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            line.sendMessage(to, str(ret_))                            
                        except Exception as error:
                            line.sendMessage(to, str(error))
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in lineMID:
                            try:
                                line.kickoutFromGroup(msg.to,[sender])
                                line.sendMessage("คุณพูดคำต้องห้าม จำเป็นต้องนำออก sorry(╯°□°）╯︵ ┻━┻")
                            except Exception as e:
                                print(e)
                    if "/ti/g/" in msg.text.lower():
                        if settings["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = line.findGroupByTicket(ticket_id)
                                line.acceptGroupInvitationByTicket(group.id,ticket_id)
                                line.sendMessage(to, "🍯เข้าร่วมกลุ่ม %s \n🍯ผ่านการแชร์ด้วยลิ้งค์🍯" % str(group.name))                                  
                if msg.toType == 0 and settings["autoReply"] and sender != lineMID:
                    contact = line.getContact(sender)
                    rjct = ["auto", "ngetag"]
                    validating = [a for a in rjct if a.lower() in text.lower()]
                    if validating != []: return
                    if contact.attributes != 32:
                        msgSticker = settings["messageSticker"]["listSticker"]["sleepSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                        if "@!" in settings["replyPesan"]:
                            msg_ = settings["replyPesan"].split("@!")
                            sendMention(to, sender, "Sleep Mode :\n" + msg_[0], msg_[1])
                        sendMention(to, sender, "Sleep Mode :\nว่าไงคับ", settings["replyPesan"])
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    if settings["detectMentionPM"] == True:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                sendMention(sender, sender, "「ตอบแทคอัตโนมัติ」\n", "\n" + str(settings["ResponPM"]))
                                break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in msg.contentMetadata.keys() != None:
        	             if settings['kickMention'] == True:
        		             contact = line.getContact(msg._from)
        		             cName = contact.displayName
        		             balas = ["เนื่องจากตอนนี้ผมเปิดระบบเตะคนแทคไว้ " + "\n👉" + cName + "\n🔴ต้องขออภัยด้วยจริงๆ🔴Bye!!!"]
        		             ret_ = "" + random.choice(balas)                     
        		             name = re.findall(r'@(\w+)', msg.text)
        		             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
        		             mentionees = mention["MENTIONEES"]
        		             for mention in mentionees:
        			               if mention['M'] in admin:
        				                  line.sendText(msg.to,ret_)
        				                  line.kickoutFromGroup(msg.to,[msg._from])
        				                  break                                  
        			               if mention['M'] in lineMID:
        				                  line.sendText(msg.to,ret_)
        				                  line.kickoutFromGroup(msg.to,[msg._from])
        				                  break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                         if settings['potoMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.pictureStatus
                             mi_d = contact.mid
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in lineMID:
                                          line.sendImageWithURL(to,ret_)
                                          line.sendContact(msg.to, mi_d)
                                          break  
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             balas = [ cName ]
                             ret_ = "" + random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          #line.sendMessage(to,ret_)
                                          line.sendMessage(to, "[ " + ret_ + " ]\n" + str(settings["Respontag"]))
                                          msgSticker = settings["messageSticker"]["listSticker"]["คนแทค"]
                                          if msgSticker != None:
                                              sid = msgSticker["STKID"]
                                              spkg = msgSticker["STKPKGID"]
                                              sver = msgSticker["STKVER"]
                                              sendSticker(to, sver, spkg, sid)
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['delayMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          sendMessageWithMention(to, contact.mid)
                                          break
#===========ชุด API คำสั่งใช้งานบอทสิริเชนวี10 ========================== 
        if op.type == 26:
            msg = op.message
          #  if settings ["Aip"] == True:
           # 	if msg.text in ["leanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","Kick","Kick","กระเด็น","หวด"]:
            #        line.kickoutFromGroup(receiver,[sender])
             #       line.sendText(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม จำเป็นต้องนำออกเพื่อความปลอดภัยของสมาชิก (｀・ω・´)")
           # if settings ["Aip"] == True:
            #    if msg.text in ["ควย","หี","แตด","เย็ดแม่","เย็ดเข้","ค.วย","สัส","เหี้ย","ไอ้เหี้ย","พ่อมึงตาย","ไอ้เลว","ระยำ","ชาติหมา","หน้าหี","เซลกาก","ไอ้เรส","ไอ้เหี้ยเรส","ไอ่เรส","พ่องตาย","ส้นตีน","แม่มึงอ่ะ","แม่มึงดิ","พ่อมึงดิ"]:
              #      line.kickoutFromGroup(receiver,[sender])
               #     line.sendText(msg.to,"ตรวจพบคำพูดหยาบคายไม่สุภาพ จำเป็นต้องนำออกเพื่อความสงบสุขของสมาชิก (｀・ω・´)")
#            if settings ["Api"] == True:
#                if msg.text in ["ป๊า","ป๊าเรส","ลุง","เรส","นาย","เพื่อน","จาร์ย","อาจาร์ย","เฮีย"]:
#                    line.sendMessage(msg.to, str(settings["comment1"]))
#            if settings ["Api"] == True:
#                if msg.text in ["เซล","เซลบอท","selfbot","ขายบอท"]:
#                    line.sendMessage(msg.to, str(settings["comment"]))
#                    line.sendMessage(msg.to, None, contentMetadata={"STKID":"52114123","STKPKGID":"11539","STKVER":"1"}, contentType=7)
#            if settings ["Api"] == True:
#                if msg.text in ["55","555","5555","55555","55+","555+","5555+","ขำ",".ขำ"]:
#                    line.sendText(msg.to,"ฮ่าๆๆๆ..ขำไรจ๊ะ..\n😆มึงไปโดนตัวใหนมาเนี่ย😆")
#                    line.sendMessage(msg.to, None, contentMetadata={"STKID":"51626504","STKPKGID":"11538","STKVER":"1"}, contentType=7)
#            if settings["Api"] == True:
#                if msg.text in ["กำ","กำหำ","กำหอย"]:
#                    line.sendText(msg.to,"กำเบาๆนะเค้าเจ็บ😁😁")
#                    line.sendMessage(msg.to, None, contentMetadata={"STKID":"51626498","STKPKGID":"11538","STKVER":"1"}, contentType=7)
#            if settings["Api"] == True:
#                if msg.text in ["งง","งงง",]:
#                    line.sendText(msg.to,"ไม่ต้องงงคับ ผมหล่อแบบนี้มาตั้งนานแล้ว😂😂")
#                    line.sendMessage(msg.to, None, contentMetadata={"STKID":"51626512","STKPKGID":"11538","STKVER":"1"}, contentType=7)
#            if settings["Api"] == True:
#                if msg.text in ["หรา","หราา",]:
#                    line.sendMessage(msg.to, None, contentMetadata={"STKID":"51626516","STKPKGID":"11538","STKVER":"1"}, contentType=7)
            if settings ["Api"] == True:
                if msg.text in ["ออน"]:
                    line.sendText(msg.to,"🍭✯のิՁυิπ⇴ℂℝỦҾⱢ✯🍭")
#            if settings ["Api"] == True:
#                if msg.text in ["หลุดไหม"]:
#                    line.sendText(msg.to,"ไม่หลุดนะค่ะ🍯")

        if op.type ==25:
            msg = op.message
            if settings ["Siri"] == True:
                if msg.text in ["/รองแอด","/รอง","/แอดรอง","/แอดสำรอง","/@2"]:
                    line.sendText(msg.to,"Siriv10:extracreator")
                    line.sendText(msg.to,"👇คนนี้คือแอดสำรองห้องนี้")#, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})            
            if settings ["Siri"] == True:
                if msg.text in ["/เช็ค","/เช็คตั้งค่า","/ตั้งค่า"]:
                    line.sendText(msg.to,"Set:status")
                    line.sendText(msg.to,"เช็คการตั้งค่าบอทสิริ")                     
            if settings ["Siri"] == True:
                if msg.text in ["/ตั้งแอดรอง","/ตั้งรอง","/ตั้งแอดรอง"]:
                    line.sendText(msg.to,"設定:予備作者変更")
                    line.sendText(msg.to,"ลงคำสั่งแล้ว ส่ง คท. แอดรองลงครับ") 
            if settings ["Siri"] == True:
                if msg.text in ["/แอด","/@","/@1"]:
                    line.sendText(msg.to,"Siri:groupcreator")
                    line.sendText(msg.to,"👇คนนี้คือแอดมินกลุ่มนี้ ")
            if settings ["Siri"] == True:
                if msg.text in ["/สลับ","/สลับแอด"]:
                    line.sendText(msg.to,"設定:作者交換")
                    line.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะแอดมินหลักกับรอง\nลงคำสั่ง 1 ครับพอนะครับ")     
            if settings ["Siri"] == True:
                if msg.text in ["/ปลดแอด","/ปลดแอดมิน","/ล้างแอด"]:
                    line.sendText(msg.to,"siri:forcerelease")
                    line.sendText(msg.to,"คำสั่งนี้ใช้ในกรณีที่แอดห้องลบบัญชี\nให้ลงคำสั่ง 1 ครั้ง\nแล้วรอ5นาทีแล้วเช็คแอดดูครับ ")       
            if settings ["Siri"] == True:
                if msg.text in ["/ทวิทเต้อ","/ทวิท","/ผูกทวิทเต้อ"]:
                    line.sendText(msg.to,"Siri:Twitter紐付け")
                    line.sendText(msg.to,"คำสั่งเฉพาะคนขายตั๋ว \nใช้ผูททวิทเต้อเพื่อซื้อตั๋ว")    
            if settings ["Siri"] == True:
                if msg.text in ["/ย้ายตั๋ว","/ส่งตั๋ว","/ขายตั๋ว"]:
                    line.sendText(msg.to,"Siri:招待券移行:1")
                    line.sendText(msg.to,"ใช้สำหรับส่งตั๋วเชิญบอทให้คนที่ซื้อ\nลงคำสั่ง1ครั้ง แล้วลง คท. ลูกค้าที่ซื้อตั๋ว 2 ครั้งครับ\n(สั่งในบอทสิริเซ็นเตอร์)")      
            if settings ["Siri"] == True:
                if msg.text in ["/กลับ","/บอทกลับ","/มา"]:
                    line.sendText(msg.to,"Siriv10:reinvite")
                    line.sendText(msg.to,"คำสั่งเรียกบอทกลับห้อง") 
            if settings ["Siri"] == True:
                if msg.text in ["/ชุดล็อค","/ชุดล็อคen","/ชุดล๊อคen"]:
                    line.sendText(msg.to,"Set:iconlock:on")
                    line.sendText(msg.to,"Set:blockinvite:on")
                    line.sendText(msg.to,"Set:ownerlock:on")
                    line.sendText(msg.to,"Set:changenamelock:on")
                    line.sendText(msg.to,"Siriv10:DenyURLInvite")
                    line.sendText(msg.to,"Set:StampLimitation:On")
                    line.sendText(msg.to,"ชุดล๊อคห้องสิริวี10 ให้คัดลอกคำสั่ง\nแล้วางลงห้องทีละคำครับ")            
            if settings ["Siri"] == True:
                if msg.text in ["/ดำ","/สั่งดำ","/เพิ่มดำ"]:
                    line.sendText(msg.to,"Set:addblacklist")
                    line.sendText(msg.to,"เพิ่มบัญชีดำ(วิธีสั่ง>ลงคำสั่ง+ส่งข้อมูล)")    
            if settings ["Siri"] == True:
                if msg.text in ["/ขาว","/แก้ดำ","/เพิ่มขาว"]:
                    line.sendText(msg.to,"Set:addwhitelist")
                    line.sendText(msg.to,"เพิ่มบัญชีขาว(วิธีสั่ง>ลงคำสั่ง+ส่งข้อมูล)")          
            if settings ["Siri"] == True:
                if msg.text in ["/ลบค้างเขิญ","/ลบเชิญ","/ยกเชิญ"]:
                    line.sendText(msg.to,"Siriv10:cancelinvite")
                    line.sendText(msg.to,"ลบค้างเชิญ (สั่ง2ครั้ง)")    
            if settings ["Siri"] == True:
                if msg.text in ["/เปลี่ยนแอด","/เปลี่ยนหัว","/ตั้งแอด"]:
                    line.sendText(msg.to,"Set:changeowner")
                    line.sendText(msg.to,"เปลี่ยนหัวห้อง(วิธีสั่ง>ลงคำสั่ง+ส่งข้อมูล)")   
            if settings ["Siri"] == True:
                if msg.text in ["/ปิดลิ้ง","/ปิดลิ้งค์"]:
                    line.sendText(msg.to,"Siriv10:DenyURLInvite")
                    line.sendText(msg.to,"คำสั่งปิดลิ้งห้อง")          
            if settings ["Siri"] == True:
                if msg.text in ["/ตั้งเวลา","/ตั้งอ่าน","/รีเซ็ท"]:
                    line.sendText(msg.to,"SetLastPoint")
                    line.sendText(msg.to,"กำลังตั่งค่าการอ่าน บอทสิริ.")   
            if settings ["Siri"] == True:
                if msg.text in ["/ใครอ่าน","/อ่าน","/คนแอบ"]:
                    line.sendText(msg.to,"Viewlastseen")
                    line.sendText(msg.to,"ดูคนที่กำลังอ่านตอนนี้")
            if settings ["Siri"] == True:
                if msg.text in ["/ล็อคแอด","/ล๊อคแอด","/ล๊อคแอดมิน"]:
                    line.sendText(msg.to,"設定:作成者ロック:オン")
                    line.sendText(msg.to,"คำสั่งใช้ล๊อคแอดมิน\nกันโดนเตะออกจากห้อง")
            if settings ["Siri"] == True:
                if msg.text in ["/ปิดการเชิญ","/ปิดเชิญ"]:
                    line.sendText(msg.to,"設定:招待拒否:オン")
                    line.sendText(msg.to,"คำสั่งปฏิเสธการเชิญสมาชิกคนนอก")
            if settings ["Siri"] == True:
                if msg.text in ["/รันติก","/ล๊อคติก","/ล็อคติก"]:
                    line.sendText(msg.to,"Set:StampLimitation:On")
                    line.sendText(msg.to,"คำสั่งห้ามคนรันติกเก้อร์เกิน15ตัว")
            if settings ["Siri"] == True:
                if msg.text in ["/เปิดเชิญ","/อนุญาติเชิญ"]:
                    line.sendText(msg.to,"設定:招待拒否:オフ")
                    line.sendText(msg.to,"อนุญาติการเชิญสมาชิกเข้าร่วมกลุ่ม")
            if settings ["Siri"] == True:
                if msg.text in ["/เปิดพูด","/เปิดบอท","/เปิดตอบ"]:
                    line.sendText(msg.to,"Siriv10:オン")
                    line.sendText(msg.to,"เปิดใช้งานบอทอ่าน")
            if settings ["Siri"] == True:
                if msg.text in ["/ปิดพูด","/ปิดตอบ","/ปิดบอท"]:
                    line.sendText(msg.to,"Siriv10:オフ")
                    line.sendText(msg.to,"คำสั่งปิดใช้งานบอทอ่านสิริ")
            if settings ["Siri"] == True:
                if msg.text in ["/คัดลอก","/Copy","/copy"]:
                    line.sendText(msg.to,"Set:copyownlist")   
                    line.sendText(msg.to,"คำสั่งคัดลอกบัญชีห้อง")
            if settings ["Siri"] == True:
                if msg.text in ["/เซ็ตบัญชี","/ลบรีส","/ตั้งค่าบัญชี"]:
                    line.sendText(msg.to,"Set:deletelist")
                    line.sendText(msg.to,"คำสั่งตั้งค่าใหม่สำหรับ\nการคัดลอกครั้งใหม่")
            if settings ["Siri"] == True:
                if msg.text in ["/ปิดลิ้ง"]:
                    line.sendText(msg.to,"Siriv10:DenyURLInvite")
                    line.sendText(msg.to,"สั่งปิดลิ้งห้อง")
            if settings ["Siri"] == True:
                if msg.text in ["/เปิดลิ้งค์","/เปิดลิ้ง"]:
                    line.sendText(msg.to,"Siriv10:inviteurl")
                    line.sendText(msg.to,"คำสั่งเปิดลิ้งห้อง")
            if settings ["Siri"] == True:
                if msg.text in ["/ล็อครูป","/ล๊อครูป","/ลอครูป"]:
                    line.sendText(msg.to,"Set:iconlock:on")
                    line.sendText(msg.to,"คำสั่งล็อครูปห้อง")
            if settings ["Siri"] == True:
                if msg.text in ["/ลอคชื่อ","/ล็อคชื่อ","/ล๊อคชื่อ"]:
                    line.sendText(msg.to,"Set:changenamelock:on")
                    line.sendText(msg.to,"คำสั่งล็อคชื่อห้อง")
            if settings ["Siri"] == True:
                if msg.text in ["/ล๊อคแอด","/ลอคแอด","/ล็อคแอด"]:
                    line.sendText(msg.to,"Set:ownerlock:on")
                    line.sendText(msg.to,"คำสั่งใช้ล๊อคแอดมินห้อง")
            if settings ["Siri"] == True:
                if msg.text in ["/ล๊อคเชิญ","/ลอคเชิญ","/ล็อคเชิญ"]:
                    line.sendText(msg.to,"Set:blockinvite:on")
                    line.sendText(msg.to,"คำสั่งล็อคการเชิญสมาชิก")
            if settings ["Siri"] == True:
                if msg.text in ["/ชุดล๊อคjp","/ชุดล็อค2","/ชุดล็อคjp"]:
                    line.sendText(msg.to,"設定:スタンプ規制:オン")
                    line.sendText(msg.to,"Siriv10:招待URL拒否")
                    line.sendText(msg.to,"設定:招待拒否:オン")
                    line.sendText(msg.to,"設定:アイコンロック:オン")
                    line.sendText(msg.to,"設定:グループ名ロック:オン")
                    line.sendText(msg.to,"設定:作成者ロック:オン")
                    line.sendText(msg.to,"ชุดคำสั่งล๊อคห้องภาษาญี่ปุ่น")
         #       if msg.text in ["คถ","คิดถึง","คถ."]:
          #          line.sendMessage(msg.to,"คิดถึงเหมือนกันนะ (*_*)")  
#==============================================================================#
        if op.type == 26:
 #            if settings ["mutebot2"] == True:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if settings["unsend"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"lokasi":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                if msg.contentType == 1:
                    if settings["unsend"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2:
                    if settings["unsend"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3:
                    if settings["unsend"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7:
                    if settings["unsend"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13:
                    if settings["unsend"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14:
                    if settings["unsend"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
#==============================================================================#
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsend"] == True:
                at = op.param1
                msg_id = op.param2
                if msg_id in msg_dict:
                    ah = time.time()
                    ikkeh = line.getContact(msg_dict[msg_id]["from"])
                    if "text" in msg_dict[msg_id]:
                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                        waktumsg = format_timespan(waktumsg)
                        rat_ = "\nสปีด : {}".format(waktumsg)
                        rat_ += "\nพิมว่า : {}".format(msg_dict[msg_id]["text"])
                        sendMention(at, ikkeh.mid, "** 🍉ตรวจพบการยกเลิกข้อความ🍉 **\n\nMaker :\n", str(rat_))
                        #line.sendMessage(at, "** พบการยกเลิกข้อความ **\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                        del msg_dict[msg_id]
                    else:
                        if "image" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nสปีด : {}".format(waktumsg)
                            rat_ += "\nรูป : "
                            line.sendMessage(at, "** 🍉พบการยกเลิกข้อความ🍉 **\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                            line.sendImage(at, msg_dict[msg_id]["image"])
                            del msg_dict[msg_id]
                        else:
                            if "video" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nสปีด : {}".format(waktumsg)
                                rat_ += "\nวีดีโอ : "
                                line.sendMessage(at, "** 🍉พบการยกเลิกข้อความ🍉 **\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                                line.sendVideo(at, msg_dict[msg_id]["video"])
                                del msg_dict[msg_id]
                            else:
                                if "audio" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nสปีด : {}".format(waktumsg)
                                    rat_ += "\nเสียง : "
                                    line.sendMessage(at, "** 🍉พบการยกเลิกข้อความ🍉 **\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                                    line.sendAudio(at, msg_dict[msg_id]["audio"])
                                    del msg_dict[msg_id]
                                else:
                                    if "sticker" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nสปีด : {}".format(waktumsg)
                                        rat_ += "\nสติ๊กเกอร์ :"
                                        line.sendMessage(at, "** 🍉พบการยกเลิกข้อความ🍉 **\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                                        line.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "mid" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nสปีด : {}".format(waktumsg)
                                            rat_ += "\nคอนแทค : "
                                            line.sendMessage(at, "** 🍉พบการยกเลิกข้อความ🍉 **\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                                            line.sendContact(at, msg_dict[msg_id]["mid"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "lokasi" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nสปีด : {}".format(waktumsg)
                                                rat_ += "\nตำแหน่ง :"
                                                line.sendMessage(at, "** 🍉พบการยกเลิกข้อความ🍉 **\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                                                line.sendLocation(at, msg_dict[msg_id]["lokasi"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "file" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nสปีด : {}".format(waktumsg)
                                                    rat_ += "\nไฟล์ : "
                                                    line.sendMessage(at, "** 🍉พบการยกเลิกข้อความ🍉 **\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                                                    line.sendFile(at, msg_dict[msg_id]["file"])
                                                    del msg_dict[msg_id]
                else:
                    line.sendMessage(at, "มีการยกเลิกข้อความ\n\n✯のิՁυิπ⇴ℂℝỦҾⱢ✯ ")
                    
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n🍯" + Name
                            pref=['จ๊ะเอ๋','รู้นะว่าแอบอยู่','เล่นซ่อนแอบกันเหรอ','คิดว่าเป็นนินจารึไง','ว่าไง','อ่านอย่างเดียวเลยนะ','ออกมาคุยหน่อย','ออกมาเดี๋ยวนี้']
                            sendMessageWithMention(op.param1, op.param2)
                            line.sendMessage(op.param1, str(random.choice(pref)) + '\n♪ ♬ ヾ(´︶`♡)ﾉ ♬ ♪')
                            line.sendContact(op.param1, op.param2)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	line.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	line.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            print ("ＦＡＲＩＳＢＯＴＬＩＮＥ")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass 
    except Exception as error:
        logError(error)
#==============================================================================#
def a2():
    now2 = datetime.now() 
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
        

while True:
    try:
        ops = oepoll.singleTrace(count=5)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
