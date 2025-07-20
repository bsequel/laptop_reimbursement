# data1 = ['Asset_Number', 'CO / CGM Office', 'CostofRepair_1', 'CostofRepair_2', 'CostofRepair_3', 'DOP', 'DORepr_1', 'DORepr_2', 'DORepr_3', 'Description_of_Laptop', 'Device_Serial_Number', 'Emp_Desg', 'Emp_Id', 'Emp_Name', 'Excluding_GST', 'GST_Rate', 'Invoice_No.', 'Invoiced_Value', 'RefInvoiceNo_1', 'RefInvoiceNo_2', 'RefInvoiceNo_3', 'Reimb_Value', 'Requested Date', 'SAPRefrenceBillPassing', 'SAPRefrenceBillPassing_1', 'SAPRefrenceBillPassing_2', 'SAPRefrenceBillPassing_3', 'SAPRefrenceDateMaker_1', 'SAPRefrenceDateMaker_2', 'SAPRefrenceDateMaker_3', 'SAPRefrenceMaker_1', 'SAPRefrenceMaker_2', 'SAPRefrenceMaker_3', 'SAPRefrencePayment', 'SAPRefrencePayment1', 'SAPRefrencePayment2', 'SAPRefrencePayment3', 'SAP_Doc_Date', 'SAP_Doc_Ref_No', 'SN', 'Status', 'Status_1', 'Status_2', 'Status_3', 'costCenter', 'manufacturer', 'plant', 'state', 'uselife', 'vendercode']
# print(len(data1))

from config import *

makeTableQuery = f''' create table if not exists dffcil_laptop_reim_report(
                        db_uniq_id character varying COLLATE pg_catalog."default",
                        input_date_time character varying COLLATE pg_catalog."default",

                        asset_number character varying COLLATE pg_catalog."default",
                        co_cgm_office character varying COLLATE pg_catalog."default",
                        cost_of_repair_1 character varying COLLATE pg_catalog."default",
                        cost_of_repair_2 character varying COLLATE pg_catalog."default",
                        cost_of_repair_3 character varying COLLATE pg_catalog."default",
                        date_of_purchase character varying COLLATE pg_catalog."default",
                        do_repair_1 character varying COLLATE pg_catalog."default",
                        do_repair_2 character varying COLLATE pg_catalog."default",
                        do_repair_3 character varying COLLATE pg_catalog."default",
                        description_of_laptop character varying COLLATE pg_catalog."default",
                        device_serial_number character varying COLLATE pg_catalog."default",
                        emp_desg character varying COLLATE pg_catalog."default",
                        emp_id character varying COLLATE pg_catalog."default",
                        emp_name character varying COLLATE pg_catalog."default",
                        excluding_gst character varying COLLATE pg_catalog."default",
                        gst_rate character varying COLLATE pg_catalog."default",
                        invoce_no character varying COLLATE pg_catalog."default",
                        invoice_value character varying COLLATE pg_catalog."default",
                        ref_invoice_no_1 character varying COLLATE pg_catalog."default",
                        ref_invoice_no_2 character varying COLLATE pg_catalog."default",
                        ref_invoice_no_3 character varying COLLATE pg_catalog."default",
                        reimb_value character varying COLLATE pg_catalog."default",
                        requested_date character varying COLLATE pg_catalog."default",
                        sap_refrence_bill_passing character varying COLLATE pg_catalog."default",
                        sap_refrence_bill_passing_1 character varying COLLATE pg_catalog."default",
                        sap_refrence_bill_passing_2 character varying COLLATE pg_catalog."default",
                        sap_refrence_bill_passing_3 character varying COLLATE pg_catalog."default",
                        sap_refrence_date_maker_1 character varying COLLATE pg_catalog."default",
                        sap_refrence_date_maker_2 character varying COLLATE pg_catalog."default",
                        sap_refrence_date_maker_3 character varying COLLATE pg_catalog."default",
                        sap_refrence_maker_1 character varying COLLATE pg_catalog."default",
                        sap_refrence_maker_2 character varying COLLATE pg_catalog."default",
                        sap_refrence_maker_3 character varying COLLATE pg_catalog."default",
                        sap_refrence_payment character varying COLLATE pg_catalog."default",
                        sap_refrence_payment_1 character varying COLLATE pg_catalog."default",
                        sap_refrence_payment_2 character varying COLLATE pg_catalog."default",
                        sap_refrence_payment_3 character varying COLLATE pg_catalog."default",
                        sap_doc_date character varying COLLATE pg_catalog."default",
                        sap_doc_ref_no character varying COLLATE pg_catalog."default",
                        sn character varying COLLATE pg_catalog."default",
                        status character varying COLLATE pg_catalog."default",
                        status_1 character varying COLLATE pg_catalog."default",
                        status_2 character varying COLLATE pg_catalog."default",
                        status_3 character varying COLLATE pg_catalog."default",
                        cost_center character varying COLLATE pg_catalog."default",
                        manufacturer character varying COLLATE pg_catalog."default",
                        plant character varying COLLATE pg_catalog."default",
                        state character varying COLLATE pg_catalog."default",
                        uselife character varying COLLATE pg_catalog."default",
                        vendercode character varying COLLATE pg_catalog."default",
                        
                        bot_status character varying COLLATE pg_catalog."default",
                        as01_msg character varying COLLATE pg_catalog."default",
                        as01_doc_no character varying COLLATE pg_catalog."default",
                        abzon_msg character varying COLLATE pg_catalog."default",
                        abzon_doc_no character varying COLLATE pg_catalog."default"
                        
    ) '''
# cursor.execute(makeTableQuery)
# con.commit()

# delTable = "delete from dffcil_laptop_reim_report"
# cursor.execute(delTable)
# con.commit()


# import pandas as pd
# q = "select * from dffcil_laptop_reim_report"
# df = pd.read_sql_query(q, con=con)
# print(df)