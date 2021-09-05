import os

import xbmc
import xbmcaddon
import xbmcgui

#########################################################
#         Global Variables - DON'T EDIT!!!              #
#########################################################
ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
PATH = xbmcaddon.Addon().getAddonInfo('path')
ART = os.path.join(PATH, 'resources', 'media')
#########################################################

#########################################################
#        User Edit Variables                            #
#########################################################
ADDONTITLE = 'Zadar Team Wizard'
BUILDERNAME = 'ZTW'
EXCLUDES = [ADDON_ID]
# Text File with build info in it.
BUILDFILE = 'http://zadarbuild.com.hr/BuildzipZD/KODI-19/builds.txt'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE = 'http://'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE = 'Youtube help and tips'
YOUTUBEFILE = 'http://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE = 'http://'
#########################################################

#########################################################
#        Theming Menu Items                             #
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'https://buntic-team.com/photo/icon.png'
# Leave as http:// for default icon
ICONBUILDS = 'http://zadarbuild.com.hr/slike/icon.png'
ICONMAINT = 'http://zadarbuild.com.hr/slike/icon.png'
ICONSPEED = os.path.join(ART, 'speed.png')
ICONAPK = 'http://zadarbuild.com.hr/slike/icon.png'
ICONADDONS = 'http://zadarbuild.com.hr/slike/icon.png'
ICONYOUTUBE = 'http://zadarbuild.com.hr/slike/icon.png'
ICONSAVE = 'http://zadarbuild.com.hr/slike/icon.png'
ICONTRAKT = 'http://zadarbuild.com.hr/slike/icon.png'
ICONREAL = 'http://zadarbuild.com.hr/slike/icon.png'
ICONLOGIN = 'http://zadarbuild.com.hr/slike/icon.png'
ICONCONTACT = 'http://zadarbuild.com.hr/slike/icon.png'
ICONSETTINGS = 'http://zadarbuild.com.hr/slike/icon.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS = 'No'
# Character used in seperator
SPACER = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1 = 'red'
COLOR2 = 'blue'
# Primary menu items   / {0} is the menu item and is required
THEME1 = u'[COLOR {color1}][I]([COLOR {color1}][B]Z.[/B][/COLOR][COLOR {color2}][B]T.[/B][COLOR {color1}][/COLOR][COLOR {color1}][B]W[/B])[/I][/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(
    color1=COLOR1, color2=COLOR2)
# Build Names          / {0} is the menu item and is required
THEME2 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# Alternate items      / {0} is the menu item and is required
THEME3 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# Current Build Header / {0} is the menu item and is required
THEME4 = u'[COLOR {color1}]Current Build:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Current Theme Header / {0} is the menu item and is required
THEME5 = u'[COLOR {color1}]Current Theme:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT = 'No'
# You can add \n to do line breaks
CONTACT = xbmcaddon.Addon().getLocalizedString(32039)
# Images used for the contact window.  http:// for default icon and fanart
CONTACTICON = 'https://buntic-team.com/photo/icon.png'
CONTACTFANART = 'https://buntic-team.com/photo/fanart.jpg'
#########################################################

#########################################################
#        Auto Update For Those With No Repo             #
#########################################################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE = 'Yes'
#########################################################

#########################################################
#        Auto Install Repo If Not Installed             #
#########################################################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL = 'Yes'
# Addon ID for the repository
REPOID = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML = 'http://'
# Url to folder zip is located in
REPOZIPURL = 'http://'
#########################################################

#########################################################
#        Notification Window                            #
#########################################################
# Enable Notification screen Yes or No
ENABLE = 'No'
# Url to notification file
NOTIFICATION = 'http://'
# Use either 'Text' or 'Image'
HEADERTYPE = 'Text'
# Font size of header
FONTHEADER = 'Font14'
HEADERMESSAGE = '[COLOR red][B]Open[/B][/COLOR]Wizard'
# url to image if using Image 424x180
HEADERIMAGE = 'http://'
# Font for Notification Window
FONTSETTINGS = 'Font13'
# Background for Notification Window
BACKGROUND = 'http://zadarbuild.com.hr/slike/fanart.jpg'
#########################################################
