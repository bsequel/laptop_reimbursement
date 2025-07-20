import os
import json
import requests
import uuid
from datetime import datetime

from config import *
import config
table_name = config.table_name
url = config.getUrl

# def get_data_from_api_fun1():
#     description = ''' 12.9 inch iPad M2 Pro WiFi + Cellular 256 GB
#     Magic Keyboard for iPad Pro
#     Apple Pencil (2nd Generation)
#     Apple Care+ for iPad Pro '''
    
#     description = str(' '.join(description.split('\n'))).strip()
#     print(description)
#     if len(description) > 50:
#         description1 = description[0:50]
#         description2 = description[50:]
#         if len(description2) > 50:
#             description2 = description2[0:50]
#     else:
#         description1 = description
#         description2 = ''
#     description1 = str(description1).strip()
#     description2 = str(description2).strip()

#     print(description1, type(description1), len(description1))
#     print(description2, type(description2), len(description2))

#     data_dict = {}


#     data_dict["description1"] = description1   # Description  ==>> C
#     data_dict["description2"] = description2    # Description  ==>> C
#     data_dict["serialNumber"] = 'SKQ10MF4T2P'   # serial number ==>> D
#     data_dict["invNumber"] = 'TI/LN/2324/9697'          # invoiceNumber  ==>> M
#     data_dict["costCenter"] = "2010090"   # Pending
#     data_dict["plant"] = "2000"   # Pending
#     data_dict["personalNumber"] = "100019"      # Emp Id  ==>> I
#     data_dict["state"] = "30"   # Pending
#     data_dict["evaluationGroup"] = "1038"       # Fix for laptop
#     data_dict["vendorCode"] = "20000380"   # Pending
#     data_dict["manufacturer"] = "HP"   # Pending
#     data_dict["countryOfOrigins"] = "IN"        # Fixed
#     data_dict["dateOfPuchase"] = "04.03.2024"   # Date of purchase  ==>> B
#     data_dict["reimbValue"] = "159300"          #Reimbersment value  ==>> F
#     data_dict["useLife"] = "3"   # Pending
    
#     return data_dict, "Success"

def filter_usefull_data(data_dict):
    
    valuesList = list(data_dict.values())
    keysList = list(data_dict.keys())
    exceptionList = "Value found:- "
    
    if '' in valuesList or "NA" in valuesList or "na" in valuesList or "None" in valuesList or "none" in valuesList or 'NaN' in valuesList or 'nan'  in valuesList or None in valuesList or "N/A" in valuesList or "n/a" in valuesList:
        if '' in valuesList:
            val = ''
            valIndex = valuesList.index(val)
            keyName = keysList[valIndex]
            if keyName != 'description2':
                exceptionList = f"{exceptionList} {keyName} = {val},"
            
        if "NA" in valuesList:
            val = 'NA'
            valIndex = valuesList.index(val)
            keyName = keysList[valIndex]
            exceptionList = f"{exceptionList} {keyName} = {val},"
            
        if "N/A" in valuesList:
            val = 'N/A'
            valIndex = valuesList.index(val)
            keyName = keysList[valIndex]
            exceptionList = f"{exceptionList} {keyName} = {val},"
        
        if "n/a" in valuesList:
            val = 'n/a'
            valIndex = valuesList.index(val)
            keyName = keysList[valIndex]
            exceptionList = f"{exceptionList} {keyName} = {val},"
            
        if "na" in valuesList:
            val = 'na'
            valIndex = valuesList.index(val)
            keyName = keysList[valIndex]
            exceptionList = f"{exceptionList} {keyName} = {val},"
            
        if "None" in valuesList:
            val = 'None'
            valIndex = valuesList.index(val)
            keyName = keysList[valIndex]
            exceptionList = f"{exceptionList} {keyName} = {val},"
            
        if "none" in valuesList:
            val = 'none'
            valIndex = valuesList.index(val)
            keyName = keysList[valIndex]
            exceptionList = f"{exceptionList} {keyName} = {val},"

        if "NaN" in valuesList:
            val = 'NaN'
            valIndex = valuesList.index(val)
            keyName = keysList[valIndex]
            exceptionList = f"{exceptionList} {keyName} = {val},"
            
        if None in valuesList:
            val = None
            valIndex = valuesList.index(val)
            keyName = keysList[valIndex]
            exceptionList = f"{exceptionList} {keyName} = {val},"
        
        if exceptionList == "Value found:- ":
            return "Success"
        
        else:
            updateQuery = f''' update {table_name} set bot_status = '{exceptionList}' where db_uniq_id = '{data_dict["db_id"]}' and input_date_time = '{data_dict["input_date_time"]}' '''
            cursor.execute(updateQuery)
            con.commit()
        
            return "Fail"
    
    else:
        # print(valuesList)
        return "Success"
    

def get_data_from_api_fun():
    # url = "https://uat.dfccil.com/vig/Fetchdata"

    response = requests.get(url)

    # print("response:- ", response)
    rcvData = response.json()
    print(rcvData)
    # print("Total no. of received data:- ", len(rcvData["Data"]))
    print("Total no. of received data:- ", len(rcvData))
    
    
    receivedDataJson = os.path.join(os.path.join(config.scriptPath,"received_data_from_api"), "receivedJsonData_new.json")
    with open(receivedDataJson, 'w+') as fl:
        json.dump(rcvData, fl, indent=4)
    # input()
    # data = rcvData["Data"]
    data = rcvData
    for i in range(len(data)):
        # print(i, "=====================================", type(data[i]))
        for key in list(data[i].keys()):
            # print(key)
            if str(data[i][key]) in ['nan', 'NaN', 'NAN']:
                data[i][key] = 'NA'
                

    for j in range(len(data)):
        id = str(uuid.uuid4())
        input_time = datetime.now()
        
        db_column_names = ["db_uniq_id", "input_date_time", "asset_number", "co_cgm_office", "cost_of_repair_1", "cost_of_repair_2", "cost_of_repair_3", "date_of_purchase", "do_repair_1", "do_repair_2", "do_repair_3", "description_of_laptop", "device_serial_number", "emp_desg", "emp_id", "emp_name", "excluding_gst", "gst_rate", "invoce_no", "invoice_value", "ref_invoice_no_1", "ref_invoice_no_2", "ref_invoice_no_3", "reimb_value", "requested_date", "sap_refrence_bill_passing", "sap_refrence_bill_passing_1", "sap_refrence_bill_passing_2", "sap_refrence_bill_passing_3", "sap_refrence_date_maker_1", "sap_refrence_date_maker_2", "sap_refrence_date_maker_3", "sap_refrence_maker_1", "sap_refrence_maker_2", "sap_refrence_maker_3", "sap_refrence_payment", "sap_refrence_payment_1", "sap_refrence_payment_2", "sap_refrence_payment_3", "sap_doc_date", "sap_doc_ref_no", "sn", "status", "status_1", "status_2", "status_3", "cost_center", "manufacturer", "plant", "state", "uselife", "vendercode"]
        
        # data_keys = ['Asset_Number', 'CO / CGM Office', 'CostofRepair_1', 'CostofRepair_2', 'CostofRepair_3', 'DOP', 'DORepr_1', 'DORepr_2', 'DORepr_3', 'Description_of_Laptop', 'Device_Serial_Number', 'Emp_Desg', 'Emp_Id', 'Emp_Name', 'Excluding_GST', 'GST_Rate', 'Invoice_No.', 'Invoiced_Value', 'RefInvoiceNo_1', 'RefInvoiceNo_2', 'RefInvoiceNo_3', 'Reimb_Value', 'Requested Date', 'SAPRefrenceBillPassing', 'SAPRefrenceBillPassing_1', 'SAPRefrenceBillPassing_2', 'SAPRefrenceBillPassing_3', 'SAPRefrenceDateMaker_1', 'SAPRefrenceDateMaker_2', 'SAPRefrenceDateMaker_3', 'SAPRefrenceMaker_1', 'SAPRefrenceMaker_2', 'SAPRefrenceMaker_3', 'SAPRefrencePayment', 'SAPRefrencePayment1', 'SAPRefrencePayment2', 'SAPRefrencePayment3', 'SAP_Doc_Date', 'SAP_Doc_Ref_No', 'SN', 'Status', 'Status_1', 'Status_2', 'Status_3', 'costCenter', 'manufacturer', 'plant', 'state', 'uselife', 'vendercode']
        # data_keys = ['Asset_Number', 'CO___CGM_Office', 'CostofRepair_1', 'CostofRepair_2', 'CostofRepair_3', 'DOP', 'DORepr_1', 'DORepr_2', 'DORepr_3', 'Description_of_Laptop', 'Device_Serial_Number', 'Emp_Desg', 'Emp_Id', 'Emp_Name', 'Excluding_GST', 'GST_Rate', 'Invoice_No_', 'Invoiced_Value', 'RefInvoiceNo_1', 'RefInvoiceNo_2', 'RefInvoiceNo_3', 'Reimb_Value', 'Requested_Date', 'SAPRefrenceBillPassing', 'SAPRefrenceBillPassing_1', 'SAPRefrenceBillPassing_2', 'SAPRefrenceBillPassing_3', 'SAPRefrenceDateMaker_1', 'SAPRefrenceDateMaker_2', 'SAPRefrenceDateMaker_3', 'SAPRefrenceMaker_1', 'SAPRefrenceMaker_2', 'SAPRefrenceMaker_3', 'SAPRefrencePayment', 'SAPRefrencePayment1', 'SAPRefrencePayment2', 'SAPRefrencePayment3', 'SAP_Doc_Date', 'SAP_Doc_Ref_No', 'SN', 'Status', 'Status_1', 'Status_2', 'Status_3', 'costCenter', 'manufacturer', 'plant', 'state', 'uselife', 'vendercode']
        data_keys = ['Asset_Number', 'CO___CGM_Office', 'CostofRepair_1', 'CostofRepair_2', 'CostofRepair_3', 'DOP', 'DORepr_1', 'DORepr_2', 'DORepr_3', 'Asset Description', 'Serial  No', 'Emp_Desg', 'Emp_Id', 'Emp_Name', 'Excluding_GST', 'GST_Rate', 'Bill Number', 'Invoiced_Value', 'RefInvoiceNo_1', 'RefInvoiceNo_2', 'RefInvoiceNo_3', 'Reimb_Value', 'Requested_Date', 'SAPRefrenceBillPassing', 'SAPRefrenceBillPassing_1', 'SAPRefrenceBillPassing_2', 'SAPRefrenceBillPassing_3', 'SAPRefrenceDateMaker_1', 'SAPRefrenceDateMaker_2', 'SAPRefrenceDateMaker_3', 'SAPRefrenceMaker_1', 'SAPRefrenceMaker_2', 'SAPRefrenceMaker_3', 'SAPRefrencePayment', 'SAPRefrencePayment1', 'SAPRefrencePayment2', 'SAPRefrencePayment3', 'SAP_Doc_Date', 'SAP_Doc_Ref_No', 'SN', 'Status', 'Status_1', 'Status_2', 'Status_3', 'costCenter', 'manufacturer', 'Company Code', 'state', 'uselife', 'vendercode']
        # "prevData":["Asset_Number", "CO / CGM Office", "CostofRepair_1", "CostofRepair_2", "CostofRepair_3", "DOP", "DORepr_1", "DORepr_2", "DORepr_3", "Description_of_Laptop", "Device_Serial_Number", "Emp_Desg", "Emp_Id", "Emp_Name", "Excluding_GST", "GST_Rate", "Invoice_No.", "Invoiced_Value", "RefInvoiceNo_1", "RefInvoiceNo_2", "RefInvoiceNo_3", "Reimb_Value", "Requested Date", "SAPRefrenceBillPassing", "SAPRefrenceBillPassing_1", "SAPRefrenceBillPassing_2", "SAPRefrenceBillPassing_3", "SAPRefrenceDateMaker_1", "SAPRefrenceDateMaker_2", "SAPRefrenceDateMaker_3", "SAPRefrenceMaker_1", "SAPRefrenceMaker_2", "SAPRefrenceMaker_3", "SAPRefrencePayment", "SAPRefrencePayment1", "SAPRefrencePayment2", "SAPRefrencePayment3", "SAP_Doc_Date", "SAP_Doc_Ref_No", "SN", "Status", "Status_1", "Status_2", "Status_3", "costCenter", "manufacturer", "plant", "state", "uselife", "vendercode"],
        dataValues = []
        
        for key in data_keys:
            value = data[j][key]
            dataValues.append(value)
            
        # for key in data_keys:
        #     try:
        #         value = data[j][key]
        #     except:
        #         value = ''
        #     dataValues.append(value)
        
        dataValues.insert(0, id)
        dataValues.insert(1, input_time)
        
        insertQuery = f''' insert into {table_name}({', '.join(db_column_names)}) values({', '.join(['%s']*len(dataValues))}) '''
        # print(insertQuery)
        cursor.execute(insertQuery, tuple(dataValues))
        con.commit()
        
        
    fetchData = f''' select db_uniq_id, input_date_time, description_of_laptop, device_serial_number, invoce_no, cost_center, plant, emp_id, state, vendercode, manufacturer, date_of_purchase, reimb_value, uselife from {table_name} '''
    cursor.execute(fetchData)
    fetchData = cursor.fetchall()
    
    requiredDataList = []
    for k in range(len(fetchData)):
        data_dict = {}
        
        description = str(fetchData[k][2]).strip()
        # print(description, "====================== Main Description first ==========================")
        
        descriptionList = description.split('\n')
        cleaned_lines = [line.strip() for line in descriptionList]
        description = str(' '.join(cleaned_lines))
        
        # print(description, "====================== Main Description ==========================")
        if len(description) > 50:
            description1 = description[0:50]
            description2 = description[50:]
            if len(description2) > 50:
                description2 = description2[0:50]
        else:
            description1 = description
            description2 = ''
        description1 = str(description1).strip()
        description2 = str(description2).strip()
        
        # print(description1, "========= Description 1 ==========================")
        # print(description2, "========= Description 2 ==========================")
        # input()
        
        date1 = str(fetchData[k][11]).strip()
        date_Obj = datetime.strptime(date1, "%d/%m/%Y")
        formatDate = date_Obj.strftime("%d.%m.%Y")

        data_dict["db_id"] = str(fetchData[k][0]).strip()
        data_dict["input_date_time"] = fetchData[k][1]
        data_dict["description1"] = description1
        data_dict["description2"] = description2
        data_dict["serialNumber"] = str(fetchData[k][3]).strip()
        data_dict["invNumber"] = str(fetchData[k][4]).strip()
        data_dict["costCenter"] = str(fetchData[k][5]).strip() 
        data_dict["plant"] = str(fetchData[k][6]).strip()
        data_dict["personalNumber"] = str(fetchData[k][7]).strip() ### emp_id
        data_dict["state"] = str(fetchData[k][8]).strip()
        data_dict["evaluationGroup"] = "1038"       # Fix for laptop
        data_dict["vendorCode"] = str(fetchData[k][9]).strip()
        data_dict["manufacturer"] = str(fetchData[k][10]).strip()
        data_dict["countryOfOrigins"] = "IN"        # Fixed
        data_dict["dateOfPuchase"] = formatDate
        data_dict["reimbValue"] = str(fetchData[k][12]).strip()
        data_dict["useLife"] = str(fetchData[k][13]).strip()
        
        filterStatus = filter_usefull_data(data_dict)
        if filterStatus == 'Success':
            requiredDataList.append(data_dict)
        else:
            continue
    
    # print(requiredDataList)
    print("No. of data received with required fields:- ", len(requiredDataList))
    # input()
    return requiredDataList, "Success"
        


# deleteQuery = f''' delete from {table_name} '''
# cursor.execute(deleteQuery)
# con.commit()
# input()

# requiredData, status = get_data_from_api_fun()
# print(requiredData, len(requiredData))

