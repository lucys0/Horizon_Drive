from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
style.use('ggplot')

AVI_DEVICES = ('Device 1', 'Device 2', 'Device 3')
THERMAL_DEVICES = ('Device 1', 'Device 2', 'Device 3')
A_O_DEVICES = ('Device 1', 'Device 2', 'Device 3')
D_I_O_DEVICES = ('Device 1', 'Device 2', 'Device 3')
analog_voltage_input = [1,2,3,4,5,6,7,8]
thermocouple_input = [1,2,3,4]
analog_output = [1,2]
digital_i_o = [1,2,3,4,5,6,7,8]
results_chart = ["Q Factor","Thrust","Thrust/P"]
counter = 0
r0 = 5
r1 = 2
r2 = 5
r3 = 5
r4 = 8

def run_test():
    import time
    progress['maximum'] = 100
    for i in range (101):
        time.sleep(0.05)
        progress['value'] = i
        progress.update()

    messagebox.showinfo("Test Status", "Test Completed Successfully")
    progress['value'] = 0
    
def stop_test():
    import time
    progress.stop()



def start_test_warning():
    messagebox.showwarning("WARNING","You are about to start a test cycle. Before continuing please make sure the following items are completed: \n1. Safety glasses\n2.Something\n3.Something")
            
def onError():
    messagebox.showerror("Error","Could not open file")
        
def onWarning():
    messagebox.showwarning("Warning", "Deprecatred function call")
        
def onQuestion(self):
    messagebox.askquestion("Question","Are you sure you want to quit?")
        
def onInfo():
    messagebox.showinfo("Information","Download completed")
    
def onCancel():
    ok = messagebox.askokcancel(message="You are about to start a test cycle. Before continuing please make sure the following items are completed: \n1. Safety glasses\n2.Something\n3.Something")
    
    if ok:
        run_test()
    
def onYesNo():
    messagebox.askyesno("Yes","No")
    
def onRetryCancel():
    messagebox.askretrycancel("Retry","Cancel")
        
def onOpen():
    ftypes = askopenfile(mode='r', filetypes=[('Python files', '*.py'),('All files','*')])
    if ftypes is not None:
        content = ftypes.read()
        print(content)
        
        
def readFile(self,filename):
    with open(filename,"r") as f:
        text = f.read()
    return text
    
    
def get_118_info():
    stat_118 = Toplevel()
    stat_118.title("MCC 118")
    #info_118 = mcc118.info()
    #firmware_version_118 = mcc118.firmware_version()
    #serial_118 = mcc118.serial()
    
def get_134_info():
    stat_134 = Toplevel()
    stat_134.title("MCC 134")
    #info_134 = mcc134.info()
    #firmware_version_134 = mcc134.firmware_version()
    #serial_134 = mcc134.serial()

def get_152_info():
    stat_152 = Toplevel()
    stat_152.title("MCC 152")
    #info_152 = mcc152.info()
    #firmware_virsion_152 = mcc152.firmware_version()
    #serial_152 = mcc152.serial()

def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000,count)
    count()

def save():
    files = [('All Files', '*.*'),('Python Files', '*.py'),('Text Document','*.txt'),('CSV Files','*.csv')]
    file = asksaveasfile(filetypes = files,defaultextension = files)
    
    
def animate(i):
    pullData = open('sampleText.txt','r').read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    displacement_from_power.clear()
    displacement_from_power.plot(xar,yar)
        
class NoiseWindow(Toplevel):
    def __init__(self,parent=None,side=LEFT):
        super().__init__()
        self.title("External Noise Input Menu")
        self.geometry("500x300")
        #self.configure(background = "green" )
        Label(self, text ="Check any factor that may have contributed to noise:").grid(row=0,sticky=W+E)
        chkbtn1 = Checkbutton(self, text = "No external noise").grid(row=2,sticky=W)
        chkbtn2 = Checkbutton(self, text = "Air Currents (Atmospheric Test)").grid(row=3,sticky=W)
        chkbtn3 = Checkbutton(self, text = "RF Interaction with the Surrounding Environment").grid(row=4,sticky=W)
        chkbtn4 = Checkbutton(self, text = "Magnetic Interaction").grid(row=5,sticky=W)
        chkbtn5 = Checkbutton(self, text = "Thermal Expansion and Contraction").grid(row=6,sticky=W)
        chkbtn6 = Checkbutton(self, text = "Vibration").grid(row=7,sticky=W)
        chkbtn7 = Checkbutton(self, text = "Electrostatic Interaction").grid(row=8,sticky=W)
        chkbtn8 = Checkbutton(self, text = "Outgassing").grid(row=9,sticky=W)
        chkbtn9 = Checkbutton(self, text = "Photon Rocket Force").grid(row=10,sticky=W)
        chkbtn10 = Checkbutton(self, text = "Impulsive/Thermal Signal Decoupling Error").grid(row=11,sticky=W)
        confirm_button = Button(self,text = "Confirm").grid(row=14,column=1)
        cancel_button = Button(self,text = "Cancel")
        cancel_button.grid(row=14,column=0)
        cancel_button.bind("<Button>",lambda e: self.destroy())
        
class colorpicker(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        
        self.initiate_color_settings()
        
    def initiate_color_settings(self):
        self.title("Color chooser")
        self.btn = Button(self, text='Choose Color', command=self.onChoose)
        self.btn.grid(row=0)
        self.frame = Frame(self, border=1, relief=SUNKEN,width=100,height=100)
        self.frame.grid(row=0,column=1)
        
    def onChoose(self):
        (rgb,hx) = colorchooser.askcolor()
        self.frame.config(bg=hx)
        
class NewWindow(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        
    def graph_settings(self):
        self.title("Graph settings")
        self.geometry("500x310")
        graph_settings_tab = ttk.Notebook(self)
        
        general_settings = ttk.Frame(graph_settings_tab)
        filters = ttk.Frame(graph_settings_tab)

        graph_settings_tab.add(filters, text= "Graph Filters")
        graph_settings_tab.add(general_settings, text="Graph Settings")
        graph_settings_tab.grid(row=0)
        
        chkbtn1 = Checkbutton(filters, text = "No external noise").grid(row=2,sticky=W)
        chkbtn2 = Checkbutton(filters, text = "Air Currents (Atmospheric Test)").grid(row=3,sticky=W)
        chkbtn3 = Checkbutton(filters, text = "RF Interaction with the Surrounding Environment").grid(row=4,sticky=W)
        chkbtn4 = Checkbutton(filters, text = "Magnetic Interaction").grid(row=5,sticky=W)
        chkbtn5 = Checkbutton(filters, text = "Thermal Expansion and Contraction").grid(row=6,sticky=W)
        chkbtn6 = Checkbutton(filters, text = "Vibration").grid(row=7,sticky=W)
        chkbtn7 = Checkbutton(filters, text = "Electrostatic Interaction").grid(row=8,sticky=W)
        chkbtn8 = Checkbutton(filters, text = "Outgassing").grid(row=9,sticky=W)
        chkbtn9 = Checkbutton(filters, text = "Photon Rocket Force").grid(row=10,sticky=W)
        chkbtn10 = Checkbutton(filters, text = "Impulsive/Thermal Signal Decoupling Error").grid(row=11,sticky=W)
        confirm_button = Button(self,text = "Confirm").grid(row=14,column=1)
        cancel_button = Button(self,text = "Cancel")
        cancel_button.grid(row=14,column=0)
        cancel_button.bind("<Button>",lambda e: self.destroy())
        
    def daq_settings(self):
        self.title("Program Settings")
        self.geometry("400x400")
        daq_settings_tab = ttk.Notebook(self)
        
        general_settings = ttk.Frame(daq_settings_tab)
        device_info = ttk.Frame(daq_settings_tab)
        
        daq_settings_tab.add(device_info, text="Device Info")
        daq_settings_tab.add(general_settings, text="Settings")
        
    def camera_window(self):
        self.title("Camera")
        self.geometry("350x350")
        
class menubar(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.master.title("Horizon Drive DAQ GUI")
        menu = Menu(self.master)
        toolbar = Frame(self.master,bd=1,relief=RAISED)
        
        self.master.config(menu=menu)
        
        # Adding File Menu and commands
        file = Menu(menu, tearoff = 0)
        menu.add_cascade(label="File",menu=file)
        file.add_command(label="New File",command=None)
        file.add_command(label="Open...",command=onOpen)
        file.add_command(label="Save",command=save)
        file.add_separator()
        file.add_command(label="Exit",command=None)
        
        status_menu = Menu(file)
        status_menu.add_command(label="MCC 118",command=get_118_info)
        status_menu.add_command(label='MCC 152', command=get_152_info)
        status_menu.add_command(label='MCC 134', command=get_134_info)
        file.add_cascade(label='Get Shield Info',menu=status_menu)
        
        save_as_menu = Menu(file)
        save_as_menu.add_command(label='.csv',command=None)
        save_as_menu.add_command(label='python pickle',command=None)
        save_as_menu.add_command(label='.xslx',command=None)
        file.add_cascade(label='Save as...',menu=save_as_menu)
        
        # Adding Edit Menu and commands
        edit = Menu(menu, tearoff = 0)
        menu.add_cascade(label ='Edit', menu = edit)
        edit.add_command(label ='Cut', command = None)
        edit.add_command(label ='Copy', command = None)
        edit.add_command(label ='Paste', command = None)
        edit.add_command(label ='Select All', command = None)
        edit.add_separator()
        edit.add_command(label ='Find...', command = None)
        edit.add_command(label ='Find again', command = None)
        
        # Adding View Menu and commands
        view = Menu(menu, tearoff = 0)
        menu.add_cascade(label = 'View',menu=view)
        view.add_command(label='Show Toolbar', command=None)
        view.add_command(label='Show Module', command=None)
        view.add_command(label='Change Color',command=colorpicker)
        
          
        # Adding Help Menu
        help_ = Menu(menu, tearoff = 0)
        menu.add_cascade(label ='Help', menu = help_)
        help_.add_command(label ='Tk Help', command = None)
        help_.add_command(label ='Demo', command = None)
        
        # Adding toolbar
        error_btn = Button(toolbar, text ="error", relief=RAISED,bitmap="error").grid(row=0,column=0)
        hourglass_btn = Button(toolbar, text ="hourglass", relief=RAISED,bitmap="hourglass").grid(row=0,column=1)
        info_btn = Button(toolbar, text ="info", relief=RAISED,bitmap="info",command=onInfo).grid(row=0,column=2)
        question_btn = Button(toolbar, text ="question", relief=RAISED,bitmap="question").grid(row=0,column=3)
        warning_btn = Button(toolbar, text ="warning", relief=RAISED,bitmap="warning").grid(row=0,column=4)
        questhead_btn = Button(toolbar, text ="questhead", relief=RAISED,bitmap="questhead").grid(row=0,column=5)
        gray1_btn = Button(toolbar, text ="gray12", relief=RAISED,bitmap="gray12").grid(row=0,column=6)
        gray2_btn = Button(toolbar, text ="gray25", relief=RAISED,bitmap="gray25").grid(row=0,column=7)
        gray3_btn = Button(toolbar, text ="gray50", relief=RAISED,bitmap="gray50").grid(row=0,column=8)
        gray4_btn = Button(toolbar, text ="gray75", relief=RAISED,bitmap="gray75").grid(row=0,column=9)
        gray5_btn = Button(toolbar, text ="gray12", relief=RAISED,bitmap="gray12").grid(row=0,column=10)
        gray6_btn = Button(toolbar, text ="gray25", relief=RAISED,bitmap="gray25").grid(row=0,column=11)
        gray7_btn = Button(toolbar, text ="gray50", relief=RAISED,bitmap="gray50").grid(row=0,column=12)
        gray8_btn = Button(toolbar, text ="gray75", relief=RAISED,bitmap="gray75").grid(row=0,column=13)
        
        toolbar.grid(row=1,column=0,sticky=W)

    
    
# driver code
if __name__ == "__main__":
    root = Tk() # Create a new GUI window
    root.title('Horizon Drive DAQ GUI')
    root.configure(background = 'light blue') # Set the background color of GUI window
    root.geometry("1237x880") # Set the configuration of GUI window
    
    app = menubar()
    
    #headlabel = Label(root,text="Horizon Drive",fg='black',font=('futura',24,'italic'))
    tabControl = ttk.Notebook(root)
    progress = ttk.Progressbar(root,orient=HORIZONTAL,length=300,mode='determinate')
    progress.grid(row=1,column=2,sticky=W+E+N+S)
    
    test_run_buttons = PanedWindow(orient='vertical')
    test_run_buttons.grid(row=2,column=2,sticky=W+E+N+S)
    test_start_button = Button(root,text="START",height=2,highlightcolor='light green',relief=RAISED,background='green',activebackground='red')
    test_start_button.bind("<Button>", lambda e: onCancel())
    test_pause_button = Button(root,text="STOP TEST",height=2,highlightcolor='red2',relief=RAISED,background='red',activebackground='yellow')
    test_pause_button.bind("<Button>", lambda e: stop_test())
    camera_feed_button = Button(root,text="VIEW CAMERA FEED",relief=GROOVE)
    camera_feed_button.bind("<Button>",lambda e: NewWindow(root).camera_window())
    graph_btn = Button(root,text="GRAPH FILTERS",relief=RIDGE)
    graph_btn.bind("<Button>",lambda e: NewWindow(root).graph_settings())
    

    results_pane = Label(text="Results\n Q Factor:\n Thrust:\n Thrust/Power:",justify=LEFT,anchor=W,relief=RIDGE)
    active_sensor_pane = Label(text="Active Sensors:\nThermocouple\n Current Sensor\n Vacuum Pressure\n Magnetic Field\n Laser",justify=LEFT,anchor=W,relief=RIDGE)
    
    pw = PanedWindow(orient='horizontal')
    pw.grid(row=3,column=3)
    left = Label(text="Set test cycle length:")
    pw.add(left)
    cycle_length = Spinbox(from_=0,to=5)
    pw.add(cycle_length)
    
    test_run_buttons.add(active_sensor_pane)
    test_run_buttons.add(pw)
    test_run_buttons.add(test_start_button)
    test_run_buttons.add(test_pause_button)
    test_run_buttons.add(graph_btn)
    test_run_buttons.add(camera_feed_button)
    
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)

    tabControl.add(tab1,text="MCC 118 ANALOG VOLTAGE INPUT")
    tabControl.add(tab2,text="MCC 134 THERMOCOUPLE INPUT")
    tabControl.add(tab3,text="MCC 152 ANALOG OUTPUT / DIGITAL I/O")
    
    #count_label = Label(root)
    #count_label.grid(row=1,column=1)
    #counter_label(count_label)
    
    a = StringVar()
    b = StringVar()
    c = StringVar()
    gg = StringVar()
    ff = StringVar()
    aa = StringVar()
    dd = StringVar()
    zz = StringVar()
    gh = StringVar()
    
    stringvarlist = [a,b,c,gg,ff,aa,dd,zz,gh]
    
    temp_channel_1 = StringVar()
    temp_channel_2 = StringVar()
    temp_channel_3 = StringVar()
    temp_channel_4 = StringVar()
    temp_channel_5 = StringVar()
    
    temp_string_var_list = [temp_channel_1,temp_channel_2,temp_channel_3,temp_channel_4,temp_channel_5]
    
    analog_output_channel_1 = StringVar()
    analog_output_channel_2 = StringVar()
    analog_output_channel_3 = StringVar()
    
    analog_output_var_list = [analog_output_channel_1,analog_output_channel_2,analog_output_channel_3]
    
    dio_ch1 = StringVar()
    dio_ch2 = StringVar()
    dio_ch3 = StringVar()
    dio_ch4 = StringVar()
    dio_ch5 = StringVar()
    dio_ch6 = StringVar()
    dio_ch7 = StringVar()
    dio_ch8 = StringVar()
    dio_ch9 = StringVar()
    
    digital_output_var_list = [dio_ch1,dio_ch2,dio_ch3,dio_ch4,dio_ch5,dio_ch6,dio_ch7,dio_ch8,dio_ch9]
    
    ttk.Label(tab1,text="Channel Number").grid(row=0,column=0)
    for channels in analog_voltage_input:
        ttk.Label(tab1,text=channels).grid(row=r1,column=0,sticky=W)
        _avi_devices = ttk.Combobox(tab1,textvariable=stringvarlist[channels],takefocus=0)
        _avi_devices['values'] = AVI_DEVICES
        _avi_devices.grid(row=r1,column=1)
        avi_btn = ttk.Button(tab1,text=channels)
        avi_btn.grid(row=r1,column=2,sticky=W)
        avi_btn.bind("<Button>",lambda e: NewWindow(root))
        ttk.Entry(tab1,text=channels).grid(row=r1,column=3,sticky=W)
        r1+=1
    avi_button = Button(tab1,text="Get Shield Info")
    avi_button.grid(row=15,column=0)
    avi_button.bind("<Button>",lambda e: get_118_info())

    ttk.Label(tab2,text="Channel Number").grid(row=0,column=0)
    for channels in thermocouple_input:
        ttk.Label(tab2,text=channels).grid(row=r2,column=0,sticky=W)
        temp_devices = ttk.Combobox(tab2,textvariable=temp_string_var_list[channels],takefocus=0)
        temp_devices['values'] = THERMAL_DEVICES
        temp_devices.grid(row=r2,column=1)
        thermo_btn = ttk.Button(tab2,text=channels)
        thermo_btn.grid(row=r2,column=2)
        thermo_btn.bind("<Button>",lambda e: NewWindow(root))
        ttk.Label(tab2,text=channels).grid(row=r2,column=3)
        r2+=1
    thm_button = Button(tab2,text="Get Shield Info")
    thm_button.grid(row=15,column=0)
    thm_button.bind("<Button>",lambda e: get_134_info())
    
    ttk.Label(tab3,text="Channel Number").grid(row=0,column=0)
    for channels in analog_output:
        ttk.Label(tab3,text=channels).grid(row=r3,column=0,sticky=W)
        _avo_devices = ttk.Combobox(tab3,textvariable=analog_output_var_list[channels],takefocus=0)
        _avo_devices['values'] = A_O_DEVICES
        _avo_devices.grid(row=r3,column=1)
        ttk.Entry(tab3,text=channels).grid(row=r3,column=2)
        ao_btn = ttk.Button(tab3,text=channels)
        ao_btn.grid(row=r3,column=3)
        ao_btn.bind("<Button>",lambda e: NewWindow(root))
        ttk.Label(tab3,text=channels).grid(row=r3,column=4,sticky=W)
        r3+=1
    
        
    for channels in digital_i_o:
        ttk.Label(tab3,text=channels).grid(row=r4,column=0,sticky=W)
        digital_io_devices = ttk.Combobox(tab3,textvariable=digital_output_var_list[channels],takefocus=0)
        digital_io_devices['values'] = D_I_O_DEVICES
        digital_io_devices.grid(row=r4,column=1)
        dio_btn = ttk.Button(tab3,text=channels)
        dio_btn.grid(row=r4,column=2,sticky=W+E+N+S)
        dio_btn.bind("<Button>",lambda e: NewWindow(root))
        ttk.Label(tab3,text=channels).grid(row=r4,column=3,sticky=W)
        r4+=1
    dio_button = Button(tab3,text="Get Shield Info")
    dio_button.grid(row=20,column=0)
    dio_button.bind("<Button>",lambda e: get_152_info())


    noise_btn = Button(text="External Disturbance Input\n (Click after a test cycle is conducted if needed.)")
    noise_btn.bind("<Button>",lambda e: NoiseWindow(root))
    test_run_buttons.add(noise_btn)
    test_run_buttons.add(results_pane)
    
    # grid method is used for placing widgets at their respective positions
    #headlabel.grid(row=0,column=0,sticky=W+E+N+S,columnspan=3)
    tabControl.grid(row=2,column=0,columnspan=2,sticky=W+E+N+S)

    uN_mA_graph = Figure(figsize=(4,4),dpi=100)
    nm_uN_graph = Figure(figsize=(4,4),dpi=100)
    nm_W_graph = Figure(figsize=(4,4),dpi=100)
    em_force_as_function = uN_mA_graph.add_subplot(111,xlabel="Current (mA)",ylabel="Force (µN)")
    em_force_variations = nm_uN_graph.add_subplot(111,xlabel="Force (µN)",ylabel="Displacement (nm)")
    displacement_from_power = nm_W_graph.add_subplot(111,xlabel="Power (W)",ylabel="Displacement (nm)")
    em_force_as_function.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    em_force_variations.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    displacement_from_power.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5]) # most likely scenario would be to open a file to the csv text of the displacement data
    #dfp_plot = animation.FuncAnimation(nm_W_graph,animate,interval=1000)
    uN_mA_graph.suptitle("Force Produced from Current")
    nm_uN_graph.suptitle("Displacement with Varied Magnet Distances")
    nm_W_graph.suptitle("Displacement from Power")

    
    canvas1 = FigureCanvasTkAgg(uN_mA_graph,root)
    canvas2 = FigureCanvasTkAgg(nm_uN_graph,root)
    canvas3 = FigureCanvasTkAgg(nm_W_graph,root)
    canvas1.draw()
    canvas2.draw()
    canvas3.draw()
    canvas1.get_tk_widget().grid(row=3,column=1)
    canvas2.get_tk_widget().grid(row=3,column=0)
    canvas3.get_tk_widget().grid(row=3,column=2)

    
    root.mainloop()
