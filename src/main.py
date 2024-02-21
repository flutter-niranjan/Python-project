from tkinter import *
from tkinter import messagebox
import random,os

billnumber=random.randint(500,1000)

if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno("Confirm","Do you want to save the bill")
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f"bills/{billnumber}.txt",'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'bill number {billnumber} is saved successfully')
        billnumber=random.randint(500,1000)



def total():
    global soapprice,hairsprayprice,hairgelprice,facecreamprice,facewashprice,bodylotionprice
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairgelprice=int(hairgelEntry.get())*150
    hairsprayprice=int(hairsprayEntry.get())*80
    bodylotionprice=int(bodylotionEntry.get())*60

    totalcosmeticprice=soapprice+facewashprice+facecreamprice+hairgelprice+hairsprayprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmeticprice} Rs')
    cosmtictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,f'{cosmtictax} Rs')

    global riceprice,daalprice,oilprice,wheatprice,sugerprice,teaprice
    riceprice=int(riceEntry.get())*30 
    daalprice=int(daalEntry.get())*100
    oilprice=int(oilEntry.get())*120
    wheatprice=int(wheatEntry.get())*50
    sugerprice=int(sugarEntry.get())*140
    teaprice=int(teaEntry.get())*80

    totalgroceryprice=riceprice+daalprice+oilprice+wheatprice+sugerprice+teaprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice} Rs')
    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,f'{grocerytax} Rs')

    global mazzaprice,pepsiprice,spriteprice,dewprice,frootiprice,cocacolaprice
    mazzaprice=int(mazzaEntry.get())*20
    pepsiprice=int(pepsiEntry.get())*20
    spriteprice=int(spritEntry.get())*20
    dewprice=int(dewEntry.get())*20
    frootiprice=int(frootiEntry.get())*20
    cocacolaprice=int(cocacolaEntry.get())*20

    totalcolddrinkprice=mazzaprice+pepsiprice+spriteprice+dewprice+frootiprice+cocacolaprice
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,f'{totalcolddrinkprice} Rs')
    drinktax=totalcolddrinkprice*0.08
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,f'{drinktax} Rs')
    global totalbill
    totalbill=totalcosmeticprice+totalgroceryprice+totalcolddrinkprice+cosmtictax+grocerytax+drinktax

def bill_area():
    name=nameEntry.get()

    if nameEntry.get()=="" or phoneEntry.get()=="":
        messagebox.showerror("Error","Customer Details Required")

    elif cosmeticpriceEntry.get()=="" and grocerypriceEntry.get()=="" and drinkspriceEntry.get()=="":
        messagebox.showerror("Error","No products are selected")

    elif cosmeticpriceEntry.get()=="0 Rs" and grocerypriceEntry.get()=="0 Rs" and drinkspriceEntry.get()=="0 Rs":
        messagebox.showerror("Error","No products are selected")
        
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,"*\t\t*WELCOME CUSTOMER**\n\n")
        textarea.insert(END,f"\nBill Number: {billnumber}\n")
        textarea.insert(END,f"\nCustomer Name: {nameEntry.get()}\n")
        textarea.insert(END,f"\nCustomer Phone number: {phoneEntry.get()}\n")
        textarea.insert(END,'\n=======================================================\n')
        textarea.insert(END,"Product\t\t\tQuantity\t\t\tPrice")
        textarea.insert(END,'\n=======================================================\n')

        if bathsoapEntry.get()!="0":
            textarea.insert(END,f"\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs")
        if hairsprayEntry.get()!="0":
            textarea.insert(END,f"\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs")
        if hairgelEntry.get()!="0":
            textarea.insert(END,f"\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs")
        if facecreamEntry.get()!="0":
            textarea.insert(END,f"\nFaceCream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs")
        if facewashEntry.get()!="0":
            textarea.insert(END,f"\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs")
        if bodylotionEntry.get()!="0":
            textarea.insert(END,f"\nbody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{hairgelprice} Rs")

        
        if riceEntry.get()!="0":
            textarea.insert(END,f"\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs")
        if daalEntry.get()!="0":
            textarea.insert(END,f"\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs")
        if oilEntry.get()!="0":
            textarea.insert(END,f"\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs")
        if wheatEntry.get()!="0":
            textarea.insert(END,f"\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs")
        if sugarEntry.get()!="0":
            textarea.insert(END,f"\nSuger\t\t\t{sugarEntry.get()}\t\t\t{sugerprice} Rs")
        if teaEntry.get()!="0":
            textarea.insert(END,f"\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs")

        
        if mazzaEntry.get()!="0":
            textarea.insert(END,f"\nMazza\t\t\t{mazzaEntry.get()}\t\t\t{mazzaprice} Rs")
        if pepsiEntry.get()!="0":
            textarea.insert(END,f"\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs")
        if spritEntry.get()!="0":
            textarea.insert(END,f"\nSprite\t\t\t{spritEntry.get()}\t\t\t{pepsiprice} Rs")
        if dewEntry.get()!="0":
            textarea.insert(END,f"\nDew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs")
        if frootiEntry.get()!="0":
            textarea.insert(END,f"\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs")
        if cocacolaEntry.get()!="0":
            textarea.insert(END,f"\nCocaCola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaprice} Rs")

        textarea.insert(END,'\n------------------------------------------------------\n')

        if cosmetictaxEntry.get()!="0.0 Rs":
            textarea.insert(END,f"\nCosmetic Tax\t\t\t\t{cosmetictaxEntry.get()}")
        if grocerytaxEntry.get()!="0.0 Rs":
            textarea.insert(END,f"\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}")
        if drinkstaxEntry.get()!="0.0 Rs":
            textarea.insert(END,f"\nDrinks Tax\t\t\t\t{drinkstaxEntry.get()}")
        textarea.insert(END,f"\n\nTotal bill\t\t\t\t{totalbill}")
        
        textarea.insert(END,'\n=======================================================\n')

        save_bill()


root=Tk()

root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('asset/images/bill.ico')
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold','underline'),bg='lightcyan3',fg='dark slate gray',bd=12,relief=RAISED)
headingLabel.pack(fill=X,)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),bg='lightcyan3',fg='dark slate gray',bd=8,relief=RAISED)
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billNumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billNumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),bg='lightcyan3',fg='dark slate gray',bd=8,relief=RAISED)
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
facewashEntry.insert(0,0)

hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),bg='lightcyan3',fg='dark slate gray',bd=8,relief=RAISED)
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
oilEntry.insert(0,0)

daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
daalEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
wheatEntry.insert(0,0)

sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
sugarEntry.insert(0,0)

teaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
teaEntry.insert(0,0)

colddrinksFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),bg='lightcyan3',fg='dark slate gray',bd=8,relief=RAISED)
colddrinksFrame.grid(row=0,column=2)

mazzaLabel=Label(colddrinksFrame,text='Mazza',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
mazzaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

mazzaEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
mazzaEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
mazzaEntry.insert(0,0)

pepsiLabel=Label(colddrinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

pepsiEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
pepsiEntry.insert(0,0)

spritLabel=Label(colddrinksFrame,text='Sprit',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
spritLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

spritEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spritEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
spritEntry.insert(0,0)

dewLabel=Label(colddrinksFrame,text='Dew',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

dewEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
dewEntry.insert(0,0)

frootiLabel=Label(colddrinksFrame,text='Frooti',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

frootiEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
frootiEntry.insert(0,0)

cocacolaLabel=Label(colddrinksFrame,text='Coca Cola',font=('times new roman',15,'bold'),bg='lightcyan3',fg='black')
cocacolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

cocacolaEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cocacolaEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
cocacolaEntry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=RAISED)
billframe.grid(row=0,column=3,padx=10)

billarealLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=RAISED)
billarealLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),bg='lightcyan3',fg='dark slate gray',bd=8,relief=RAISED)
billmenuFrame.pack()
0
cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',14,'bold'),bg='lightcyan3',fg='black')
cosmeticpriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')

cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10,sticky='w')

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',14,'bold'),bg='lightcyan3',fg='black')
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10,sticky='w')

drinkspriceLabel=Label(billmenuFrame,text='Cold Drinks Price',font=('times new roman',14,'bold'),bg='lightcyan3',fg='black')
drinkspriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')

drinkspriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=6,padx=10,sticky='w')

cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',14,'bold'),bg='lightcyan3',fg='black')
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')

cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10,sticky='w')

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',14,'bold'),bg='lightcyan3',fg='black')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')

grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10,sticky='w')

drinkstaxLabel=Label(billmenuFrame,text='Cold Drinks Tax',font=('times new roman',14,'bold'),bg='lightcyan3',fg='black')
drinkstaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')

drinkstaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=6,padx=10,sticky='w')


buttonframe=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonframe.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonframe,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonframe,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonframe,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonframe,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonframe,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
clearButton.grid(row=0,column=4,pady=20,padx=5)

root.mainloop()