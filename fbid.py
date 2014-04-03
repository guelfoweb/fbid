#!/usr/bin/env python

# Facebook ID - by Gianni 'guelfoweb' Amato
# Show info by facebook photo url
# Example:
# $ python fbid.py https://scontent-a-lhr.xx.fbcdn.net/hphotos-prn2/t1.0-9/1464008_10151964855117182_1514212999_n.jpg

import sys
import re
import urllib2
import json

def internet_on():
    try:
        response=urllib2.urlopen('http://74.125.228.100',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

def validate_photo_url(url):
	match = re.search("[0-9]*_[0-9]*_[0-9]*_[a-z].jpg", url, re.IGNORECASE)
	if match:
		return True
	else:
		return False

def show_fbid(url):
	url_split = url.split('_')
	return url_split[1]

def check_profile_id(fbid):
	data = urllib2.urlopen("https://www.facebook.com/photo.php?fbid="+fbid).read()
	if data:
		match = re.findall("owner\":[0-9]*", data, re.IGNORECASE)
		if match:			
			profileid = match[0].split(':')
			return profileid[1]
		else:
			return False

def show_profile_id(profileid):
	info = []
	data = urllib2.urlopen("https://graph.facebook.com/"+profileid).read()
	if data:
		decoded = json.loads(data)
		id         = decoded['id']
		name       = decoded['name']
		try:
			first_name = decoded['first_name']
			last_name  = decoded['last_name']
			link       = decoded['link']
			gender     = decoded['gender']
			locale     = decoded['locale']
			username = decoded['username']
		except:
			info.append([id,name])
			return info

		info.append([id,name,first_name,last_name,link,gender,locale,username])
		return info
	else:
		return False

def help():
	print "Facebook ID photo url analysis"
	print "Gianni 'guelfoweb' Amato"
	print
	print "Usage: ".ljust(4), "fbid.py <photo url>"
	sys.exit(0)
	
# ________MAIN_______

if len(sys.argv) == 1 or len(sys.argv) > 2:
	help()
	
if len(sys.argv) == 2:
	url = sys.argv[1]

if internet_on() and validate_photo_url(url):
	fbid = show_fbid(url)
	
	profileid = check_profile_id(fbid)
	if profileid == False:
		print "fbid".ljust(18), fbid
		print "id".ljust(18), "Friends Only"
		sys.exit(0)
		
	info = show_profile_id(profileid)
	
	# Page Profile
	if len(info[0]) == 2:
		print "id".ljust(18), info[0][0]
		print "name".ljust(18), info[0][1]
		print "link".ljust(18), "https://www.facebook.com/"+info[0][0]
		sys.exit(0)
		
	# User Profile
	print "id".ljust(18), info[0][0]
	print "name".ljust(18), info[0][1]
	print "first_name".ljust(18), info[0][2]
	print "last_name".ljust(18), info[0][3]
	print "link".ljust(18), info[0][4]
	print "gender".ljust(18), info[0][5]
	print "locale".ljust(18), info[0][6]
	print "username".ljust(18), info[0][7]
