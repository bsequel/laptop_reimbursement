import os
import re
import time

from datetime import datetime

from save_screenshot import save_screenshot_function

def sap_tcode_abzon(session, data_dict):
    try:
        as01PostingNo = data_dict["as01PostingNo"]
        invoiceNumber = data_dict["invNumber"]
        reimbValue = data_dict["reimbValue"]
        
        todaydate = datetime.now().strftime("%d.%m.%Y")

        session.findById("wnd[0]/tbar[0]/okcd").text = "/nabzon"
        session.findById("wnd[0]").sendVKey(0)
        
        session.findById("wnd[0]/usr/subOBJECT:SAPLAMDP:0310/ctxtRAIFP2-ANLN1").text = as01PostingNo   # Existing Asset
        
        ######################## Transaction data container ###############################
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA2:SAPLAMDP:0501/subSUBSCREEN1:SAPLAMDP:0200/ctxtRAIFP1-BLDAT").text = todaydate # Document date
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA2:SAPLAMDP:0501/subSUBSCREEN3:SAPLAMDP:0202/ctxtRAIFP1-BZDAT").text = todaydate # Asset value date
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA3:SAPLAMDP:0500/subSUBSCREEN1:SAPLAMDP:0214/txtRAIFP2-ANBTR").text = reimbValue      # Amount posted
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA3:SAPLAMDP:0500/subSUBSCREEN2:SAPLAMDP:0216/txtRAIFP2-MENGE").text = "1"           # Quantity
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA3:SAPLAMDP:0500/subSUBSCREEN2:SAPLAMDP:0216/ctxtRAIFP2-MEINS").text = "Nos"        # Qty Unit
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA7:SAPLAMDP:0506/subSUBSCREEN1:SAPLAMDP:0206/txtRAIFP2-SGTXT").text = invoiceNumber     # Text
        
        ###################### Additional Details ############################################
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA7:SAPLAMDP:0506/subSUBSCREEN1:SAPLAMDP:0206/txtRAIFP2-SGTXT").setFocus()
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB01/ssubSUBSC:SAPLATAB:0200/subAREA7:SAPLAMDP:0506/subSUBSCREEN1:SAPLAMDP:0206/txtRAIFP2-SGTXT").caretPosition = 7
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02").select()
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02/ssubSUBSC:SAPLATAB:0200/subAREA1:SAPLAMDP:0507/subSUBSCREEN2:SAPLAMDP:0204/ctxtRAIFP1-BLART").text = "AA"  # Posting type
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02/ssubSUBSC:SAPLATAB:0200/subAREA1:SAPLAMDP:0507/subSUBSCREEN3:SAPLAMDP:0213/ctxtRAIFP2-GKONT").text = "27000000" # Offsetting acct no.
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02/ssubSUBSC:SAPLATAB:0200/subAREA2:SAPLAMDP:0508/subSUBSCREEN1:SAPLAMDP:0205/ctxtRAIFP1-BWASL").text = "100"     # Transaction Type
        
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02/ssubSUBSC:SAPLATAB:0200/subAREA2:SAPLAMDP:0508/subSUBSCREEN1:SAPLAMDP:0205/ctxtRAIFP1-BWASL").setFocus()
        session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02/ssubSUBSC:SAPLATAB:0200/subAREA2:SAPLAMDP:0508/subSUBSCREEN1:SAPLAMDP:0205/ctxtRAIFP1-BWASL").caretPosition = 3
        session.findById("wnd[0]/tbar[0]/btn[11]").press()
        
        time.sleep(2)
        
        abzonPostingMsg = session.findById("wnd[0]/sbar").text
        abzonPostingNo = re.findall(r"\d{10}", abzonPostingMsg)
        
        if len(abzonPostingNo) > 0:
            abzonPostingNo = abzonPostingNo[0]
            status = "Success"
        else:
            abzonPostingNo = ''
            status = "Fail"
        
        res = {"as01Msg": abzonPostingMsg, "abzonPostingNo": abzonPostingNo, "status": status}
        
        # import config
        # import json
        # mainFolder = config.mainFolder
        # as01JsonPath = os.path.join(os.path.join(mainFolder,"outputMsg"), "abzonRes.json")
        # with open(as01JsonPath, 'w+') as fl:
        #     json.dump(res, fl, indent=4)
        
        return abzonPostingMsg, abzonPostingNo, status

    except:
        try:
            save_screenshot_function(session, "abzon", data_dict)
            return "", "", "Fail"
        
        except:
            return "", "", "Fail"
    