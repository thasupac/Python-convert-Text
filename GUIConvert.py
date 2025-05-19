from tkinter import*
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from read_txt_sep import *
transFer = MainConvert()

MainGUI = Tk()
MainGUI.title('Convert data')


def center_windows(w,h):
    ws = MainGUI.winfo_screenwidth() #screen width
    hs = MainGUI.winfo_screenheight() #screen height
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    return f'{w}x{h}+{x:.0f}+{y:.0f}'
win_size = center_windows(800,550)
MainGUI.geometry(win_size)

#font size
FONT1 = ('Angsana New', 25, 'bold')
FONT2 = ('Angsana New', 18, )
FONT3 = ('Angsana New', 16, )

#frame input
F_input = LabelFrame(MainGUI, text='Text Folder Locations', width=380, height=250)
F_input.pack(fill='both',side="left", expand="yes", padx=10, pady=10)

#frame output
F_output = LabelFrame(MainGUI, text='CSV Folder Locations', width=380, height=250)
F_output.pack(fill='both',side="right", expand="yes", padx=10, pady=10)

#folder select input
def folderSelect():
    for iter in textFilelist.get_children():
        textFilelist.delete(iter)
    
    file_path = filedialog.askdirectory()
    v_dirfile.set(file_path)
    files = os.listdir(file_path)
    for i in files:
        if i:
            if i.endswith(".txt"):
                textFilelist.column('File name', anchor="center", width=5) 
                textFilelist.heading('File name', text='File name',anchor="center")
                textFilelist.insert('', 'end', values=i)
       
        else:
            textFilelist['columns']=("ไม่พบผลลัพธ์ที่ตรงกับคำค้นหา")
            textFilelist.column("ไม่พบผลลัพธ์ที่ตรงกับคำค้นหา", anchor="center", width=250)
            textFilelist.heading("ไม่พบผลลัพธ์ที่ตรงกับคำค้นหา", text="ไม่พบผลลัพธ์ที่ตรงกับคำค้นหา", anchor="center")

L = ttk.Button(F_input, text='Input folder:', command=folderSelect)
L.place(x=22, y=55)
v_dirfile = StringVar()
E = ttk.Entry(F_input, textvariable=v_dirfile, font=FONT2)
E.place(x=108, y=50, height=30, width=250 )

#folder select output
def folderSelectOutput():
    for iter in textFilelistOutput.get_children():
        textFilelistOutput.delete(iter)
    
    file_pathOutput = filedialog.askdirectory()
    v_dirfileOutput.set(file_pathOutput)
   
L = ttk.Button(F_output, text='Output folder:', command=folderSelectOutput)
L.place(x=22, y=55)
v_dirfileOutput = StringVar()
E = ttk.Entry(F_output, textvariable=v_dirfileOutput, font=FONT2)
E.place(x=108, y=50, height=30, width=250 )


#create list machine input
header = ["File name"]
headerw = [250]
textFilelist = ttk.Treeview(F_input, columns=header, show='headings')
textFilelist.place(x=20, y=90, width=335, height=400)

#create list machine output
headerOutput = ["File name"]
headerwOutput = [250]
textFilelistOutput = ttk.Treeview(F_output, columns=header, show='headings')
textFilelistOutput.place(x=20, y=90, width=335, height=400)

#convert txt to csv
def ConvertData():
    dirPath = v_dirfile.get()
    dirPathOutput = v_dirfileOutput.get()
    if dirPath and dirPathOutput !=(''):
        transFer.StartConvert(dirPath,dirPathOutput)

        filesoutput = os.listdir(dirPathOutput)
        for ic in  filesoutput:
            textFilelistOutput.column('File name', anchor="center", width=5) 
            textFilelistOutput.heading('File name', text='File name',anchor="center")
            textFilelistOutput.insert('', 'end', values=ic)
   
    else:
        messagebox.showinfo('Convert data', 'Please fill path')

B = ttk.Button(F_input, text='Convert data', command=ConvertData)
B.place(x=280, y=20,)

#clear
def ClearData():
    #clear input
    for iter in textFilelist.get_children():
        textFilelist.delete(iter)
    
    #clear output
    for iter in textFilelistOutput.get_children():
        textFilelistOutput.delete(iter)

    #clear path input
    v_dirfile.set('')

    #clear output
    v_dirfileOutput.set('')

B = ttk.Button(F_output, text='Clear', command=ClearData)
B.place(x=20, y=20)

MainGUI.mainloop()