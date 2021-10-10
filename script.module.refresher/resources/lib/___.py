import xbmc, xbmcaddon, xbmcgui, xbmcvfs
from resources.lib import simplejson as json
from resources.lib import requests
import uuid
import os
import xml.etree.ElementTree as ET
def pvr():
    try:
        __addon__ = xbmcaddon.Addon(id='pvr.zadarteamw64mat')
    except:
        pass
    try:
        __addon__ = xbmcaddon.Addon(id='pvr.zadarteamaarch64mat')
    except:
        pass
    try:
        __addon__ = xbmcaddon.Addon(id='pvr.zadarteamarmv7mat')
    except:
        pass
    try:
        __addon__ = xbmcaddon.Addon(id='pvr.zadarteamwi686mat')
    except:
        pass
    __addondir__ = xbmc.translatePath( __addon__.getAddonInfo('profile') )
    pth = os.path.join(__addondir__, 'settings.xml')
    return pth
u = 'http://glade.eu.pythonanywhere.com/'
def s(valid=True):
    if valid:
        L = None
        P = ET.XMLParser(encoding="utf-8")
        aa = xbmcaddon.Addon(id='script.module.refresher')
        dir = xbmc.translatePath(aa.getAddonInfo('profile'))
        try:
            pth = os.path.join(dir, 'settings.xml')
            tree = ET.parse(pth, parser=P)
            root = tree.getroot()
            for id in root:
                if id.attrib['id'] == 'licence_key':
                    L = id.text
        except FileNotFoundError:
            L = 'Nema licence'
        finally:
            return L

def get_id_from_server():
    pp = {}
    pp['getmac'] = True
    m = requests.post('http://bloodsousage.pythonanywhere.com/getid', json=json.dumps(pp))
    P = ET.XMLParser(encoding="utf-8")
    aa = xbmcaddon.Addon(id='script.module.refresher')
    dir = xbmc.translatePath(aa.getAddonInfo('profile'))
    try:
        pth = os.path.join(dir, 'settings.xml')
        tree = ET.parse(pth, parser=P)
        root = tree.getroot()
        for id in root:
            if id.attrib['id'] == 'mac':
                if id.text == None:
                    id.text = m.text
                    
    except FileNotFoundError:
        pass
    else:
        new2_xml = ET.tostring(root, encoding='utf-8')
        file = xbmcvfs.File(pth, 'wb') #xbmcvfs.File
        file.write(new2_xml)
        file.close()

def get_id_from_system():
    P = ET.XMLParser(encoding="utf-8")
    aa = xbmcaddon.Addon(id='script.module.refresher')
    dir = xbmc.translatePath(aa.getAddonInfo('profile'))
    try:
        pth = os.path.join(dir, 'settings.xml')
        tree = ET.parse(pth, parser=P)
        root = tree.getroot()
        for id in root:
            if id.attrib['id'] == 'mac':
                mac = id.text
    except FileNotFoundError:
        mac = 'None'
    finally:
        return mac

def rs(ss, valid):
  if valid:
    get_id_from_server()
    mac = get_id_from_system()
    sy = {}
    sy['licencekey'] = ss
    if mac != None:
        sy['mac'] = mac
    else:
        sy['mac'] = 'None'
    result = requests.post('http://bloodsousage.pythonanywhere.com/activatelicence', json=json.dumps(sy))
    return result.text