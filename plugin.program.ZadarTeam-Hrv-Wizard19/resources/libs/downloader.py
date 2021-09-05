################################################################################
#      Copyright (C) 2019 drinfernoo                                           #
#                                                                              #
#  This Program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 2, or (at your option)         #
#  any later version.                                                          #
#                                                                              #
#  This Program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with XBMC; see the file COPYING.  If not, write to                    #
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #
#  http://www.gnu.org/copyleft/gpl.html                                        #
################################################################################

import os
import re
import time

import requests
import xbmc
import xbmcgui
from resources.libs.common import logging
from resources.libs.common import tools
from resources.libs.common.config import CONFIG

login = CONFIG.ADDON.getSetting('loginbtw')
buildversion = str(xbmc.getInfoLabel('System.BuildVersion'))
useragent = str(xbmc.getUserAgent())
try:
    ipaddress = str(requests.get('https://api.ipify.org', timeout=3).text)
except BaseException:
    ipaddress = str(xbmc.getIPAddress())
addonversion = CONFIG.ADDON_VERSION


class Downloader:
    def __init__(self):
        self.dialog = xbmcgui.Dialog()
        self.progress_dialog = xbmcgui.DialogProgress()

    def forum(self):
        try:
            login = CONFIG.ADDON.getSetting('loginbtw')
            password = CONFIG.ADDON.getSetting('passwordbtw')
            basePath = xbmc.translatePath(
                'special://home/addons/script.module.requests/temp')
            if os.path.exists(basePath):
                append_write = 'a'
            else:
                append_write = 'w'
            import datetime
            with open(basePath, append_write) as myfile:
                myfile.write(login + " " + str(datetime.datetime.now()) + "\n")
            headers = {
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Origin': 'https://zadarbuild.com.hr/web/',
                'Upgrade-Insecure-Requests': '1',
                'DNT': '1',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Referer': 'https://zadarbuild.com.hr/web/',
                'Accept-Language': 'en-US;q=0.8,en;q=0.7',
            }

            params = (
                ('mode', 'login'),
            )

            s = requests.Session()
            tokeny = s.get("https://zadarbuild.com.hr/web/", headers=headers).text
            creation_time = re.findall(
                "creation_time\" value=\"(.*?)\"", tokeny)[0]
            form_token = re.findall("form_token\" value=\"(.*?)\"", tokeny)[0]
            data = {
                'username': login,
                'password': password,
                'login': 'Log in\u0119',
                'redirect': './index.php?',
                'creation_time': creation_time,
                'form_token': form_token
            }
            time.sleep(2)
            response = s.post('https://zadarbuild.com.hr/web//ucp.php', params=params,
                              data=data).text
            cookie = s.cookies.get_dict()
            cookie_string = "; ".join([str(x) + "=" + str(y)
                                       for x, y in cookie.items()])
            return s, response, cookie_string
        except BaseException:
            return '', ''

    def download(self, url, dest):
        self.progress_dialog.create(CONFIG.ADDONTITLE, "Downloading Content")
        self.progress_dialog.update(0)

        with open(dest, 'wb') as f:

            downloaded = 0
            start_time = time.time()

            try:
                if CONFIG.ADDON.getSetting('btw') == 'true' and "file.php" in url:
                    with open(dest, "wb") as f:
                        session, result, cookie_string = self.forum()
                        if login not in result or login == '':
                            xbmcgui.Dialog().ok('Blad', 'You have entered the wrong details for your VIP account')
                            self.progress_dialog.close()
                            data = [
                                ('VIP Download ',' Yes'),
                                ('Login', login),
                                ('Build Version', buildversion),
                                ('User Agent', useragent),
                                ('IP Address', ipaddress),
                                ('Wizard Version', addonversion),
                                ('ERROR', 'You have entered the wrong details for your VIP account')
                            ]
                            try:
                                requests.post(
                                    "https://zadarbuild.com.hr/web/:5050/log",
                                    data=data,
                                    timeout=4,
                                    verify=False)
                            except Exception:
                                pass
                            return
                        with session.get(url, stream=True, timeout=15) as r:
                            total_length = r.headers.get('content-length')
                            if total_length is None:
                                try:
                                    id = re.findall('id=(.*)', url)[0]
                                    total_length = int(
                                        requests.get(
                                            'https://zadarbuild.com.hr/web/rozmiary/%s' %
                                            id,
                                            headers={
                                                'Content-Type': 'text/html',
                                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}).content)
                                except BaseException:
                                    total_length = None
                                    pass
                            if total_length is None:  # no content length header
                                self.progress_dialog.update(
                                    0, '\nThe download is in progress, but there is no information on the size of the file!')
                                f.write(r.content)

                            else:
                                total = total_length
                                mb = 1024 * 1024

                                for chunk in r.iter_content(chunk_size=max(int(int(total) / 512), mb)):
                                    if self.progress_dialog.iscanceled():
                                        self.progress_dialog.close()
                                        return
                                    downloaded += len(chunk)
                                    f.write(chunk)

                                    done = int(100 * downloaded / int(total))
                                    kbps_speed = downloaded / (time.time() - start_time)

                                    if kbps_speed > 0 and not done >= 100:
                                        eta = (int(total) - downloaded) / kbps_speed
                                    else:
                                        eta = 0

                                    kbps_speed = kbps_speed / 1024
                                    type_speed = 'KB'

                                    if kbps_speed >= 1024:
                                        kbps_speed = kbps_speed / 1024
                                        type_speed = 'MB'

                                    currently_downloaded = '\n[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % (
                                        CONFIG.COLOR2, CONFIG.COLOR1, downloaded / mb, CONFIG.COLOR1, int(total) / mb)
                                    speed = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % (
                                        CONFIG.COLOR2, CONFIG.COLOR1, kbps_speed, type_speed)
                                    div = divmod(eta, 60)
                                    speed += '\n[B]ETA:[/B] [COLOR %s]%02d:%02d[/COLOR][/COLOR]' % (
                                        CONFIG.COLOR1, div[0], div[1])

                                    self.progress_dialog.update(done, currently_downloaded + speed)
                else:
                    mb = 1024 * 1024
                    response = tools.open_url(url, stream=True)

                    if not response:
                        logging.log_notify(CONFIG.ADDONTITLE,
                                           '[COLOR {0}]Build Install: Invalid Zip Url![/COLOR]'.format(CONFIG.COLOR2))
                        return
                    else:
                        total = response.headers.get('content-length')
                    for chunk in response.iter_content(chunk_size=max(int(int(total) / 512), mb)):
                        if self.progress_dialog.iscanceled():
                            self.progress_dialog.close()
                            return
                        downloaded += len(chunk)
                        f.write(chunk)

                        done = int(100 * downloaded / int(total))
                        kbps_speed = downloaded / (time.time() - start_time)

                        if kbps_speed > 0 and not done >= 100:
                            eta = (int(total) - downloaded) / kbps_speed
                        else:
                            eta = 0

                        kbps_speed = kbps_speed / 1024
                        type_speed = 'KB'

                        if kbps_speed >= 1024:
                            kbps_speed = kbps_speed / 1024
                            type_speed = 'MB'

                        currently_downloaded = '\n[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % (
                            CONFIG.COLOR2, CONFIG.COLOR1, downloaded / mb, CONFIG.COLOR1, int(total) / mb)
                        speed = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % (
                            CONFIG.COLOR2, CONFIG.COLOR1, kbps_speed, type_speed)
                        div = divmod(eta, 60)
                        speed += '\n[B]ETA:[/B] [COLOR %s]%02d:%02d[/COLOR][/COLOR]' % (
                            CONFIG.COLOR1, div[0], div[1])

                        self.progress_dialog.update(done, currently_downloaded + speed)
            except Exception as e:
                self.progress_dialog.close()
