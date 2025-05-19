from tkinter import *
from tkinter import messagebox
from threading import Thread
import threading
import pandas as pd
import os


class MainConvert:
    ##--progress
    def StartConvert(self,dirPath,dirPathOutput):
        def center_windows(w,h):
            ws = window.winfo_screenwidth() #screen width
            hs = window.winfo_screenheight() #screen height
            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            return f'{w}x{h}+{x:.0f}+{y:.0f}'
    
        window = Toplevel()
        win_size = center_windows(200,100)
        window.geometry(win_size)
        window.title('Progress functions')
        label = Label(window, text = 'Convert data...')
        label.pack()
        window.update()
        thread = threading.Thread(target = MainConvert.ConvertData(self,dirPath,dirPathOutput))
        thread.start()
        window.destroy()
        window.update()
        messagebox.showinfo('Convert data', 'The convert data sucessfully')

    def ConvertData(self,dirPath,dirPathOutput):
        #รับ path มา
        file_path = str(dirPath)

        #list จำนวนไฟล์ในpath
        files = os.listdir(file_path)
        
        for x in files:
            if x.endswith(".txt"):

                df = pd.read_csv(f'{file_path}/{x}', delimiter=',', header=None)

                data_list = df.values.tolist() 

                #data frame
                Numbers = []
                MeasurementnameS = []
                Element1s = []
                Blank1 = []
                Element2s = []
                Judgements = []
                Measurementresults = []
                Units = []
                DesignvaluE = []
                UppertolerancE = []
                LowertolerancE =[]
                CommenT = []

                #analysis data
                startNum = 1
                countfile = 0
                datainonE = len(data_list)  #เช็คว่าใน 1 text file มีกี่ค่า

                
                while datainonE>0:
                    try:
                        datainonE-=1
                        for i in data_list:
                            dataFramE = {'Number': Numbers,
                                'Measurement name':MeasurementnameS,
                                'Element 1':Element1s,
                                '':Blank1,
                                'Element 2':Element2s,
                                'Judgement':Judgements,
                                'Measurementresult':Measurementresults,
                                'Unit':Units,
                                'Design value':DesignvaluE,
                                'Upper tolerance':UppertolerancE,
                                'Lower tolerance':LowertolerancE,
                                'Comment':CommenT}
                            
                            #นับความยาวของไฟล์ 1 ไฟล์
                            sep_file_len = len(i)   #นับเพื่อเอาตำแหน่งของข้อมูลที่ถูกต้อง

                            #add data
                            #1_file name
                            file_name = [f'{i[sep_file_len-(sep_file_len-6)]}']
                            for editName in file_name:
                                namefilEedit = editName.split('\\n')    #เมื่อเจอ \n ให้ตัด \n ออก
                                newnamE = dirPathOutput +'/'+namefilEedit[0]   #newnamE จะเป็นทั้งชื่อไฟล์และ path เช่น "C:\Users\thanongsak_su\Desktop\SFA40111-14-A01-52-PIC-00032.csv"
                            
                            #u1
                            Measurementresults.append(i[sep_file_len-(sep_file_len-11)])  #value1 (U1A)
                            Measurementresults.append(i[sep_file_len-(sep_file_len-12)])  #value2 (U1B)
                            Measurementresults.append(i[sep_file_len-(sep_file_len-13)])  #value3 (U1C)
                            Measurementresults.append(i[sep_file_len-(sep_file_len-14)])  #value4 (U1D)

                            #u2
                            Measurementresults.append(i[sep_file_len-(sep_file_len-15)])  #value1 (U2A) 
                            Measurementresults.append(i[sep_file_len-(sep_file_len-16)])  #value2 (U2B)
                            Measurementresults.append(i[sep_file_len-(sep_file_len-17)])  #value3 (U2C)
                            Measurementresults.append(i[sep_file_len-(sep_file_len-18)])  #value4 (U2D)

                            #u3
                            Measurementresults.append(i[sep_file_len-(sep_file_len-19)])  #value1 (U3A)
                            Measurementresults.append(i[sep_file_len-(sep_file_len-20)])  #value2 (U3B)
                            Measurementresults.append(i[sep_file_len-(sep_file_len-21)])  #value3 (U3C)
                            Measurementresults.append(i[sep_file_len-(sep_file_len-22)])  #value4 (U3D)

                            #u4
                            Measurementresults.append(i[sep_file_len-(sep_file_len-23)])  #value1 (U4A)
                            Measurementresults.append(i[sep_file_len-(sep_file_len-24)])  #value2 (U4B)
                            Measurementresults.append(i[sep_file_len-(sep_file_len-25)])  #value3 (U4C)
                            Measurementresults.append(i[sep_file_len-(sep_file_len-26)])  #value4 (U4D)

                            #u5
                            Measurementresults.append(i[sep_file_len-(sep_file_len-27)])  #value1 (U5A)
                            Measurementresults.append(i[sep_file_len-(sep_file_len-28)])  #value2 (U5B)
                            Measurementresults.append(i[sep_file_len-(sep_file_len-29)])  #value3 (U5C)
                            Measurementresults.append(i[sep_file_len-(sep_file_len-30)])  #value4 (U5D)

                            ##ให้นับจำนวนข้อมูล
                            profilE = len(Measurementresults)
                            for ix in Measurementresults:
                                Numbers.append(profilE-(profilE-startNum))
                                MeasurementnameS.append('Profile') #ใส่คำว่า Profile
                                startNum+=1

                            #blank
                            blanK = (len(Measurementresults))/2
                            while blanK>0:
                                Blank1.append(1)    #ใส่ตัวเลข 1
                                Blank1.append(2)    #ใส่ตัวเลข 2
                                blanK-=1

                            #element1
                            el1 = (len(Measurementresults))
                            start = el1
                            step = el1
                            while el1>0:
                                Element1s.append(f'Parallel{1+(start-step)}')   #ใส่คำว่า parallel
                                Element1s.append(f'Parallel{1+(start-step)}')   #ใส่คำว่า parallel
                                el1-=2
                                step-=1
                            
                            #element 2
                            el2 = (len(Measurementresults))/2
                            start = len(Measurementresults)
                            step = len(Measurementresults)
                            while el2 > 0:
                                Element2s.append(f'U{1+(start-step)}_A')    #ใส่ U..A
                                Element2s.append(f'U{1+(start-step)}_B')    #ใส่ U..B
                                Element2s.append(f'U{1+(start-step)}_C')    #ใส่ U..C
                                Element2s.append(f'U{1+(start-step)}_D')    #ใส่ U..D
                                step-=1
                                el2-=2

                            #Judgement
                            for JuD in Measurementresults:
                                if JuD > 350:
                                    Judgements.append('Fail')
                                elif JuD < 330:
                                    Judgements.append('Fail')
                                else:
                                    Judgements.append('Pass')

                            #unit
                            for uniT in Measurementresults:
                                Units.append('um')

                            #design value
                            for dEs in Measurementresults:
                                DesignvaluE.append(0)

                            #upper
                            for upV in Measurementresults:
                                UppertolerancE.append(0)

                            #lower
                            for lwV in Measurementresults:
                                LowertolerancE.append(0)

                            #comment
                            for com in Measurementresults:
                                CommenT.append(0)

                            #clear data
                            Numbers = []
                            MeasurementnameS = []
                            Element1s = []
                            Blank1 = []
                            Element2s = []
                            Judgements = []
                            Measurementresults = []
                            Units = []
                            DesignvaluE = []
                            UppertolerancE = []
                            LowertolerancE =[]
                            CommenT = []

                            dfcsv = pd.DataFrame(dataFramE) 
                            dfcsv.to_csv(f'{newnamE}.csv', index=False)
                            countfile+=1
                            startNum = 1
                            
                        else:
                            break
                    except Exception as e:
                        messagebox.showerror("Error", f"The file name {x} \n Failed to data: {e}")

        # messagebox.showinfo('Convert data', f'Total convert file : {countfile}')
        # return True
        