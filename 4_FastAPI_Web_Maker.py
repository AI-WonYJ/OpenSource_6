#  -*- coding: utf-8 -*-
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

# addlog("on/on/on")로 사용하기만 하면 자동으로 됨 주의할 점은 만약에 외부에서 해당함수 사용할 경우에는 파일 경로 변환해줄것 fs,f,st2부분
def addlog():
    # string="on/off/0"
    with open("info.txt", "r", encoding='UTF8') as file:
        line=file.readline().split('/')
    for i in range(0,len(line)):
        if line[i]=='g':
            line[i]='on'
        elif line[i]=='b':
            line[i]='off'
        else:
            line[i]='0'
    string=line[0]+"/"+line[1]
    fs = open("state.txt", 'r', encoding='UTF8')
    st = fs.read().split()
    fs.close()
    alist = string.split("/")
    for i in range(len(alist)):
        if alist[i] != st[i]:
            f = open("logfolder/log.txt", "a", encoding='UTF8')
            f.write("%d번째 자리 상태" % (i + 1) + " "
                    + str(st[i]) + "-->" + str(alist[i]) +
                    "  " + str(datetime.now()) + '\n')
            st[i] = alist[i]
            f.close()
    st2 = open("state.txt", "w")
    st2.write(st[0] + ' ' + st[1] )
    st2.close()

# 웹 출력
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def mainreturn(request: Request):
    addlog()
    fs = open("state.txt", 'r', encoding='UTF8')
    statemain = fs.read().split()
    fs.close()
    fl = open("logfolder/log.txt", 'r', encoding='UTF8')
    inform = list(fl.readlines())
    if len(inform) > 8:
        inform = inform[:8]
    fl.close()
    print(inform)
    print(len(inform))
    return templates.TemplateResponse("main.html", {"request": request, "machine1st": statemain[0], "machine2st": statemain[1], "informationlist": list(inform)})

@app.get("/main.html")
async def mainreturn_nav(request: Request):
    addlog()
    fs = open("state.txt", 'r', encoding='UTF8')
    statement = fs.read().split()
    fs.close()
    fl = open("logfolder/log.txt", 'r', encoding='UTF8')
    inform = list(fl.readlines())
    if len(inform) > 7:
        inform = inform[:7]
    return templates.TemplateResponse("main.html", {"request": request, "machine1st": statement[0], "machine2st": statement[1], "imformationlist": inform})

@app.get("/main2.html")
async def main2return_nav(request: Request):
    fl = open("logfolder/log.txt", 'r', encoding='UTF8')
    inform = list(fl.readlines())
    if len(inform) > 21:
        inform = inform[:21]
    return templates.TemplateResponse("main2.html", {"request": request, "imformationlist": inform})