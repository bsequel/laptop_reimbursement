import os
from PIL import Image
from datetime import datetime
import time

import config

screenShotFolderPth = config.screenShotFolderPth

def compress_image(filePath):
    img = Image.open(filePath)
    myHeight, myWidth = img.size
    img = img.resize((myHeight, myWidth), Image.LANCZOS)
    savePath = filePath
    img.save(savePath)

def save_screenshot_function(session, process, data_dict):
    screenShotFolderaPath = screenShotFolderPth
    processFolder = os.path.join(screenShotFolderaPath,process)
    current_time = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    filePath = os.path.join(processFolder, f"{data_dict["db_id"]}_{current_time}.png")
    # C:\\Users\\hp\\Desktop\\ss\\main\\BOT\\40db11fe-6a7c-41dc-8960-26c99269ef5f_28_10_2024_14_39_51.png
    if os.path.exists(processFolder):
        pass
    else:
        os.makedirs(processFolder)
        
    for i in range(0,6): 
        time.sleep(5)
        ################################################################## 
        try: 
            session.findById("wnd[3]").HardCopy(filePath) 
            compress_image(filePath) 
            break 
        except: 
            try: 
                session.findById("wnd[2]").HardCopy(filePath) 
                compress_image(filePath) 
                break 
            except: 
                try: 
                    session.findById("wnd[1]").HardCopy(filePath) 
                    compress_image(filePath) 
                    break 
                except: 
                    try: 
                        session.findById("wnd[0]").HardCopy(filePath) 
                        compress_image(filePath) 
                        break 
                    except Exception as e: 
                        print(e) 
                        time.sleep(5) 
                        print(f'Screenshot not captured in approch{i+1}') 
        ######################################################################################
                        