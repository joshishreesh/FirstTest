from django.shortcuts import render
from erplogin.models import sqlserverconn
from django.forms.models import model_to_dict
import pyodbc
import base64

def login(request):
    return render(request, "index.html")

def connsql(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=UNICORN\SQLSERVER19;'
                        'Database=MIPLERP;'
                        'Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute("select EMPLOYEE_CODE,FIRST_NAME,LAST_NAME,LOGIN_PASSKEY from MST_EMPLOYEE_MASTER order by FIRST_NAME")
    result= cursor.fetchall()
    return render(request,'index.html',{'sqlserverconn':result})

def loginuser(request):

    username=request.POST['userid']
    password=request.POST['pass']
    validlogin=checkLogin(username=str(username),password=str(password))
    if (validlogin==True):
        return render(request, "dashboard.html")
    else:
        return render(request, "index.html")

def checkLogin(username:str,password:str):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=UNICORN\SQLSERVER19;'
                        'Database=MIPLERP;'
                        'Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute("select LOGIN_PASSKEY from MST_EMPLOYEE_MASTER where isactive=0 and EMPLOYEE_CODE= %s " % username)
    row=cursor.fetchval() 
       
    pass1byte=password.encode('ascii')
    baseByte=base64.b64encode(pass1byte)
    baseString=baseByte.decode('ascii')

    if (row==baseString):
        return True
    else:
        return False
