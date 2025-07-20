import os
import psycopg2

con = psycopg2.connect(dbname = 'SequelString', user = 'postgres', password = 'rpa@321', host = 'localhost', port = '5432')
cursor = con.cursor()

sap_connection_name = "ECQ [10.22.22.23]"
sap_user_name = "BOT_USER"
sap_password = "Admin@1234567890"

table_name = "dffcil_laptop_reim_report"

scriptPath = os.path.dirname(__file__)
mainFolder = os.path.dirname(scriptPath)


screenShotFolderPth = os.path.join(scriptPath,"screenShots")

outputFolder = os.path.join(mainFolder,"output")

# getUrl = "https://uat.dfccil.com/vig/Fetchdata"
getUrl = "https://uat.dfccil.com/DeviceAPI/SAPDeviceData?ClientId=SAPDfccil1504&Token=6f2cb9dd8f4b65e24e1c3f3fa5bc57982349237f11abceacd45bbcb74d621c25"

# postUrl = "https://uat.dfccil.com/Vig/UpdateAssets"
postUrl = "https://https://uat.dfccil.com/DeviceAPI/UpdateAssets"


# as01path = r"c:\Users\hp\Desktop\ss\main\screenShots\BOT\as01"
# abzonpath = r"c:\Users\hp\Desktop\ss\main\screenShots\BOT\abzon"
# screenShotFolderPth = os.path.join(r"C:\Users\hp\Desktop\ss\main","screenShots")

# C:\Users\hp\Desktop\ss\main\BOT\screenShots

