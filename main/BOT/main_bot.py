import os
import re


from sap_function import create_sap_connection, sap_login
from get_data_from_api import get_data_from_api_fun
from tcode_as01 import sap_tcode_as01
from tcode_abzon import sap_tcode_abzon
from config import *
import config

table_name = config.table_name
userName = config.sap_user_name
password = config.sap_password
connectionName = config.sap_connection_name

screenShotFolderPth = config.screenShotFolderPth
# as01path = config.as01path
# abzonpath = config.abzonpath

def clean_all_file_and_data():
    # for file in os.listdir(screenShotFolderPth):
    #     filePath = os.path.join(screenShotFolderPth, file)
    #     os.remove(filePath)
        
    # for file in os.listdir(as01path):
    #     filePath = os.path.join(as01path, file)
    #     os.remove(filePath)
        
    # for file in os.listdir(abzonpath):
    #     filePath = os.path.join(abzonpath, file)
    #     os.remove(filePath)
    # if os.path.exists(as01path):
    #     os.remove(as01path)
    
    # if os.path.exists(abzonpath):
    #     os.remove(abzonpath)
    
    deleteQuery = f''' delete from {table_name} '''
    cursor.execute(deleteQuery)
    con.commit()

clean_all_file_and_data()


received_data, getDataSatatus = get_data_from_api_fun()

print("Received Data:-\n", received_data, len(received_data))

if len(received_data) > 0:
    
    session = create_sap_connection(connectionName)
    print(session)
    ##############################
    loginSatus = sap_login(session, userName, password)
    print(loginSatus)
    
    sapFlag = 1
    
    for i in range(len(received_data)):
        data_dict = received_data[i]
        print(data_dict["description1"])
        print(data_dict["description2"])
        if sapFlag == 0:
            session = create_sap_connection(connectionName)
            print(session)
            ##############################
            loginSatus = sap_login(session, userName, password)
            print(loginSatus)

        as01PostingMsg, as01PostingNo, as01Status = sap_tcode_as01(session, data_dict)
        
        if as01Status == "Success":
            print("Message from sa01 Tcode:- ", as01PostingMsg)
            data_dict["as01PostingMsg"] = as01PostingMsg
            data_dict["as01PostingNo"] = as01PostingNo
            data_dict["as01Status"] = as01Status
            
            abzonPostingMsg, abzonPostingNo, abzonStatus = sap_tcode_abzon(session, data_dict)
            print("Message from abzon Tcode:- ", abzonPostingMsg)
            
            if abzonStatus == "Success":
                data_dict["abzonPostingMsg"] = abzonPostingMsg
                data_dict["abzonPostingNo"] = abzonPostingNo
                data_dict["abzonStatus"] = abzonStatus
                
                updateQuery2 = f''' update {table_name} set bot_status = 'Processed', as01_msg =  '{as01PostingMsg}', as01_doc_no = '{as01PostingNo}', abzon_msg = '{abzonPostingMsg}', abzon_doc_no = '{abzonPostingNo}' where db_uniq_id = '{data_dict["db_id"]}' and input_date_time = '{data_dict["input_date_time"]}' '''
                cursor.execute(updateQuery2)
                con.commit()
            
            else:
                sap_flag = 0
                
                if abzonPostingMsg == "":
                    abzon_msg = "An Error found while posting AS01"
                else:
                    abzon_msg = abzonPostingMsg
                    
                updateQuery2 = f''' update {table_name} set bot_status = 'An Error found while posting AS01', as01_msg =  '{as01PostingMsg}', as01_doc_no = '{as01PostingNo}', abzon_msg = '{abzon_msg}', abzon_doc_no = '{abzon_msg}' where db_uniq_id = '{data_dict["db_id"]}' and input_date_time = '{data_dict["input_date_time"]}' '''
                cursor.execute(updateQuery2)
                con.commit()
        
        else:
            sap_flag = 0
            
            if as01PostingMsg == "":
                as01_msg = "An Error found while posting AS01"
            else:
                as01_msg = as01PostingMsg
                
            updateQuery1 = f''' update {table_name} set bot_status = 'An Error found while posting AS01', as01_msg = '{as01_msg}', as01_doc_no = '{as01_msg}', abzon_msg = 'An Error found while posting AS01', abzon_doc_no = 'An Error found while posting AS01' where db_uniq_id = '{data_dict["db_id"]}' and input_date_time = '{data_dict["input_date_time"]}' '''
            cursor.execute(updateQuery1)
            con.commit()
            
    try:
        os.system("taskkill /im saplogon.exe /F")
    except:
        pass
    # input('stop')
    
else:
    print("No any data required data found")
    