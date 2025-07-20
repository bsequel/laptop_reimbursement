import os
import requests
import json

from config import *
import config

dffcil_laptop_reim_report = config.table_name
url = config.postUrl

try:
    fetch_query = f''' select db_uniq_id, input_date_time, device_serial_number, as01_doc_no from {dffcil_laptop_reim_report} where as01_doc_no is not null '''
    cursor.execute(fetch_query)
    data = cursor.fetchall()
    # print(data)

    allData = []
    for i in range(len(data)):
        row_data = {
            "Device_Serial_Number": data[i][2],
            "Asset_Number": data[i][3]
        }
        allData.append(row_data)

    print(f"No of total processed data id:- {len(allData)}")

    processedData = {"lstLaptops": allData}

    # data1 = {
    # "lstLaptops" : [
    #         {
    #             "Device_Serial_Number": "bzj7g13",
    #             "Asset_Number": "abc"
    #         },
    #         {
    #             "Device_Serial_Number": "CXL8QM3",
    #             "Asset_Number": "nudefll"
    #         }
    #     ]

    # }


    # url = "https://uat.dfccil.com/Vig/UpdateAssets"

    reportJsonPath = os.path.join(config.scriptPath,"postPayload.json")
    with open(reportJsonPath, 'w+') as fl:
        json.dump(processedData, fl, indent=4)

    payload = json.dumps(processedData)
    # print(payload)
    headers = {
            "Content-Type": "application/json"
        }
    # print("+=======================+++++++++++++", url, data1)
    if len(allData) > 0:
        response = requests.post(url, data=payload, headers=headers)
        # print("+=============++++==============")
        
        print(response)
        print(response.json())
        # print("+=======================")

        if response.status_code == 200:
            try:
                response_data = response.json()  # Attempt to parse JSON
                print("Response JSON:", response_data)
            except requests.exceptions.JSONDecodeError:
                print("Error: The server response is not valid JSON.")
                print("Response Text:", response.text)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print("Response Content:", response.text)
    else:
        print("No any upadated data found")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")