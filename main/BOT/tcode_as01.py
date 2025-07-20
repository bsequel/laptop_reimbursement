import os
import re
import time

from save_screenshot import save_screenshot_function

def sap_tcode_as01(session, data_dict):
    description1 = data_dict["description1"]
    description2 = data_dict["description2"]
    serialNumber = data_dict["serialNumber"] #'SKQ10MF4T2P'
    costCenter = data_dict["costCenter"] # 2010090
    plant = data_dict["plant"] # 2000
    personalNumber = data_dict["personalNumber"] # 100019
    state = data_dict["state"] # 30
    evaluationGroup = data_dict["evaluationGroup"] # 1038
    vendorCode = data_dict["vendorCode"] # 20000380
    manufacturer = data_dict["manufacturer"] # HP
    countryOfOrigins = data_dict["countryOfOrigins"] # IN
    dateOfPuchase = data_dict["dateOfPuchase"] # 04.03.2024
    reimbValue = data_dict["reimbValue"] # 135000
    useLife = data_dict["useLife"] # 3
    
    # requiredField = [description1, description2, serialNumber]
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nas01"
        session.findById("wnd[0]").sendVKey(0)
        
        session.findById("wnd[0]/usr/ctxtANLA-ANLKL").text = "8100" # Asset class
        session.findById("wnd[0]/usr/ctxtANLA-BUKRS").text = "1000" # company code
        session.findById("wnd[0]/usr/ctxtANLA-BUKRS").setFocus()
        session.findById("wnd[0]/usr/ctxtANLA-BUKRS").caretPosition = 4
        session.findById("wnd[0]").sendVKey(0)
        
        
        #### for general container ####
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA1:SAPLAIST:1140/btnGS_LTXT_ICONS-GENE").press()
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA1:SAPLAIST:1140/txtANLA-TXT50").text = description1 #description
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA1:SAPLAIST:1140/txtANLA-TXA50").text = description2 #description
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA1:SAPLAIST:1140/txtANLA-SERNR").text = serialNumber #serialNumber
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA1:SAPLAIST:1140/txtANLA-MENGE").text = "1"
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA1:SAPLAIST:1140/ctxtANLA-MEINS").text = "Nos"
        # time.sleep(5)
        
        #### for time dependent container ########################
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA1:SAPLAIST:1140/ctxtANLA-MEINS").setFocus()
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA1:SAPLAIST:1140/ctxtANLA-MEINS").caretPosition = 3
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02").select()
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1145/ctxtANLZ-KOSTL").text = costCenter #cost center
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1145/ctxtANLZ-WERKS").text = plant   # plant
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1145/ctxtANLZ-STORT").text = plant    # Location => also filed plamnt here
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1145/ctxtANLZ-PERNR").text = personalNumber  # personal number
        # time.sleep(5)

        ####### For Allocations container #######################
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1145/ctxtANLZ-PERNR").setFocus()
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1145/ctxtANLZ-PERNR").caretPosition = 6
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB03").select()
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB03/ssubSUBSC:SAPLATAB:0200/subAREA1:SAPLAIST:1160/ctxtANLA-ORD41").text = state    # state
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB03/ssubSUBSC:SAPLATAB:0200/subAREA1:SAPLAIST:1160/ctxtANLA-ORD42").text = evaluationGroup  # evaluation group
        # time.sleep(5)
        
        ######### For origin container #########################
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB03/ssubSUBSC:SAPLATAB:0200/subAREA1:SAPLAIST:1160/ctxtANLA-ORD42").setFocus()
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB03/ssubSUBSC:SAPLATAB:0200/subAREA1:SAPLAIST:1160/ctxtANLA-ORD42").caretPosition = 4
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB04").select()
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB04/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1181/ctxtANLA-LIFNR").text = vendorCode # vendor code 
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB04/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1181/ctxtANLA-LIFNR").caretPosition = 8
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB04/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1181/chkRA02S-XNEU_AM").selected = True
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB04/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1181/txtANLA-HERST").text = manufacturer # manufacturer
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB04/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1181/ctxtANLA-LAND1").text = countryOfOrigins # country of origins
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB04/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1181/ctxtANLA-AIBDT").text = dateOfPuchase # acq on = date of purchase
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB04/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1181/txtANLA-URWRT").text = reimbValue # original value = Reimb value
        # time.sleep(5)
        
        ########### for India Specific data container ###############
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB04/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1181/txtANLA-URWRT").setFocus()
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB04/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1181/txtANLA-URWRT").caretPosition = 6
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB06").select()
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB06/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLGLO_FIAA_SCREENS:4000/ctxtGLOFAAASSETDATA-GLO_IN_BLK_KEY").text = "0600"  # Block Key
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB06/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLGLO_FIAA_SCREENS:4000/ctxtGLOFAAASSETDATA-GLO_IN_AST_USE").text = dateOfPuchase   # Put to use data
        # time.sleep(5)

        #################### for Deprec Areas container ##########################
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB06/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLGLO_FIAA_SCREENS:4000/ctxtGLOFAAASSETDATA-GLO_IN_AST_USE").setFocus()
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB06/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLGLO_FIAA_SCREENS:4000/ctxtGLOFAAASSETDATA-GLO_IN_AST_USE").caretPosition = 10
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07").select()
        
        for i in range(0,4):
            session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB/ctxtANLB-AFABE[1,0]").setFocus()
            area_number = session.findById(f"wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB/ctxtANLB-AFABE[1,{i}]").text
            print(area_number, f"========={area_number}======", type(area_number), "<<<<<======= Area Number is")
            if str(area_number).strip() == '01':
                print(area_number, "<<<<<======= Area Number is")
                session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB").columns.elementAt(1).width = 15
                session.findById(f"wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB/ctxtANLB-AFASL[3,{i}]").text = "SLIN"
                session.findById(f"wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB/txtANLB-NDJAR[4,{i}]").text = useLife
                session.findById(f"wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB/ctxtANLB-AFABG[6,{i}]").text = dateOfPuchase
                print(area_number, "<<<<<======= Area Number is")
                
            elif str(area_number).strip() == '15':
                print(area_number, "<<<<<======= Area Number is")
                session.findById(f"wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB/ctxtANLB-AFASL[3,{i}]").text = "SLIN"
                session.findById(f"wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB/txtANLB-NDJAR[4,{i}]").text = useLife
                session.findById(f"wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB/ctxtANLB-AFABG[6,{i}]").text = dateOfPuchase
                
                print(area_number, "<<<<<======= Area Number is")
                
            elif str(area_number).strip() == '20':
                print(area_number, "<<<<<======= Area Number is")
                session.findById(f"wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB/ctxtANLB-AFASL[3,{i}]").text = "SLIN"
                session.findById(f"wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB/txtANLB-NDJAR[4,{i}]").text = useLife
                session.findById(f"wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB/ctxtANLB-AFABG[6,{i}]").text = dateOfPuchase
                
                print(area_number, "<<<<<======= Area Number is")
                
            elif str(area_number).strip() == '40':
                print(area_number, "<<<<<======= Area Number is")
                session.findById(f"wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB/ctxtANLB-AFASL[3,{i}]").text = "SLIN"
                session.findById(f"wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB/txtANLB-NDJAR[4,{i}]").text = useLife
                session.findById(f"wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB07/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLAIST:1190/tblSAPLAISTTC_ANLB/ctxtANLB-AFABG[6,{i}]").text = dateOfPuchase
                
                print(area_number, "<<<<<======= Area Number is")
                
        session.findById("wnd[0]/tbar[0]/btn[11]").press()
        time.sleep(2)
        
        as01PostingMsg = session.findById("wnd[0]/sbar").text
        
        as01PostingNo = re.findall(r"\d{11}", as01PostingMsg)
        if len(as01PostingNo) > 0:
            as01PostingNo = as01PostingNo[0]
            status = "Success"
        else:
            as01PostingNo = ''
            status = "Fail"
        
        res = {"as01Msg": as01PostingMsg, "as01PostingNo": as01PostingNo, "status": status}
        
        # import config
        # import json
        # mainFolder = config.mainFolder
        # as01JsonPath = os.path.join(os.path.join(mainFolder,"outputMsg"), "as01Res.json")
        # with open(as01JsonPath, 'w+') as fl:
        #     json.dump(res, fl, indent=4)
        
        return as01PostingMsg, as01PostingNo, status

    except:
        try:
            save_screenshot_function(session, "as01", data_dict)
            return "", "", "Fail"
        except:
            return "", "", "Fail"
