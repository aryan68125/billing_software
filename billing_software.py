import tkinter as tk

from tkinter import*

#config_bill_var module is the custome module that holds all the global variables that is to be used in the program
import config_bill_var

#custome module to send emails to customer
import send_custom_email

#import Developer_info.py module in the module
import Developer_info

#if the import of ImageTk does't work then 
#type in terminal :- for python3.5 and above--> sudo apt-get install python3-pil python3-pil.imagetk
#this module allows us to use png and jpg images in our program
from PIL import ImageTk,Image

#import database db module
#from db import Database class
from db import Database

#import system date and time
import current_date_time_of_india

#import messagebox library from tkinter
from tkinter import messagebox

#now here we will instanciate the db object
#it will create the table if not already present
db = Database('store.db')

#importing the custom email validator module that will validate the email address entered by the user
import email_address_validator

class Bill_App:
    #initializing function 
    #initializing all the ui elements of the application
    def __init__(self,window):
        #initializing the main window of the billing application
        self.window = window
        #setting up the window titile
        self.window.title("Billing Software")
        #setting up the window size on first boot
        self.window.geometry("1100x700")

        # setting up the minimum size and maximum size for the application's main window
        # set minimum window size value
        window.minsize(1080, 700)

        # set maximum window size value
        window.maxsize(1080, 700)

        """--------------------------------------variables used in the program-----------------------------------------------------"""

        #cosmetics_frame variables
        self.soap = IntVar() #number of soap purchased
        self.Face_cream = IntVar() #number of face cream purchased
        self.Face_Wash = IntVar() #number of face wash purchased
        self.Hair_spray = IntVar() #number of hair spray purchased
        self.Hair_gel = IntVar() #number of hair gel purchased
        self.Body_lotion = IntVar() #number of body lotion purchased

        #Grocery_frame variables
        self.Rice = IntVar() #number of kg rice purchased
        self.Food_oil = IntVar()
        self.Daal = IntVar() #number of kg dall purchased
        self.wheat = IntVar() #number of kg wheat purchased
        self.Sugar = IntVar() #number of kg sugar purchased
        self.Tea = IntVar()

        #cold_drinks frame variables
        self.maza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.thumbs_up = IntVar()
        self.Limca = IntVar()
        self.sprite = IntVar()

        #Bill_menu frame variables total product price and tax variables
        #total products prices variables
        self.total_cosmetics_price = StringVar()
        self.total_grocery_price = StringVar()
        self.total_cold_drink_price = StringVar()
        #tax variables
        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.Cold_Drink_tax = StringVar()
        self.Total_Payble_amount = StringVar()

        #customer info variables
        self.customer_name = StringVar()
        self.customer_phone_number = StringVar()
        self.customer_email_address = StringVar()

        """------------------------------------------------------------------------------------------------------------------------"""

        #--------------------customer Frame deals with the customer details------------------
        #background color for customer frame
        background_color_customer_frame = "#00008B"
        customer_frame = LabelFrame(self.window,text="Customer Details",font=("times new roman", 15, "bold"),fg = "gold", bg = background_color_customer_frame)
        #.place(x=0,y=80,relwidth=1) x and y is the position where the frame will appear in the window
        # relwidth is the welative width of the frame relative to the other ui components of the application
        customer_frame.place(x=0,y=0,relwidth=1)
        #frame height adjusts according to the content of the frame

        #customer name
        #fore ground color for the label fg="white"
        customer_name_Label = Label(customer_frame,text="Customer Name", font=("times new roman",12,"bold"),pady=3,padx=10,bg=background_color_customer_frame,fg="white").grid(row=0,column=0)
        #now creating the input text field for the customer_name_Label
        #border size -> bd=7,border style -> relief=SUNKEN
        customer_name_input_field = Entry(customer_frame, textvariable=self.customer_name,width=15,font = "arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=2)

        #customer phone number
        #fore ground color for the label fg="white"
        customer_phone_number_Label = Label(customer_frame,text="Phone number", font=("times new roman",12,"bold"),pady=3,padx=10,bg=background_color_customer_frame,fg="white").grid(row=0,column=2)
        #now creating the input text field for the customer_phone_number_Label
        #border size -> bd=7,border style -> relief=SUNKEN
        customer_phone_number_input_field = Entry(customer_frame, textvariable=self.customer_phone_number,width=15,font = "arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=2)

        #customer bill number
        #fore ground color for the label fg="white"
        customer_email_address_Label = Label(customer_frame,text="email address", font=("times new roman",12,"bold"),pady=3,padx=10,bg=background_color_customer_frame,fg="white").grid(row=0,column=4)
        #now creating the input text field for the customer_bill_number_Label
        #border size -> bd=7,border style -> relief=SUNKEN
        customer_email_address_input_field = Entry(customer_frame, textvariable=self.customer_email_address,width=15,font = "arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=3,padx=2)
        
        #search button customer frame
        #bill_search_button = Button(customer_frame, text=f"Search", bd=7,font = "arial 12 bold").grid(row=0,column=6,padx=2,pady=3)

        #--------------cosmetics Frame-----------------
        #background color for customer frame
        background_color_cosmetics_frame = "#9400d3"
        cosmetics_frame = LabelFrame(self.window,text="Cosmetics",font=("times new roman", 15, "bold"),fg = "white", bg = background_color_cosmetics_frame)
        #.place(x=0,y=80,relwidth=1) x and y is the position where the frame will appear in the window
        # relwidth is the welative width of the frame relative to the other ui components of the application
        #frame height and width are adjusted by the user
        cosmetics_frame.place(x=0,y=83,width=257,height=298)

        Bath_soap_Label = Label(cosmetics_frame,text="Bath Soap",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_cosmetics_frame,fg="white").grid(row=0,column=0,padx=5,pady=5,sticky="w")
        bath_soap_input_field = Entry(cosmetics_frame,textvariable=self.soap,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=5)

        Face_cream_Label = Label(cosmetics_frame,text="Face Cream",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_cosmetics_frame,fg="white").grid(row=1,column=0,padx=5,pady=5,sticky="w")
        Face_cream_input_field = Entry(cosmetics_frame,textvariable=self.Face_cream,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=5)

        Face_wash_Label = Label(cosmetics_frame,text="Face Wash",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_cosmetics_frame,fg="white").grid(row=2,column=0,padx=5,pady=5,sticky="w")
        Face_wash_input_field = Entry(cosmetics_frame,textvariable=self.Face_Wash,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=5)

        Hair_spray_Label = Label(cosmetics_frame,text="Hair Spray",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_cosmetics_frame,fg="white").grid(row=3,column=0,padx=5,pady=5,sticky="w")
        Hair_spray_input_field = Entry(cosmetics_frame,textvariable=self.Hair_spray,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=5)

        Hair_Gel_Label = Label(cosmetics_frame,text="Hair Gel",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_cosmetics_frame,fg="white").grid(row=4,column=0,padx=5,pady=5,sticky="w")
        Hair_Gel_input_field = Entry(cosmetics_frame,textvariable=self.Hair_gel,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=5)

        Body_Lotion_Label = Label(cosmetics_frame,text="Body Lotion",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_cosmetics_frame,fg="white").grid(row=5,column=0,padx=5,pady=5,sticky="w")
        Body_Lotion_input_field = Entry(cosmetics_frame,textvariable=self.Body_lotion,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=5,column=1,padx=5,pady=5)

        #--------------Grocery Frame-----------------
        #background color for Grocery frame
        background_color_Grocery_frame = "#800000"
        Grocery_frame = LabelFrame(self.window,text="Grocery",font=("times new roman", 15, "bold"),fg = "white", bg = background_color_Grocery_frame)
        #.place(x=0,y=80,relwidth=1) x and y is the position where the frame will appear in the window
        # relwidth is the welative width of the frame relative to the other ui components of the application
        Grocery_frame.place(x=259,y=83,width=233,height=298)
        #frame height and width are adjusted by the user

        Rice_Label = Label(Grocery_frame,text="Rice",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_Grocery_frame,fg="white").grid(row=0,column=0,padx=5,pady=5,sticky="w")
        Rice_input_field = Entry(Grocery_frame,textvariable=self.Rice,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=5)

        Food_oil_Label = Label(Grocery_frame,text="Food Oil",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_Grocery_frame,fg="white").grid(row=1,column=0,padx=5,pady=5,sticky="w")
        Food_oil_input_field = Entry(Grocery_frame,textvariable=self.Food_oil,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=5)

        Daal_Label = Label(Grocery_frame,text="Daal",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_Grocery_frame,fg="white").grid(row=2,column=0,padx=5,pady=5,sticky="w")
        Daal_input_field = Entry(Grocery_frame,textvariable=self.Daal,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=5)

        Wheat_Label = Label(Grocery_frame,text="Wheat",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_Grocery_frame,fg="white").grid(row=3,column=0,padx=5,pady=5,sticky="w")
        Wheat_input_field = Entry(Grocery_frame,textvariable=self.wheat,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=5)

        Sugar_Label = Label(Grocery_frame,text="Sugar",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_Grocery_frame,fg="white").grid(row=4,column=0,padx=5,pady=5,sticky="w")
        Sugar_input_field = Entry(Grocery_frame,textvariable=self.Sugar,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=5)

        Tea_Label = Label(Grocery_frame,text="Tea",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_Grocery_frame,fg="white").grid(row=5,column=0,padx=5,pady=5,sticky="w")
        Tea_input_field = Entry(Grocery_frame,textvariable=self.Tea,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=5,column=1,padx=5,pady=5)


        #--------------Cold Drink Frame-----------------
        #background color for Cold Drink frame
        background_color_Cold_Drink_frame = "#8B8000"
        Cold_Drink_frame = LabelFrame(self.window,text="Cold Drink",font=("times new roman", 15, "bold"),fg = "white", bg = background_color_Cold_Drink_frame)
        #.place(x=0,y=80,relwidth=1) x and y is the position where the frame will appear in the window
        # relwidth is the welative width of the frame relative to the other ui components of the application
        Cold_Drink_frame.place(x=494,y=83,width=250,height=298)
        #frame height and width are adjusted by the user

        Maza_Label = Label(Cold_Drink_frame,text="Maza",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_Cold_Drink_frame,fg="white").grid(row=0,column=0,padx=5,pady=5,sticky="w")
        Maza_input_field = Entry(Cold_Drink_frame,textvariable=self.maza,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=0,column=1,padx=3,pady=5)

        coke_Label = Label(Cold_Drink_frame,text="Coke",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_Cold_Drink_frame,fg="white").grid(row=1,column=0,padx=5,pady=5,sticky="w")
        coke_input_field = Entry(Cold_Drink_frame,textvariable=self.coke,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=1,column=1,padx=3,pady=5)

        Frooti_Label = Label(Cold_Drink_frame,text="Frooti",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_Cold_Drink_frame,fg="white").grid(row=2,column=0,padx=5,pady=5,sticky="w")
        Frooti_input_field = Entry(Cold_Drink_frame,textvariable=self.frooti,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=2,column=1,padx=3,pady=5)

        Thumbs_Up_Label = Label(Cold_Drink_frame,text="Thumbs Up",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_Cold_Drink_frame,fg="white").grid(row=3,column=0,padx=5,pady=5,sticky="w")
        Thumbs_Up_input_field = Entry(Cold_Drink_frame,textvariable=self.thumbs_up,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=3,column=1,padx=3,pady=5)

        Limca_Label = Label(Cold_Drink_frame,text="Limca",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_Cold_Drink_frame,fg="white").grid(row=4,column=0,padx=5,pady=5,sticky="w")
        Limca_input_field = Entry(Cold_Drink_frame,textvariable=self.Limca,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=4,column=1,padx=3,pady=5)

        Sprite_Label = Label(Cold_Drink_frame,text="Sprite",font=("times new roman",12,"bold"),pady=3,padx=5,bg=background_color_Cold_Drink_frame,fg="white").grid(row=5,column=0,padx=5,pady=5,sticky="w")
        Sprite_input_field = Entry(Cold_Drink_frame,textvariable=self.sprite,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=5,column=1,padx=3,pady=5)

        #---------------------Bill Area--------------------------------
        #background color for Bill Area frame
        background_color_Bill_Area_frame = "#FF8C00"
        Bill_Area_frame = Frame(self.window,bd=7,relief=GROOVE)
        #.place(x=0,y=80,relwidth=1) x and y is the position where the frame will appear in the window
        # relwidth is the welative width of the frame relative to the other ui components of the application
        Bill_Area_frame.place(x=747,y=83,width=330,height=298)
        #frame height and width are adjusted by the user
        
        #Label bill title
        Bill_title_Label = Label(Bill_Area_frame,text="Bill Area",font = "arial 12 bold", bd=5, relief=GROOVE).pack(fill=X)

        #scrollbar in y axis
        scroll_bar_for_bill_area_textView = Scrollbar(Bill_Area_frame, orient=VERTICAL)

        #here I am defining thew scroll bar position
        #here we will use self because i want this to appear global;ly throughout the page
        self.textarea = Text(Bill_Area_frame, yscrollcommand = scroll_bar_for_bill_area_textView.set)
        scroll_bar_for_bill_area_textView.pack(side=RIGHT,fill=Y)

        #configuring scrollbar
        scroll_bar_for_bill_area_textView.config(command = self.textarea.yview)
        self.textarea.pack(fill=BOTH)

        #---------------------------Menu Frame--------------------------
        #background color for Menu_frame
        Menu_frame_backgrount_color = "#d2582f"
        Menu_frame = LabelFrame(self.window,text="Bill Menu",font=("times new roman", 15, "bold"),fg = "white", bg = Menu_frame_backgrount_color)
        #.place(x=0,y=80,relwidth=1) x and y is the position where the frame will appear in the window
        # relwidth is the welative width of the frame relative to the other ui components of the application
        Menu_frame.place(x=0,y=385,relwidth=True,height=295)
        #frame height and width are adjusted by the user

        #Total prices of the purchased items
        Total_Cosmetics_Price_Label = Label(Menu_frame, text = "Total Cosmetic Price", font=("times new roman", 15, "bold"),fg = "white", bg = Menu_frame_backgrount_color).grid(row=0,column=0,padx=3,pady=5,sticky="W")
        Total_Cosmetics_Price_Entry = Entry(Menu_frame,textvariable=self.total_cosmetics_price,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=0,column=1,padx=3,pady=5)

        Total_Grocery_Price_Label = Label(Menu_frame, text = "Total Grocery Price", font=("times new roman", 15, "bold"),fg = "white", bg = Menu_frame_backgrount_color).grid(row=1,column=0,padx=3,pady=5,sticky="W")
        Total_Grocery_Price_Entry = Entry(Menu_frame,textvariable=self.total_grocery_price,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=1,column=1,padx=3,pady=5)
        
        Total_Cold_Drinks_Price_Label = Label(Menu_frame, text = "Total Cold Drinks Price", font=("times new roman", 15, "bold"),fg = "white", bg = Menu_frame_backgrount_color).grid(row=2,column=0,padx=3,pady=5,sticky="W")
        Total_Cold_Drinks_Price_Entry = Entry(Menu_frame,textvariable=self.total_cold_drink_price,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=2,column=1,padx=3,pady=5)

        # Tax on the purchased items by the customer
        Cosmetics_Price_Tax_Label = Label(Menu_frame, text = "Cosmetic Tax", font=("times new roman", 15, "bold"),fg = "white", bg = Menu_frame_backgrount_color).grid(row=0,column=2,padx=3,pady=5,sticky="W")
        Cosmetics_Price_Tax_Entry = Entry(Menu_frame,textvariable=self.cosmetic_tax,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=0,column=3,padx=3,pady=5)

        Grocery_Price_Tax_Label = Label(Menu_frame, text = "Grocery Tax", font=("times new roman", 15, "bold"),fg = "white", bg = Menu_frame_backgrount_color).grid(row=1,column=2,padx=3,pady=5,sticky="W")
        Grocery_Price_Tax_Entry = Entry(Menu_frame,textvariable=self.grocery_tax,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=1,column=3,padx=3,pady=5)
        
        Cold_Drinks_Tax_Price_Label = Label(Menu_frame, text = "Cold Drinks Tax", font=("times new roman", 15, "bold"),fg = "white", bg = Menu_frame_backgrount_color).grid(row=2,column=2,padx=3,pady=5,sticky="W")
        Cold_Drinks_Tax_Entry = Entry(Menu_frame,textvariable=self.Cold_Drink_tax,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=2,column=3,padx=3,pady=5)

        Total_Payble_amount_Label = Label(Menu_frame, text = "Total amount", font=("times new roman", 15, "bold"),fg = "white", bg = Menu_frame_backgrount_color).grid(row=3,column=0,padx=3,pady=5,sticky="W")
        Total_Payble_amount_Entry = Entry(Menu_frame,textvariable=self.Total_Payble_amount,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN).grid(row=3,column=1,padx=3,pady=5)


        #frame that will hold buttons Button_Frame
        Button_Frame_background = "#006400"
        Button_Frame = Frame(Menu_frame,bd=5,relief=GROOVE,bg=Button_Frame_background)
        Button_Frame.place(x=680,width=365,height=180)

        #buttons inside the button frame

        #it should generate the total amount paybale by the customer
        Total_Button = Button(Button_Frame,command = self.calculate_total_price,text = "Total",pady=5).grid(row=0,column=0,padx=5,pady=5)

        #when we press total button it should genearate the final bill for the customer and save the bill inside the database
        Generate_Bill_Button = Button(Button_Frame,command = self.welcome_bill,text = "Generate Bill",pady=5).grid(row=0,column=1,padx=5,pady=5)

        #when the user press this button it should open a new window where the developers info will be shown
        Dev_Info_Button = Button(Button_Frame,text = "Developer info",pady=5,command = open_a_new_window).grid(row=0,column=2,padx=5,pady=5)


        #when the user presses the clear button it should clear all the input fields in the application
        Clear_Button = Button(Button_Frame,command = self.clear,text = "Clear",pady=5).grid(row=1,column=0,padx=5,pady=5)

        #this button should open a new window and in that window there will be list 
        Show_all_Bills_Button = Button(Button_Frame,text = "Show all bills",pady=5,command=show_all_bills).grid(row=1,column=1,padx=5,pady=5)
        
        #this button will send bill via email self.send_mail()                
        Send_mail_via_email_button = Button(Button_Frame,text = "send bill",pady=5,command=self.send_mail).grid(row=1,column=2,padx=5,pady=5,sticky="W")

    #this function will handle all the calculation related to the purchased items
    def calculate_total_price(self):
        print("calculate_total_price()")
        
        #total cosmetics price calulation isnumeric()
        try:
            config_bill_var.soap_bought = self.soap.get()
            config_bill_var.Face_cream_bought = self.Face_cream.get()
            config_bill_var.Face_Wash_bought = self.Face_Wash.get()
            config_bill_var.Hair_spray_bought = self.Hair_spray.get()
            config_bill_var.Hair_gel_bought = self.Hair_gel.get()
            config_bill_var.Body_lotion_bought = self.Body_lotion.get()
        except:
            print("An exception occurred")
            self.textarea.insert(END,"Oops! something went wrong\nwhile calculating cosmetics price")

        #total price of the cosmetics 
        total_cosmetics_price_calculation = float(
        (config_bill_var.soap_bought*40) + (config_bill_var.Face_cream_bought*120) + (config_bill_var.Face_Wash_bought*60) + (config_bill_var.Hair_spray_bought*180) + 
        (config_bill_var.Hair_gel_bought*140) + (config_bill_var.Body_lotion_bought*180)
        )

        config_bill_var.total_cosmetics_price_global = str(total_cosmetics_price_calculation)
        self.total_cosmetics_price.set(config_bill_var.total_cosmetics_price_global)
        print(f"config_bill_var.total_cosmetics_price_global {config_bill_var.total_cosmetics_price_global}")

        #total cosmetic price tax
        cosmetic_tax = float(config_bill_var.total_cosmetics_price_global) * 0.05 #cosmetic tax calculation
        config_bill_var.cosmetic_tax_global = round(cosmetic_tax,2)
        self.cosmetic_tax.set(str(config_bill_var.cosmetic_tax_global)) 
        print(f"config_bill_var.cosmetic_tax_global = {config_bill_var.cosmetic_tax_global}")

        #total grocery price calculation
        try:
            config_bill_var.Rice_bought = self.Rice.get()
            config_bill_var.Food_oil_bought = self.Food_oil.get()
            config_bill_var.Daal_bought = self.Daal.get()
            config_bill_var.wheat_bought = self.wheat.get()
            config_bill_var.Sugar_bought = self.Sugar.get()
            config_bill_var.Tea_bought = self.Tea.get()
        except:
            print("An exception occurred")
            self.textarea.insert(END,"Oops! something went wrong\nwhile calculating grocery price")

        #total price of the grocery 
        total_grocery_price_calculation = float(
          (config_bill_var.Rice_bought*80) + (config_bill_var.Food_oil_bought*180) + (config_bill_var.Daal_bought*60) + (config_bill_var.wheat_bought*240) + 
          (config_bill_var.Sugar_bought*45) + (config_bill_var.Tea_bought*150)
            )

        config_bill_var.total_grocery_price_global = str(total_grocery_price_calculation)
        self.total_grocery_price.set(config_bill_var.total_grocery_price_global)
        print(f"config_bill_var.total_grocery_price_global {config_bill_var.total_grocery_price_global}")

        #total grocery price tax
        grocery_tax = float(config_bill_var.total_grocery_price_global) * 0.1 #grocery tax calculation
        config_bill_var.grocery_tax_global = round(grocery_tax,2)
        self.grocery_tax.set(str(config_bill_var.grocery_tax_global)) 
        print(f"config_bill_var.grocery_tax_global = {config_bill_var.grocery_tax_global}")

        #total cold drink price calculation
        try:
            config_bill_var.maza_bought = self.maza.get()
            config_bill_var.coke_bought = self.coke.get()
            config_bill_var.frooti_bought = self.frooti.get()
            config_bill_var.thumbs_up_bought = self.thumbs_up.get()
            config_bill_var.Limca_bought = self.Limca.get()
            config_bill_var.sprite_bought = self.sprite.get()
        except:
            print("An exception occurred")
            self.textarea.insert(END,"Oops! something went wrong\nwhile calculating cold drinks price")

        #total price of the cold drink 
        total_cold_drink_price_calculation = float(
          (config_bill_var.maza_bought*60) + (config_bill_var.coke_bought*60) + (config_bill_var.frooti_bought*50) + (config_bill_var.thumbs_up_bought*45) + 
          (config_bill_var.Limca_bought*40) + (config_bill_var.sprite_bought*60)
            )

        config_bill_var.total_cold_drink_price_global = str(total_cold_drink_price_calculation)
        self.total_cold_drink_price.set(config_bill_var.total_cold_drink_price_global)
        print(f"config_bill_var.total_cold_drink_price_global {config_bill_var.total_cold_drink_price_global}")

        #total cold drink price tax
        cold_drink_tax = float(config_bill_var.total_cold_drink_price_global) * 0.15 #cold drink tax calculation
        config_bill_var.Cold_Drink_tax_global = round(cold_drink_tax,2)
        self.Cold_Drink_tax.set(str(config_bill_var.Cold_Drink_tax_global)) 
        print(f"config_bill_var.Cold_Drink_tax_global = {config_bill_var.Cold_Drink_tax_global}")

        #calculation of total payable amount
        Total_amount_to_be_payed_by_customer = float(
            float(config_bill_var.total_cosmetics_price_global) + float(config_bill_var.cosmetic_tax_global) + float(config_bill_var.total_grocery_price_global) + float(config_bill_var.grocery_tax_global) + float(config_bill_var.total_cold_drink_price_global) + float(config_bill_var.Cold_Drink_tax_global)
            )
        config_bill_var.Total_payable_amount_global = str(Total_amount_to_be_payed_by_customer)
        self.Total_Payble_amount.set(config_bill_var.Total_payable_amount_global)

        #get current date and time
        current_date_time = str(current_date_time_of_india.datetime_India)
        config_bill_var.current_date_time_global = current_date_time
        print(f"config_bill_var.current_date_time_global :- {config_bill_var.current_date_time_global}")

        #database insert operation
        #inseting customer into the database when total button is clicked
        if self.customer_name.get() == "" or self.customer_phone_number.get() == "" or self.customer_email_address.get() == "":
            print("cutomer details cannot be empty")
            config_bill_var.flag = 1

        else:
            config_bill_var.flag = 0
            #refreshing the bill area text field
            self.textarea.delete("1.0","end")

            #validate email
            if email_address_validator.check(self.customer_email_address.get()) == False:
                messagebox.showerror("Error 0xA420Emailx4200", "email address is not valid!")
            elif email_address_validator.check(self.customer_email_address.get()) == True:
                db.insert(config_bill_var.current_date_time_global,self.customer_name.get(),self.customer_phone_number.get(),self.customer_email_address.get(),self.soap.get(),self.Face_cream.get(),self.Face_Wash.get(),self.Hair_spray.get(),self.Hair_gel.get(),self.Body_lotion.get(), self.Rice.get(),self.Food_oil.get(),self.Daal.get(),self.wheat.get(),self.Sugar.get(),self.Tea.get(),self.maza.get(),self.coke.get(),self.frooti.get(),self.thumbs_up.get(),self.Limca.get(),self.sprite.get(),self.total_cosmetics_price.get(),self.total_grocery_price.get(),self.total_cold_drink_price.get(),self.cosmetic_tax.get(),self.grocery_tax.get(),self.Cold_Drink_tax.get(),self.Total_Payble_amount.get())
                #getting data from the database by reading the entire database using forloop
                for row in db.fetch():
                    #compare the date and time if config_bill_var.current_date_time_global == str(row[1]) {CURRENT DATE AND TIME FROM THE DATABASE}
                    date_and_time_from_database = str(row[1])
                    print(f"date_and_time_from_database :- {date_and_time_from_database}")
                    if config_bill_var.current_date_time_global == date_and_time_from_database:
                        #getting the bill id from the database 
                        #note that the bill id = database row id
                        #END = the new info will be inserted at the end of the list box
                        #tnd the things we are inserting will be the row returned by the fetch() method
                        config_bill_var.bill_number_global = str(row[0])
                        print("bill id:- "+config_bill_var.bill_number_global)
                        print(row)
    
                        #getting the email id of the customer from the database
                        #this email id will be used to send bill via email to the customer when we generate the bill for the customer
                        config_bill_var.reciever_email_address = str(row[4])
                        print(f"config_bill_var.reciever_email_address :- {config_bill_var.reciever_email_address}")
    
        #create an error dialogue box to show error message
        if config_bill_var.flag == 1:
            messagebox.showerror("Error 0xA113Inputx0000", "Customer Details is empty!")
            config_bill_var.flag = 0        

    #this function will generate a welcome message in the bill area
    def welcome_bill(self):
        print("welcome_bill()")
        #refreshing the bill area text field
        self.textarea.delete("1.0","end")
        #getting data from the database by reading the entire database using forloop
        for row in db.fetch():
            #compare the date and time if config_bill_var.current_date_time_global == str(row[1]) {CURRENT DATE AND TIME FROM THE DATABASE}
            date_and_time_from_database = str(row[1])
            print(f"date_and_time_from_database :- {date_and_time_from_database}")
            if config_bill_var.current_date_time_global == date_and_time_from_database:
                #refresh the bill area
                self.textarea.delete("1.0","end")
                # print a welcome message
                self.textarea.insert(END,"Welcome to test retail\n")
                #getting the bill id from the database 
                #note that the bill id = database row id
                #END = the new info will be inserted at the end of the list box
                #tnd the things we are inserting will be the row returned by the fetch() method
                config_bill_var.bill_number_global = str(row[0])
                print("bill id:- "+config_bill_var.bill_number_global)
                
                config_bill_var.customer_name_global = str(row[2]) #customer name
                self.textarea.insert(END,"Customer name:- "+config_bill_var.customer_name_global+"\n")
                
                config_bill_var.customer_phone_number_global = str(row[3])
                self.textarea.insert(END,"Ph no:- "+config_bill_var.customer_phone_number_global+"\n")

                config_bill_var.bill_number_global = str(row[0])
                self.textarea.insert(END,"bill no:- "+config_bill_var.bill_number_global+"\n")

                config_bill_var.current_date_time_global = str(row[1])
                self.textarea.insert(END,"date & time:- "+config_bill_var.current_date_time_global+"\n")

                config_bill_var.reciever_email_address = str(row[4])
                self.textarea.insert(END,"email:- "+config_bill_var.reciever_email_address+"\n")

                config_bill_var.soap_bought = int(row[5])
                self.textarea.insert(END,"soap (pcs):- "+str(config_bill_var.soap_bought)+"\n")

                config_bill_var.Face_cream_bought = int(row[6])
                self.textarea.insert(END,"face cream (pcs):- "+str(config_bill_var.Face_cream_bought)+"\n")

                config_bill_var.Face_Wash_bought = int(row[7])
                self.textarea.insert(END,"face wash (pcs):- "+str(config_bill_var.Face_Wash_bought)+"\n")

                config_bill_var.Hair_spray_bought = int(row[8])
                self.textarea.insert(END,"hair spray (pcs):- "+str(config_bill_var.Hair_spray_bought)+"\n")

                config_bill_var.Hair_gel_bought = int(row[9])
                self.textarea.insert(END,"hair gel (pcs):- "+str(config_bill_var.Hair_gel_bought)+"\n")

                config_bill_var.Body_lotion_bought = int(row[10])
                self.textarea.insert(END,"body lotion (pcs):- "+str(config_bill_var.Body_lotion_bought)+"\n")

                config_bill_var.Rice_bought = int(row[11])
                self.textarea.insert(END,"Rice (Kg):- "+str(config_bill_var.Rice_bought)+"\n")

                config_bill_var.Food_oil_bought = int(row[12])
                self.textarea.insert(END,"food oil (pcs):- "+str(config_bill_var.Food_oil_bought)+"\n")

                config_bill_var.Daal_bought = int(row[13])
                self.textarea.insert(END,"Daal (Kg):- "+str(config_bill_var.Daal_bought)+"\n")

                config_bill_var.wheat_bought = int(row[14])
                self.textarea.insert(END,"Wheat (Kg):- "+str(config_bill_var.wheat_bought)+"\n")

                config_bill_var.Sugar_bought = int(row[15])
                self.textarea.insert(END,"Sugar (Kg):- "+str(config_bill_var.Sugar_bought)+"\n")

                config_bill_var.Tea_bought = int(row[16])
                self.textarea.insert(END,"Tea (pcs):- "+str(config_bill_var.Tea_bought)+"\n")

                config_bill_var.maza_bought = int(row[17])
                self.textarea.insert(END,"Maza (pcs):- "+str(config_bill_var.maza_bought)+"\n")

                config_bill_var.coke_bought = int(row[18])
                self.textarea.insert(END,"Coke (pcs):- "+str(config_bill_var.coke_bought)+"\n")

                config_bill_var.frooti_bought = int(row[19])
                self.textarea.insert(END,"frooti (pcs):- "+str(config_bill_var.frooti_bought)+"\n")

                config_bill_var.thumbs_up_bought = int(row[20])
                self.textarea.insert(END,"thumbs up (pcs):- "+str(config_bill_var.thumbs_up_bought)+"\n")

                config_bill_var.Limca_bought = int(row[21])
                self.textarea.insert(END,"Limca (pcs):- "+str(config_bill_var.Limca_bought)+"\n")

                config_bill_var.sprite_bought = int(row[22])
                self.textarea.insert(END,"Sprite (pcs):- "+str(config_bill_var.sprite_bought)+"\n")

                config_bill_var.total_cosmetics_price_global = str(row[23])
                self.textarea.insert(END,"Total Cosmetic Price:- "+config_bill_var.total_cosmetics_price_global+"\n")

                config_bill_var.cosmetic_tax_global = str(row[26]) 
                self.textarea.insert(END,"cosmetic tax:- "+config_bill_var.cosmetic_tax_global+"\n")

                config_bill_var.total_grocery_price_global = str(row[24])
                self.textarea.insert(END,"Total grocery price:- "+config_bill_var.total_grocery_price_global+"\n")

                config_bill_var.grocery_tax_global = str(row[27]) 
                self.textarea.insert(END,"grocery tax:- "+config_bill_var.grocery_tax_global+"\n")

                config_bill_var.total_cold_drink_price_global = str(row[25]) 
                self.textarea.insert(END,"Total cold drink price:- "+config_bill_var.total_cold_drink_price_global+"\n")

                config_bill_var.Cold_Drink_tax_global = str(row[28]) 
                self.textarea.insert(END,"cold drinks tax:- "+config_bill_var.Cold_Drink_tax_global+"\n")

                config_bill_var.Total_payable_amount_global = str(row[29]) 
                self.textarea.insert(END,"Total payable amount:- "+config_bill_var.Total_payable_amount_global+"\n")
                
                print(str(self.textarea.get("1.0","end")))
                print(row)
                config_bill_var.flag_error_total = 0

            else:
                print("price not calculated .....")
                print("please calculate the price and try again later!")
                #create an error dialogue box to show error message
                config_bill_var.flag_error_total = 1
            
        if config_bill_var.flag_error_total == 1:
            messagebox.showerror("Error 0xS#E*X69007", "Price not calculated!")
            config_bill_var.flag_error_total = 0

    #this function will generate bill in the bill area
    #attach this function to the generate bill button
    def send_mail(self):
            print("send_email()")
            try:
                #send the bill via email to the customer
                config_bill_var.mail_body = str(self.textarea.get("1.0","end"))
                send_custom_email.send_email()
                messagebox.showinfo("Email sent", "Bill sent to customer named: \n"+ config_bill_var.customer_name_global)

                #reset global config_module for the email body to refresh the email client
                config_bill_var.mail_body = ""
                #send the bill via text message to the customer via mobile number
            except:
                print("An exception occurred")
                self.textarea.insert(END,"Could not send bill via email")

    #this function will clear all the text and entry fields 
    def clear(self):
        print("clear()")
        self.textarea.delete("1.0","end")
                #cosmetics_frame variables
        self.soap.set("") #number of soap purchased
        self.Face_cream.set("") #number of face cream purchased
        self.Face_Wash.set("") #number of face wash purchased
        self.Hair_spray.set("") #number of hair spray purchased
        self.Hair_gel.set("")#number of hair gel purchased
        self.Body_lotion.set("") #number of body lotion purchased

        #Grocery_frame variables
        self.Rice.set("") #number of kg rice purchased
        self.Food_oil.set("")
        self.Daal.set("") #number of kg dall purchased
        self.wheat.set("")#number of kg wheat purchased
        self.Sugar.set("") #number of kg sugar purchased
        self.Tea.set("")

        #cold_drinks frame variables
        self.maza.set("")
        self.coke.set("")
        self.frooti.set("")
        self.thumbs_up.set("")
        self.Limca.set("")
        self.sprite.set("")

        #Bill_menu frame variables total product price and tax variables
        #total products prices variables
        self.total_cosmetics_price.set("")
        self.total_grocery_price.set("")
        self.total_cold_drink_price.set("")
        #tax variables
        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.Cold_Drink_tax.set("")
        self.Total_Payble_amount.set("")

        #customer info variables
        self.customer_name.set("")
        self.customer_phone_number.set("")
        self.customer_email_address.set("")


#----------------------------function for developer info-----------------------------------------------------------------------

#this function will open a new window that will show the developer info inside the new window
#importing image to our program
#note this has to be done outside any function otherwise the import will not happen
#image5 = ImageTk.PhotoImage(Image.open("/home/aditya/development/python/imageViewer/icons/linux5.png"))

#creating a function that will create a new window
def open_a_new_window():
    developer_window = Toplevel()
    #setting up the window titile
    developer_window.title("Developer Information")
    developer_window.geometry("530x500")

    # setting up the minimum size and maximum size for the application's developer window
    # set minimum window size value
    developer_window.minsize(530, 500)

    # set maximum window size value
    developer_window.maxsize(530, 500)

    #background color for Menu_frame
    Developer_frame_backgrount_color = "#fa8072"
    Developer_frame = LabelFrame(developer_window,text="Developer Information",bd=7,relief=GROOVE,font=("times new roman", 15, "bold"),fg = "white", bg = Developer_frame_backgrount_color)
    #.place(x=0,y=80,relwidth=1) x and y is the position where the frame will appear in the window
    # relwidth is the welative width of the frame relative to the other ui components of the application
    Developer_frame.place(x=0,y=0,width=528,height=500)

    #developer info is shown here using Labels
    #name
    Dev_name_Label = Label(Developer_frame,text="Name:-",font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=0,column=0,padx=5,pady=5,sticky="w")
    Dev_name_aditya_Label = Label(Developer_frame,text=Developer_info.Name,font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=0,column=1,padx=5,pady=5,sticky="w")
    #roll number
    Roll_Number_Label = Label(Developer_frame,text="Roll no:-",font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=1,column=0,padx=5,pady=5,sticky="w")
    Roll_number_Label = Label(Developer_frame,text=Developer_info.Roll_Number,font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=1,column=1,padx=5,pady=5,sticky="w")
    #College_code
    College_code_Label = Label(Developer_frame,text="College code:-",font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=2,column=0,padx=5,pady=5,sticky="w")
    College_code_Label = Label(Developer_frame,text=Developer_info.College_code,font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=2,column=1,padx=5,pady=5,sticky="w")
    #Branch
    Branch_Label = Label(Developer_frame,text="Branch:-",font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=3,column=0,padx=5,pady=5,sticky="w")
    Branch_2_Label = Label(Developer_frame,text=Developer_info.Branch,font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=3,column=1,padx=5,pady=5,sticky="w")
    #Course
    Course_Label = Label(Developer_frame,text="Course:-",font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=4,column=0,padx=5,pady=5,sticky="w")
    Course_2_Label = Label(Developer_frame,text=Developer_info.Course,font=("times new roman",12,"bold"),pady=3,padx=5,bg=Developer_frame_backgrount_color,fg="white").grid(row=4,column=1,padx=5,pady=5,sticky="w")
    
    #import image from the directory
    #make canvas and img varables into global variable otherwise the image will not show up in the application
    global canvas
    global img
    canvas = Canvas(Developer_frame, width =229, height = 355)  
    canvas.grid(row=0,column=2,rowspan=5)  
    img = ImageTk.PhotoImage(Image.open("dev.png"))  
    #canvas.create_image(x = 2,y = 2, anchor=NW, image=img) 
    #canvas will start drawing the image from the coordinates 2,2  
    canvas.create_image(2, 2, anchor=NW, image=img)  

#------------------------------------------function for show all bills button-----------------------------------------------------
#this function will create a new window and show all the list of customers that has purchased items from the shop
def show_all_bills():
    global show_all_bills_window
    show_all_bills_window = Toplevel()
    #setting up the window titile
    show_all_bills_window.title("Bill Archive")
    show_all_bills_window.geometry("890x500")

    # setting up the minimum size and maximum size for the application's developer window
    # set minimum window size value
    show_all_bills_window.minsize(1024, 715)

    # set maximum window size value
    show_all_bills_window.maxsize(1024, 715)

    #---------------------Bill List-------------------------------------------------
    #background color for Bill list frame
    Bill_List_Background_color = "#6495ed"
    Bill_List_frame = LabelFrame(show_all_bills_window,text="List of Bills",font=("times new roman", 15, "bold"),fg = "white", bg = Bill_List_Background_color)

    Bill_List_frame.place(x=0,y=0,relwidth=1,height=350)
    #frame height and width are adjusted by the user

    #now here we are creating a listBox widget which will show the list of computer parts
    #border =0 will create a border less listbox tkinter widget height=10 , width=50
    global bill_List
    bill_List = Listbox(Bill_List_frame,border=0)
    bill_List.place(x=5,y=0,width=990,height=317)

    #populate the bill_list from the database
    populate_list()

    #adding a scrollbar in the
    # step-1: import tkinter as tk
    #step-2: then use tk object of tkinter to call Scrollbar tk.Scrollbar(Bill_Area_frame_Bill_Archive_window_Frame,orient = VERTICAL)
    """otherwise error will generate scroll_y = Scrollbar(Bill_Area_frame_Bill_Archive_window_Frame,orient = VERTICAL) 
    TypeError: 'Scrollbar' object is not callable"""
    #now creating a scrollbar for our ListBox widget which will allow us to scroll the contents of our ListBox
    Scrollbar = tk.Scrollbar(Bill_List_frame)
    Scrollbar.pack(side=RIGHT,fill=Y)
    #now here we are connecting our scrollbar to our ListBox
    bill_List.configure(yscrollcommand=Scrollbar.set)
    #command = bill_List.yview->is telling scrollbar wighet to scroll the listBox in y axis when scrollbar is scrolled
    #by the user in y axis
    Scrollbar.configure(command = bill_List.yview)
    #binding our select item function '<<ListboxSelect>>'  to our listBox and function that we are using is select_item()
    bill_List.bind('<<ListboxSelect>>',select_item)
    #---------------------Bill List END-------------------------------------------------

    #---------------------Bill Details Frame----------------------------------------------
    #background color for Bill list frame
    Bill_details_Background_color = "#008080"
    Bill_details_frame = LabelFrame(show_all_bills_window,text="Bill Details",font=("times new roman", 15, "bold"),fg = "white", bg = Bill_details_Background_color)
    Bill_details_frame.place(x=0,y=352,relwidth=1,height=350)

    #---------------------------Bill Show Area Frame--------------------------------------
    #background color for Bill Area frame
    Bill_Area_frame_Bill_Archive_window_bg_color = "#FF8C00"
    Bill_Area_frame_Bill_Archive_window_Frame = Frame(Bill_details_frame,bd=7,relief=GROOVE)
    #.place(x=0,y=80,relwidth=1) x and y is the position where the frame will appear in the window
    # relwidth is the welative width of the frame relative to the other ui components of the application
    Bill_Area_frame_Bill_Archive_window_Frame.place(x=3,y=0,width=460,height=318)
    #frame height and width are adjusted by the user

    #Label bill title
    Bill_title_Archive_window_Label = Label(Bill_Area_frame_Bill_Archive_window_Frame,text="Bill Area",font = "arial 12 bold", bd=5, relief=GROOVE).pack(fill=X)
    
    #adding a scrollbar in the
    # step-1: import tkinter as tk
    #step-2: then use tk object of tkinter to call Scrollbar tk.Scrollbar(Bill_Area_frame_Bill_Archive_window_Frame,orient = VERTICAL)
    """otherwise error will generate scroll_y = Scrollbar(Bill_Area_frame_Bill_Archive_window_Frame,orient = VERTICAL) 
    TypeError: 'Scrollbar' object is not callable"""
    scroll_y = tk.Scrollbar(Bill_Area_frame_Bill_Archive_window_Frame,orient = VERTICAL)
    scroll_y.pack(side=RIGHT,fill=Y) 

    #adding text area to the Bill_Area_frame_Bill_Archive_window_Frame
    global textarea
    textarea = Text(Bill_Area_frame_Bill_Archive_window_Frame,yscrollcommand=scroll_y.set)
    textarea.pack(fill=BOTH)

    #configuring scroll bar
    scroll_y.configure(command = textarea.yview)
    #--------------------------------Bill Show Area Frame END----------------------------------------------

    #-----------------------------Bill search by id frame START-------------------------------------------
    #now create a Bill search frame in the Bill_details_frame
    #background color for Bill list frame
    Bill_Search_Background_color = "#556b2f"
    Bill_Search_frame = LabelFrame(Bill_details_frame,text="Search or Delete Bill",font=("times new roman", 15, "bold"),fg = "white", bg = Bill_Search_Background_color)

    Bill_Search_frame.place(x=480,y=0,width=400,height=220)

    Bill_id_search_Lable = Label(Bill_Search_frame,text="Search by Bill id",font=("times new roman", 15, "bold"),fg = "white", bg = Bill_Search_Background_color)
    Bill_id_search_Lable.grid(row=0,column=0,padx=10,pady=5)

    global bill_id_var
    global Bill_id_search_database_entry
    bill_id_var=StringVar()
    Bill_id_search_database_entry = Entry(Bill_Search_frame,textvariable = bill_id_var,width=15,font=("times new roman",12,"bold"), bd=5,relief=SUNKEN)
    Bill_id_search_database_entry.grid(row=0,column=1,padx=10,pady=5)
 
    #when the user presses the Search button it should Search the bill using bill id as a search parameter
    #the search operation must be performed by using binary search technique
    Bill_id_search_database_button = Button(Bill_Search_frame,command = search_the_bill_via_bill_id,text = "Search",pady=5).grid(row=1,column=1,padx=10,pady=5,sticky="W")
    
    Delete_bill_button = Button(Bill_Search_frame,command = delete_bill_id,text = "Delete",pady=5).grid(row=2,column=1,padx=10,pady=5,sticky="W")

    #this button will send bill via email send_mail_copy()                
    Send_mail_via_email_button = Button(Bill_Search_frame,text = "send bill",pady=5,command=send_mail_copy).grid(row=3,column=1,padx=10,pady=5,sticky="W")

    #-----------------------------Bill search by id frame END-------------------------------------------
    #---------------------Bill Details Frame END----------------------------------------------

    
def search_the_bill_via_bill_id():
    print("search_the_bill_via_bill_id()")
    config_bill_var.search_bill_global = str(bill_id_var.get()) #bill id to be searched in the database
    print("entry bill id:- "+ config_bill_var.search_bill_global)
    
    #getting data from the database by reading the entire database using forloop
    for row in db.fetch():
        #compare the date and time if config_bill_var.search_bill_global == bill_id_from_database
        bill_id_from_database = str(row[0])
        print(f"bill_id_from_database :- {bill_id_from_database}")
        if config_bill_var.search_bill_global == bill_id_from_database:
            #refresh the bill area
            textarea.delete("1.0","end")
            # print a welcome message
            textarea.insert(END,"Welcome to test retail\n")
            #getting the bill id from the database 
            #note that the bill id = database row id
            #END = the new info will be inserted at the end of the list box
            #tnd the things we are inserting will be the row returned by the fetch() method
            config_bill_var.bill_number_global = str(row[0])
            print("bill id:- "+config_bill_var.bill_number_global)
                
            config_bill_var.customer_name_global = str(row[2]) #customer name
            textarea.insert(END,"Customer name:- "+config_bill_var.customer_name_global+"\n")
                
            config_bill_var.customer_phone_number_global = str(row[3])
            textarea.insert(END,"Ph no:- "+config_bill_var.customer_phone_number_global+"\n")

            config_bill_var.bill_number_global = str(row[0])
            textarea.insert(END,"bill no:- "+config_bill_var.bill_number_global+"\n")

            config_bill_var.current_date_time_global_window_two = str(row[1])
            textarea.insert(END,"date & time:- "+config_bill_var.current_date_time_global_window_two+"\n")

            config_bill_var.reciever_email_address = str(row[4])
            textarea.insert(END,"email:- "+config_bill_var.reciever_email_address+"\n")

            config_bill_var.soap_bought = int(row[5])
            textarea.insert(END,"soap (pcs):- "+str(config_bill_var.soap_bought)+"\n")

            config_bill_var.Face_cream_bought = int(row[6])
            textarea.insert(END,"face cream (pcs):- "+str(config_bill_var.Face_cream_bought)+"\n")

            config_bill_var.Face_Wash_bought = int(row[7])
            textarea.insert(END,"face wash (pcs):- "+str(config_bill_var.Face_Wash_bought)+"\n")

            config_bill_var.Hair_spray_bought = int(row[8])
            textarea.insert(END,"hair spray (pcs):- "+str(config_bill_var.Hair_spray_bought)+"\n")

            config_bill_var.Hair_gel_bought = int(row[9])
            textarea.insert(END,"hair gel (pcs):- "+str(config_bill_var.Hair_gel_bought)+"\n")

            config_bill_var.Body_lotion_bought = int(row[10])
            textarea.insert(END,"body lotion (pcs):- "+str(config_bill_var.Body_lotion_bought)+"\n")

            config_bill_var.Rice_bought = int(row[11])
            textarea.insert(END,"Rice (Kg):- "+str(config_bill_var.Rice_bought)+"\n")

            config_bill_var.Food_oil_bought = int(row[12])
            textarea.insert(END,"food oil (pcs):- "+str(config_bill_var.Food_oil_bought)+"\n")

            config_bill_var.Daal_bought = int(row[13])
            textarea.insert(END,"Daal (Kg):- "+str(config_bill_var.Daal_bought)+"\n")

            config_bill_var.wheat_bought = int(row[14])
            textarea.insert(END,"Wheat (Kg):- "+str(config_bill_var.wheat_bought)+"\n")

            config_bill_var.Sugar_bought = int(row[15])
            textarea.insert(END,"Sugar (Kg):- "+str(config_bill_var.Sugar_bought)+"\n")

            config_bill_var.Tea_bought = int(row[16])
            textarea.insert(END,"Tea (pcs):- "+str(config_bill_var.Tea_bought)+"\n")

            config_bill_var.maza_bought = int(row[17])
            textarea.insert(END,"Maza (pcs):- "+str(config_bill_var.maza_bought)+"\n")

            config_bill_var.coke_bought = int(row[18])
            textarea.insert(END,"Coke (pcs):- "+str(config_bill_var.coke_bought)+"\n")

            config_bill_var.frooti_bought = int(row[19])
            textarea.insert(END,"frooti (pcs):- "+str(config_bill_var.frooti_bought)+"\n")

            config_bill_var.thumbs_up_bought = int(row[20])
            textarea.insert(END,"thumbs up (pcs):- "+str(config_bill_var.thumbs_up_bought)+"\n")

            config_bill_var.Limca_bought = int(row[21])
            textarea.insert(END,"Limca (pcs):- "+str(config_bill_var.Limca_bought)+"\n")

            config_bill_var.sprite_bought = int(row[22])
            textarea.insert(END,"Sprite (pcs):- "+str(config_bill_var.sprite_bought)+"\n")

            config_bill_var.total_cosmetics_price_global = str(row[23])
            textarea.insert(END,"Total Cosmetic Price:- "+config_bill_var.total_cosmetics_price_global+"\n")

            config_bill_var.cosmetic_tax_global = str(row[26]) 
            textarea.insert(END,"cosmetic tax:- "+config_bill_var.cosmetic_tax_global+"\n")

            config_bill_var.total_grocery_price_global = str(row[24])
            textarea.insert(END,"Total grocery price:- "+config_bill_var.total_grocery_price_global+"\n")

            config_bill_var.grocery_tax_global = str(row[27]) 
            textarea.insert(END,"grocery tax:- "+config_bill_var.grocery_tax_global+"\n")

            config_bill_var.total_cold_drink_price_global = str(row[25]) 
            textarea.insert(END,"Total cold drink price:- "+config_bill_var.total_cold_drink_price_global+"\n")

            config_bill_var.Cold_Drink_tax_global = str(row[28]) 
            textarea.insert(END,"cold drinks tax:- "+config_bill_var.Cold_Drink_tax_global+"\n")

            config_bill_var.Total_payable_amount_global = str(row[29]) 
            textarea.insert(END,"Total payable amount:- "+config_bill_var.Total_payable_amount_global+"\n")

            print(str(textarea.get("1.0","end")))
            print(row)
            config_bill_var.flag_error_total = 0
            break

        else:
            print("Bill not found .....")
            print("The customer is not present in the database!")
            #create an error dialogue box to show error message
            config_bill_var.flag_error_total = 1
            
    if config_bill_var.flag_error_total == 1:
        textarea.delete("1.0","end")
        textarea.insert(END,"-----------bill not found in the database!!---------\n")
        config_bill_var.flag_error_total = 0

#this function is responsible for actually getting the data from the database
def populate_list():
    print("populate")
    #this will delete any previously stored information in our listBox
    bill_List.delete(0, END)
    # db.fetch() = def fetch(self): function inside our db.py module and we are accessing that using db object in this module
    #so here in this for loop we are going to loop through all the rows of our table and populate our listBox
    #beacause we know def fetch(self): is returning rows in db.py module
    for row in db.fetch():
        #END = the new info will be inserted at the end of the list box
        #tnd the things we are inserting will be the row returned by the fetch() method
        print("id:- "+str(row[0]))
        print(row)
        bill_List.insert(END, row)

#this function helps to select a bill from the list box 
selected_item_details =''
def select_item(event):
    print("Select Item")
    try:
        global selected_item
        global selected_item_details
        global Selected_item_view

        #Selected_item_view.config(text="")
        #now we will be getting the index of the selected item in the listBox
        index = bill_List.curselection()[0]
        selected_item = bill_List.get(index)
        print("printing selected_item = "+ str(selected_item))

        #here we will put the selected_item data into the input Fiedls
        #but before we put in the data related to our selected_item data we need to remove anything present int the input fields
        #clear_input()
        
        # inserting the selected record details from the lisBox widget to our text area and the bill id should be inserted in the search entry
        #refresh the bill area
        textarea.delete("1.0","end")
        # print a welcome message
        textarea.insert(END,"Welcome to test retail\n")
        #getting the bill id from the database 
        #note that the bill id = database selected_item id
        #END = the new info will be inserted at the end of the list box
        #tnd the things we are inserting will be the selected_item returned by the fetch() method
        config_bill_var.bill_number_global = str(selected_item[0])
        print("bill id:- "+config_bill_var.bill_number_global)
        #set the bill id entry to the selected bill id from the list
        bill_id_var.set(config_bill_var.bill_number_global)
                
        config_bill_var.customer_name_global = str(selected_item[2]) #customer name
        textarea.insert(END,"Customer name:- "+config_bill_var.customer_name_global+"\n")
              
        config_bill_var.customer_phone_number_global = str(selected_item[3])
        textarea.insert(END,"Ph no:- "+config_bill_var.customer_phone_number_global+"\n")

        config_bill_var.bill_number_global = str(selected_item[0])
        textarea.insert(END,"bill no:- "+config_bill_var.bill_number_global+"\n")

        config_bill_var.current_date_time_global_window_two = str(selected_item[1])
        textarea.insert(END,"date & time:- "+config_bill_var.current_date_time_global_window_two+"\n")

        config_bill_var.reciever_email_address = str(selected_item[4])
        textarea.insert(END,"email:- "+config_bill_var.reciever_email_address+"\n")

        config_bill_var.soap_bought = int(selected_item[5])
        textarea.insert(END,"soap (pcs):- "+str(config_bill_var.soap_bought)+"\n")

        config_bill_var.Face_cream_bought = int(selected_item[6])
        textarea.insert(END,"face cream (pcs):- "+str(config_bill_var.Face_cream_bought)+"\n")

        config_bill_var.Face_Wash_bought = int(selected_item[7])
        textarea.insert(END,"face wash (pcs):- "+str(config_bill_var.Face_Wash_bought)+"\n")

        config_bill_var.Hair_spray_bought = int(selected_item[8])
        textarea.insert(END,"hair spray (pcs):- "+str(config_bill_var.Hair_spray_bought)+"\n")

        config_bill_var.Hair_gel_bought = int(selected_item[9])
        textarea.insert(END,"hair gel (pcs):- "+str(config_bill_var.Hair_gel_bought)+"\n")

        config_bill_var.Body_lotion_bought = int(selected_item[10])
        textarea.insert(END,"body lotion (pcs):- "+str(config_bill_var.Body_lotion_bought)+"\n")

        config_bill_var.Rice_bought = int(selected_item[11])
        textarea.insert(END,"Rice (Kg):- "+str(config_bill_var.Rice_bought)+"\n")

        config_bill_var.Food_oil_bought = int(selected_item[12])
        textarea.insert(END,"food oil (pcs):- "+str(config_bill_var.Food_oil_bought)+"\n")

        config_bill_var.Daal_bought = int(selected_item[13])
        textarea.insert(END,"Daal (Kg):- "+str(config_bill_var.Daal_bought)+"\n")

        config_bill_var.wheat_bought = int(selected_item[14])
        textarea.insert(END,"Wheat (Kg):- "+str(config_bill_var.wheat_bought)+"\n")

        config_bill_var.Sugar_bought = int(selected_item[15])
        textarea.insert(END,"Sugar (Kg):- "+str(config_bill_var.Sugar_bought)+"\n")

        config_bill_var.Tea_bought = int(selected_item[16])
        textarea.insert(END,"Tea (pcs):- "+str(config_bill_var.Tea_bought)+"\n")

        config_bill_var.maza_bought = int(selected_item[17])
        textarea.insert(END,"Maza (pcs):- "+str(config_bill_var.maza_bought)+"\n")

        config_bill_var.coke_bought = int(selected_item[18])
        textarea.insert(END,"Coke (pcs):- "+str(config_bill_var.coke_bought)+"\n")

        config_bill_var.frooti_bought = int(selected_item[19])
        textarea.insert(END,"frooti (pcs):- "+str(config_bill_var.frooti_bought)+"\n")

        config_bill_var.thumbs_up_bought = int(selected_item[20])
        textarea.insert(END,"thumbs up (pcs):- "+str(config_bill_var.thumbs_up_bought)+"\n")

        config_bill_var.Limca_bought = int(selected_item[21])
        textarea.insert(END,"Limca (pcs):- "+str(config_bill_var.Limca_bought)+"\n")

        config_bill_var.sprite_bought = int(selected_item[22])
        textarea.insert(END,"Sprite (pcs):- "+str(config_bill_var.sprite_bought)+"\n")

        config_bill_var.total_cosmetics_price_global = str(selected_item[23])
        textarea.insert(END,"Total Cosmetic Price:- "+config_bill_var.total_cosmetics_price_global+"\n")

        config_bill_var.cosmetic_tax_global = str(selected_item[26]) 
        textarea.insert(END,"cosmetic tax:- "+config_bill_var.cosmetic_tax_global+"\n")

        config_bill_var.total_grocery_price_global = str(selected_item[24])
        textarea.insert(END,"Total grocery price:- "+config_bill_var.total_grocery_price_global+"\n")

        config_bill_var.grocery_tax_global = str(selected_item[27]) 
        textarea.insert(END,"grocery tax:- "+config_bill_var.grocery_tax_global+"\n")

        config_bill_var.total_cold_drink_price_global = str(selected_item[25]) 
        textarea.insert(END,"Total cold drink price:- "+config_bill_var.total_cold_drink_price_global+"\n")

        config_bill_var.Cold_Drink_tax_global = str(selected_item[28]) 
        textarea.insert(END,"cold drinks tax:- "+config_bill_var.Cold_Drink_tax_global+"\n")

        config_bill_var.Total_payable_amount_global = str(selected_item[29]) 
        textarea.insert(END,"Total payable amount:- "+config_bill_var.Total_payable_amount_global+"\n")

        print(str(textarea.get("1.0","end")))
        config_bill_var.flag_error_total = 0

    except IndexError:
        pass
 
#this function should delete the bill selected in the list box 
def delete_bill_id():
    #get the bill id from the bill id search entry in window 2
    bill_number_to_be_deleted = int(bill_id_var.get())
    
    #delete the bill from the database
    db.remove(bill_number_to_be_deleted)
    populate_list()
    textarea.delete("1.0","end")
    bill_id_var.set("")

#this function will generate bill in the bill area
def send_mail_copy():
    print("nont a self send_email() function")
    try:
        #send the bill via email to the customer
        config_bill_var.mail_body = str(textarea.get("1.0","end"))
        send_custom_email.send_email()
        print(config_bill_var.mail_body)
    except:
        print("An exception occurred")
        textarea.insert(END,"Could not send bill via email")

#creating a tkinter object
window = Tk()

#creating the object for the Bill_App class
obj = Bill_App(window)
window.mainloop()