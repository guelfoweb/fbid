#!/usr/bin/env python

# Facebook Photo ID - by Gianni 'guelfoweb' Amato
# Show info by facebook photo url or photo name
# Version 2.0
# Example:
# $ python fbid.py https://scontent-a-lhr.xx.fbcdn.net/hphotos-prn2/t1.0-9/1464008_10151964855117182_1514212999_n.jpg

import re
import sys
import json
import urllib2

def validate_photo_url(url):
	photo_format = "[0-9]*_[0-9]*_[0-9]*_[a-z].(jpg|png)"
	match = re.search(photo_format, url, re.IGNORECASE)
	if match:
		return True
	else:
		exit('Invalid url or filename.')

def show_postid(url):
	postid = url.split('_')
	return postid[1]

def check_info(postid):
	photourl = "https://www.facebook.com/photo.php?fbid="+postid
	ownerid = "ownerid:\"[0-9]*"
	ownername = "ownername:\".*\""
	result = []

	opener = urllib2.build_opener()
	opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
	data = opener.open(photourl).read()

	if data:
		# ownerId
		match_ownerid = re.findall(ownerid, data, re.IGNORECASE)
		if match_ownerid:
			profileid = match_ownerid[0].split('"')[1]
			result.append(profileid)
		else:
			result = {'photourl': photourl, 'status': 'Friends Only'}
			result = json.dumps(result, indent=4, separators=(',', ': '))
			exit(result)

		# ownerName
		match_ownername = re.findall(ownername, data, re.IGNORECASE)
		if match_ownername:
			ownername = match_ownername[0].split('"')
			ownername = ownername[1]
			result.append(ownername)

		return result

if __name__ == "__main__":
	
	if len(sys.argv) != 2:
		exit(sys.argv[0]+' <photo url or photo name>')

	url = sys.argv[1]
	validate_photo_url(url)
	postid = show_postid(url)
	info = check_info(postid)

	if info:
		profileid = 'https://www.facebook.com/'+info[0]
		name = info[1]
		photourl = "https://www.facebook.com/photo.php?fbid="+postid

		result = {'name': name, 'profileid': profileid, 'status': 'Public Photo', 'photourl': photourl}
		exit(json.dumps(result, indent=4, separators=(',', ': ')))
	else:
		exit('Error')
