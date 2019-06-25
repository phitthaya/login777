# -*- coding: utf-8 -*-
from random import randint
from bs4 import BeautifulSoup
from wikiapi import WikiApi
from akad.ttypes import *
from kbbi import KBBI
from datetime import datetime, timedelta, date
from youtube_dl import YoutubeDL
from Aditya import Kaskus
from Aditya.AdityaMangakyo import *
import youtube_dl
from multiprocessing import Pool, Process
import time,random,sys,json,requests,os,subprocess,re,ast,traceback,humanize,threading,base64
from Aditya.AdityaSplitGood import AdityaSplitGood
from Aditya.memedit import *
import ntpath

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
    kuciyose = {}

    def __init__(self):
        self.isLogin = True

    """User"""

    def changecpvv(self,to,wait):
        try:
            path_vid = wait['talkban']['video']
            files = {'file': open(path_vid, 'rb')}
            obs_params = self.genOBSParams({'oid': self.profile.mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
            data = {'params': obs_params}
            if wait['talkban']['pict'] == '':
                return self.sendMessage(to, " 「 Profile 」\nType: Change Profile Video Picture\nStatus: Send the image....♪")
            self.sendMessage(to, " 「 Profile 」\nType: Change Profile Video Picture\nStatus: Waiting....♪")
            r_vp = self.server.postContent('{}/talk/vp/upload.nhn'.format(str(self.server.LINE_OBS_DOMAIN)), data=data, files=files)
            if r_vp.status_code != 201:return "Failed"
            path_pic = wait['talkban']['pict']
            wait['talkban']['cvp'] = False
            wait['talkban']['pict'] = ''
            self.updateProfilePicture(path_pic, 'vp')
        except Exception as e:
            self.sendMessage(to, " 「 Profile 」\nType: Change Profile Video Picture\nStatus: ERROR 404 Plese Try again")
    def fancyfancy(self,wait):
                if wait['ChangeCover'] == True:
                        try:
                            if time.time() - wait['talkban']['time'] >= wait['talkban']['timer']:
                                a = random.randint(0,len(wait['timeline']))
                                self.updateProfileAttribute(2, wait['timeline'][a])
                                wait['talkban']['time'] = time.time()
                                wait['talkban']['timer'] = wait['talkban']['timer']
                        except:pass

    def aditcontenttype(self,msg,wait,kuciyose):
        if msg.contentType == 16:
            if msg.to in wait["kitsuneshare"]:
                zxc = " 「 POST NOTIFICATION 」\nCreate By: @!"
                try:a = msg.contentMetadata["text"]
                except:a = 'None'
                zxc+= '\nText: '+a+'\nLink: '+msg.contentMetadata["postEndUrl"]
                self.sendMention(msg.to,zxc,'',[msg.contentMetadata["postEndUrl"][25:58]])
        if msg.contentType == 2:
            if wait['talkban']['cvp'] == True:
                try:
                    path = self.downloadObjectMsg(msg.id)
                    wait['talkban']['pict'] = ''
                    wait['talkban']['video'] = path
                    self.changecpvv(msg.to,wait)
                except Exception as e:                         
                    self.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
        if msg.contentType == 1:
                if wait["ChangeDP"] == True:
                    try:
                        path = self.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id, 'path')
                        self.updateProfilePicture(path)
                        self.sendMessage(msg.to, " 「 Profile 」\nType: Change Profile Picture\nStatus: Profile Picture Hasbeen change♪")
                    except Exception as e:
                        self.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                    wait["ChangeDP"] = False
                if wait['talkban']['cvp'] == True:
                    try:
                        path = self.downloadObjectMsg(msg.id)
                        wait['talkban']['pict'] = path
                        self.changecpvv(msg.to,wait)
                        self.sendMessage(msg.to, " 「 Profile 」\nType: Change Profile Video Picture\nStatus: Profile Video Picture Hasbeen change♪")
                    except Exception as e:                         
                        self.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                if wait["GN"] == True:
                    try:
                        self.downloadObjectMsg(msg_id,'path','dataSeen/'+msg.to+'.png')
                    except Exception as e:                         
                        self.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                    wait["GN"] = False
                if msg.to in wait["setTimess"]:
                    try:
                        path = self.downloadObjectMsg(msg.id,'path','dataSeen/adityab.png')
                        self.updateGroupPicture(msg.to,path)
                        self.sendMessage(msg.to, " 「 Group 」\nType: Change Cover Group\nStatus: Cover Group Hasbeen change♪")
                    except Exception as e:                         
                        self.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                    wait["setTimess"].remove(msg.to)
                if wait['ChangeGDP'] == True:
                    try:
                        a = self.downloadObjectMsg(msg.id,'path','s.png')
                        self.addImageToAlbum(msg.to, wait["Images"]['anu'], 's.png')
                    except Exception as e:
                        self.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                    wait["Img"] = {}
                    wait['ChangeGDP'] = False
                if kuciyose['MakeWaterColor'] == True:
                    try:a = threading.Thread(target=self.imageGenerate, args=(msg,'http://ari-api.herokuapp.com/watercolor?type=2&rancol=on&url=',)).start();kuciyose['MakeWaterColor'] = False
                    except:self.sendMessage(msg.to,' 「 Water Color 」\nType: Image Generator\nStatus: Error Proses Image..♪\nImportant: Please Send the image again')
                if kuciyose['DrawImage'] == True:
                    try:a = threading.Thread(target=self.imageGenerate, args=(msg,'http://ari-api.herokuapp.com/drawing?url=',)).start();kuciyose['DrawImage'] = False
                    except:self.sendMessage(msg.to,' 「 Water Color 」\nType: Image Generator\nStatus: Error Proses Image..♪\nImportant: Please Send the image again')
                if kuciyose['MakeMeme'] == True:
                    try:
                        path = self.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id, 'path','dataSeen/%s.jpg' % kuciyose['MakeMemeText1'])
                        make_meme(kuciyose['MakeMemeText1'], kuciyose['MakeMemeText2'], 'dataSeen/%s.jpg' % kuciyose['MakeMemeText1'])
                        self.sendImage(msg.to,'dataSeen/%s.jpg' % kuciyose['MakeMemeText1'])
                        os.remove('dataSeen/%s.jpg' % kuciyose['MakeMemeText1'])
                        kuciyose['MakeMeme'] = False
                    except:
                        self.sendMessage(msg.to,' 「 Meme 」\nType: Meme Generator\nStatus: Error Proses Image..♪\nImportant: Please Send the image again')
                if wait["Addimage"] == True:
                    try:
                        url = 'https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id
                        try:
                            if msg.contentMetadata != {}:
                                wait["Images"][wait["Img"]] = 'dataSeen/%s.gif' % wait["Img"];path = self.downloadObjectMsg(msg.id,'path','dataSeen/%s.gif' % wait["Img"],True)
                        except:wait["Images"][wait["Img"]] = 'dataSeen/%s.jpg' % wait["Img"];path = self.downloadFileURL(url, 'path','dataSeen/%s.jpg' % wait["Img"])
                        self.sendMessage(msg.to, " 「 Picture 」\nType: Add Picture\nStatus: Success Add Picture♪")
                    except Exception as e:
                        self.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                    wait["Img"] = {}
                    wait["Addimage"] = False
        if msg.contentType == 7:
            a = self.shop.getProduct(packageID=int(msg.contentMetadata['STKPKGID']), language='ID', country='ID')
            if wait["Addsticker"] == True:
                wait["Sticker"][wait["Img"]] = msg.contentMetadata
                self.sendMessage(msg.to, " 「 Sticker 」\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                wait["Img"] = {}
                wait["Addsticker"] = False
            if msg.to in wait["GROUP"]['AR']['S']:
                if wait["GROUP"]['AR']['S'][msg.to]['AP'] == True:
                    wait["GROUP"]['AR']['S'][msg.to]['Sticker'] = msg.contentMetadata
                    self.sendMessage(msg.to, " 「 Autorespon Sticker 」\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                    wait["GROUP"]['AR']['S'][msg.to]['AP'] = False
            if msg.to in wait["GROUP"]['WM']['S']:
                if wait["GROUP"]['WM']['S'][msg.to]['AP'] == True:
                    wait["GROUP"]['WM']['S'][msg.to]['Sticker'] = msg.contentMetadata
                    self.sendMessage(msg.to, " 「 Welcome Sticker 」\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                    wait["GROUP"]['WM']['S'][msg.to]['AP'] = False
            if msg.to in wait["GROUP"]['LM']['S']:
                if wait["GROUP"]['LM']['S'][msg.to]['AP'] == True:
                    wait["GROUP"]['LM']['S'][msg.to]['Sticker'] = msg.contentMetadata
                    self.sendMessage(msg.to, " 「 Leave Sticker 」\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                    wait["GROUP"]['LM']['S'][msg.to]['AP'] = False
        if msg.contentType == 13:
                self.adityeksekusidata(msg,wait)
                if msg.to in wait["kitsunecontact"]:
                    s=msg.contentMetadata["mid"];a = self.getContact(s);zxc = " 「 Contact 」\nName: @!\n\nMid: "+s+"\n\nStatus Message:\n"+a.statusMessage 
                    self.sendMention(msg.to, zxc,'', [s])
    def set(self,msg,wait,kuciyose):
        md = " 「 ANBot Beta v4.0 」\nSettings:"
        if wait["setkey"] == '': md+="\n- Key: DISABLED"
        else: md+="\n- Key: "+wait["setkey"]
        md+="\nGroup Settings:"
        if msg.to in wait["GROUP"]['AM']['AP']:md+="\n- Auto Respon: ENABLED♪"
        else:md+="\n- Auto Respon: DISABLED♪"
        if msg.to in wait["GROUP"]['WM']['AP']:md+="\n- Welcome MSG: ENABLED♪"
        else:md+="\n- Welcome MSG: DISABLED♪"
        if msg.to in wait["GROUP"]['LM']['AP']:md+="\n- Leave MSG: ENABLED♪"
        else:md+="\n- Leave MSG: DISABLED♪"
        try:
            if wait['tos'][msg.to]['setset'] == True:md+="\n- Unsend Detect: ENABLED♪"
            else:md+="\n- Unsend Detect: DISABLED♪"
        except:
            wait['tos'][msg.to] = {'setset':False}
            if wait['tos'][msg.to]['setset'] == True:md+="\n- Unsend Detect: ENABLED♪"
            else:md+="\n- Unsend Detect: DISABLED♪"
        if msg.to in wait["setTimess"]:md+="\n- ChangeDP Group: ENABLED♪"
        else:md+="\n- ChangeDP Group: DISABLED♪"
        md+="\nGenerator:"
        if kuciyose['MakeMeme'] == True:md+="\n- Meme Generator: ENABLED♪"
        else:md+="\n- Meme Generator: DISABLED♪"
        if kuciyose['MakeWaterColor'] == True:md+="\n- Image Watercolor: ENABLED♪"
        else:md+="\n- Image Watercolor: DISABLED♪"
        if kuciyose['DrawImage'] == True:md+="\n- Image Drawing: ENABLED♪"
        else:md+="\n- Image Drawing: DISABLED♪"
        self.sendMessage(msg.to,md)
    def imageGenerate(self,msg,wait):
        path = self.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id, 'path','dataSeen/s.jpg')
        r=requests.post(url="http://api.ntcorp.us/storage/make", data={'category':'kolorikolori',"submit": " "},files={'file': open(path,'rb')})
        data = r.json()
        self.sendImageWithURL(msg.to,'{}{}'.format(wait,self.ub64("http://api.ntcorp.us/storage/get/{}".format(data["result"]["id"]))))
    def backupmyprofile(self,to,wait):
        hh = self.profile.mid
        self.updateProfileAttribute(2, wait['talkblacklist']['L'])
        self.updateProfileAttribute(16, wait['talkblacklist']['U'])
        path = self.downloadFileURL("http://dl.profile.line-cdn.net/"+wait['talkblacklist']['O'], 'path')
        self.updateProfilePicture(path)
        self.updateProfileCoverById(wait['talkblacklist']['S'])
        self.sendMessage(to," 「 Backup Profil 」\nSukses Backup\nDisplayName:" + wait['talkblacklist']['L'] + "\n「 Status 」\n" + wait['talkblacklist']['U'])
        try:
            self.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,'Profile')
        except Exception as e:
            self.sendMessage(to,"「 Auto Respond 」\n"+str(e))
    def setbackupprofile(self,to,wait):
        hh = self.profile.mid
        S = self.getProfileCoverId(hh)
        L = self.getProfile().displayName;U = self.getProfile().statusMessage;O = self.getProfile().picturePath;self.sendMessage(to," 「 Backup Profil 」\nSukses Setdefault\nDisplayName:" + self.getProfile().displayName + "\n「Status 」\n" + self.getProfile().statusMessage + "\n「Picture 」")
        wait['talkblacklist'] = {'L':L,'U':U,'O':O,'S':S}
        me = self.getProfile()
        self.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + me.picturePath,'Profile')
    def waktu(self,secs):
        mins, secs = divmod(secs,60)
        hours, mins = divmod(mins,60)
        days, hours = divmod(hours, 24)
        return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

    def restart_program(self):
        os.system('clear')
        python = sys.executable
        os.execl(python, python, * sys.argv)

    """Message"""
    def sendMention(self,to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@ADIT GANTENG "
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
    def templatefoot(self,link,AI,AN):
        a={'AGENT_LINK': link,
        'AGENT_ICON': AI,
        'AGENT_NAME': AN}
        return a
    def igsearch(self,msg,wait):
        to = msg.to
        msg.text = self.mycmd(msg.text,wait)
        text = msg.text.split(' ')[1]
        if len(msg.text.split(' ')) == 2:
            try:
                r = requests.get("http://rahandiapi.herokuapp.com/instainfo/"+msg.text.split(' ')[1]+"?key=betakey")
                data = r.json()
                a=" 「 Instagram 」\nType: Search User Instagram"
                a+="\nName : "+str(data['result']['name'])
                a+="\nBiography :\n   "+str(data['result']['bio'])
                a+="\nFollower : "+humanize.intcomma(data['result']['follower'])
                a+="\nFollowing : "+humanize.intcomma(data['result']['following'])
                a+="\nMedia : "+humanize.intcomma(data['result']['mediacount'])
                a+="\nPrivate : "+str(data['result']['private'])
                a+= "\nUsage:%s instagram %s num" %(wait["setkey"], str(text))
                self.sendImageWithURL(to,data['result']['url'],str(data['result']['name']))
                self.sendMessage(to,a, self.templatefoot('https://www.instagram.com/{}/'.format(data['result']['username']),'https://3xl39023n0uyvr5xx1gc1btk-wpengine.netdna-ssl.com/wp-content/uploads/2015/10/element-social-circle-instagram.png',str(data['result']['name'])))
            except:
                return self.sendMessage(to,"Status: 404\nReason: Instagram {} tidak ditemukan".format(text))
        if len(msg.text.split(' ')) == 3:
            try:
                data1 = self.adityarequestweb('http://rahandiapi.herokuapp.com/instapost/{}/{}?key=betakey'.format(msg.text.split(' ')[1],msg.text.split(' ')[2]))
                try:
                    if data1['media']['caption'] == '':a = ''
                    else:a = 'Caption: {}'.format(data1['media']['caption'])
                    a+="\nLikes : "+humanize.intcomma(data1['media']['like_count'])
                    try:
                        url = data1['media']['url']
                        if '.mp4' in url:
                            try:
                                self.sendVideoWithURL(to,url)
                            except:self.sendMessage(to,'Video Gagal Dimuat Silahkan Coba Kembali')
                        else:
                            self.sendImageWithURL(to,url,'Post IG')
                    except:
                        url = data1['media']['url']
                        if '.mp4' in url:
                            try:
                                self.sendVideoWithURL(to,url)
                            except:self.sendMessage(to,'Video Gagal Dimuat Silahkan Coba Kembali')
                        else:
                            b = []
                            for hgd in range(0,len(data1['media']['url'])):
                                self.sendImageWithURL(to,data1['media']['url'][hgd]['url'],'Post Ig')
                    self.sendMessage(to,a, self.templatefoot('https://www.instagram.com/{}/'.format(msg.text.split(' ')[1]),'https://3xl39023n0uyvr5xx1gc1btk-wpengine.netdna-ssl.com/wp-content/uploads/2015/10/element-social-circle-instagram.png',str(msg.text.split(' ')[1])))
                except:
                    return self.sendMessage(to," 「 Instagram 」\nStatus: 404\nReason: Post or Username I'cant found")
            except Exception as e:
                ee = traceback.format_exc()
                return self.sendMessage(to,'{}'.format(e))
    def ub64(self,url):hasil = base64.b64encode(url.encode());return hasil.decode('utf-8')
    def makewatercolor(self,msg,wait,kuciyose):
        msg.text = self.mycmd(msg.text,wait)
        if msg.text.lower().startswith("watercolor "):
            if msg.text.split(' ')[1] == 'on':kuciyose['MakeWaterColor'] = True;return self.sendMessage(msg.to,' 「 Water Color 」\nType: Image Generator\nStatus: Send the image....')
            try:
                if 'http://' in msg.text:
                    self.sendImageWithURL(msg.to,'http://ari-api.herokuapp.com/watercolor?type=2&rancol=on&url={}'.format(self.ub64(self.adityasplittext(msg.text.lower()))))
            except Exception as e:
                self.sendMessage(msg.to,str(e))
    def makedrawingimage(self,msg,wait,kuciyose):
        msg.text = self.mycmd(msg.text,wait)
        if msg.text.lower().startswith("drawimage "):
            if msg.text.split(' ')[1] == 'on':kuciyose['DrawImage'] = True;return self.sendMessage(msg.to,' 「 Drawing 」\nType: Image Generator\nStatus: Send the image....')
            try:
                if 'http://' in msg.text:
                    self.sendImageWithURL(msg.to,'http://ari-api.herokuapp.com/drawing?url={}'.format(self.ub64(self.adityasplittext(msg.text.lower()))))
            except Exception as e:
                self.sendMessage(msg.to,str(e))
    def makememe(self,msg,wait,kuciyose):
        msg.text = self.mycmd(msg.text,wait)
        if msg.text.lower().startswith("meme "):
            kitsunesplit = self.adityasplittext(msg.text.lower()).split("|")
            if len(kitsunesplit) >= 2:
                try:
                    try:
                        getTemplate=self.get_memes()[int(kitsunesplit[2])-1]['id']
                        genMeme=self.imgflipMeme(kitsunesplit[0],kitsunesplit[1],getTemplate,"impact")
                    except:
                        getTemplate=self.get_memes()[int(kitsunesplit[1])-1]['id']
                        genMeme=self.imgflipMeme(kitsunesplit[0],'',getTemplate,"impact")
                    self.sendImageWithURL(msg.to,genMeme['url'],'Meme Generator')
                except:
                    kuciyose['MakeMeme'] = True;kuciyose['MakeMemeText1'] = kitsunesplit[0];kuciyose['MakeMemeText2'] = kitsunesplit[1]
                    self.sendMessage(msg.to,' 「 Meme 」\nType: Meme Generator\nStatus: Send the image....')
    def imgflipMeme(self,upper_text,lower_text,template_id,font="impact"):
        username = "kopisusu"
        password = "kopisusu27"
        text0 = upper_text
        text1 = lower_text
        url = "https://api.imgflip.com/caption_image"
        mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
        payload = {'username':username, 'password':password, 'template_id':template_id, 'text0':text0, 'text1':text1, 'font':font}
        req = requests.post(url, data=payload)
        req.raise_for_status()
        response = req.json()
        if response['success']:
            return response['data']
        else:
            raise RuntimeError("Imgflip returned error message: " + response['error_message'])
    def memelist(self,msg,wait):
        getTemplate=self.get_memes()
        listtemp="List Template Meme:"
        for i in range(0,100):
            listtemp += "\n"+str(i+1) + ". " + getTemplate[i]['name']
        listtemp += "\nType %smeme txt|text|num" %(wait["setkey"])                        
        self.sendMessage(msg.to,listtemp)
    def get_memes(self):
        url = 'https://api.imgflip.com/get_memes'
        r = requests.get(url)
        r.raise_for_status()
        response = r.json()
        if response['success']:
            return response['data']['memes']
        else:
            raise RuntimeError("Imgflip returned error message: " + response['error_message'])
    def youtubelist(self,msg,wait):
        kolor = msg.text
        msg.text = self.mycmd(msg.text,wait)
        cmk = msg.text.lower()
        kitsunesplit = self.adityasplittext(msg.text.lower(),'s').split("|")
        a = self.adityarequestweb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+kitsunesplit[0]+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
        to = msg.to
        kk = random.randint(0,999)
        ditkey = ''
        if msg.text.lower().startswith('youtube info '):
            if(len(kitsunesplit) == 1 or len(kitsunesplit) == 2):self.sendMessage(to,' 「 Youtube 」\nWaiting....')
            if(len(kitsunesplit) == 1):dfghj = self.adityasplittext(msg.text,'s');hs = self.adityarequestweb('http://rahandiapi.herokuapp.com/youtubeapi?key=betakey&q='+self.adityasplittext(msg.text,'s'))
            if(len(kitsunesplit) == 2):dfghj = 'https://www.youtube.com/watch?v='+a["items"][int(kitsunesplit[1])-1]["id"]['videoId'];hs = self.adityarequestweb('http://rahandiapi.herokuapp.com/youtubeapi?key=betakey&q='+dfghj)
            meta = hs['result']
            if meta['description'] == '':hjk = ''
            else:hjk = '\nDescription:\n{}'.format(meta['description'])
            t = ' 「 Youtube 」\nTitle: {}{}\n\nLike: {}  Dislike: {}\nViewers: {}'.format(meta['title'],hjk,humanize.intcomma(meta['likes']),humanize.intcomma(meta['dislikes']),humanize.intcomma(meta['viewcount']))
            self.sendMessage(to,t, self.templatefoot(dfghj,'https://cdn3.iconfinder.com/data/icons/follow-me/256/YouTube-512.png',meta['title']))
            self.sendImageWithURL(to,meta['thumbnail'],meta['title'])
        if msg.text.lower().startswith('youtube download '):
            if len(kitsunesplit) == 1:
                with youtube_dl.YoutubeDL({}) as ydl:
                    dfg = self.adityasplittext(kolor,'s').replace('youtu.be/','youtube.com/watch?v=').replace('download ','')
                    meta = ydl.extract_info(dfg, download=False)
                    self.sendImageWithURL(to,meta['thumbnail'])
                    try:
                        data1 = self.adityarequestweb('http://rahandiapi.herokuapp.com/youtubeapi?key=betakey&q='+dfg)
                        a= " 「 LINK DL 」\nType: Youtube Video\n"
                        a+= "\nTitle: " + str(data1["result"]['title'])
                        a+= "\nDuration: " + str(data1["result"]['duration'])
                        a+= "\nAuthor: "+str(data1["result"]['author'])
                        a+= "\nLike: "+humanize.intcomma(data1["result"]['likes'])
                        if data1["result"]['videolist'] != []:
                            a+= "\n\n 「 Video 」"
                            no = 0
                            for music in data1["result"]['videolist']:
                                no +=1
                                a+= '\n    '+str(no)+'. '+music['resolution']+' '+music['extension']+' Size: '+music['size']
                                a+= '\n         '+music['url']
                        if data1["result"]['audiolist'] != []:
                            a+= "\n\n 「 Audio 」"
                            nos = 0
                            for musics in data1["result"]['audiolist']:
                                nos +=1
                                a+= '\n    '+str(nos)+'. '+musics['resolution']+' '+musics['extension']+' Size: '+musics['size']
                                a+= '\n         '+musics['url']
                        self.sendMessage(to,str(a))
                    except:
                        self.sendMessage(to,'Error 404')
            if len(kitsunesplit) == 2:
                with youtube_dl.YoutubeDL({}) as ydl:
                    meta = ydl.extract_info('https://youtube.com/watch?v={}'.format(a["items"][int(kitsunesplit[1])-1]["id"]['videoId']), download=False)
                    self.sendImageWithURL(to,meta['thumbnail'])
                    adit = str(a["items"][int(kitsunesplit[1])-1]["id"]['videoId'])
                    try:
                        data1 = self.adityarequestweb('http://rahandiapi.herokuapp.com/youtubeapi?key=betakey&q=https://www.youtube.com/watch?v='+adit)
                        a= " 「 LINK DL 」\nType: Youtube Video\n"
                        a+= "\nTitle: " + str(data1["result"]['title'])
                        a+= "\nDuration: " + str(data1["result"]['duration'])
                        a+= "\nAuthor: "+str(data1["result"]['author'])
                        a+= "\nLike: "+humanize.intcomma(data1["result"]['likes'])
                        if data1["result"]['videolist'] != []:
                            a+= "\n\n 「 Video 」"
                            no = 0
                            for music in data1["result"]['videolist']:
                                no +=1
                                a+= '\n    '+str(no)+'. '+music['resolution']+' '+music['extension']+' Size: '+music['size']
                                a+= '\n         '+music['url']
                        if data1["result"]['audiolist'] != []:
                            a+= "\n\n 「 Audio 」"
                            nos = 0
                            for musics in data1["result"]['audiolist']:
                                nos +=1
                                a+= '\n    '+str(nos)+'. '+musics['resolution']+' '+musics['extension']+' Size: '+musics['size']
                                a+= '\n         '+musics['url']
                        self.sendMessage(to,str(a))
                    except:
                        self.sendMessage(to,'Error 404')
        if(cmk.startswith("youtube video ") or cmk.startswith("youtube audio ")):
            if len(kitsunesplit) == 1:dfghj = self.adityasplittext(kolor,'s').replace('youtu.be/','youtube.com/watch?v=').replace('video ','').replace('audio ','');hs = self.adityarequestweb('http://rahandiapi.herokuapp.com/youtubeapi?key=betakey&q='+dfghj)
            if len(kitsunesplit) == 2:dfghj = 'https://www.youtube.com/watch?v='+a["items"][int(kitsunesplit[1])-1]["id"]['videoId'];hs = self.adityarequestweb('http://rahandiapi.herokuapp.com/youtubeapi?key=betakey&q='+dfghj)
            if(cmk.startswith("youtube audio ")):sddd = [a['url'] for a in hs["result"]['audiolist'] if a['extension'] == 'm4a'];ghj= 'mp3';sdd = hs["result"]['videolist'][len(hs["result"]['audiolist'])-1]
            if(cmk.startswith("youtube video ")):sdd = hs["result"]['videolist'][len(hs["result"]['videolist'])-1];ghj = sdd['extension']
            hhhh = ' 「 Youtube 」\nJudul: {}\nDuration: {}\nEx: {}.{} {}\nSize: {}\nStatus: Waiting... For Upload'.format(hs['result']['title'],hs['result']['duration'],hs['result']['title'],ghj,sdd['resolution'],sdd['size'])
            self.sendMessage(msg.to,hhhh, self.templatefoot('{}'.format(dfghj),'https://cdn3.iconfinder.com/data/icons/follow-me/256/YouTube-512.png',hs['result']['title']))
            if(cmk.startswith("youtube audio ")):self.sendAudioWithURL(to,sddd[0])
            if(cmk.startswith("youtube video ")):self.sendVideoWithURL(to,sdd['url'])
        if msg.text.lower().startswith("youtube search "):
            if a["items"] != []:
                no = 0
                ret_ = "╭──「 Youtube 」\n│Type: Youtube Video"
                for music in a["items"]:
                    no += 1 
                    asd = "\n│{}. {}".format(no,music['snippet']['title'])
                    if no == len(a["items"]):ss='╰'
                    else:ss='│'
                    if len(asd) >= 30:
                        if no == len(a["items"]):ghj = ''
                        else:ghj = "\n{}   {}".format(ss,music['snippet']['title'][30:])
                        ret_ +="\n{}{}. {}{}".format(ss,no,music['snippet']['title'][:31],ghj)
                    else:ret_ += "\n{}{}. {}".format(ss,no,music['snippet']['title'])
                self.sendMessage(to,ret_)
            else:
                self.sendMessage(to,"Type: Search Youtube Video\nStatus: "+str(self.adityasplittext(msg.text,'s'))+" not found")
    def adityarequestweb(self,url):
        r = requests.get("{}".format(url))
        data = r.text
        data = json.loads(data)
        return data
    def GroupPost(self,msg,wait):
        to = msg.to
        data = self.getGroupPost(to)
        msg.text = self.mycmd(msg.text,wait)
        if msg.text.lower() == 'get note':
            if data['result'] != []:
                try:
                    no = 0
                    b = []
                    a = " 「 Groups 」\nType: Get Note"
                    for i in data['result']['feeds']:
                        b.append(i['post']['userInfo']['writerMid'])
                        try:
                            for aasd in i['post']['contents']['textMeta']:b.append(aasd['mid'])
                        except:pass
                        no += 1
                        gtime = i['post']['postInfo']['createdTime']
                        try:g = i['post']['contents']['text'].replace('@','@!')
                        except:g="None"
                        if no == 1:sddd = '\n'
                        else:sddd = '\n\n'
                        a +="{}{}. Penulis : @!\nDescription: {}\nTotal Like: {}\nCreated at: {}".format(sddd,no,g,i['post']['postInfo']['likeCount'],humanize.naturaltime(datetime.fromtimestamp(gtime/1000)))
                    a +="Status: Success Get "+str(data['result']['homeInfo']['postCount'])+" Note"
                    self.sendMention(to,a,'',b)
                except Exception as e:
                    return self.sendMessage(to,"「 Auto Respond 」\n"+str(e))
        if msg.text.lower().startswith('get note '):
            try:
                music = data['result']['feeds'][int(msg.text.split(' ')[2]) - 1]
                b = [music['post']['userInfo']['writerMid']]
                try:
                    for a in music['post']['contents']['textMeta']:b.append(a['mid'])
                except:pass
                try:
                    g= "\n\nDescription:\n"+str(music['post']['contents']['text'].replace('@','@!'))
                except:
                    g=""
                a="\n   Total Like: "+str(music['post']['postInfo']['likeCount'])
                a +="\n   Total Comment: "+str(music['post']['postInfo']['commentCount'])
                gtime = music['post']['postInfo']['createdTime']
                a +="\n   Created at: "+str(humanize.naturaltime(datetime.fromtimestamp(gtime/1000)))
                a += g
                zx = ""
                zxc = " 「 Groups 」\nType: Get Note\n   Penulis : @!"+a
                try:
                    self.sendMention(to,zxc,'',b)
                except Exception as e:
                    self.sendMessage(to, str(e))
                try:
                    for c in music['post']['contents']['media']:
                        params = {'userMid': self.getProfile().mid, 'oid': c['objectId']}
                        path = self.server.urlEncode(self.server.LINE_OBS_DOMAIN, '/myhome/h/download.nhn', params)
                        if 'PHOTO' in c['type']:
                            try:
                                self.sendImageWithURL(to,path,'POST')
                            except:pass
                        else:
                            pass
                        if 'VIDEO' in c['type']:
                            try:
                                self.sendVideoWithURL(to,path)
                            except:pass
                        else:
                            pass
                except:
                    pass
            except Exception as e:
                return self.sendMessage(to,"「 Auto Respond 」\n"+str(e))
    def disguiseons(self,msg):
        to=msg.to
        if 'MENTION' in msg.contentMetadata.keys()!= None:
            key = eval(msg.contentMetadata["MENTION"])
            key1 = key["MENTIONEES"][0]["M"]
            self.cloneContactProfile(key1)
            group = self.getContact(key1);contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus;self.sendImageWithURL(to,contact,'DISGUISE')
            self.sendMention(to, ' 「 Copy Profile 」\n- Target: @!\n- Status: Success Copy profile♪','',[key1])  
    def fancynamehelp(self,wait,dd):
        if 'timer' not in wait['talkban']:
            wait['talkban']['timer'] = 60
        if 'name' not in wait['talkban']:
            wait['talkban']['name'] = self.getProfile().displayName
        try:
            if wait['timeline'] == False:wait['timeline'] = []
        except:pass
        if wait['ChangeCover'] == True:d = '\n│State: ON\n│Timer: {}second'.format(wait['talkban']['timer'])
        else:d = '\n│State: OFF'
        if wait["timeline"] == []:
            a='None'
        else:
            a = ""
            for b in wait["timeline"]:
                a+= '\n│'+b
        return "┌───「 Fancy Name 」───────\n│Backup Name: "+dd+"\n│FancyName Set:"+a+d+"\n│    | Command |  \n│Set Name\n│  Key: "+wait["setkey"].title()+" fancyname set [enter|name]\n│Set Time\n│  Key: "+wait["setkey"].title()+" fancyname on [time]\n└────────────"
    def lagulagu(self,wait):return "╭───「 Music 」─\n│    | Command |  \n│Search Music\n│  Key: "+wait["setkey"].title()+" soundcloud [query]\n│Detail Music\n│  Key: "+wait["setkey"].title()+" soundcloud [query|num]\n│Lyric\n│  Key: "+wait["setkey"].title()+" lyric [judul]\n╰──────"
    def copy(self,wait):return "╭───「 Disguise 」─\n│    | Command |  \n│Disguise ON\n│  Key: "+wait["setkey"].title()+" disguise on [@]\n│Disguise OFF\n│  Key: "+wait["setkey"].title()+" disguise off\n│Disguise Setdefault\n│  Key: "+wait["setkey"].title()+" disguise setdefault\n╰──────"
    def steal(self,wait):return "╭───「 Steal 」─\n│    | Command |  \n│Get Profile Picture\n│  Key: "+wait["setkey"].title()+" steal pp [@]\n│Get Cover Picture\n│  Key: "+wait["setkey"].title()+" steal cover [@]\n│Get ID\n│  Key: "+wait["setkey"].title()+" getid, getid [@|num]\n╰──────"
    def movie(self,wait):return "╭───「 Movie 」─\n│    | Command |  \n│Search Movie\n│  Key: "+wait["setkey"].title()+" movie [query]\n│Search Detail Movie\n│  Key: "+wait["setkey"].title()+" movie [query|1]\n╰──────"
    def keep(self,wait):return "╭───「 MEME 」─\n│    | Command |  \n│List\n│  Key: "+wait["setkey"].title()+" memelist\n│MemeGen\n│  Key: "+wait["setkey"].title()+" meme [text|text|num]\n│  Key: "+wait["setkey"].title()+" meme [text|num]\n│  Key: "+wait["setkey"].title()+" meme [text|text]\n╰──────"
    def image(self,wait):return "╭───「 Image 」─\n│    | Command |  \n│Google Image\n│  Key: "+wait["setkey"].title()+" gimage [query]\n│Artstation Image\n│  Key: "+wait["setkey"].title()+" artimage [query]\n│Image Generator\n│  Water Color\n│    Key: "+wait["setkey"].title()+" watercolor [url]\n│    Key: "+wait["setkey"].title()+" watercolor on\n│  Drawing Image\n│    Key: "+wait["setkey"].title()+" drawimage [url]\n│    Key: "+wait["setkey"].title()+" drawimage on\n╰──────"
    def kaskus(self,wait):return "╭───「 Kaskus 」─\n│    | Command |  \n│Hot Thread\n│  Key: "+wait["setkey"].title()+" kaskus ht\n│Hot Thread Detail\n│  Key: "+wait["setkey"].title()+" kaskus ht [num]\n╰──────"
    def instagram(self,wait):return "╭───「 Instagram 」─\n│    | Command |  \n│Search Instagram\n│  Key: "+wait["setkey"].title()+" instagram [username]\n│Search Instagram Post\n│  Key: "+wait["setkey"].title()+" instagram [username] [num]\n│Search Instagram Story\n│  Key: "+wait["setkey"].title()+" instastory [username] [num]\n╰──────"
    def youtube(self,wait):return "╭───「 Youtube 」─\n│    | Command |  \n│Search\n│  Key: "+wait["setkey"].title()+" youtube search [query]\n│MP4\n│  Key: "+wait["setkey"].title()+" youtube video [query|num]\n│  Key: "+wait["setkey"].title()+" youtube video [url]\n│Downloader\n│  Key: "+wait["setkey"].title()+" youtube download [query|num]\n│  Key: "+wait["setkey"].title()+" youtube download [url]\n│MP3\n│  Key: "+wait["setkey"].title()+" youtube audio [query|num]\n│  Key: "+wait["setkey"].title()+" youtube audio [url]\n│Info\n│  Key: "+wait["setkey"].title()+" youtube info [query|num]\n│  Key: "+wait["setkey"].title()+" youtube info [url]\n╰──────"
    def media(self,wait):return "╭─「 Media 」─\n│    | Command |  \n│Qur'an\n│  Key: "+wait["setkey"].title()+" qur'an\n│Word\n│  Key: "+wait["setkey"].title()+" word\n│Image\n│  Key: "+wait["setkey"].title()+" image\n│Youtube\n│  Key: "+wait["setkey"].title()+" youtube\n│Music\n│  Key: "+wait["setkey"].title()+" music\n│Instagram\n│  Key: "+wait["setkey"].title()+" instagram\n│Kaskus\n│  Key: "+wait["setkey"].title()+" kaskus\n│Anime\n│  Key: "+wait["setkey"].title()+" anime\n│Webtoon\n│  Key: "+wait["setkey"].title()+" webtoon\n│Meme\n│  Key: "+wait["setkey"].title()+" meme\n╰──────"
    def quran(self,wait):return "╭─「 Qur'an 」─\n│    | Command |  \n│Daftar Surah\n│  key: "+wait["setkey"].title()+" quranlist\n│Get Ayat Surah\n│  key: "+wait["setkey"].title()+" qur'an [numsurah]\n│  key: "+wait["setkey"].title()+" qur'an [numsurah] [1|<|>|-]\n╰──────"
    def webtoon(self,wait):return "╭─「 Webtoon 」─\n│    | Command |  \n│Drama\n│  key: "+wait["setkey"].title()+" webtoon drama\n│  key: "+wait["setkey"].title()+" webtoon drama [num]\n│Fantasi\n│  key: "+wait["setkey"].title()+" webtoon fantasi\n│  key: "+wait["setkey"].title()+" webtoon fantasi [num]\n│Comedy\n│  key: "+wait["setkey"].title()+" webtoon comedy\n│  key: "+wait["setkey"].title()+" webtoon comedy [num]\n│Slice of Life\n│  key: "+wait["setkey"].title()+" webtoon sol\n│  key: "+wait["setkey"].title()+" webtoon sol [num]\n│Romance\n│  key: "+wait["setkey"].title()+" webtoon romance\n│  key: "+wait["setkey"].title()+" webtoon romancethriller [num]\n│Thriller\n│  key: "+wait["setkey"].title()+" webtoon thriller\n│  key: "+wait["setkey"].title()+" webtoon thriller [num]\n│Horror\n│  key: "+wait["setkey"].title()+" webtoon horror\n│  key: "+wait["setkey"].title()+" webtoon horror [num]\n╰──────"
    def anime(self,wait):return "╭─「 Anime 」─\n│    | Command |  \n│Anime List\n│  key: "+wait["setkey"].title()+" anilist\n│  key: "+wait["setkey"].title()+" anilist [num]\n│  key: "+wait["setkey"].title()+" anilist [num] [numepisode]\n│Mangakyo\n│  Cek Page Manga\n│     key: "+wait["setkey"].title()+" mangakyo \n│     key: "+wait["setkey"].title()+" mangakyo page [num]\n╰──────"
    def word(self,wait):return "╭─「 Word 」─\n│    | Command |  \n│Urban\n│  Key: "+wait["setkey"].title()+" urban [query]\n│KBBI\n│  Key: "+wait["setkey"].title()+" kbbi [query]\n│Wikipedia\n│  Key: "+wait["setkey"].title()+" wikipedia [query]\n╰──────"

    def autoreadon(self,wait):return " 「 Auto Read 」\nUsage:"+wait["setkey"]+" autoread on <trigger>\nTrigger:\n1 - Personal\n2 - Group"
    def autoreadoff(self,wait):return " 「 Auto Read 」\nUsage:"+wait["setkey"]+" autoread off <trigger>\nTrigger:\n1 - Personal\n2 - Group"    
    def list(self,wait):return "╭───「 List 」─\n│    | Command |  \n│Group\n│  Key: "+wait["setkey"].title()+" grouplist\n│Square\n│  Key: "+wait["setkey"].title()+" squarelist\n│Sticker\n│  Key: "+wait["setkey"].title()+" list sticker\n│Image\n│  Key: "+wait["setkey"].title()+" list pict\n│WhiteList\n│  Key: "+wait["setkey"].title()+" whitelist\n│BlackList\n│  Key: "+wait["setkey"].title()+" blacklist\n│MimicList\n│  Key: "+wait["setkey"].title()+" mimiclist\n╰──────"
    def group(self,wait):return "╭───「 Group 」─\n│    | Command |  \n│Auto Respon\n│  Key: "+wait["setkey"].title()+" autorespon\n│Welcome Message\n│  Key: "+wait["setkey"].title()+" welcomemsg\n│Leave Message\n│  Key: "+wait["setkey"].title()+" leavemsg\n│Search Contact\n│  Key: "+wait["setkey"].title()+" get group [@]\n│Get Note\n│  Key: "+wait["setkey"].title()+" get note\n│  Key: "+wait["setkey"].title()+" get note [num]\n│Get Album\n│  Key: "+wait["setkey"].title()+" get album\n│  Key: "+wait["setkey"].title()+" get album [1] [<|>|-|num]\n╰──────"
    def friend(self,wait):return "╭───「 Friend 」─\n│    | Command |  \n│List Friends\n│  Key: "+wait["setkey"].title()+" friendlist\n│Del Friend\n│  Key: "+wait["setkey"].title()+" del friend [on|<|>|-|@|num]\n│BlockList\n│  Key: "+wait["setkey"].title()+" blocklist\n│Del Blcok\n│  Key: "+wait["setkey"].title()+" del block [<|>|-|num]\n╰──────"
    def Announcementssa(self,wait):return "╭───「 Announcements 」─\n│    | Command |  \n│Create Announcements\n│  Key: "+wait["setkey"].title()+" announ create lock [text]\n│  Key: "+wait["setkey"].title()+" announ create unlock [text]\n│  Key: "+wait["setkey"].title()+" announ create all [text]\n│Announcements Del\n│  Key: "+wait["setkey"].title()+" announ clear\n│Get Announcements\n│  Key: "+wait["setkey"].title()+" get announ\n│  Key: "+wait["setkey"].title()+" get announ [num]\n╰──────"
    def mykeyoff(self,wait):wait["setkey"] = "";return " 「 Rname 」\nKey has been set to DISABLED♪"
    def mykeyreset(self,wait):wait["setkey"] = "anbot";return " 「 Rname 」\nKey has been set to "+wait["setkey"].title()
    def github(self,wait):return"╭───「 Github 」─\n│    | Command |  \n│Search User\n│  Key: "+wait["setkey"].title()+" github [username]\n│Search User Follower\n│  Key: "+wait["setkey"].title()+" gitfol [username]\n│Search User Repostory\n│  Key: "+wait["setkey"].title()+" gitrepos [username]\n╰──────"
    def profdetail(self,wait):return "╭───「 Profile 」─\n│    | Command |  \n│Change Profile Picture\n│  Key: "+wait["setkey"].title()+" changedp\n│  Key: "+wait["setkey"].title()+" changedp video\n│Change Group Picture\n│  Key: "+wait["setkey"].title()+" changedp group\n│Change Name\n│  Key: "+wait["setkey"].title()+" myname [text]\n│Change Status\n│  Key: "+wait["setkey"].title()+" mybio [enter|text]\n╰──────"
    def broadcast(self,wait):return "╭───「 Broadcast 」─\n│    | Command |  \n│All\n│  Key: "+wait["setkey"].title()+" broadcast 1 [text]\n│Contact\n│  Key: "+wait["setkey"].title()+" broadcast 2 [text]\n│Group\n│  Key: "+wait["setkey"].title()+" broadcast 3 [text]\n╰──────"

    def autjoin(self,wait,msg):
        if wait['autoJoin'] == True:
            msgs=" 「 Auto Join 」\nState: ENABLED♪\nState: "+str(wait["Members"])+" Available join\n"
        else:
            msgs=" 「 Auto Join 」\nState: DISABLED♪\nState: "+str(wait["Members"])+" Available join\n"
        self.sendMessage(msg.to, msgs+"\n  |Command|\n- Autojoin group\n   Usage:"+wait["setkey"]+" autojoin [on|off]\n- Available min join\n   Usage:"+wait["setkey"]+" autojoin set <num>")
    def aborted(self,wait,msg):
        a = ' 「 Abort 」'
        try:
            if wait['talkban']['cvp'] == True:
                wait['talkban']['pict'] = ''
                wait['talkban']['cvp'] = False
        except:
            wait['talkban']['pict'] = ''
            wait['talkban']['cvp'] = False
            a+= '\nChange Profile Video Dibatalkan'
        if wait["Addimage"] == True:
            wait["Addimage"] = False
            a+= '\nAdd Pict Dibatalkan'
        if wait["ChangeDP"] == True:
            wait["ChangeDP"] = False
            a+= '\nChangeDP Dibatalkan'
        if msg.to in wait["setTimess"]:
            wait["setTimess"].remove(msg.to)
            a+= '\nChangeDP Group Dibatalkan'
        return a
    def lyric(self,to,text):
        try:
            r = requests.get("https://api.genius.com/search?q="+text+"&access_token=2j351ColWKXXVxq1PdUNXDYECI2x4zClLyyAJJkrIeX8K7AQ0F-HTmWfG6tNVszO")
            data = r.json()
            hits = data["response"]["hits"][0]["result"]["api_path"]
            title= "\nTitle: "+data["response"]["hits"][0]["result"]["title"].strip()
            oleh = "\nArtis: "+data["response"]["hits"][0]["result"]["primary_artist"]["name"].strip()
            g = data["response"]["hits"][0]["result"]['song_art_image_thumbnail_url']
            r1 = requests.get("https://api.genius.com"+hits+"?&access_token=2j351ColWKXXVxq1PdUNXDYECI2x4zClLyyAJJkrIeX8K7AQ0F-HTmWfG6tNVszO")
            data1 = r1.json()
            path = data1["response"]["song"]["path"]
            release = data1["response"]["song"]["release_date"]
            page_url = "http://genius.com" + path
            page = requests.get(page_url)
            html = BeautifulSoup(page.text, "html.parser")
            [h.extract() for h in html('script')]
            lyrics = html.find("div", class_="lyrics").get_text().strip()
            pesan = " 「 Lyric 」"+title+oleh+'\n'+lyrics
            k = len(pesan)//10000
            for aa in range(k+1):
                self.sendMessage(to,'{}'.format(pesan[aa*10000 : (aa+1)*10000]))
        except:
            self.sendMessage(to,"「 404 」\nStatus: Error\nReason: I'cant found lyric {}".format(text))
    def eksekusilurk(self,op,wait):
        try:
            if op.param1 in wait['readPoint']:
                if op.param2 in wait['ROM1'][op.param1]:
                    wait['setTime'][op.param1][op.param2] = op.createdTime
                else:
                    wait['ROM1'][op.param1][op.param2] = op.param2
                    wait['setTime'][op.param1][op.param2] = op.createdTime
                    try:
                        if wait['lurkauto'] == True:
                            if len(wait['setTime'][op.param1]) % 5 == 0:
                                self.anulurk(op.param1,wait)
                    except:pass
            elif op.param2 in wait['readPoints']:
                wait['lurkt'][op.param1][op.param2][op.param3] = op.createdTime
                wait['lurkp'][op.param1][op.param2][op.param3] = op.param2
            else:pass
        except:
            pass
    def blekedok(self,t:int=None,tt:str=None):
        r = requests.get('https://www.webtoons.com/id/genre')
        soup = BeautifulSoup(r.text,'html5lib')
        data = soup.find_all(class_='card_lst')
        datea = data[t].find_all(class_='info')
        if tt == 'data':
            return datea
        else:
            return data[t].find_all('a')
    def kbbi(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        data = KBBI(self.adityasplittext(msg.text.lower()))
        self.sendMessage(msg.to,'{}'.format(data))
    def wikipedia(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        try:
            wiki = WikiApi({'locale' : 'id'})
            result = wiki.find(self.adityasplittext(msg.text.lower()))
            b = random.randint(0,len(result)-1)
            article = wiki.get_article(result[b])
            a=" 「 Wikipedia 」\nType: Wikipedia Definition\nData: Wikipedia {} #{} from #{}".format(self.adityasplittext(msg.text.lower()),b+1,len(result))
            a+= "\nSummary:\n{}".format(article.summary)
            self.sendMessage(msg.to,a, self.templatefoot(article.url,"http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,self.adityasplittext(msg.text.lower())))
        except:
            self.sendMessage(msg.to," 「 Wikipedia 」\nType: Wikipedia Definition\nData: Wikipedia {} Not Found".format(self.adityasplittext(msg.text.lower())), self.templatefoot('line://ti/p/~{}'.format(self.profile.userid),"http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,self.adityasplittext(msg.text.lower())))
    def urbandata(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        try:
            data = self.adityarequestweb('http://api.urbandictionary.com/v0/define?term={}'.format(self.adityasplittext(msg.text.lower())))
            b = random.randint(0,len(data['list'])-1)
            a=" 「 Urban 」\nType: Urban Definition\nData: Urban {} #{} from #{}".format(self.adityasplittext(msg.text.lower()),b+1,len(data['list']))
            a+= "\nAuthor: {}\nDictionary:\n{}\n\nExample: {}".format(data['list'][b]['author'],data['list'][b]['definition'],data['list'][b]['example'])
            self.sendMessage(msg.to,a, self.templatefoot(data['list'][b]['permalink'],"http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,data['list'][b]['word']))
        except:
            self.sendMessage(msg.to," 「 Urban 」\nType: Urban Definition\nData: Urban {} Not Found".format(self.adityasplittext(msg.text.lower())), self.templatefoot('line://ti/p/~{}'.format(self.profile.userid),"http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,self.adityasplittext(msg.text.lower())))
    def WebtoonDrama(self,msg):
        msg.text = self.mycmd(msg.text,wait)
        drama = msg.text.split(' ')[1].lower()
        try:
            if drama == 'drama':aa = 0
            if drama == 'fantasi':aa = 1
            if drama == 'comedy':aa = 2
            if drama == 'sol':aa = 3
            if drama == 'romance':aa = 4
            if drama == 'thriller':aa = 5
            if drama == 'horror':aa = 6
            a = self.blekedok(aa,'data')
            try:
                if int(msg.text.split(' ')[2]) > len(a):
                    return self.sendMessage(msg.to,' 「 Webtoon 」\nDaftar Webtoon {} urutan ke {} tidak ditemukan'.format(drama.title(),msg.text.split(' ')[2]))
                gd = self.blekedok(aa)[int(msg.text.split(' ')[2])-1].get('href')
                b = requests.get(gd)
                soup1 = BeautifulSoup(b.text,'html5lib')
                data11 = soup1.find_all(class_='subj')
                data1 = soup1.find_all(class_='date')
                data2 = soup1.find_all(id='_listUl')
                data3 = data2[0].find_all('a')
                A = ' 「 Webtoon 」\n    | {} |'.format(a[int(msg.text.split(' ')[2])-1].find_all('p')[0].text)
                for c in range(0,10):
                    if c+1 == 1:AA = '\n'
                    else:AA = '\n\n'
                    A+= '{}{}. {} | {}\n    {}'.format(AA,c+1,data11[c+1].text,data1[c].text.strip(),data3[c].get('href'))
                self.sendMessage(msg.to,A)
            except:
                A = ' 「 Webtoon 」\n    | {} |'.format(drama.replace('sol','slice of life').title())
                no=0
                for b in a:
                    no+=1
                    if no == 1:AA = '\n'
                    else:AA = '\n\n'
                    if len(str(no)) == 1:cdd = '\n     Author: {}'.format(b.find_all('p')[1].text)
                    if len(str(no)) == 2:cdd = '\n      Author: {}'.format(b.find_all('p')[1].text)
                    A+= '{}{}. {} | {} Like{}'.format(AA,no,b.find_all('p')[0].text[:20],b.find_all('p')[2].find_all('em')[0].text,cdd)
                self.sendMessage(msg.to,A)
        except Exception as e:self.sendMessage(msg.to,str(e))
    def albumNamaGrup(self,msg,wait):
        to = msg.to
        ha = self.getGroupAlbum(to)
        msg.text = self.mycmd(msg.text,wait)
        if msg.text.lower() == 'get album':
            a = [a['title'] for a in ha['result']['items']];c=[a['photoCount'] for a in ha['result']['items']]
            b = '╭「 Album Group 」'
            no=0
            for i in range(len(a)):
                no+=1
                if no == len(a):b+= '\n╰{}. {} | {}'.format(no,a[i],c[i])
                else:b+= '\n│{}. {} | {}'.format(no,a[i],c[i])
            self.sendMessage(to,"{}".format(b))
        if msg.text.lower().startswith('get album '):
            a = msg.text.split(' ')
            selection = AdityaSplitGood(a[3],range(1,len(ha['result']['items'])+1))
            for i in selection.parse():
                try:
                    b = random.randint(0,999)
                    self.getImageGroupAlbum(msg.to,ha['result']['items'][int(a[2])-1]['id'], ha['result']['items'][int(a[2])-1]['recentPhotos'][i-1]['oid'], returnAs='path', saveAs='{}.png'.format(b))
                    self.sendImage(msg.to,'{}.png'.format(b))
                    os.remove('{}.png'.format(b))
                except:continue
        else:
            a = msg.text.split(' ')
            if len(a) == 5:
                wait["Images"]['anu']=ha['result']['items'][int(a[4])-1]['id']
                wait['ChangeGDP'] = True
                self.sendMessage(msg.to," 「 Album 」\nSend a Picture for add to album")
    def datamention(self,msg,text,data,ps=''):
        if(data == [] or data == {}):return self.sendMention(msg.to," 「 {} 」\nSorry @! I can't found maybe empty".format(text),text,[msg._from])
        k = len(data)//100
        for aa in range(k+1):
            if aa == 0:dd = '╭「 {} 」─{}'.format(text,ps);no=aa
            else:dd = '├「 {} 」─{}'.format(text,ps);no=aa*100
            msgas = dd
            for i in data[aa*100 : (aa+1)*100]:
                no+=1
                if no == len(data):msgas+='\n╰{}. @!'.format(no)
                else:msgas+='\n│{}. @!'.format(no)
            self.sendMention(msg.to, msgas,' 「 {} 」'.format(text), data[aa*100 : (aa+1)*100])
    def mentionalfl(self,msg,wait):
        msg.text = msg.text = self.mycmd(msg.text,wait)
        if msg.text.lower().startswith('friendlist '):
                if len(msg.text.split(' ')) == 2:
                    a = self.refreshContacts()
                    self.getinformation(msg.to,a[int(msg.text.split(' ')[1])-1],wait)
        if msg.text.lower() == 'friendlist':a = self.refreshContacts();self.datamention(msg,'List Friend',a)
        if msg.text.lower() == 'friend request':
            a = self.getRecommendationIds()
            self.sendMessage(msg.to,'{}'.format(a)[:10000])
        if msg.text.lower() == 'blocklist':a = self.getBlockedRecommendationIds();self.datamention(msg,'List Block',a)
    def datamentions(self,msg,text,data,date,wait,ps=''):
        if(data == [] or data == {}):return self.sendMention(msg.to," 「 {} 」\nSorry @! I can't found maybe empty".format(text),text,[msg._from])
        k = len(data)//100
        for aa in range(k+1):
            if aa == 0:dd = '╭「 {} 」─{}'.format(text,ps);no=aa
            else:dd = '├「 {} 」─{}'.format(text,ps);no=aa*100
            msgas = dd
            for i in data[aa*100 : (aa+1)*100]:
                no+=1
                if date == 'ADDWL':
                    if i in wait["bots"]:a = 'WL User'
                    else:
                        if i not in wait["blacklist"]:a = 'Add WL';wait["bots"].append(i)
                        else:a = 'BL User'
                if date == 'DELWL':
                    try:wait["bots"].remove(i);a = 'Del WL'
                    except:a = 'Not WL User'
                if date == 'ADDBL':
                    if i in wait["bots"]:a = 'WL User'
                    else:
                        if i not in wait["blacklist"]:a = 'Add BL';wait["blacklist"].append(i)
                        else:a = 'BL User'
                if date == 'DELBL':
                    try:wait["blacklist"].remove(i);a = 'Del BL'
                    except:a = 'Not BL User'
                if date == 'DELFL':
                    try:self.AdityadeleteContact(i);a = 'Del Friend'
                    except:a = 'Not Friend User'
                if date == 'ADDML':
                    if i in wait["target"]:a = 'ML User'
                    else:a = 'Add ML';wait["target"].append(i)
                if date == 'DELML':
                    try:wait["target"].remove(i);a = 'Del ML'
                    except:a = 'Not ML User'
                if no == len(data):msgas+='\n╰{}. @!{}'.format(no,a)
                else:msgas+='\n│{}. @!{}'.format(no,a)
            self.sendMention(msg.to, msgas,' 「 {} 」'.format(text), data[aa*100 : (aa+1)*100])
    def ekseuksi(self,wait,msg):
        to = msg.to
        msg.text = self.mycmd(msg.text,wait)
        dits = msg.text.lower()
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            targets = []
            key = eval(msg.contentMetadata["MENTION"])
            key["MENTIONEES"][0]["M"]
            for x in key["MENTIONEES"]:
                targets.append(x["M"])
            if dits.startswith('addbl '):self.datamentions(msg,'Blacklist',targets,'ADDBL',wait,ps='\n├ Type: Add Blacklist')
            elif dits.startswith('delbl '):self.datamentions(msg,'Blacklist',targets,'DELBL',wait,ps='\n├ Type: Delete Blacklist')
            elif dits.startswith('addwl '):self.datamentions(msg,'Whitelist',targets,'ADDWL',wait,ps='\n├ Type: Add Whitelist')
            elif dits.startswith('delwl '):self.datamentions(msg,'Whitelist',targets,'DELWL',wait,ps='\n├ Type: Delete Whitelist')
            elif dits.startswith('addml '):self.datamentions(msg,'Mimiclist',targets,'ADDML',wait,ps='\n├ Type: Add Mimiclist')
            elif dits.startswith('delml '):self.datamentions(msg,'Mimiclist',targets,'DELML',wait,ps='\n├ Type: Delete Mimiclist')
            elif dits.startswith('del friend '):self.datamentions(msg,'Friendlist',targets,'DELFL',wait,ps='\n├ Type: Delete Friendlist')
        else:
            if dits.startswith('delbl '):self.adityaarchi(wait,'Blacklist','delbl',to,self.adityasplittext(msg.text),msg,'\n├ Type: Delete Blacklist',nama=wait['blacklist'])
            if dits.startswith('delwl '):self.adityaarchi(wait,'Whitelist','delwl',to,self.adityasplittext(msg.text),msg,'\n├ Type: Delete Whitelist',nama=wait['bots'])
            if dits.startswith('delml '):self.adityaarchi(wait,'Mimiclist','delml',to,self.adityasplittext(msg.text),msg,'\n├ Type: Delete Mimiclist',nama=wait['target'])
            if dits.startswith('del friend ') or dits == 'del friend on':
                if dits == 'del friend on':return self.adityanuindata(to,'Friendlist',wait["Anime"],'DELFriendlist',wait)
                self.sendMessage(to,' 「 Friendlist 」\nWaiting.....');self.adityaarchi(wait,'Friendlist','delfriend',to,self.adityasplittext(msg.text,'s'),msg,'\n├ Type: Delete Friendlist',nama=self.refreshContacts())
            if dits.startswith('del block '):self.sendMessage(to,' 「 Blocklist 」\nWaiting.....');self.adityaarchi(wait,'Blocklist','delblock',to,self.adityasplittext(msg.text,'s'),msg,'\n├ Type: Delete Blocklist',nama=self.getBlockedRecommendationIds())
    def mentionmention(self,to,wait, text, dataMid=[], pl='', ps='',pg='',pt=[]):
        arr = []
        list_text=ps
        i=0
        no=pl
        if pg == 'MENTIONALLUNSED':
            for l in dataMid:
                no+=1
                if no == len(pt):list_text+='\n╰'+str(no)+'. @[adit-'+str(i)+'] '
                else:list_text+='\n│'+str(no)+'. @[adit-'+str(i)+'] '
                i=i+1
            text=list_text+text
        if pg == 'SIDERMES':
            for l in dataMid:
                chiya = []
            for rom in wait["lurkt"][to][dataMid[0]].items():
                chiya.append(rom[1])
            for b in chiya:
                a = '{}'.format(humanize.naturaltime(datetime.fromtimestamp(b/1000)))
                no+=1
                if no == len(pt):list_text+='\n│'+str(no)+'. @[adit-'+str(i)+']\n╰    「 '+a+" 」"
                else:list_text+='\n│'+str(no)+'. @[adit-'+str(i)+']\n│    「 '+a+" 」"
                i=i+1
            text=list_text+text
        if pg == 'DELML':
            for l in dataMid:
                if l not in wait["target"]:
                    a = 'Not ML User'
                else:
                    a = 'DEL ML'
                    wait["target"].remove(l)
                no+=1
                if no == len(pt):list_text+='\n╰'+str(no)+'. @[adit-'+str(i)+'] '+a
                else:list_text+='\n│'+str(no)+'. @[adit-'+str(i)+'] '+a
                i=i+1
            text=list_text
        i=0
        for l in dataMid:
            mid=l
            name='@[adit-'+str(i)+']'
            ln_text=text.replace('\n',' ')
            if ln_text.find(name):
                line_s=int( ln_text.index(name) )
                line_e=(int(line_s)+int( len(name) ))
            arrData={'S': str(line_s), 'E': str(line_e), 'M': mid}
            arr.append(arrData)
            i=i+1
        contentMetadata={'MENTION':str('{"MENTIONEES":' + json.dumps(arr).replace(' ','') + '}')}
        if pg == 'MENTIONALLUNSED':self.unsendMessage(self.sendMessage(to, text, contentMetadata).id)
        else:self.sendMessage(to, text, contentMetadata)
    def pictlock(self,msg,wait):
            if msg.text.lower().startswith('pict lock '):
                spl = msg.text.lower().replace('pict lock ','')
                if spl == 'on':
                    contact = self.getGroup(msg.to).pictureStatus
                    cu = "http://dl.profile.line-cdn.net/" + contact
                    if msg.to in wait['ppict']:
                        msgs=" 「 Picture Lock 」\nStatus: already ENABLED♪"
                        wait['GN'] = True
                    else:
                        msgs=" 「 Picture Lock 」\nStatus: set to ENABLED♪"
                        wait['ppict'].append(msg.to)
                        wait['GN'] = True
                        wait['pro_pict'][msg.to] = 'dataSeen/'+msg.to+'.png'
                    self.sendMessage(msg.to, msgs)
                    self.sendImageWithURL(msg.to,cu)
                if spl == 'off':
                    if msg.to in wait['ppict']:
                        msgs=" 「 Picture Lock 」\nStatus: set to DISABLED♪"
                        wait['ppict'].remove(msg.to)
                    else:
                        msgs=" 「 Picture Lock 」\nStatus: already DISABLED♪"
                    self.sendMessage(msg.to, msgs)
    def adityanuindata(self,to,text,data,pl,wait):
        if 'ADDWhitelist' in pl:
            wait["wwhitelist"] = True
            b = " 「 {} 」\nType: Add {}\nStatus: Turned ON\nSend a contact to add into {}♪".format(text,text,text)
        if 'ADDBlacklist' in pl:
            wait["wblacklist"] = True
            b = " 「 {} 」\nType: Add {}\nStatus: Turned ON\nSend a contact to add into {}♪".format(text,text,text)
        if 'DELWhitelist' in pl:
            wait["dwhitelist"] = True
            b = " 「 {} 」\nType: Delete {}\nStatus: Turned ON\nSend a contact to delete from {}♪".format(text,text,text)
        if 'DELBlacklist' in pl:
            wait["dblacklist"] = True
            b = " 「 {} 」\nType: Delete {}\nStatus: Turned ON\nSend a contact to delete from {}♪".format(text,text,text)
        if 'DELFriendlist' in pl:
            wait["Anime"] = True
            b = " 「 {} 」\nType: Delete {}\nStatus: Turned ON\nSend a contact to delete from {}♪".format(text,text,text)
        self.sendMessage(to,b)
    def changedpgroup(self,wait,msg):
        if msg.toType == 2:
            if msg.to not in wait["setTimess"]:
                wait["setTimess"].append(msg.to)
            self.sendMessage(msg.to, " 「 Group 」\nType: Change Cover Group\nStatus: Send the image....")
    def spam(self,wait):return "╭───「 Spam 」─\n│    | Command |  \n│Message\n│  Key: "+wait["setkey"].title()+"spam 1 [1][enter|text]\n│Gift\n│  Key: "+wait["setkey"].title()+"spam 2 [1][@|]\n│Contact\n│  Key: "+wait["setkey"].title()+"spam 3 [1][@]\n│Tag\n│  Key: "+wait["setkey"].title()+"spam 4 [1][@]\n╰──────"
    def mykey(self,wait):
        if wait["setkey"] == '':return "Your Key: DISABLED♪\nRname set - Set Your Key\nRname off - Disable Your Key\nRname reset - Reset Your Key"
        else:return "Your Key: " + wait["setkey"].title() + "\nRname: - Set Your Key\nRname Off - Disable Your Key\nRname Reset - Reset Your Key"
    def getid(self,wait,msg,dits):
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            key = eval(msg.contentMetadata["MENTION"])
            key1 = key["MENTIONEES"][0]["M"]
            self.getinformation(msg.to,key1,wait)
        else:
            if dits.startswith("getid"):
                if len(dits.split(' ')) == 2:
                    a = self.getGroupIdsJoined()
                    self.getinformation(msg.to,a[int(dits.split(' ')[1])-1],wait)
            if dits == 'getid':self.getinformation(msg.to,msg.to,wait)
    def stealcover(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        if msg.text.lower().startswith('steal cover') or msg.text.lower() == 'steal cover' or msg.text.lower() == 'my cover':
            if 'MENTION' in msg.contentMetadata.keys()!=None:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                self.sendImageWithURL(msg.to,'{}'.format(self.getProfileCoverURL(key1)),'Cover Picture')
            else:
                if msg.text.lower() == 'my cover':
                    self.sendImageWithURL(msg.to,'{}'.format(self.getProfileCoverURL(msg._from)),'Cover Picture')
                if msg.text.lower() == 'steal cover':
                    if msg.toType == 2:
                        return
                    self.sendImageWithURL(msg.to,'{}'.format(self.getProfileCoverURL(msg.to)),'Cover Picture')
    def stealpp(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        if msg.text.lower().startswith('steal pp') or msg.text.lower() == 'steal pp' or msg.text.lower() == 'my pp':
            if 'MENTION' in msg.contentMetadata.keys()!=None:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                try:contact = self.getGroup(key1)
                except:contact = self.getContact(key1)
                try:
                    cu = "http://dl.profile.line.naver.jp"+ contact.picturePath + "/vp"
                    self.sendVideoWithURL(msg.to,cu)
                    cu = "http://dl.profile.line.naver.jp" + contact.picturePath
                    self.sendImageWithURL(msg.to,cu,'{} Picture'.format(contact.displayName))
                except:
                    cu = "http://dl.profile.line.naver.jp" + contact.picturePath
                    self.sendImageWithURL(msg.to,cu,'{} Picture'.format(contact.displayName))
            else:
                if msg.text.lower() == 'steal pp':to = msg.to
                if msg.text.lower() == 'my pp':to = msg._from
                if msg.toType == 2:contact = self.getGroup(to);pppp = contact.name
                else:contact = self.getContact(to);pppp = contact.displayName
                try:
                    cu = "http://dl.profile.line.naver.jp"+ contact.picturePath + "/vp"
                    self.sendVideoWithURL(msg.to,cu)
                except:
                    cu = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    self.sendImageWithURL(msg.to,cu,'{} Picture'.format(pppp))
    def mayhem(self,msg):
        a = []
        b = self.getGroup(msg.to)
        for i in b.members:
            if i.mid not in wait["bots"]:
                a.append(i.mid)
        self.sendMessage(msg.to," 「 Mayhem 」\nMayhem is STARTING♪\n'abort' to abort♪""")
        self.sendMessage(msg.to," 「 Mayhem 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(a))
        for c in a:
            self.kickoutFromGroup(msg.to,[c])
    def sendMessages(self, messageObject):
        return self.talk.sendMessage(0, messageObject)
    def AdityaWeather(self,msg):
        msg.text = self.mycmd(msg.text,wait)
        ts = self.adityasplittext(msg.text)
        t = msg.to
        try:
            data = self.adityarequestweb("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{}%2C%20id%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys".format(ts))
            wloc = data['query']['results']['channel']['location']
            wlocs = data['query']['results']['channel']['item']['condition']
            wlocss = data['query']['results']['channel']['wind']
            wlocsss = data['query']['results']['channel']['atmosphere']
            b = float(data['query']['results']['channel']['item']['lat'])
            h = float(data['query']['results']['channel']['item']['long'])
            a = '🔭 Prakiraan Cuaca\n{},{} {}\n\nTemperatur {} \u00b0C {}\nRange 22 sd 28 \u00b0C\nAngin {}.{} km/h\nDengan Arah {}\u00b0\nKelembapan {}%\n\n🗓 {}'.format(wloc['city'],wloc['region'],wloc['country'],wlocs['code'],wlocs['text'],wlocss['speed'],wlocss['chill'],wlocss['direction'],wlocsss['humidity'],data['query']['results']['channel']['lastBuildDate'])
            self.sendMessage(t,a)
            msgs = Message()
            msgs.to = msg.to
            msgs.location=Location(longitude=h, address='{}.{} {}'.format(wloc['city'],wloc['region'],wloc['country']), title=' 「 Location 」', phone=None, latitude=b)
            self.sendMessages(msgs)
        except:
            return self.sendMessage(t, "Lokasi Tidak Ditemukan")
    def lurk(self,to,data):
        wait = data
        if 'lurkauto' not in wait:wait['lurkauto'] = False
        if wait['lurkauto'] == False:sd = "\n│Lurk Auto: OFF"
        else:sd = "\n│Lurk Auto: ON"
        if to in data['readPoint']:
            a = "\n│Lurk State: ON"+sd
        else:
            a = "\n│Lurk State: OFF"+sd
        if to in data["lurkp"]:
            if data["lurkp"][to] == {}:
                b='\n╰Lurk People: None'
                h="╭「 Lurk 」─"+a+"\n│    | Command |  \n│Lurtk Point\n│  Key: "+data["setkey"].title()+" lurk on\n│  Key: "+data["setkey"].title()+" lurk auto on\n│Lurk Del\n│  Key: "+data["setkey"].title()+" lurk off\n│  Key: "+data["setkey"].title()+" lurk auto off\n│Lurk Cek\n│  Key: "+data["setkey"].title()+" lurk result"
                self.sendMessage(to,h+b)
            else:
                h= "╭「 Lurk 」─"+a+"\n│    | Command |  \n│Lurk Point\n│  Key: "+data["setkey"].title()+" lurk on\n│  Key: "+data["setkey"].title()+" lurk auto on\n│Lurk Del\n│  Key: "+data["setkey"].title()+" lurk off\n│  Key: "+data["setkey"].title()+" lurk auto off\n│Lurk Cek\n│  Key: "+data["setkey"].title()+" lurk result\n│Lurk People: {}".format(len(data["lurkp"][to]))
                no=0
                hh = []
                for c in data["lurkp"][to]:
                    no+=1
                    hh.append(c)
                    if no == len(data["lurkp"][to]):h+= '\n╰ {}. @!'.format(no)
                    else:h+= '\n│ {}. @!'.format(no)
                self.sendMention(to,h,'',hh)
        else:
            b='\n╰Lurk People: None'
            h="╭「 Lurk 」─"+a+"\n│    | Command |  \n│Lurk Point\n│  Key: "+data["setkey"].title()+" lurk on\n│  Key: "+data["setkey"].title()+" lurk auto on\n│Lurk Del\n│  Key: "+data["setkey"].title()+" lurk off\n│  Key: "+data["setkey"].title()+" lurk auto off\n│Lurk Cek\n│  Key: "+data["setkey"].title()+" lurk result"
            self.sendMessage(to,h+b)
    def animeget(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        r = requests.get('https://www.kurogaze.top/ongoing-anime/')
        s = BeautifulSoup(r.text,'html5lib')
        dd = s.select('ul > li > div.sera > a.series')
        sgd = s.select('ul > li > div.sera > a.series > div.title > span')
        if msg.text.lower().startswith('anilist'):
            if len(msg.text.split(' ')) == 1:
                d = '╭「 Anime List 」'
                no = 0
                for c in sgd:
                    no+=1
                    if no == len(sgd):sdk = '╰'
                    else:sdk = '│'
                    d+= '\n{}{}. {}'.format(sdk,no,c.text.replace('no Imouto','no\n│    Imouto').replace('– Kaikou','–\n│      Kaikou').replace('Gale Online','Gale\n│      Online').replace('Genwaku Kitan','Genwaku\n│      Kitan').replace('Izakaya Nobu','Izakaya\n│      Nobu').replace('no Monogatari','no\n│      Monogatari'))
                self.sendMessage(msg.to,'{}'.format(d))
            if len(msg.text.split(' ')) == 2:
                ds = dd[int(msg.text.split(' ')[1])-1]
                sgd = sgd[int(msg.text.split(' ')[1])-1]
                self.sendMessage(msg.to,' 「 Anime 」\nStatus: Waiting....\nRequest: Get a {}'.format(sgd.text))
                r = requests.get(ds.get('href'))
                s = BeautifulSoup(r.text,'html5lib')
                dd = s.select('div.episodelist > ul > li > span.t1 > a')
                ddd = s.select('div.episodelist > ul > li > span.t2')
                d = ' 「 Epsiode List 」\n  | Anime {} |'.format(sgd.text)
                no = 0
                dd = [c.text.strip() for c in dd];dd.reverse()
                ddd = [c.text.strip() for c in ddd];ddd.reverse()
                for c in range(0,len(dd)):
                    no+=1
                    d+= '\n{}. {} | {}'.format(no,dd[c],ddd[c])
                self.sendMessage(msg.to,d)
            if len(msg.text.split(' ')) == 3:
                ds = dd[int(msg.text.split(' ')[1])-1]
                sgd = sgd[int(msg.text.split(' ')[1])-1]
                self.sendMessage(msg.to,' 「 Anime 」\nStatus: Waiting....\nRequest: Get a {}\nTarget: {}'.format(sgd.text,msg.text.split(' ')[2]))
                r = requests.get(ds.get('href'))
                s = BeautifulSoup(r.text,'html5lib')
                dd = s.select('div.episodelist > ul > li > span.t3 > a')
                dd = [c.get('href') for c in dd]
                dd.reverse()
                ds = dd[int(msg.text.split(' ')[2])-1]
                r = requests.get(ds)
                s = BeautifulSoup(r.text,'html5lib')
                try:
                    try:
                        sdd = s.select('div.thumbnail')[0].find('img')['data-lazy-src']
                        self.sendImageWithURL(msg.to,sdd,'Anime')
                    except:
                        pass
                    sd = s.select('div.dl-box > div > a')
                    ggg = " 「 {} 」".format(s.select('div.headpost > h1.title')[0].text)
                    h = [self.google_url_shorten(a.get('href')) for a in sd if a.text == 'GDrive']
                    ggg+= '\n{}\n\n{}\n\n   | Downloader |\n    1. 240P {}\n    2. 360P {}\n    3. 480P {}\n    4. 720P {}'.format(s.select('div.singlecontent > p')[0].text,s.select('div.singlecontent > p')[1].text.replace('Genres','\nGenres').replace('Credit','\nCredit'),h[0],h[1],h[2],h[3])
                    self.sendMessage(msg.to,ggg)
                except:self.sendMessage(msg.to," 「 404 」\nStatus: Error So sorry I'cant Find a Video or maybe this episode hasbeen del")
    def google_url_shorten(self,url):
        req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
        payload = {'longUrl': url}
        headers = {'content-type': 'application/json'}
        r = requests.post(req_url, data=json.dumps(payload), headers=headers)
        resp = json.loads(r.text)
        return resp['id'].replace("https://","")
    def kaskusget(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        kaskus = Kaskus()
        if msg.text.lower().startswith('kaskus ht'):
            h = kaskus.getHotThreads()
            if len(msg.text.split(' ')) == 2:
                d = ' 「 Kaskus Hot Thread 」'
                no = 0
                for c in h.data:
                    no+=1
                    d+= '\n{}. {}'.format(no,c.title)
                self.sendMessage(msg.to,d)
            if len(msg.text.split(' ')) == 3:
                d = h.data[int(msg.text.split(' ')[2])-1]
                r = requests.get(d.short_url)
                s = BeautifulSoup(r.text,'html5lib')
                sd = s.find_all('span',{'data-attr':'size'})
                tt = ''
                for a in sd:
                    if a == sd[0]:tt+= ''+a.text
                    else:tt+= '\n\n'+a.text
                self.sendMessage(msg.to,'{}....'.format(tt[:2996].strip()), self.templatefoot(str(d.short_url),'https://lh3.googleusercontent.com/MJjKnEPXaCF9FCEILJGvShuPnrw1yMt1yAZgBMiD7J3EvmXvmzFYatAsXlvSWhstNw',str(d.title)))
                try:self.sendImageWithURL(msg.to,d.image,'Kaskus')
                except:pass
    def lurkoff(self,to,wait,msg):
        msg.text = self.mycmd(msg.text,wait)
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            key = eval(msg.contentMetadata["MENTION"])
            targets = key["MENTIONEES"][0]["M"]
            if targets not in wait['readPoints']:
                self.sendMention(to, " 「 Lurk 」\nLurk in @! already mute",'',[targets])
            else:
                try:
                    del wait['readPoints'][targets];wait['lurkt'][to]  = {};wait['lurkp'][to] = {}
                except:
                    pass
                self.sendMention(to, " 「 Lurk 」\nLurk in @! set to mute",'',[targets])
        else:
            if msg.text.lower() == "lurk off":
                if msg.to not in wait['readPoint']:
                    self.sendMessage(to, " 「 Lurk 」\nLurk already off♪")
                else:
                    try:
                       del wait['readPoint'][to];wait['setTime'][to] = {};wait['ROM1'][to] = {}
                    except:
                       pass
                    self.sendMessage(to, " 「 Lurk 」\nLurk point off♪")
    def lurkon(self,to,wait,msg):
        msg.text = self.mycmd(msg.text,wait)
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            key = eval(msg.contentMetadata["MENTION"])
            targets = key["MENTIONEES"][0]["M"]
            if targets in wait['readPoints']:
                self.sendMention(to, " 「 Lurk 」\nLurk in @! already active",'',[targets])
            else:
                try:
                    del wait['readPoints'][targets];del wait['lurkt'][to];del wait['lurkp'][to][targets]
                except:
                    pass
                wait['readPoints'][targets] = msg.id
                if to not in wait['lurkt']:
                    wait['lurkt'][to]  = {}
                    wait['lurkp'][to] = {}
                if targets not in wait['lurkp'][to]:
                    wait['lurkp'][to][targets] = {}
                    wait['lurkt'][to][targets] = {}
                self.sendMention(to, " 「 Lurk 」\nLurk in @! set to active",'',[targets])
        else:
            if msg.text.lower() == "lurk on":
                if to in wait['readPoint']:
                    self.sendMessage(to, " 「 Lurk 」\nLurk already set♪")
                else:
                    try:
                        del wait['readPoint'][to];del wait['setTime'][to]
                    except:
                        pass
                    wait['readPoint'][to] = msg.id;wait['setTime'][to]  = {};wait['ROM1'][to] = {}
                    self.sendMessage(to, " 「 Lurk 」\nLurk point set♪")
    def lurkauto(self,to,wait,msg):
            msg.text = self.mycmd(msg.text,wait)
            if msg.text.lower() == "lurk auto off":
                if wait['lurkauto'] == False:
                    self.sendMessage(to, " 「 Lurk 」\nLurk auto already off♪")
                else:
                    wait['lurkauto'] = False
                    self.sendMessage(to, " 「 Lurk 」\nLurk auto point off♪")
            if msg.text.lower() == "lurk auto on":
                if to in wait['readPoint']:
                    if wait['lurkauto'] == True:self.sendMessage(to, " 「 Lurk 」\nLurk already set♪")
                else:
                    try:
                        del wait['readPoint'][to];del wait['setTime'][to]
                    except:
                        pass
                    wait['readPoint'][to] = msg.id;wait['setTime'][to]  = {};wait['ROM1'][to] = {}
                    wait['lurkauto'] = True
                    self.sendMessage(to, " 「 Lurk 」\nLurk point set♪")
    def cekmention(self,to,wait):
        if to in wait['ROM']:
            moneys = {}
            msgas = ''
            for a in wait['ROM'][to].items():
                moneys[a[0]] = [a[1]['msg.id'],a[1]['waktu']] if a[1] is not None else idnya
            sort = sorted(moneys)
            sort.reverse()
            sort = sort[0:]
            msgas = ' 「 Mention Me 」'
            h = []
            no = 0
            for m in sort:
                has = ''
                nol = -1
                for kucing in moneys[m][0]:
                    nol+=1
                    has+= '\nline://nv/chatMsg?chatId={}&messageId={} {}'.format(to,kucing,humanize.naturaltime(datetime.fromtimestamp(moneys[m][1][nol]/1000)))
                h.append(m)
                no+=1
                if m == sort[0]:
                    msgas+= '\n{}. @!{}x{}'.format(no,len(moneys[m][0]),has)
                else:
                    msgas+= '\n\n{}. @!{}x{}'.format(no,len(moneys[m][0]),has)
            self.sendMention(to, msgas,'', h)
            del wait['ROM'][to]
        else:
            try:
                msgas = 'Sorry @!In {} nothink get a mention'.format(self.getGroup(to).name)
                self.sendMention(to, msgas,' 「 Mention Me 」\n', [self.getProfile().mid])
            except:
                msgas = 'Sorry @!In Chat @!nothink get a mention'
                self.sendMention(to, msgas,' 「 Mention Me 」\n', [self.getProfile().mid,to])
    def adityasuperdata(self,msg,wait,text='',text1='',data=[]):
        to = msg.to
        key = wait["setkey"].title()
        if data == []:return self.sendMessage(to, "╭───「 {} 」─\n│{}: None\n│    | Command |  \n│Add {}\n│  Key:{} add{} [@|on]\n│Del {}\n│  Key:{} del{} [@|on|>|<|num 1]\n╰──────".format(text,text,text,key,text1,text,key,text1,key,text1))
        self.datamention(msg,'{}'.format(text),data)
    def lurkr(self,to,wait,msg):
        msg.text = self.mycmd(msg.text,wait)
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            key = eval(msg.contentMetadata["MENTION"])
            targets = key["MENTIONEES"][0]["M"]
            if targets in wait['readPoints']:
                chiya = []
                for rom in wait["lurkp"][to][targets].items():
                    chiya.append(rom[1])
                k = len(chiya)//100
                for a in range(k+1):
                    if a == 0:self.mentionmention(to=to,wait=wait,text='',dataMid=chiya[:100],pl=0,ps='╭「 Lurkers 」─',pg='SIDERMES',pt=chiya)
                    else:self.mentionmention(to=to,wait=wait,text='',dataMid=chiya[a*100 : (a+1)*100],pl=a*100,ps='├「 Lurkers 」─',pg='SIDERMES',pt=chiya)
                wait['lurkt'][to][targets]  = {};wait['lurkp'][to][targets] = {}
            else:self.sendMention(to, " 「 Lurk 」\nLurk in @! not active",'',[targets])
        else:
            if msg.text.lower() == "lurk result":
                if to in wait['readPoint']:
                    try:
                        self.anulurk(to,wait)
                        wait['setTime'][to]  = {}
                    except:self.sendMessage(to,'╭「 Lurkers 」─\n╰ None')
                else:self.sendMessage(to, " 「 Lurk 」\nLurk point not on♪")
    def anulurk(self,to,wait):
        moneys = {}
        for a in wait["setTime"][to].items():
            moneys[a[1]] = [a[0]] if a[1] is not None else idnya
        sort = sorted(moneys)
        sort = sort[0:]
        k = len(sort)//100
        for a in range(k+1):
            if a == 0:no= a;msgas = '╭「 Lurkers 」─'
            else:no = a*100;msgas = '├「 Lurkers 」─'
            h = []
            for i in sort[a*100 : (a+1)*100]:
                h.append(moneys[i][0])
                no+=1
                a = '{}'.format(humanize.naturaltime(datetime.fromtimestamp(i/1000)))
                if no == len(sort):msgas+='\n│{}. @!\n╰    「 {} 」'.format(no,a)
                else:msgas+='\n│{}. @!\n│    「 {} 」'.format(no,a)
            self.sendMention(to, msgas,'', h)
    def autoaddmsgset(self,wait,msg):
        msg.text = self.mycmd(msg.text,wait)
        if len(msg.text.split("\n")) >= 2:
            wait["autoaddpesan"] = msg.text.replace(msg.text.split("\n")[0]+"\n","").replace('|','@!')
            self.sendMessage(msg.to," 「 Auto Add 」\nAuto add message has been set to:\n" + wait["autoaddpesan"])
    def autoaddoff(self,wait):
        if wait['autoAdd'] == False:
            msgs=" 「 Auto Add 」\nAuto Add already DISABLED♪\nNote: Auto add message is not affected♪"
        else:
            msgs=" 「 Auto Add 」\nAuto Add set to DISABLED♪\nNote: Auto add message is not affected♪"
            wait['autoAdd']=False
        return msgs
    def autoaddon(self,wait):
        if wait['autoAdd'] == True:
            msgs=" 「 Auto Add 」\nAuto Add already Enable♪\nNote: Auto add message is not affected♪"
        else:
            msgs=" 「 Auto Add 」\nAuto Add set to Enable♪\nNote: Auto add message is not affected♪"
            wait['autoAdd']=True
        return msgs
    def autoresponoff(self,wait,msg):
        if msg.to not in wait["GROUP"]['AR']['AP']:
            msgs=" 「 Auto Respon 」\nAuto Respon already DISABLED♪"
        else:
            msgs=" 「 Auto Respon 」\nAuto Respon set to DISABLED♪"
            wait["GROUP"]['AR']['AP'].remove(msg.to)
        return msgs
    def autoresponmsgclear(self,wait,msg):
        autorespon = wait["GROUP"]['AR']['P'][msg.to]
        msgs=" 「 Auto Respon 」\nAuto Respon DISABLED♪\nMessage backup:"
        msgs+="\n" + autorespon
        wait["GROUP"]['AR']['P'][msg.to] = ""
        return msgs
    def autoresponon(self,wait,msg):
        if msg.to in wait["GROUP"]['AR']['AP']:
            msgs=" 「 Auto Respon 」\nAuto Respon already ENABLED♪"
        else:
            msgs=" 「 Auto Respon 」\nAuto Respon set to ENABLED♪"
            wait["GROUP"]['AR']['AP'].append(msg.to)
        return msgs
    def autoresponmsgset(self,wait,msg):
        msg.text = self.mycmd(msg.text,wait)
        if len(msg.text.split("\n")) >= 2:
            wait["GROUP"]['AR']['P'][msg.to] = msg.text.replace(msg.text.split("\n")[0]+"\n","")
            self.sendMessage(msg.to," 「 Auto Respon 」\nAuto Respon message has been set to:\n" + wait["GROUP"]['AR']['P'][msg.to])
    def autorespon(self,wait,msg):
        if msg.to in wait["GROUP"]['AR']['AP']:
            msgs=" 「 Auto Respon 」\nAuto Respon: ON♪"
            if msg.to in wait["GROUP"]['AR']['S']:
                a = self.shop.getProduct(packageID=int(wait["GROUP"]['AR']['S'][msg.to]['Sticker']['STKPKGID']), language='ID', country='ID')
                msgs+="\nSticker: " + a.title
            else:msgs+=''
            if msg.to in wait["GROUP"]['AR']['P']:
                if wait["GROUP"]['AR']['P'][msg.to] == '':msgs+= ''
                else:msgs+="\nMessage: \n" + wait["GROUP"]['AR']['P'][msg.to] + "\n"
            else:msgs+=''
        else:
            msgs=" 「 Auto Respon 」\nAuto Respon: OFF"
            if msg.to in wait["GROUP"]['AR']['S']:
                a = self.shop.getProduct(packageID=int(wait["GROUP"]['AR']['S'][msg.to]['Sticker']['STKPKGID']), language='ID', country='ID')
                msgs+="\nSticker: " + a.title
            else:msgs+=''
            if msg.to in wait["GROUP"]['AR']['P']:
                if wait["GROUP"]['AR']['P'][msg.to] == '':msgs+= ''
                else:msgs+="\nMessage: \n" + wait["GROUP"]['AR']['P'][msg.to] + "\n"
            else:msgs+=''
        return msgs+"\n  |Command|\n- AutoRespon Set\n   Usage:"+wait["setkey"].title()+" autorespon [on|off]\n- AutoRespon Sticker\n   Usage:"+wait["setkey"].title()+" add stickerauto respon\n- autorespon msg setting\n   Usage:"+wait["setkey"].title()+" autorespon msg set <text>\n   OR:"+wait["setkey"].title()+" autorespon msg set <text|text>"
    def autoaddmsgclear(self,wait):
        autoadd = wait["autoaddpesan"]
        msgs=" 「 Auto Add 」\nAuto add message DISABLED♪\nMessage backup:"
        msgs+="\n" + autoadd
        wait["autoaddpesan"] = ""
        return msgs
    def fancynameon(self,msg,wait,sdg):
        msg.text = self.mycmd(msg.text,wait)
        wait['talkban'] = {'time':time.time(),'timer':int(self.adityasplittext(msg.text.lower(),'s')),'cvp':False,'video':'','pict':''}
        if 'name' not in wait['talkban']:wait['talkban']['name'] = sdg
        if wait['ChangeCover'] == True:
            msgs=" 「 Fancy Name 」\nFancy Name already ENABLED With Timer {}sec♪".format(wait['talkban']['timer'])
        else:
            msgs=" 「 Fancy Name 」\nFancy Name set to ENABLED With Timer {}sec♪".format(wait['talkban']['timer'])
            wait['ChangeCover']=True
        return msgs
    def fancynameoff(self,wait):
        if wait['ChangeCover'] == False:
            msgs=" 「 Fancy Name 」\nFancy Name already DISABLE♪"
        else:
            msgs=" 「 Fancy Name 」\nFancy Name set to DISABLE♪"
            wait['ChangeCover']=False
            wait['talkban'] = {'time':time.time(),'timer':wait['talkban']['timer'],'cvp':False,'video':'','pict':'','name':wait['talkban']['name']}
            self.updateProfileAttribute(2, wait['talkban']['name'])
        return msgs
    def autoadd(self,wait):
        if wait['autoAdd'] == True:
            if wait["autoaddpesan"] == '':
                msgs=" 「 Auto Add 」\nAdd Back: True♪\nAdd Message: False♪\n\n\n"
            else:
                msgs=" 「 Auto Add 」\nAdd Back: True♪\nAdd Message: True♪"
                msgs+="\n" + wait['autoaddpesan'] + "\n\n"
        else:
            if wait["autoaddpesan"] == '':
                msgs=" 「 Auto Add 」\nAdd Back: False♪\nAdd Message: False♪\n\n\n"
            else:
                msgs=" 「 Auto Add 」\nAdd Back: False♪\nAdd Message: True♪"
                msgs+="\n" + wait['autoaddpesan'] + "\n"
        return msgs+"\n  |Command|\n- Autoadd friend\n   Usage:"+wait["setkey"].title()+" autoadd [on|off]\n- Autoadd msg setting\n   Usage:"+wait["setkey"].title()+" autoadd msg set <text>\n   OR:"+wait["setkey"].title()+" autoadd msg set <text|text>"
    def anugrupinvitti(self,op,wait,waita,sdd):
        if self.getProfile().mid in op.param3 and waita["name"][sdd]["pay"] >= time.time():
            G = self.getCompactGroup(op.param1)
            if wait["autoJoin"] == True:
                if len(G.members) <= wait["Members"]:
                    self.rejectGroupInvitation(op.param1)
                else:
                    self.acceptGroupInvitation(op.param1)
            if len(G.members) <= wait["Members"]:
                self.rejectGroupInvitation(op.param1)
        else:
            if op.param1 in wait['kitsuneshare']:
                group = self.getCompactGroup(op.param1)
                gMembMids = [contact.mid for contact in group.invitee]
                for _mid in gMembMids:
                    if _mid in op.param3:
                        self.cancelGroupInvitation(op.param1,[_mid])
                    else:pass
    def waktunjir(self):
        sd = ''
        if datetime.now().hour > 1 and datetime.now().hour <10:sd+= 'Good Morning'
        if datetime.now().hour > 10 and datetime.now().hour <15:sd+= 'Good Afternoon'
        if datetime.now().hour > 15 and datetime.now().hour <18:sd+= 'Good Evening'
        if datetime.now().hour >= 18:sd+= 'Good Night'
        return sd
    def anuaccgroup(self,op,wait,waita,sdd):
        if op.param1 in wait["GROUP"]['WM']['AP'] and waita["name"][sdd]["pay"] >= time.time():
            if op.param1 in wait["GROUP"]['WM']['S']:
                self.sendMessage(op.param1,text=None,contentMetadata=wait["GROUP"]['WM']['S'][op.param1]['Sticker'], contentType=7)
            if(wait["GROUP"]['WM']['P'][op.param1] in [""," ","\n",None]):
                return
            if '@!' not in wait["GROUP"]['WM']['P'][op.param1]:
                wait["GROUP"]['WM']['P'][op.param1] = '@!'+wait["GROUP"]['WM']['P'][op.param1]
            nama = self.getGroup(op.param1).name
            sd = self.waktunjir()
            self.sendMention(op.param1,wait["GROUP"]['WM']['P'][op.param1].replace('greeting',sd).replace('Greeting',sd).replace(';',nama),' 「 Welcome Message 」\n',[op.param2]*wait["GROUP"]['WM']['P'][op.param1].count('@!'))
    def anualeavegroup(self,op,wait,waita,sdd):
        if op.param1 in wait["GROUP"]['LM']['AP'] and waita["name"][sdd]["pay"] >= time.time():
            if op.param1 in wait["GROUP"]['LM']['S']:
                self.sendMessage(op.param2,text=None,contentMetadata=wait["GROUP"]['LM']['S'][op.param1]['Sticker'], contentType=7)
            self.sendMention(op.param2, "{}".format(wait["GROUP"]['LM']['P'][op.param1].replace('|',' @!')),' 「 Leave Detect 」\n',[op.param2])
    def sendstickers(self,msg):
        msg.text = self.mycmd(msg.text,wait)
        if len(msg.text.split(" ")) >= 2:
            self.sendall(msg.to,self.adityasplittext(msg.text,'s'))
    def setbroadcast(self,wait,msg):
        msg.text = self.mycmd(msg.text,wait)
        if msg.text.lower().startswith('broadcast 3'):
            if len(msg.text.split("\n")) >= 2:
                a = self.getGroupIdsJoined()
                for i in a:
                    G = self.getGroup(i)
                    if len(G.members) > wait["Members"]:
                        self.sendMessage(i,msg.text.replace(msg.text.split("\n")[0]+"\n",""))
        if msg.text.lower().startswith('broadcast 2'):
            if len(msg.text.split("\n")) >= 2:
                a = self.getAllContactIds()
                for i in a:
                    self.sendMessage(i,msg.text.replace(msg.text.split("\n")[0]+"\n",""))
        if msg.text.lower().startswith('broadcast 1'):
            if len(msg.text.split("\n")) >= 2:
                a = self.getGroupIdsJoined()
                for i in a:
                    G = self.getGroup(i)
                    if len(G.members) > wait["Members"]:
                        self.sendMessage(i,msg.text.replace(msg.text.split("\n")[0]+"\n",""))
                a = self.getAllContactIds()
                for i in a:
                    self.sendMessage(i,msg.text.replace(msg.text.split("\n")[0]+"\n",""))
    def setname(self,to,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        profile = self.getProfile()
        if len(msg.text.split(" ")) <= 2 or len(msg.text.split("\n")) <= 1:self.sendMention(to,'@!','',[self.getProfile().mid])
        if len(msg.text.split("\n")) >= 2:
            profiles = self.getProfile()
            profile = self.getProfile()
            profile.displayName = msg.text.replace(msg.text.split("\n")[0]+"\n","")
            wait['talkban']['name'] = profile.displayName
            self.updateProfileAttribute(2, profile.displayName)
            self.sendMessage(to," 「 Profile 」\nType: Change Display Name\nStatus: Success\nFrom: "+profiles.displayName+"\nTo: "+profile.displayName)
    def setfancy(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        wait['timeline'] = []
        wait['timeline'] = msg.text.split("\n")[1:]
        d = ' 「 Fancy Name 」\nFancy Name Set to:'
        for a in wait['timeline']:
            d+= '\n{}'.format(a)
        self.sendMessage(msg.to,'{}'.format(d))
    def setbio(self,to,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        profile = self.getProfile()
        if len(msg.text.split(" ")) <= 2 or len(msg.text.split("\n")) <= 1:self.sendMessage(to,profile.statusMessage)
        if len(msg.text.split("\n")) >= 2:
            profile.statusMessage = msg.text.replace(msg.text.split("\n")[0]+"\n","")
            self.updateProfileAttribute(16, profile.statusMessage)
            self.sendMessage(to," 「 Profile 」\nType: Change a status message\n" + profile.statusMessage+"\nStatus: Success change status message")
    def adityaarchi(self,wait,sd,dd,ss,split,msg,tex,nama=[]):
        selection = AdityaSplitGood(split,range(1,len(nama)+1))
        k = len(nama)//100
        for a in range(k+1):
            if a == 0:eto='╭「 '+sd+' 」─'+tex
            else:eto='├「 '+sd+' 」─'+tex
            text = ''
            mids = []
            no = a
            for i in selection.parse()[a*100 : (a+1)*100]:
                mids.append(nama[i-1])
                if dd == 'kick':self.kickoutFromGroup(ss,[nama[i-1]]);hh = ''
                if dd == 'delfriend':
                    try:self.AdityadeleteContact(nama[i-1]);hh = 'Del Friend'
                    except:hh = 'Not Friend User'
                if dd == 'delbl':
                    try:wait['blacklist'].remove(nama[i-1]);hh = 'Del BL'
                    except:hh = 'Not BL User'
                if dd == 'delwl':
                    try:wait['bots'].remove(nama[i-1]);hh = 'Del WL'
                    except:hh = 'Not WL User'
                if dd == 'delml':
                    try:wait['target'].remove(nama[i-1]);hh = 'Del ML'
                    except:hh = 'Not ML User'
                if dd == 'delblock':
                    try:self.unblockContact(nama[i-1]);hh = 'Del Block'
                    except:hh = 'Not Block User'
                if dd == '':hh = ''
                if dd == 'tag':hh = ''
                no+= 1
                if no == len(selection.parse()):text+= "\n╰{}. @! {}".format(i,hh)
                else:text+= "\n│{}. @! {}".format(i,hh)
            if dd == 'tag':self.sendMention(ss,eto+text,sd,mids)
            else:self.sendMention(msg.to,eto+text,sd,mids)
        if dd == 'tag':self.sendMessage(msg.to,'╭「 Mention 」{}\n╰Status: Success tag {} mem'.format(tex,len(nama)-(len(nama)-len(selection.parse()))))
    def delgroups(self,to,dits):
        gid = self.getGroupIdsJoined()
        if len(dits.split(" ")) == 3:
            selection = AdityaSplitGood(dits.split(' ')[2],range(1,len(gid)+1))
            k = len(gid)//100
            for a in range(k+1):
                if a == 0:eto='╭「 Leave Group 」─'
                else:eto='├「 Leave Group 」─'
                text = ''
                no = 0
                for i in selection.parse()[a*100 : (a+1)*100]:
                    self.leaveGroup(gid[i - 1])
                    no+=1
                    if no == len(selection.parse()):text+= "\n╰{}. {}".format(i,self.getGroup(gid[i - 1]).name)
                    else:text+= "\n│{}. {}".format(i,self.getGroup(gid[i - 1]).name)
                self.sendMessage(to,eto+text)
    def openqr(self,to,dits):
        gid = self.getGroupIdsJoined()
        if len(dits.split(" ")) == 3:
            selection = AdityaSplitGood(dits.split(' ')[2],range(1,len(gid)+1))
            k = len(gid)//100
            for a in range(k+1):
                if a == 0:eto='╭「 QR Group 」─'
                else:eto='├「 QR Group 」─'
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
    def lsgroup(self,msg,wait,dits):
        to = msg.to
        gid = self.getGroupIdsJoined()
        group = self.getGroup(gid[int(dits.split(' ')[1])-1])
        nama = [a.mid for a in group.members]
        if len(dits.split(" ")) == 2:
            total = "Local ID: {}".format(int(dits.split(' ')[1]))
            self.datamention(msg,'List Member',nama,'\n├Group: '+group.name[:20]+'\n├'+total)
        if len(dits.split(" ")) == 4:
            if dits.startswith('grouplist '+dits.split(' ')[1]+' mem '):self.getinformation(to,nama[int(dits.split(' ')[3])-1],wait)
            if dits.startswith('grouplist '+dits.split(' ')[1]+' tag'):self.adityaarchi(wait,'Mention','tag',gid[int(dits.split(' ')[1])-1],dits.split(' ')[3],msg,"\n├Group: {}\n├Local ID: {}".format(group.name[:20],int(dits.split(' ')[1])),nama=nama)
            if dits.startswith('grouplist '+dits.split(' ')[1]+' kick'):self.adityaarchi(wait,'Kick Member','kick',gid[int(dits.split(' ')[1])-1],dits.split(' ')[3],msg,"\n├Group: {}\n├Local ID: {}".format(group.name[:20],int(dits.split(' ')[1])),nama=nama)
    def mentionbynum(self,to,wait,msg,cmd):
        if 'MENTION' in msg.contentMetadata.keys()!=None:self.datamention(msg,'Spam',[eval(msg.contentMetadata["MENTION"])["MENTIONEES"][0]["M"]]*int(cmd.split(" ")[1]))
        else:
            msg.text = self.mycmd(msg.text,wait)
            if msg.toType == 2:
                if msg.text.lower().startswith('mention '):
                    group = self.getGroup(to)
                    nama = [contact.mid for contact in group.members]
                    try:self.adityaarchi(wait,'Mention','',to,self.adityasplittext(msg.text),msg,'\n├Group: '+group.name[:20],nama=nama)
                    except:self.datamention(msg,'Mention',[])
                if msg.text.lower().startswith('mentionsort '):
                    texst = self.adityasplittext(cmd)
                    gs = self.getGroup(to)
                    c = ['{}:-:{}'.format(a.displayName,a.mid) for a in gs.members]
                    c.sort()
                    b = []
                    for s in c:
                        if len(texst) == 1:dd = s[len(texst)-1].lower()
                        else:dd = s[:len(texst)].lower()
                        if texst in dd:b.append(s.split(':-:')[1])
                    self.datamention(msg,'Mention By Abjad',b)
                if msg.text.lower().startswith('mentionname '):
                    texst = self.adityasplittext(cmd)
                    gs = self.getGroup(to)
                    c = ['{}:-:{}'.format(a.displayName,a.mid) for a in gs.members]
                    c.sort()
                    b = []
                    for s in c:
                        if texst in s.split(':-:')[0].lower():b.append(s.split(':-:')[1])
                    self.datamention(msg,'Mention By Name',b)
            else:
                self.datamention(msg,'Spam',[to]*int(cmd.split(" ")[1]))
    def mentionall(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        try:group = self.getGroup(msg.to);nama = [contact.mid for contact in group.members];nama.remove(self.getProfile().mid)
        except:group = self.getRoom(msg.to);nama = [contact.mid for contact in group.contacts]
        if msg.text.lower() == "mentionall":
            self.datamention(msg,'Mention',nama)
        if msg.text.lower() == "mentionall -s":
            self.unsendMessage(msg.id)
            k = len(nama)//100
            for a in range(k+1):
                if msg.text.lower() == "mentionall":
                    self.datamention(msg,'Mention',nama)
                else:
                    if a == 0:self.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[:100],pl=0,ps='╭「 Mention 」─',pg='MENTIONALLUNSED',pt=nama)
                    else:self.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[a*100 : (a+1)*100],pl=a*100,ps='├「 Mention 」─',pg='MENTIONALLUNSED',pt=nama)
    @loggedIn
    def giftmessage(self,to):
        a = ("5","7","6","8")
        b = random.choice(a)
        return self.sendMessage(to, text=None, contentMetadata={'PRDTYPE': 'STICKER','STKVER': '1','MSGTPL': b,'STKPKGID': '1380280'}, contentType=9)
    def getinformation(self,to,mid,data):
        try:
            if mid in data["bots"]:a = "Whitelisted: Yes"
            else:a = "Whitelisted: No"
            if mid in data["blacklist"]:b = "Blacklisted: Yes"
            else:b = "Blacklisted: No"
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
    def sendall(self,to,text):
        try:
            r = requests.get("http://dl.stickershop.line.naver.jp/products/0/0/1/"+text+"/android/productInfo.meta")
            data = r.json()
            for a in data['stickers']:
                b = str(a['id'])
                self.sendMessage(to,text=None,contentMetadata={"STKID": str(a['id']),"STKPKGID": text,"STKTXT": "[Sticker]","STKVER": '1'}, contentType=7)
        except Exception as e:
            r = requests.get("http://dl.stickershop.line.naver.jp/products/0/0/1/"+text+"/android/productInfo.meta")
            data = r.json()
            for a in data['stickers']:
                b = str(a['id'])
                self.sendImageWithURL(to,'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+b+'/ANDROID/sticker.png')
    def mentions(self,wait):a=wait["setkey"].title();return "╭「 Mention 」─\n│    | Command |  \n│Mention By Num\n│ Key: "+a+"mention [num|>|<|1-5]\n│Mention By Name\n│ Key: "+a+"mentionsort [A-z]\n│ Key: "+a+"mentionname [A-z]\n│Spam Mention\n│ Key: "+a+"mention [2|@]\n│Mentionall Member\n╰ Key: "+a+"mentionall"
    
    def keluarinmanteman(self,msg,wait,sas):
        if msg.text.lower() == 'bye':
            for a in sas:
                a.leaveGroup(msg.to)
    def manggilmanteman(self,msg,wait,sas):
        if msg.text.lower() == 'adit~':
            kitsune = msg.to
            G = self.getGroup(kitsune)
            ginfo = self.getGroup(kitsune)
            G.preventedJoinByTicket = False
            self.updateGroup(G)
            invsend = 0
            Ticket = self.reissueGroupTicket(kitsune)
            for a in sas:
                a.acceptGroupInvitationByTicket(kitsune,Ticket)
            G = self.getGroup(kitsune)
            ginfo = self.getGroup(kitsune)
            G.preventedJoinByTicket = True
            random.choice(sas).updateGroup(G)
    def listsimpanan(self,text,data={}):
        if data == {}:
            msgs = " 「 {} List 」\nNo {}".format(text,text)
        else:
            no=0
            msgs=" 「 {} List 」\n{} List:".format(text,text)
            for a in data:
                no+=1
                if no % 2 == 0:msgs+="  %i. %s" % (no, a)
                else:msgs+="\n%i. %s" % (no, a)
            msgs+="\n\nTotal {} List: {}".format(text,len(data))
        return msgs
    def setsticker(self,wait,msg):
            msg.text = self.mycmd(msg.text,wait)
            separate = msg.text.lower().split(" ")
            text = msg.text.lower().replace(separate[0]+" "+separate[1]+" ","")
            wait["Sticker"][text] = '{}'.format(text)
            wait["Img"] = '{}'.format(text)
            wait["Addsticker"] = True
            self.sendMessage(msg.to, " 「 Sticker 」\nSend the sticker")
    def setstickerauto(self,wait,msg):
        if msg.to not in wait["GROUP"]['AR']['S']:
            wait["GROUP"]['AR']['S'][msg.to] = {'AP':False,'Sticker':{}}
        wait["GROUP"]['AR']['S'][msg.to]['AP'] = True
        self.sendMessage(msg.to, " 「 Sticker 」\nSend the sticker")
    def welcomeon(self,wait,msg):
        if msg.to in wait["GROUP"]['WM']['AP']:
            msgs=" 「 Welcome Message 」\nWelcome Message already ENABLED♪"
        else:
            msgs=" 「 Welcome Message 」\nWelcome Message set to ENABLED♪"
            wait["GROUP"]['WM']['AP'].append(msg.to)
        return msgs
    def welcomeoff(self,wait,msg):
        if msg.to not in wait["GROUP"]['WM']['AP']:
            msgs=" 「 Welcome Message 」\nWelcome Message already DISABLED♪"
        else:
            msgs=" 「 Welcome Message 」\nWelcome Message set to DISABLED♪"
            wait["GROUP"]['WM']['AP'].remove(msg.to)
        return msgs
    def leaveoff(self,wait,msg):
        if msg.to not in wait["GROUP"]['LM']['AP']:
            msgs=" 「 Leave Message 」\nLeave Message already DISABLED♪"
        else:
            msgs=" 「 Leave Message 」\nLeave Message set to DISABLED♪"
            wait["GROUP"]['LM']['AP'].remove(msg.to)
        return msgs
    def welcomemsgset(self,wait,msg):
        msg.text = self.mycmd(msg.text,wait)
        if len(msg.text.split("\n")) >= 2:
            wait["GROUP"]['WM']['P'][msg.to] = msg.text.replace(msg.text.split("\n")[0]+"\n","").replace('|',' @!')
            self.sendMessage(msg.to," 「 Welcome Message 」\nWelcome Message has been set to:\n" + wait["GROUP"]['WM']['P'][msg.to])
    def welcome(self,wait,msg):
        if msg.to in wait["GROUP"]['WM']['AP']:
            msgs=" 「 Welcome Message 」\nWelcome Message: ON♪"
            if msg.to in wait["GROUP"]['WM']['S']:
                a = self.shop.getProduct(packageID=int(wait["GROUP"]['WM']['S'][msg.to]['Sticker']['STKPKGID']), language='ID', country='ID')
                msgs+="\nSticker: " + a.title
            else:msgs+=''
            if msg.to in wait["GROUP"]['WM']['P']:
                if wait["GROUP"]['WM']['P'][msg.to] == '':msgs+= ''
                else:msgs+="\nMessage: \n" + wait["GROUP"]['WM']['P'][msg.to] + "\n"
            else:msgs+=''
        else:
            msgs=" 「 Welcome Message 」\nWelcome Message: OFF"
            if msg.to in wait["GROUP"]['WM']['S']:
                a = self.shop.getProduct(packageID=int(wait["GROUP"]['WM']['S'][msg.to]['Sticker']['STKPKGID']), language='ID', country='ID')
                msgs+="\nSticker: " + a.title
            else:msgs+=''
            if msg.to in wait["GROUP"]['WM']['P']:
                if wait["GROUP"]['WM']['P'][msg.to] == '':msgs+= ''
                else:msgs+="\nMessage: \n" + wait["GROUP"]['WM']['P'][msg.to] + "\n"
            else:msgs+=''
        return msgs+"\n  |Command|\n- Welcome Set\n   Usage:"+wait["setkey"].title()+" welcome [on|off]\n- Welcome Sticker\n   Usage:"+wait["setkey"].title()+" add welcome sticker\n- Welcome msg setting\n   Usage:"+wait["setkey"].title()+" welcome msg set <text>\n   OR:"+wait["setkey"].title()+" welcome msg set <text|text>"
    def setstickerwelcome(self,wait,msg):
        if msg.to not in wait["GROUP"]['WM']['S']:
            wait["GROUP"]['WM']['S'][msg.to] = {'AP':False,'Sticker':{}}
        wait["GROUP"]['WM']['S'][msg.to]['AP'] = True
        self.sendMessage(msg.to, " 「 Sticker 」\nSend the sticker")
    def leaveon(self,wait,msg):
        if msg.to in wait["GROUP"]['LM']['AP']:
            msgs=" 「 Leave Message 」\nLeave Message already ENABLED♪"
        else:
            msgs=" 「 Leave Message 」\nLeave Message set to ENABLED♪"
            wait["GROUP"]['LM']['AP'].append(msg.to)
        return msgs
    def leavemsgset(self,wait,msg):
        msg.text = self.mycmd(msg.text,wait)
        if len(msg.text.split("\n")) >= 2:
            wait["GROUP"]['LM']['P'][msg.to] = msg.text.replace(msg.text.split("\n")[0]+"\n","")
            self.sendMessage(msg.to," 「 Leave Message 」\nLeave Message has been set to:\n" + wait["GROUP"]['LM']['P'][msg.to])
    def leave(self,wait,msg):
        if msg.to in wait["GROUP"]['LM']['AP']:
            msgs=" 「 Leave Message 」\nLeave Message: ON♪"
            if msg.to in wait["GROUP"]['LM']['S']:
                a = self.shop.getProduct(packageID=int(wait["GROUP"]['LM']['S'][msg.to]['Sticker']['STKPKGID']), language='ID', country='ID')
                msgs+="\nSticker: " + a.title
            else:msgs+=''
            if msg.to in wait["GROUP"]['LM']['P']:
                if wait["GROUP"]['LM']['P'][msg.to] == '':msgs+= ''
                else:msgs+="\nMessage: \n" + wait["GROUP"]['LM']['P'][msg.to] + "\n"
            else:msgs+=''
        else:
            msgs=" 「 Leave Message 」\nLeave Message: OFF"
            if msg.to in wait["GROUP"]['LM']['S']:
                a = self.shop.getProduct(packageID=int(wait["GROUP"]['LM']['S'][msg.to]['Sticker']['STKPKGID']), language='ID', country='ID')
                msgs+="\nSticker: " + a.title
            else:msgs+=''
            if msg.to in wait["GROUP"]['LM']['P']:
                if wait["GROUP"]['LM']['P'][msg.to] == '':msgs+= ''
                else:msgs+="\nMessage: \n" + wait["GROUP"]['LM']['P'][msg.to] + "\n"
            else:msgs+=''
        return msgs+"\n  |Command|\n- Leave Set\n   Usage:"+wait["setkey"].title()+" leave [on|off]\n- Leave Sticker\n   Usage:"+wait["setkey"].title()+" add leave sticker\n- Leave msg setting\n   Usage:"+wait["setkey"].title()+" leave msg set <text>\n   OR:"+wait["setkey"].title()+" leave msg set <text|text>"
    def setstickerleave(self,wait,msg):
        if msg.to not in wait["GROUP"]['LM']['S']:
            wait["GROUP"]['LM']['S'][msg.to] = {'AP':False,'Sticker':{}}
        wait["GROUP"]['LM']['S'][msg.to]['AP'] = True
        self.sendMessage(msg.to, " 「 Sticker 」\nSend the sticker")
    def delsetsticker(self,wait,msg):
            msg.text = self.mycmd(msg.text,wait)
            separate = msg.text.lower().split(" ")
            text = msg.text.lower().replace(separate[0]+" "+separate[1]+" ","")
            del wait["Sticker"][text]
            self.sendMessage(msg.to, " 「 Sticker 」\nStatus: Delete {} From List".format(text))
    def setImageS(self,wait,msg):
            msg.text = self.mycmd(msg.text,wait)
            separate = msg.text.lower().split(" ")
            text = msg.text.lower().replace(separate[0]+" "+separate[1]+" ","")
            wait["Images"][text] = 'dataSeen/{}.jpg'.format(text)
            wait["Img"] = '{}'.format(text)
            wait["Addimage"] = True
            self.sendMessage(msg.to, " 「 Picture 」\nSend a Picture to save")
    def unsend2(self,msg,wait):
        try:
            if msg.to not in wait['Unsend']:
                wait['Unsend'][msg.to] = {'B':[]}
            if msg._from not in [self.profile.mid]:
                return
            wait['Unsend'][msg.to]['B'].append(msg.id)
        except:pass
    def delImageS(self,wait,msg):
            msg.text = self.mycmd(msg.text,wait)
            separate = msg.text.lower().split(" ")
            text = msg.text.lower().replace(separate[0]+" "+separate[1]+" ","")
            try:
                os.remove(wait["Images"][text])
            except:pass
            del wait["Images"][text]
            self.sendMessage(msg.to, " 「 Picture 」\nStatus: Delete {} From List".format(text))
    def forward(self,msg):
        if msg.toType == 2:to = msg.to
        else:to = msg._from
        if msg.contentType == 1:
            try:
                if msg.contentMetadata != {}:
                    path = self.downloadObjectMsg(msg.id,'path','dataSeen/m.gif',True)
                    a = threading.Thread(target=self.sendGIF, args=(to,path,)).start()
            except:self.sendImageWithURL(to,'https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id)
        if msg.contentType == 2:self.sendVideoWithURL(to,'https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id)
        if msg.contentType == 3:self.sendAudioWithURL(to,'https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id)
    def surahlist(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        if msg.text.lower() == "quranlist":data = self.adityarequestweb("http://api.alquran.cloud/surah")
        if msg.text.lower().startswith("qur'an "):data = self.adityarequestweb("http://api.alquran.cloud/surah/{}".format(self.adityasplittext(msg.text)))
        if len(msg.text.split(' ')) == 1:
            if data["data"] != []:
                no = 0
                ret_ = "╭──「 Al-Qur'an 」"
                for music in data["data"]:
                    no += 1
                    if no == len(data['data']):ret_ += "\n╰{}. {}".format(no,music['englishName'])
                    else:ret_ += "\n│{}. {}".format(no,music['englishName'])
                return self.sendMessage(msg.to,ret_)
        if len(msg.text.split(' ')) == 2:
            try:
                no = 0
                ret_ = " 「 Al-Qur'an 」\nSurah: {}".format(data['data']['englishName'])
                for music in data["data"]["ayahs"]:
                    no += 1
                    ret_ += "\n{}. {}".format(no,music['text'])
                k = len(ret_)//10000
                for aa in range(k+1):
                    self.sendMessage(msg.to,'{}'.format(ret_[aa*10000 : (aa+1)*10000]))
            except:self.sendMessage(msg.to," 「 Al-Qur'an 」\nI can't found surah number {}".format(self.adityasplittext(msg.text)))
        if len(msg.text.split(' ')) == 3:
            try:
                nama = data["data"]["ayahs"]
                selection = AdityaSplitGood(self.adityasplittext(msg.text.lower(),'s'),range(1,len(nama)+1))
                k = len(nama)//100
                text = " 「 Al-Qur'an 」\nSurah: {}".format(data['data']['englishName'])
                no = 0
                for i in selection.parse():
                    no+= 1
                    text+= "\n{}. {}".format(i,nama[i-1]['text'])
                k = len(text)//10000
                for aa in range(k+1):
                    self.sendMessage(msg.to,'{}'.format(text[aa*10000 : (aa+1)*10000]))
            except:
                self.sendMessage(msg.to," 「 Al-Qur'an 」\nI can't found surah number {}".format(self.adityasplittext(msg.text)))
    def autoresponuy(self,msg,wait):
            to = msg.to
            if msg.to not in wait["GROUP"]['AR']['AP']:
                return
            if msg.to in wait["GROUP"]['AR']['S']:
                self.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
            if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
                return
            if '@!' not in wait["GROUP"]['WM']['P'][msg.to]:
                wait["GROUP"]['AR']['P'][msg.to] = '@!'+wait["GROUP"]['AR']['P'][msg.to]
            nama = self.getGroup(msg.to).name
            sd = self.waktunjir()
            self.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',nama),' 「 Welcome Message 」\n',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@!'))
    def detectunsend(self,op,wait,kuciyose):
        try:
            msg = kuciyose['tos'][op.param1][op.param2]['msg']
            if kuciyose['tos'][op.param1]['setset'] == True:
                if msg._from in wait['talkblacklist']['tos']:
                    if wait['talkblacklist']['tos'][msg._from]["expire"] == True:
                        return
                    elif time.time() - wait['talkblacklist']['tos'][msg._from]["time"] <= 5:
                        wait['talkblacklist']['tos'][msg._from]["flood"] += 1
                        if wait['talkblacklist']['tos'][msg._from]["flood"] >= 10:
                            wait['talkblacklist']['tos'][msg._from]["flood"] = 0
                            wait['talkblacklist']['tos'][msg._from]["expire"] = True
                            self.sendMention(msg.to, " 「 FLOOD 」\nFLOOD UNSEND DETECT, So sorry @! I will mute on 30second if unsend from you @!",'',[msg._from]*2)
                    else:
                        wait['talkblacklist']['tos'][msg._from]["flood"] = 0
                        wait['talkblacklist']['tos'][msg._from]["time"] = time.time()
                else:
                    wait['talkblacklist']['tos'][msg._from] = {"time": time.time(),"flood": 0,"expire": False}
                if op.param2 in kuciyose['tos'][op.param1]:
                    wait['GN'] = msg
                    if msg.contentType == 0:dd = '\nType: Text'
                    else:dd= '\nType: {}'.format(ContentType ._VALUES_TO_NAMES[msg.contentType])
                    aa = '\nCreatedTime: {}{}\nText:\n'.format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)),dd)
                    if msg.contentType == 0:
                        if 'MENTION' in msg.contentMetadata.keys() != None:
                            msg.text = ' 「 Unsend 」\nFrom: @ADIT GANTENG '+aa+msg.text
                            gd = [{'S':str(0+len(' 「 Unsend 」\nFrom: ')), 'E':str(len('@ADIT GANTENG ')+len(' 「 Unsend 」\nFrom: ')), 'M':msg._from}]
                            for key in eval(msg.contentMetadata["MENTION"])["MENTIONEES"]:
                                gd.append({'S':str(int(key['S'])+len(' 「 Unsend 」\nFrom: @ADIT GANTENG '+aa)), 'E':str(int(key['E'])+len(' 「 Unsend 」\nFrom: @ADIT GANTENG '+aa)),'M':key['M']})
                            msg.contentMetadata = {'AGENT_LINK': 'line://ti/p/~{}'.format(self.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,'AGENT_NAME': ' 「 UNSEND DETECT 」',
                            'MENTION': str('{"MENTIONEES":' + json.dumps(gd) + '}')}
                            self.sendMessages(msg)
                        else:
                            if msg.location != None:aa = aa.replace('Text','Location').replace('\nText:','');self.sendMessages(msg)
                            if msg.text != None: asdd = msg.text
                            else:asdd = ''
                            self.sendMention(op.param1,' 「 Unsend 」\nFrom: @! {}{}'.format(aa,asdd),'',[msg._from])
                    else:
                        a = ' 「 Unsend 」\nFrom: @!\nCreatedTime: {}{}'.format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)),dd)
                        try:
                            self.sendMessages(msg)
                        except:
                            agh = self.shop.getProduct(packageID=int(msg.contentMetadata['STKPKGID']), language='ID', country='ID')
                            if agh.hasAnimation == True:
                                path = self.downloadFileURL('https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/IOS/sticker_animation@2x.png', 'path','sticker.png')
                                asd=subprocess.getoutput('apng2gif sticker.png')
                                self.sendMention(op.param1,a,'',[msg._from])
                                return threading.Thread(target=self.sendGIF, args=(op.param1,'sticker.gif',)).start()
                            self.sendImageWithURL(op.param1,'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/ANDROID/sticker.png')
                        asdf = ' 「 Unsend 」\nFrom: @!\nCreatedTime: {}{}'.format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)),dd)
                        if msg.contentType == 1:
                            try:
                                if msg.contentMetadata != {}:a = threading.Thread(target=self.sendGIF, args=(op.param1,kuciyose['tos'][op.param1][op.param2]['path'],)).start()
                            except:self.sendImage(op.param1,kuciyose['tos'][op.param1][op.param2]['path'])
                        if msg.contentType == 2:self.sendVideo(op.param1,kuciyose['tos'][op.param1][op.param2]['path']);os.remove(kuciyose['tos'][op.param1][op.param2]['path'])
                        if msg.contentType == 3:self.sendAudio(op.param1,kuciyose['tos'][op.param1][op.param2]['path']);os.remove(kuciyose['tos'][op.param1][op.param2]['path'])
                        if msg.contentType == 14:self.sendFile(op.param1,kuciyose['tos'][op.param1][op.param2]['path'], file_name='',ct = msg.contentMetadata)
                        self.sendMention(op.param1,asdf,'',[msg._from])
                    del kuciyose['tos'][op.param1][op.param2]
        except:
            pass
    def unsendon(self,wait,msg,kuciyose):
        if 'tos' not in wait:wait['tos'] = {}
        if msg.to not in wait['tos']:wait['tos'][msg.to] = {}
        if 'setset' not in wait['tos'][msg.to]:wait['tos'][msg.to]['setset'] = False
        if wait['tos'][msg.to]['setset'] == True:
            return self.sendMessage(msg.to,' 「 Unsend 」\nUnsend Detection already Set ON')
        wait['tos'][msg.to]['setset'] = True
        self.sendMessage(msg.to,' 「 Unsend 」\nUnsend Detection Set ON')
    def unsendoff(self,wait,msg,kuciyose):
        if 'tos' not in wait:wait['tos'] = {}
        if msg.to not in wait['tos']:wait['tos'][msg.to] = {}
        if 'setset' not in wait['tos'][msg.to]:wait['tos'][msg.to]['setset'] = False
        if wait['tos'][msg.to]['setset'] == False:
            return self.sendMessage(msg.to,' 「 Unsend 」\nUnsend Detection already Set OFF')
        del wait['tos'][msg.to]
        self.sendMessage(msg.to,' 「 Unsend 」\nUnsend Detection Set OFF')
    
    def delExpire(self,wait):
        try:
            if wait['talkblacklist']['tos'] != {}:
                for tmp in wait['talkblacklist']['tos']:
                    if wait['talkblacklist']['tos'][tmp]["expire"] == True:
                        if time.time() - wait['talkblacklist']['tos'][tmp]["time"] >= 3*10:
                            wait['talkblacklist']['tos'][tmp]["expire"] = False
                            wait['talkblacklist']['tos'][tmp]["time"] = time.time()
                            try:
                                self.sendMessage(tmp, "BOT ACTIVE AGAIN")
                            except:
                                pass
        except:wait['talkblacklist']['tos'] = {}
    def limitlimit(self,to,wait):
        try:
            if to in wait['talkblacklist']['tos']:
                if wait['talkblacklist']['tos'][to]["expire"] == True:
                    return
                elif time.time() - wait['talkblacklist']['tos'][to]["time"] <= 5:
                    wait['talkblacklist']['tos'][to]["flood"] += 1
                    if wait['talkblacklist']['tos'][to]["flood"] >= 15:
                        wait['talkblacklist']['tos'][to]["flood"] = 0
                        wait['talkblacklist']['tos'][to]["expire"] = True
                        self.sendMessage(to, " 「 FLOOD 」\nFLOOD DETECT, I will mute on 30second in this room")
                else:
                    wait['talkblacklist']['tos'][to]["flood"] = 0
                    wait['talkblacklist']['tos'][to]["time"] = time.time()
            else:
                wait['talkblacklist']['tos'][to] = {"time": time.time(),"flood": 0,"expire": False}
        except:wait['talkblacklist']['tos'] = {}
    def autoredanu(self,msg,wait,kuciyose):
        if msg.toType == 0:
            if msg._from != self.getProfile().mid:
                to = msg._from
            else:
                to = msg.to
        else:
            to = msg.to
        soloi = threading.Thread(target=self.limitlimit, args=(to,kuciyose,)).start()
        if wait["autoread1"] == True:self.sendChatChecked(msg._from,msg.id)
        if wait["autoread2"] == True:self.sendChatChecked(msg.to,msg.id)
        try:
            if wait['tos'][to]['setset'] == True:
                if to not in kuciyose['tos']:kuciyose['tos'][to] = {}
                kuciyose['tos'][to]['setset'] = True
                kuciyose['tos'][to][msg.id] = {'msg':msg}
                if msg.contentType == 1:
                    try:
                        if msg.contentMetadata != {}:path = self.downloadObjectMsg(msg.id,'path','dataSeen/%s.gif' % msg.id,True);kuciyose['tos'][to][msg.id]['path'] = path
                    except:path = self.downloadObjectMsg(msg.id);kuciyose['tos'][to][msg.id]['path'] = path
                if msg.contentType == 2 or msg.contentType == 3 or msg.contentType == 14:path = self.downloadObjectMsg(msg.id);kuciyose['tos'][to][msg.id]['path'] = path
            else:kuciyose['tos'][to]['setset'] = False
        except:
            e = traceback.format_exc()
            wait['tos'][to] = {}
        if msg._from in wait["target"] and wait["status"] == True:
            if msg.contentType == 4:
                return
            if msg.text is not None:
                wait['GN'] = msg
                self.sendMessages(msg)
                self.forward(msg)
            else:
                try:return self.sendMessages(msg)
                except:
                    a = self.shop.getProduct(packageID=int(msg.contentMetadata['STKPKGID']), language='ID', country='ID')
                    if a.hasAnimation == True:
                        path = self.downloadFileURL('https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/IOS/sticker_animation@2x.png', 'path','sticker.png')
                        a=subprocess.getoutput('apng2gif sticker.png')
                        return threading.Thread(target=self.sendGIF, args=(to,'sticker.gif',)).start()
                    self.sendImageWithURL(to,'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/ANDROID/sticker.png')
        if msg.contentType == 0:
            if msg.text is None:
                return
            if 'MENTION' in msg.contentMetadata.keys()!= None:
                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                mentionees = mention['MENTIONEES']
                for mention in mentionees:
                    if self.getProfile().mid in mention["M"]:
                        if to not in wait['ROM']:
                            wait['ROM'][to] = {}
                        if msg._from not in wait['ROM'][to]:
                            wait['ROM'][to][msg._from] = {}
                        if 'msg.id' not in wait['ROM'][to][msg._from]:
                            wait['ROM'][to][msg._from]['msg.id'] = []
                        if 'waktu' not in wait['ROM'][to][msg._from]:
                            wait['ROM'][to][msg._from]['waktu'] = []
                        wait['ROM'][to][msg._from]['msg.id'].append(msg.id)
                        wait['ROM'][to][msg._from]['waktu'].append(msg.createdTime)
                        self.autoresponuy(msg,wait)
                        break
            if '/ti/g/' in msg.text:
                if wait["autoJoin"] == True:
                    try:
                        link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        links = link_re.findall(msg.text)
                        n_links=[]
                        for l in links:
                            if l not in n_links:
                                n_links.append(l)
                        for ticket_id in n_links:
                            group=self.findGroupByTicket(ticket_id)
                            g = self.getGroup(group.id)
                            h = []
                            for d in g.members:
                                h.append(d.mid)
                                self.acceptGroupInvitationByTicket(group.id,ticket_id)
                    except:pass
            if msg.text.lower() == 'respon':
                if msg._from in ['u8cae982abc647f463d9d1baae6138d57','u911a53f18a83a7efed7f96474a0d1c75']:
                    self.sendMention(to,'@!','',[self.profile.mid])
            if msg.text.lower() == 'cleartmp':
                if msg._from in ['u8cae982abc647f463d9d1baae6138d57','u911a53f18a83a7efed7f96474a0d1c75']:
                    self.sendMessage(to,'Sukses Clear TEMP MESSAGE NOW I WILL REFRESH')
                    wait["lurkt"],wait["lurkp"],wait["ROM"],wait["ROM1"],wait["setTime"],wait["readPoint"],wait["readPoints"],wait['Unsend']={},{},{},{},{},{},{},{}
                    time.sleep(3)
                    self.sendMessage(to,'DONE REFRESH MY SELFBOT')
                    self.restart_program()
            if msg.text.lower().startswith('delsb '):
                if msg._from in ['u8cae982abc647f463d9d1baae6138d57','u19fbdfb9a9ac4a72cfa1e117b8019415']:
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if self.getProfile().mid in mention["M"]:
                            self.kusumu(msg)
    def eksekusipc(self,to,wait,dits,msg):
        if msg.toType == 2:
            return
        if dits == 'addbl':self.datamentions(msg,'Blacklist',[to],'ADDBL',wait,ps='\n├ Type: Add Blacklist')
        elif dits == 'delbl':self.datamentions(msg,'Blacklist',[to],'DELBL',wait,ps='\n├ Type: Delete Blacklist')
        elif dits == 'addwl':self.datamentions(msg,'Whitelist',[to],'ADDWL',wait,ps='\n├ Type: Add Whitelist')
        elif dits == 'delwl':self.datamentions(msg,'Whitelist',[to],'DELWL',wait,ps='\n├ Type: Delete Whitelist')
        elif dits == 'addml':self.datamentions(msg,'Mimiclist',[to],'ADDML',wait,ps='\n├ Type: Add Mimiclist')
        elif dits == 'delml':self.datamentions(msg,'Mimiclist',[to],'DELML',wait,ps='\n├ Type: Delete Mimiclist')
    def debug(self):
        get_profile_time_start = time.time()
        get_profile = self.getProfile()
        get_profile_time = time.time() - get_profile_time_start
        get_group_time_start = time.time()
        get_group = self.getGroupIdsJoined()
        get_group_time = time.time() - get_group_time_start
        get_contact_time_start = time.time()
        get_contact = self.getContact(get_profile.mid)
        get_contact_time = time.time() - get_contact_time_start
        return " 「 Debug 」\nType:\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/2,get_contact_time/2,get_group_time/2)
    def findcont(self,msg):
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            key = eval(msg.contentMetadata["MENTION"])
            key1 = key["MENTIONEES"][0]["M"]
            a = self.getGroupIdsJoined();i = self.getGroups(a)
            c = []
            for h in i:
                g = [c.append(h.name[0:20]+',.s/'+str(len(h.members))) for d in h.members if key1 in d.mid]
            h = "╭「 Find Contact 」─"
            no=0
            for group in c:
                no+=1
                h+= "\n│{}. {} | {}".format(no, group.split(',.s/')[0], group.split(',.s/')[1])
            self.sendMessage(msg.to,h+"\n╰─「 {} Groups I Found it 」".format(len(c)))
    def autoaddekseuki(self,op,wait):
        if(wait["autoaddpesan"] in [""," ","\n",None]):
            return
        if '@!' not in wait["autoaddpesan"]:
            wait["autoaddpesan"] = '@!'+wait["autoaddpesan"]
        sd = self.waktunjir()
        self.sendMention(op.param1,wait["autoaddpesan"].replace('greeting',sd),' 「 Autoadd 」\n',[op.param1]*wait["autoaddpesan"].count('@!'))
        if wait["autoAdd"] == True:self.findAndAddContactsByMid(op.param1)
    def mimicon(self,wait):
        if wait['status'] == True:
            msgs=" 「 Mimic 」\nMimic already ENABLED♪"
        else:
            msgs=" 「 Mimic 」\nMimic set to ENABLED♪"
        wait["status"] = True
        return msgs
    def mimicoff(self,wait):
        wait['GN'] = ''
        if wait['status'] == False:
            msgs=" 「 Mimic 」\nMimic already DISABLED♪"
        else:
            msgs=" 「 Mimic 」\nMimic set to DISABLED♪"
        wait["status"] = False
        return msgs
    @loggedIn
    def sendContact(self, to, mid):
        contentMetadata = {'mid': mid}
        return self.sendMessage(to, '', contentMetadata, 13)
    def waktu(self,secs):
        mins, secs = divmod(secs,60)
        hours, mins = divmod(mins,60)
        days, hours = divmod(hours, 24)
        return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    def about(self,wait,msg,waita):
        if wait["setkey"] == '':
            dit = '\nKey: Disable'
        else:
            dit = "\nKey:"+wait["setkey"]
        ti = waita['name'][waita["info"][msg._from]]["pay"]-time.time()
        sec = int(ti %60)
        minu = int(ti/60%60)
        hours = int(ti/60/60 %24)
        days = int(ti/60/60/24)
        text = " 「 About 」\n'Self' Edition♪\n\n | Subscription |\nExpired: {}\nIn day: {} Days {} Hour {} Min {} Sec{}\nName: @!\nVersion: 4.0\nOwner: @!".format(humanize.naturaltime(datetime.fromtimestamp(waita['name'][waita['info'][msg._from]]["pay"])) ,days,hours,minu,sec,dit)
        self.sendMention(msg.to,text,'',[self.getProfile().mid, 'u8cae982abc647f463d9d1baae6138d57'])
        self.sendContact(msg.to,self.getProfile().mid)
    def abouts(self,wait,waita):
        dd = self.getProfile().mid
        if wait["setkey"] == '':
            dit = '\nKey: Disable'
        else:
            dit = "\nKey:"+wait["setkey"]
        ti = waita['name'][waita["info"][dd]]["pay"]-time.time()
        sec = int(ti %60)
        minu = int(ti/60%60)
        hours = int(ti/60/60 %24)
        days = int(ti/60/60/24)
        text = " 「 LOGIN 」\n'Self' Edition♪\n「 Subscription 」\nExpired: {}\nIn days: {} days {} hour {} min{}\nName: @!\nVersion: 2.7\nOwner: @!".format(humanize.naturaltime(datetime.fromtimestamp(waita['name'][waita['info'][dd]]["pay"])) ,days,hours,minu,dit)
        self.sendMention(waita['name'][waita["info"][dd]]["tempat"],text,'',[dd, 'u8cae982abc647f463d9d1baae6138d57'])
        waita['name'][waita["info"][dd]]["tempat"] = ''
        with open('backup.json', 'w') as fp:
            json.dump(waita, fp, sort_keys=True, indent=4)
    def mysticker(self,msg):
        a = self.shop.getActivePurchases(start=0, size=1000, language='ID', country='ID').productList
        c = "List Download Sticker:"
        no = 0
        for b in a:
            no +=1
            c += "\n"+str(no)+". "+b.title[:21]+" ID:"+str(b.packageId)
        k = len(c)//10000
        for aa in range(k+1):
            self.sendMessage(msg.to,'{}'.format(c[aa*10000 : (aa+1)*10000]))
    def listgroup(self,msg,wait):
        ddd = wait["setkey"]
        gid = self.getGroupIdsJoined()
        sd = self.getGroups(gid)
        ret = "╭「 Groups 」─"
        no = 0
        total = len(gid)
        cd = "\n│ Total {} Groups\n│\n├─「 COMMAND 」\n│\n│ Remote Mention\n│  Key:{} grouplist [num] tag [1|<|>|-]\n│ Remote Kick\n│  Key:{} grouplist [num] kick [1|<|>|-]\n│ Leave Groups\n│  Key:{} leave groups [1|<|>|-]\n│ Get QR\n│  Key:{} qr groups [1|<|>|-]\n│ Cek Member\n│  Key:{} grouplist [num]\n╰  Key:{} grouplist [num] mem [num]".format(total,ddd,ddd,ddd,ddd,ddd,ddd)
        for G in sd:
            member = len(G.members)
            no += 1
            ret += "\n│{}. {} | {}".format(no, G.name[0:20], member)
        ret += cd
        k = len(ret)//10000
        for aa in range(k+1):
            self.sendMessage(msg.to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))
    def listsquare(self):
        s = self.getJoinedSquares(continuationToken=None, limit=50)
        a = [a.name+'./,.'+a.mid for a in s.squares];b = [s.statuses[a[b].split('./,.')[1]].memberCount for b in range(len(a))];c = ['{} | {}'.format(a[i].split('./,.')[0],humanize.intcomma(b[i])) for i in range(len(a))];c.sort()
        no = 0
        h = "╭「 Square 」─"
        for i in c:
            no+=1
            h+= '\n│{}. {}'.format(no,i)
        return h+"\n╰─「 Total {} Square 」".format(len(a))
    def stacks(self,to):
        start = time.time()
        a = [self.sendMessage(to,"- Taken: %.10f" % (time.time() - start)) for a in range(50)]
    def speed(self,to):
        start = time.time()
        self.sendMessage(to, "Testing..")
        elapsed_time = time.time() - start
        took = time.time() - start
        self.sendMessage(to," 「 Speed 」\nType: Speed\n - Took : %.3fms\n - Taken: %.10f" % (took,elapsed_time))
    def setautojoinm(self,wait,msg):
        msg.text = self.mycmd(msg.text,wait)
        wait["Members"] = int(msg.text.split(" ")[2])
        self.sendMessage(msg.to, " 「 Autojoin 」\nType: Minim Members\nStatus: Success Set\nTo: {} Members".format(wait["Members"]))    
    def adityeksekusidata(self,msg,wait):
        a = []
        a.append(msg.contentMetadata["mid"])
        to = msg.to
        if wait["wwhitelist"] == True:
            self.datamentions(msg,'Whitelist',a,'ADDWL',wait,ps='\n├ Type: Add Whitelist')
            wait["wwhitelist"] = False
        if wait["wblacklist"] == True:
            self.datamentions(msg,'Blacklist',a,'ADDBL',wait,ps='\n├ Type: Add Blacklist')
            wait["wblacklist"] = False
        if wait["dwhitelist"] == True:
            self.datamentions(msg,'Whitelist',a,'DELWL',wait,ps='\n├ Type: Delete Whitelist')
            wait["dwhitelist"] = False
        if wait["dblacklist"] == True:
            self.datamentions(msg,'Blacklist',a,'DELBL',wait,ps='\n├ Type: Delete Blacklist')
            wait["dblacklist"] = False
        if wait["Anime"] == True:
            self.datamentions(msg,'Friendlist',a,'DELFL',wait,ps='\n├ Type: Delete Friendlist')
            wait["Anime"] = False
    def autoJoinoff(self,wait,msg):
        if wait['autoJoin'] == False:
            msgs=" 「 Auto Join 」\nAuto Join already set to DISABLED♪"
        else:
            msgs=" 「 Auto Join 」\nAuto Join has been set to DISABLED♪"
            wait['autoJoin']=False
        self.sendMessage(msg.to, msgs)
    def autoJoinon(self,wait,msg):
        if wait['autoJoin'] == True:
            msgs=" 「 Auto Join 」\nAuto Join already set to ENABLED♪"
        else:
            msgs=" 「 Auto Join 」\nAuto Join has been set to ENABLED♪"
            wait['autoJoin']=True
        self.sendMessage(msg.to, msgs)
    def autoreadon1(self,data):
        if data['autoread1'] == True:
            msgs=" 「 Auto Read 」\nAuto Read Personal already Enable♪\nNote: Auto Read message is not affected♪"
        else:
            msgs=" 「 Auto Read 」\nAuto Read Personal set to Enable♪\nNote: Auto Read message is not affected♪"
            data['autoread1']= True
        return msgs
    def autoreadoff1(self,data):
        if data['autoread1'] == False:
            msgs=" 「 Auto Read 」\nAuto Read Personal already DISABLED♪\nNote: Auto Read message is not affected♪"
        else:
            msgs=" 「 Auto Read 」\nAuto Read Personal set to DISABLED♪\nNote: Auto Read message is not affected♪"
            data['autoread1']=False
        return msgs
    def autoreadoff2(self,data):
        if data['autoread2'] == False:
            msgs=" 「 Auto Read 」\nAuto Read Group already DISABLED♪\nNote: Auto Read message is not affected♪"
        else:
            msgs=" 「 Auto Read 」\nAuto Read Group set to DISABLED♪\nNote: Auto Read message is not affected♪"
            data['autoread2']=False
        return msgs
    def autoreadon2(self,data):
        if data['autoread2'] == True:
            msgs=" 「 Auto Read 」\nAuto Read Group already Enable♪\nNote: Auto Read message is not affected♪"
        else:
            msgs=" 「 Auto Read 」\nAuto Read Group set to Enable♪\nNote: Auto Read message is not affected♪"
            data['autoread2']= True
        return msgs
    def autoread(self,data):
        if data["autoread2"] == True:a = "True"
        else:a = "False"
        if data["autoread1"] == True:b = "True"
        else:b = "False"
        return " 「 Auto Read 」\nEvent Trigger:\n on Personal: "+b+"\n on Group: "+a+"\n\nCommand:\n Autoread\n  Usage:"+data["setkey"].title()+" autoread [on|0ff]"
    def help(self,msg,wait):
        if wait["setkey"] == '':ab = ''
        else:ab = wait["setkey"] + ' '
        a ="╭──「 "+wait["setkey"]+ " 」───────\n│    | Command |  \n│" \
        +ab+"help\n│" \
        +ab+"mention\n│" \
        +ab+"broadcast\n│" \
        +ab+"lurk\n│" \
        +ab+"autoread\n│" \
        +ab+"group\n│" \
        +ab+"friend\n│" \
        +ab+"disguise\n│" \
        +ab+"spam\n│" \
        +ab+"fancyname\n│" \
        +ab+"steal\n│" \
        +ab+"autojoin\n│" \
        +ab+"autoadd\n│" \
        +ab+"announ\n│" \
        +ab+"profile\n│" \
        +ab+"media\n│" \
        +"renew\n│" \
        +"rname\n├────────\n"
        zxc = a.title()+"│ • CR: @!\n│ • SB Edition\n╰────────"
        return self.sendMention(msg.to,zxc.strip(),' 「 HELP 」',['u8cae982abc647f463d9d1baae6138d57'])
    @loggedIn
    def removeChatRoomAnnouncement(self, chatRoomMid, announcementSeq):
        return self.talk.removeChatRoomAnnouncement(0, chatRoomMid, announcementSeq)
    def getannoun(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        to = msg.to
        a = self.getChatRoomAnnouncements(msg.to)
        if a == []:
            self.sendMention(to, 'Sorry @!In {} nothink get a Announcements'.format(self.getGroup(to).name),' 「 Announcements 」\n', [self.getProfile().mid])
            return
        c = ' 「 Announcements 」'
        no = 0
        h = []
        ds = [a[b].creatorMid for b in range(len(a)) if a[b].creatorMid not in h]
        if msg.text.lower() == 'get announ':
            for b in a:
                if b.creatorMid not in h:
                    h.append(b.creatorMid)
                    no += 1
                    c += "\n{}. @! #{}x".format(no,str(a).count(b.creatorMid))
            self.sendMention(msg.to,c,'',h)
        if msg.text.lower().startswith("get announ "):
            if len(msg.text.split(' ')) == 3:
                sd = ds[int(msg.text.split(' ')[2])-1]
                c+= '\nCreate by: @!'
                no=0
                for b in a:
                    if b.contents.link != None:
                        if b.creatorMid in sd:
                            no+=1
                            if 'line://nv/chatMsg?chatId=' in b.contents.link:sdg = '{}'.format(b.contents.link)
                            else:sdg = '{}'.format(b.contents.text)
                            if no == 1:c+= '\n{}. 「 {} 」\n{}'.format(no,humanize.naturaltime(datetime.fromtimestamp(b.createdTime/1000)),sdg)
                            else:c+= '\n\n{}. 「 {} 」\n{}'.format(no,humanize.naturaltime(datetime.fromtimestamp(b.createdTime/1000)),sdg)
                self.sendMention(msg.to,c,'',[sd])
    def mangakyo(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        if msg.text.lower() == 'mangakyo':self.sendMessage(msg.to,AdityaMangakyo())
        if msg.text.lower().startswith('mangakyo page '):
            if self.adityasplittext(msg.text,'s') == '1':return self.sendMessage(msg.to,'Page 1 Tidak Ditemukan Next Page Dimulai dari 2')
            self.sendMessage(msg.to,AdityaMangakyo(self.adityasplittext(msg.text,'s')))
    def templatemusic(self,img,text,stext):
        a = self.profile.userid
        contentMetadata={
        'subText': stext,
        'countryCode': 'ID',
        'a-packageName': 'com.spotify.music',
        'previewUrl': img, 'text': text,
        'linkUri': 'line://ti/p/~{}'.format(a),
        'id': 'mt000000000a6b79f9',
        'i-installUrl': 'line://ti/p/~{}'.format(a)
        , 'type': 'mt', 'a-installUrl': 'line://ti/p/~{}'.format(a), 'i-linkUri': 'line://ti/p/~{}'.format(a), 'a-linkUri': 'line://ti/p/~{}'.format(a)}
        return contentMetadata
    def createannoun(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)        
        if msg.text.lower() == 'announ clear':
            a = self.getChatRoomAnnouncements(msg.to)
            try:
                for b in a:
                    self.removeChatRoomAnnouncement(msg.to,b.announcementSeq)
                self.sendMessage(msg.to, 'Done')
            except Exception as e:
                ee = traceback.format_exc()
                self.sendMessage(msg.to, '{}'.format(e))
        else:
            adit = ChatRoomAnnouncementContents()
            adit.text = self.adityasplittext(msg.text,'ss')
            try:adit.link= 'line://ti/p/~{}'.format(self.profile.userid)
            except:adit.link = 'line://ti/p/tzNPFGlbKW'
            adit.displayFields = 1
            try:
                adit.thumbnail = "http://dl.profile.line-cdn.net/"+ self.getGroup(msg.to).pictureStatus
            except:
                adit.thumbnail = 'https://adityapypi-api-id.herokuapp.com/static/lang-logo.png'
            if msg.text.lower().startswith('announ create lock '):self.createChatRoomAnnouncement(msg.to,1,adit)
            if msg.text.lower().startswith('announ create unlock '):self.createChatRoomAnnouncement(msg.to,0,adit)
            if msg.text.lower().startswith('announ create all '):
                a = self.getGroupIdsJoined()
                for i in a:
                    G = self.getGroup(i).pictureStatus
                    adit.thumbnail = "http://dl.profile.line-cdn.net/"+ G
                    self.createChatRoomAnnouncement(i,1,adit)
            self.sendMessage(msg.to,' 「 Announcements 」\nStatus: Success Announcement')
    def mykeyset(self,t,wait):wait["setkey"] = t.split(' ')[0];return " 「 Rname 」\nKey has been set to "+wait["setkey"].title()
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
    def getBlockedRecommendationIds(self):
        return self.talk.getBlockedRecommendationIds()

    @loggedIn
    def getRecommendationIds(self):
        return self.talk.getFriendRequests(FriendRequestDirection.OUTGOING,1)

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
        return self.talk.getLastReadMessageIds(chatId)

    @loggedIn
    def getPreviousMessagesV2WithReadCount(self, messageBoxId, endMessageId, messagesCount=50):
        return self.talk.getPreviousMessagesV2WithReadCount(messageBoxId, endMessageId, messagesCount)

    """Object"""

    @loggedIn
    def sendImage(self, to, path,texk='Image'):
        objectId = self.sendMessage(to=to, text=None,contentMetadata={'AGENT_ICON': "http://dl.profile.line-cdn.net/" + self.getProfile().picturePath, 'AGENT_NAME': texk, 'AGENT_LINK': 'line://ti/p/~{}'.format(self.getProfile().userid)}, contentType = 1).id
        return self.uploadObjTalk(path=path, type='image', returnAs='bool', objId=objectId)

    @loggedIn
    def sendImageWithURL(self, to, url,texk='Image'):
        path = self.downloadFileURL(url, 'path')
        return self.sendImage(to, path,texk)
    def soundcloud(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        if msg.text.lower().startswith("soundcloud "):
            kitsunesplit = self.adityasplittext(msg.text.lower()).split("|")
            r = requests.get('https://soundcloud.com/search?q={}'.format(self.adityasplittext(msg.text.lower())))
            soup = BeautifulSoup(r.text,'html5lib')
            data = soup.find_all(class_='soundTitle__titleContainer')
            data = soup.select('li > h2 > a')
            if len(kitsunesplit) == 1:
                a = ' 「 Soundcloud 」';no=0
                for b in data:
                    no+=1
                    a+= '\n{}. {}'.format(no,b.text)
                self.sendMessage(msg.to,a)
            if len(kitsunesplit) == 2:
                a = data[int(kitsunesplit[1])-1];b = list(a)[0]
                kk = random.randint(0,999)
                self.sendMessage(msg.to,' 「 Soundcloud 」\nJudul: {}\nStatus: Waiting... For Upload'.format(a.text), self.templatefoot('https://soundcloud.com{}'.format(a.get('href')),"http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,a.text))
                hh=subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output {}.mp3 {}'.format(kk,'https://soundcloud.com{}'.format(a.get('href'))))
                try:self.sendAudio(msg.to,'{}.mp3'.format(kk))
                except Exception as e:self.sendMessage(msg.to,' 「 ERROR 」\nJudul: {}\nStatus: {}\nImportant: Try again'.format(a.text,e), self.templatefoot('https://soundcloud.com{}'.format(a.get('href')),"http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,a.text))
                os.remove('{}.mp3'.format(kk))

    def imagegoogle(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        to = msg.to
        data = self.image_search(self.adityasplittext(msg.text))
        try:
            a = data['ou']
            if '.gif' in a:
                return self.sendGIFWithURL(to,a)
            return self.sendImageWithURL(to,a,'Google Image')
            self.sendMention(to,' 「 Image 」\nInfo: Hy @! I get num #{} from #100'.format(aa+1),'',[msg._from])
        except Exception as e:
            self.sendMessage(to,' 「 Error 」\nStatus:\n{}'.format(e))
    def image_search(self, query):
        query = query.replace(' ', "%20")
        url = "https://www.google.com/search?hl=en&site=imghp&tbm=isch&tbs=isz:l&q=" + query
        mozhdr = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
        req = requests.get(url, headers = mozhdr)
        soupeddata = BeautifulSoup(req.content , "lxml")
        images = soupeddata.find_all("div", {"class": "rg_meta notranslate"})
        aa = random.randint(0,len(images))
        try:
            images = json.loads(images[aa].text)
            return images
        except Exception as e:return e

    def imageart(self,msg,wait):
        msg.text = self.mycmd(msg.text,wait)
        to = msg.to
        data = self.adityarequestweb("https://www.artstation.com/search/projects.json?direction=desc&order=published_at&page=1&q={}&show_pro_first=true".format(self.adityasplittext(msg.text)))
        aa = random.randint(0,len(data['data'])-1)
        try:
            a = data['data'][aa]['cover']['medium_image_url']
            self.sendImageWithURL(to,a,'Artstation')
            if data['data'][aa]['description'] == '':sdf = '\nDescription: {}'.format(data['data'][aa]['description'])
            else:sdf = ''
            self.sendMention(to,' 「 Image 」\n | INFO |\nTitle: {}{}\nImportant: Oky @! I get your image num #{} from #{}'.format(data['data'][aa]['title'],sdf,aa+1,data['total_count']),data['data'][aa]['title'],[msg._from])
        except Exception as e:
            self.sendMessage(to,' 「 Error 」\nStatus:\n{}'.format(e))

    @loggedIn
    def sendGIF(self, to, path):
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
        objectId = self.sendMessage(to=to, text=None, contentType = 3).id
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
        return self.talk.findAndAddContactsByMid(0, mid,5,'')

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
    @loggedIn
    def kusumu(self,msg):
        self.sendMessage(msg.to,'Logout From Device')
        self.logout()

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
    def mycmd(self,text,wait):
        cmd = ''
        pesan = text.lower()
        if wait['setkey'] != '':
            if pesan.startswith(wait['setkey']):
                cmd = pesan.replace(wait['setkey']+' ','').replace(wait['setkey'],'')
        else:
            cmd = text
        return cmd
    def adityasplittext(self,text,lp=''):
        separate = text.split(" ")
        if lp == '':adalah = text.replace(separate[0]+" ","")
        elif lp == 's':adalah = text.replace(separate[0]+" "+separate[1]+" ","")
        else:adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
        return adalah

    def AdityaKicks(self,msg):
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            targets = []
            key = eval(msg.contentMetadata["MENTION"])
            key["MENTIONEES"][0]["M"]
            for x in key["MENTIONEES"]:
                targets.append(x["M"])
            for target in targets:
                try:
                    self.kickoutFromGroup(msg.to,[target])
                except Exception as e:
                    self.sendMessage(msg.to,str(e))
    def AdityaSpam(self,wait,msg):
        to = msg.to
        lontong = msg.text
        msg.text = self.mycmd(msg.text,wait)
        ditcmd = msg.text.lower()
        if ditcmd.startswith('spam 1 '):j = int(msg.text.split(' ')[2])
        if ditcmd.startswith('unsend '):j = int(msg.text.split(' ')[1])
        if ditcmd.startswith('spam 2 '):j = int(msg.text.split(' ')[2])
        if ditcmd.startswith('spam 3 '):j = int(msg.text.split(' ')[2])
        if ditcmd.startswith('spam 4 '):j = int(msg.text.split(' ')[2])
        if ditcmd.startswith('spam 5 '):j = int(msg.text.split(' ')[2])
        if ditcmd.startswith('gcall '):j = int(msg.text.split(' ')[1])
        a = [self.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            key = eval(msg.contentMetadata["MENTION"])
            key1 = key["MENTIONEES"][0]["M"]
            nama = [key1]
            if ditcmd.startswith('spam 3 '):b = [self.sendContact(to,key1) for b in a];self.sendMention(to, '「 Spam 」\n@!has been spammed with {} amount of contact♪'.format(j),'',[key1])
            if ditcmd.startswith('spam 4 '):
                if lontong.lower().startswith(wait['setkey']+" "):gss = 7 + len(wait['setkey'])+1
                else:gss = 7 + len(wait['setkey'])
                msg.contentMetadata = {'AGENT_LINK': 'line://ti/p/~{}'.format(self.getProfile().userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + self.getProfile().picturePath,'AGENT_NAME': ' 「 SPAM MENTION 」','MENTION': str('{"MENTIONEES":' + json.dumps([{'S':str(int(key['S'])-gss-len(msg.text.split(' ')[2])-1+13), 'E':str(int(key['E'])-gss-len(msg.text.split(' ')[2])-1+13), 'M':key['M']} for key in eval(msg.contentMetadata["MENTION"])["MENTIONEES"]]) + '}')}
                msg.text = lontong[gss+1+len(msg.text.split(' ')[2]):].replace(lontong[gss+1+len(msg.text.split(' ')[2]):],' 「 Mention 」\n{}'.format(lontong[gss+1+len(msg.text.split(' ')[2]):]))
                b = [self.sendMessages(msg) for b in a]
            if ditcmd.startswith('spam 2 '):[self.giftmessage(key1) for b in a];self.sendMention(to, '「 Spam 」\n@!has been spammed with {} amount of gift♪'.format(j),'',[key1])
            if ditcmd.startswith('gcall '):b = [self.call.inviteIntoGroupCall(to,nama,mediaType=2) for b in a];self.sendMention(to, '「 Gcall 」\n@!has been spammed with {} amount of call♪'.format(j),'',[key1])
        else:
            if ditcmd.startswith('gcall '):
                group = self.getGroup(to);nama = [contact.mid for contact in group.members];b = [self.call.inviteIntoGroupCall(to,nama,mediaType=2) for b in a]
                self.sendMention(to, ' 「 Gcall 」\n@!spammed with {} amount of call to all member♪'.format(j),'',[msg._from])
            if ditcmd.startswith('spam 3 '):
                try:group = self.getGroup(to);nama = [contact.mid for contact in group.members];b = [self.sendContact(to,random.choice(nama)) for b in a]
                except:nama = [to,to];b = [self.sendContact(to,random.choice(nama)) for b in a]
            if ditcmd.startswith('spam 2 '):b = [self.giftmessage(to) for b in a]
            if ditcmd.startswith('spam 1 '):h = [self.sendMessage(to,b) for b in a];self.sendMessage(to, '「 Spam 」\nTarget has been spammed with {} amount of messages♪'.format(j))
            if ditcmd.startswith('unsend '):
                if len(msg.text.split(' ')) == 2:
                    h = wait['Unsend'][to]['B']
                    n = len(wait['Unsend'][to]['B'])
                    for b in h[:j]:
                        try:
                            self.unsendMessage(b)
                            wait['Unsend'][to]['B'].remove(b)
                        except:pass
                    t = len(wait['Unsend'][to]['B'])
                    self.sendMessage(to," 「 Unsend 」\nUnsend {} message".format((n-t)))
                if len(msg.text.split(' ')) >= 3:h = [self.unsendMessage(self.sendMessage(to,self.adityasplittext(msg.text,'s')).id) for b in a]