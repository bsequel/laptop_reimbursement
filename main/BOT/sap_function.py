import win32gui
import win32con
import sys,os, win32com.client
import subprocess
import time


def create_sap_connection(connection_name):
    try:
        os.system("taskkill /im saplogon.exe /F")
    except:
        pass
    
    global session, session1
    error = 'SAP Connection Error'

    path = r"C:\Program Files (x86)\SAP\FrontEnd\SapGui\saplogon.exe"
    subprocess.Popen(path)
    time.sleep(20)
    SapGuiAuto = win32com.client.GetObject("SAPGUI")
    if not type(SapGuiAuto) == win32com.client.CDispatch:
        return error, 1
    
    application = SapGuiAuto.GetScriptingEngine
    if not type(application) == win32com.client.CDispatch:
        SapGuiAuto = None
        return error, 2

    connection = application.OpenConnection(connection_name, True)
    if not type(connection) == win32com.client.CDispatch:
        application = None
        SapGuiAuto = None
        return error, 3
    
    if connection.DisabledByServer == True:
        application = None
        SapGuiAuto = None
        return error, 4
    
    session = connection.Children(0)
    session1 = session
    if not type(session) == win32com.client.CDispatch:
        connection = None
        application = None
        SapGuiAuto = None
        return error, 5
    
    if session.Info.IsLowSpeedConnection == None:
        connection = None
        application = None
        SapGuiAuto = None
        return error, 6
    
    return session


def sap_login(session, username, password):
    session.findById("wnd[0]").maximize()
    session.findById("wnd[0]/usr/txtRSYST-BNAME").text = username
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = password
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").setFocus()
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").caretPosition = 8
    session.findById("wnd[0]").sendVKey(0)
    
    try:
        print("+++++Try")
        session.findById("wnd[1]/usr/radMULTI_LOGON_OPT1").select()
        session.findById("wnd[1]/usr/radMULTI_LOGON_OPT1").setFocus()
        session.findById("wnd[1]").sendVKey(0)
        print("+++++Try")
    except:
        print("+++++Except")
        session.findById("wnd[0]").sendVKey(0)
        print("+++++Except")
    
    return "Success"


