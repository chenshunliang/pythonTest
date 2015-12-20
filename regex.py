import re

r = re.match(r'\d+', '12345')
print(r)
if r:
    print('ok')
else:
    print('not match')


# python 正则表达式
def is_mail(mail):
    matcher = r'^([\w|.]+)@\w+.com|.cn$'
    r = re.match(matcher, mail)
    if r:
        print('ok')
        print(r.group(1))
    else:
        print('not match')


is_mail('someone@gmail.com')
is_mail('bill.gates@microsoft.com')
