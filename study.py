import hashlib
import requests
from urllib import quote
import sys


# passwd = 'Hydsoft123'
# username = 'wuzhiwen@hydsoft.com'
# username = quote(username)
# hl = hashlib.md5()
# hl.update(passwd)
# passwd = hl.hexdigest()
# login_str = 'body=fromBody&usertype=0&password={}&loginId={}'.format(passwd, username)
# print login_str
# session = requests.session()
# res = session.post('http://eln.hydsoft.net:8081/elms/web/login.action?' + login_str)
# print session.cookies
# print res
# print "login"

# session_id = "H003038--SELFM00034--A1101--1--self-made--gmegv"
session_id = sys.argv[1]
# session_id = "H003038--SELFM00034--A1101--1--self-made--gmegv"
pre_str = 'command=putparam&session_id={}&version=2.2&aicc_data='.format(session_id)


paras = '[Core]\r\nLesson_Location=20\nLesson_Status=\nScore=\nTime=00:02:01\nLesson_Progress=100\n[Core_Lesson]\r\n;1-905;2-28;3-351;4-93;5-302;6-21\n'
post_str = quote(paras)

r = requests.post('http://eln.hydsoft.net:8082/aiccRelay/aiccRelayServlet?'+pre_str+quote(paras))
print r.content


# paper_id = 40
# random = [1,2,3]
# for i in random:
#     data = {
#         "paperId": paper_id,
#         "random": i
#     }
#     paras = '&paperId={}&random={}'.format(paper_id, i)
#     url = 'http://eln.hydsoft.net:8081/elms/web/paperQuestionTempSave.action?checkType=submitExam'
#     headers = {"content-type": "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
#         "Referer": "http://eln.hydsoft.net:8081/elms/web/getExamPaperQuestion.action?paperId=40&random=2",
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
#     }
#     r = session.post(url+paras, data=data, headers=headers)
#     with open('answer%s.html'%i, 'w') as f:
#         f.write(r.content)
#     continue

#     url = 'http://eln.hydsoft.net:8081/elms/web/getPaperResult.action?identifier=7760&paperId=40&userId=1231&paperType=1&md5Str=009d5b1999c6240e8998caf3b82ab8f6&view=web'
#     r = session.get(url)
#     with open('answer%s.html'%i, 'w') as f:
#         f.write(r.content)
