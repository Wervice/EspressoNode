# EspressoNode
from tkinter import *
from tkinter import ttk as ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from ttkthemes import ThemedTk
import os
import webbrowser
window = ThemedTk(theme="breeze")
window.title("EspressoNode - Tor Exit Node Specify")
window.geometry("500x200")
window.resizable(0,0)
window.iconbitmap("logo.ico")
window.config(background="white")

def run():
    try:
        folder = fd.askdirectory(mustexist=1, title="Select Tor Installation folder")
        torrc_opener = open(folder+"/Browser/TorBrowser/Data/Tor/torrc", "r")
        torrc = torrc_opener.read()
        torrc_opener.close()
        if combo.get() != "Disable":
            if "ExitNodes" in torrc:
                new_torrc = torrc.replace("ExitNodes", "# ")
                new_torrc = new_torrc+"\nExitNodes {"+combo.get().lower()+"} StrictNodes 1"
            else:
                new_torrc = torrc+"\nExitNodes {"+combo.get().lower()+"} StrictNodes 1"
        else:
            new_torrc = torrc.replace("ExitNodes", "# ")
        torrc_writer = open(folder+"/Browser/TorBrowser/Data/Tor/torrc", "w")
        torrc_writer.write(new_torrc)
        torrc_writer.close()
        if mb.askyesno(title="Upated", message="The ExitNode is up-to-date. You need to restart Tor to apply the changes. Do you want to open a new Tor Browser Session up?"):
            os.system("\""+folder+"/Browser/firefox.exe\"")
            print("\""+folder+"/Browser/firefox.exe\"")
    except FileNotFoundError:
        mb.showerror(title="Wrong Folder", message="Please select the Tor Installation Folder.")

def help():
    filename = 'file:///'+os.getcwd()+'/' + 'list.html'
    webbrowser.open_new_tab(filename)

Label(window, text="EspressoNode", height=1, width=100, font=("", 15), background="#9141ac", foreground="white", anchor="nw").place(x=0, y=0)
combo = ttk.Combobox(values = ['Disable', 'AD', 'AN', 'AE','AF','AG','AI','AL','AM','AO','AQ','AR','AS','AT','AU','AW','AX','AZ','BA','BB','BD','BE','BF','BG','BH','BI','BJ','BL','BM','BN','BO','BQ','BR','BS','BT','BV','BW','BY','BZ','CA','CC','CD','CF','CG','CH','CI','CK','CL','CM','CN','CO','CR','CU','CV','CW','CX','CY','CZ','DE','DJ','DK','DM','DO','DZ','EC','EE','EG','EH','ER','ES','ET','FI','FJ','FK','FM','FO','FR','GA','GB','GD','GE','GF','GG','GH','GI','GL','GM','GN','GP','GQ','GR','GS','GT','GU','GW','GY','HK','HM','HN','HR','HT','HU','ID','IE','IL','IM','IN','IO','IQ','IR','IS','IT','JE','JM','JO','JP','KE','KG','KH','KI','KM','KN','KP','KR','KW','KY','KZ','LA','LB','LC','LI','LK','LR','LS','LT','LU','LV','LY','MA','MC','MD','ME','MF','MG','MH','MK','ML','MM','MN','MO','MP','MQ','MR','MS','MT','MU','MV','MW','MX','MY','MZ','NA','NC','NE','NF','NG','NI','NL','NO','NP','NR','NU','NZ','OM','PA','PE','PF','PG','PH','PK','PL','PM','PN','PR','PS','PT','PW','PY','QA','RE','RO','RS','RU','RW','SA','SB','SC','SD','SE','SG','SH','SI','SJ','SK','SL','SM','SN','SO','SR','SS','ST','SV','SX','SY','SZ','TC','TD','TF','TG','TH','TJ','TK','TL','TM','TN','TO','TR','TT','TV','TW','TZ','UA','UG','UM','US','UY','UZ','VA','VC','VE','VG','VI','VN','VU','WF','WS','YE','YT','ZA','ZM','ZW'])
combo.place(x=10, y=40)
button_go = ttk.Button(master=window, text="Go", command=run)
button_go.place(x=10, y=80)
button_help = ttk.Button(master=window, text="Country codes list", command=help)
button_help.place(x=10, y=120)

mainloop()