
# study in one second

steps:

1. Go to 学习中心， 点击学习一门课程
2. 进入课程页面后， F12打开浏览器调试台， 点击network的tab
3. 刷新当前页面， 并在network的搜索里搜索： getAiccContent.action
    查看response，差不多长这样:
    ```
    <script>
	window.location.href = "http://eln.hydsoft.net:8082/ftp/selfmade/preindex.htm?aicc_sid=H003038--SELFM00037--A1101--1--self-made--onhxl&aicc_url=eln.hydsoft.net%3A8082%2FaiccRelay%2FaiccRelayServlet&aujid=SELFM00037001001000X020001&CBTLAUNCH=SELFM00037_X_A1101_X_http%3A%2F%2Feln.hydsoft.net%3A8082%2Fftp%2Fselfmade%2FSELFM00037%2FSELFM00037_B11_8v4f_File.swf%26convert%3Dtrue";
    </script>
    ```
    注意这一段：
    ```
    aicc_sid=H003038--SELFM00037--A1101--1--self-made--onhxl
    ```
    我们复制等号后面的value值
5. run command, 参数为我们刚刚复制的值
    ```
    python study.py H003038--SELFM00037--A1101--1--self-made--onhxl
    ```
6. 回去检查课程，已完成100%学习进度
7. 参加考试， 第一遍交白卷， 查看答案 :)