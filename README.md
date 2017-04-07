FB Photo Id
====

Show info about the author by facebook photo url or filename.

**Usage**

<code>$ fbid.py [photo url or photo name]</code>


**Download**

<code>$ git clone https://github.com/guelfoweb/fbid.git</code>

Example
=======

**#1 Public Photo**

<code>$ python fbid.py https://scontent-mxp1-1.xx.fbcdn.net/v/t1.0-9/1464008_10151964855117182_1514212999_n.jpg?oh=c958a419eba666f6055dfb9198488949&oe=5951B763</code>

<code>$ python fbid.py 1464008_10151964855117182_1514212999_n.jpg</code>

<pre>
{
    "status": "Public Photo",
    "profileid": "https://www.facebook.com/565977181",
    "name": "Gianni Amato",
    "photourl": "https://www.facebook.com/photo.php?fbid=10151964855117182"
}
</pre>

**#2 Public Photo**

<code>$ python fbid.py https://scontent-mxp1-1.xx.fbcdn.net/v/t1.0-9/17796398_10103620488783251_6704415260282737996_n.jpg?oh=dfef5c1b69beb09fd050e7a5875ca647&oe=5950CA1E</code>

<code>$ python fbid.py 17796398_10103620488783251_6704415260282737996_n.jpg</code>

<pre>
{
    "status": "Public Photo",
    "profileid": "https://www.facebook.com/4",
    "name": "Mark Zuckerberg",
    "photourl": "https://www.facebook.com/photo.php?fbid=10103620488783251"
}
</pre>

**#3 Friends Only**

<code>$ python fbid.py https://scontent-mxp1-1.xx.fbcdn.net/v/t1.0-9/17352554_10212767417642835_6881613682551204540_n.jpg?oh=a0254e4f3fe71df0ee8b9d5b7e8c1239&oe=5992E344</code>


<code>$ python fbid.py 17352554_10212767417642835_6881613682551204540_n.jpg</code>

<pre>
{
    "status": "Friends Only",
    "photourl": "https://www.facebook.com/photo.php?fbid=10212767417642835"
}
</pre>
