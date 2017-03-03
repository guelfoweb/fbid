FBid - NOT WORK - DEPRECATED
====

Show info about the author by facebook photo url.

**Usage**

<code>$ fbid.py [fb photo url]</code>


**Download**

<code>$ git clone https://github.com/guelfoweb/fbid.git</code>

Example
=======

**#1 Public Photo**

<code>$ python fbid.py https://scontent-a-lhr.xx.fbcdn.net/hphotos-prn2/t1.0-9/1464008_10151964855117182_1514212999_n.jpg</code>

<pre>
id                 565977181
name               Gianni Amato
first_name         Gianni
last_name          Amato
link               https://www.facebook.com/guelfoweb
gender             male
locale             it_IT
username           guelfoweb
</pre>

**#2 Public Photo**

<code>$ python fbid.py https://fbcdn-sphotos-a-a.akamaihd.net/hphotos-ak-prn2/t31.0-8/1275272_10101026493146301_791186452_o.jpg</code>

<pre>
id                 4
name               Mark Zuckerberg
first_name         Mark
last_name          Zuckerberg
link               https://www.facebook.com/zuck
gender             male
locale             en_US
username           zuck
</pre>

**#3 Friends Only**

<code>$ python fbid.py https://scontent-a-lhr.xx.fbcdn.net/hphotos-prn1/t31.0-8/q71/s720x720/10014193_10202338252912446_446761276_o.jpg</code>

<pre>
fbid               10202338252912446
id                 Friends Only
</pre>
