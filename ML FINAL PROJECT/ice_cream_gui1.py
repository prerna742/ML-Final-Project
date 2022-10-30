import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as ttk

model = pd.read_pickle('ice_cream.pickle')

app = ttk.Tk()
app.geometry('500x500')
app.title('Ice Cream Bussiness Revenue Prediction')

temp = ttk.Variable(app)
ttk.Label(app, text='Temperature', padx = 15, pady = 15).grid(row = 0, column = 0)
ttk.Entry(app, textvariable=temp, width=10).grid(row=0, column =1)

def prediction():
    global model
    query_data  = {'Temperature' : [temp.get()]}
    revenue = model.predict(pd.DataFrame(query_data))
    result.set(80*float(revenue))

ttk.Button(app, text="Calculate Revenue", command=prediction, font=('Arial',16)).grid(row=4, column=0, columnspan=2)

result=ttk.Variable(app)
result.set('0')
ttk.Label(app, text="Revenue genrated in rupees", font=('Arial', 20)).grid(row=5, column=0, columnspan=2)
ttk.Label(app, textvariable=result, pady=15, font=('Arial', 20)).grid(row=6, column=0, columnspan=2)

app.mainloop()