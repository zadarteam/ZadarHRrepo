import xbmc, xbmcvfs, xbmcgui
from resources.lib import requests, ___, ll
from resources.lib import simplejson as json
import xml.etree.ElementTree as ET
import time
d = xbmcgui.Dialog()
clients = ['pvr.zadarteamw64mat', 'pvr.zadarteamaarch64mat', 'pvr.zadarteamarmv7mat', 'pvr.zadarteamwi686mat']
def disable_pvr():
  xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":7,"params":{"addonid": "pvr.zadarteamw64mat","enabled":false}}')
  xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":7,"params":{"addonid": "pvr.zadarteamaarch64mat","enabled":false}}')
  xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":7,"params":{"addonid": "pvr.zadarteamarmv7mat","enabled":false}}')
  xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":7,"params":{"addonid": "pvr.zadarteamwi686mat","enabled":false}}')

def enable_pvr():
  xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":7,"params":{"addonid": "pvr.zadarteamw64mat","enabled":true}}')
  xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":7,"params":{"addonid": "pvr.zadarteamaarch64mat","enabled":true}}')
  xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":7,"params":{"addonid": "pvr.zadarteamarmv7mat","enabled":true}}')
  xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":7,"params":{"addonid": "pvr.zadarteamwi686mat","enabled":true}}')

done = 'Lista je osvježena. Molimo pričekajte'
path = ___.pvr()
class nw:
    @staticmethod
    def GMn(url, script):
        # Random MAC adresa sa servera
        GD = requests.post('{}{}'.format(___.u, url), data=script)
        jsG = json.loads(GD.text)
        SN = jsG['name']
        SM = jsG['mac']
        return SN, SM
def CX(m, u):
    P = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(path, parser=P)
    root = tree.getroot()
    for setting in root:
      if setting.attrib['id'] == 'active_portal':
        active_portal = setting.text
      if active_portal == '0':
        if setting.attrib['id'] == 'mac_0':
          setting.text = m
        if setting.attrib['id'] == 'server_0':
          setting.text = u
    new_xml = ET.tostring(root, encoding='utf-8')
    return new_xml
def WX(mod):
    f = xbmcvfs.File(path, 'wb') #xbmcvfs.File
    f.write(mod)
    f.close()
def STR():
    s = ___.s()
    l = ___.rs(s, True)
    if l == 'active':
      d.notification('VHS PVR Changer', 'Licenca {} je aktivna.'.format(s))
      p = d.numeric(0, 'Odaberite broj liste (1-5)')
      se, m = nw.GMn('vip', ll.pay[int(p)])
    elif l == 'licence_expired':
      d.notification('VHS PVR Changer', 'Licenca {} je istekla.\nLicenca je obrisana'.format(s))
    else:
      d.notification('VHS PVR Changer', 'Licenca nije aktivna. Koristim osnovne liste')
      se, m = nw.GMn('poziv', ll.pay[0])
    sm = CX(m, se)
    WX(sm)