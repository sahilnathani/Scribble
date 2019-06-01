# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 08:51:38 2019

@author: Sahil Nathani
"""

#ML 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import cross_validation, svm


df = pd.read_csv("DataFiles\\Admission_graduate_school.csv")

df.drop(['Serial No.'], 1, inplace=True)

x = np.array(df.drop(['Chance of Admit '], 1))
y = np.array(df['Chance of Admit '])

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)

clf = svm.SVR(kernel='linear', gamma=0.02)
clf.fit(x_train, y_train)
accuracy = clf.score(x_test, y_test)


#_____________________________________________________________________________#


#GUI
import tkinter as tk
from tkinter import StringVar, IntVar
from tkinter import ttk, messagebox#used for styling. simply put css for tkinter.
from PIL import ImageTk, Image
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
import cv2

#MongoDB
from pymongo import MongoClient
import pprint
#from IPython.display import clear_output

Large_Font = ("Verdana", 14)
Small_Font = ("Verdana", 8)

class main_class(tk.Tk):#inherited the Tk class in xyz
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        #tk.Tk.iconbitmap(self, default="C:\\Users\\Sahil Nathani\\Desktop\\DBMS_Project\\retrieve data.ico")
        tk.Tk.wm_title(self, "SCRIBBLE")
        
        container = tk.Frame(self, bg='black')
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}#dictionary of all the pages to be added in the app
        
        login_page = LoginPage(container, self)
        selection_page = SelectionPage(container, self)
        update_page = UpdatePage(container, self)
        retrieve_page = RetrievalPage(container, self)
        grapher_page = GrapherPage(container, self)
        help_page = HelpPage(container, self)
        
        self.frames[LoginPage] = login_page
        self.frames[SelectionPage] = selection_page
        self.frames[UpdatePage] = update_page
        self.frames[RetrievalPage] = retrieve_page
        self.frames[GrapherPage] = grapher_page
        self.frames[HelpPage] = help_page
        
        login_page.grid(row=0, column=0, sticky="nsew")#nsew=north, south, east, west. stretches content
        selection_page.grid(row=0, column=0, sticky="nsew")
        update_page.grid(row=0, column=0, sticky="nsew")
        retrieve_page.grid(row=0, column=0, sticky="nsew")
        grapher_page.grid(row=0, column=0, sticky="nsew")
        help_page.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(LoginPage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()#pops up the page
 
def qf(string):
   print(string) 
       
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        #nice background image
       tk.Frame.__init__(self, parent)#counstructor of tk.Frame
       
       def validate():
           user_name = str(t1.get())
           password = str(t2.get())
           if ((user_name=='robinsir') & (password=='robin19@ieee.org')):
               controller.show_frame(SelectionPage)
           elif ((user_name=='prashant') & (password=='it1707.iiitbhopal@gmail.com')):
               controller.show_frame(SelectionPage)  
           elif ((user_name=='sahil') & (password=='kannunathani@gmail.com')):
               controller.show_frame(SelectionPage) 
           else:
               messagebox.showerror(title='Invalid Credentials', message='Provided credentials are not authorised to proceed')
       
       label1 = ttk.Label(self, text="User Name", font=Large_Font)
       label1.grid(row=1, pady=40, padx=400)
       t1 = ttk.Entry(self)
       t1.grid(row=1, column=2)
       
       label2 = ttk.Label(self, text='Password', font=Large_Font)
       label2.grid(row=5)
       t2 = ttk.Entry(self)
       t2.grid(row=5, column=2)
       button1 = ttk.Button(self, text="LOGIN", command=lambda: validate())
       button1.grid(row=10)
       
       
class SelectionPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #background_image=tk.PhotoImage(file = 'C:\\Users\\Sahil Nathani\\Desktop\\DBMS_Project\\selectionpage.jpg')
        #background_label = tk.Label(parent, image=background_image)
        #background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #add the image for each button 
        button1 = ttk.Button(self, text="UPDATE & DELETE", command=lambda: controller.show_frame(UpdatePage))
        button2 = ttk.Button(self, text="RETRIEVE", command=lambda: controller.show_frame(RetrievalPage))
        button3 = ttk.Button(self, text="GRAPHER", command=lambda: controller.show_frame(GrapherPage))
        button4 = ttk.Button(self, text="HELP & CREDITS", command=lambda: controller.show_frame(HelpPage))
        button5 = ttk.Button(self, text="LOG OUT", command=lambda: controller.show_frame(LoginPage))
        #background_label.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()


class GrapherPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       
        
        def graph():
            z1 = cb1.get()
            z2 = cb2.get()
            plt.xlabel(z1)
            plt.ylabel(z2)
            plt.scatter(df[z1], df[z2])
            plt.show()
                
            
        label1 = ttk.Label(self, text="Select X-Axis for Graph", font=Small_Font)
        cb1 = ttk.Combobox(self, values=('GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA', 'Research', 'Chance of Admit'))
        label2 = ttk.Label(self, text="Select Y-Axis for Graph", font=Small_Font)
        cb2 = ttk.Combobox(self, values=('GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA', 'Research', 'Chance of Admit'))
        button1 = ttk.Button(self, text="Plot the Graph", command=lambda: graph())
        back = ttk.Button(self, text="Go back to Selection Page", command=lambda: controller.show_frame(SelectionPage))
        label1.grid(row=0, column=1)
        cb1.grid(row=0, column=10)
        label2.grid(row=5, column=1)
        cb2.grid(row=5, column=10)
        button1.grid(row=10, column=5)
        back.grid(row=10, column=10)
  
    
class HelpPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = ttk.Label(self, text = " THIS SITE MAY CONTAIN INACCURACIES AND TYPOGRAPHICAL ERRORS. \nWE DOES NOT WARRANT THE ACCURACY OR COMPLETENESS \nOF THE MATERIALS OR THE his Site and all its Contents are intended solely \nfor personal, non-commercial use. Except as expressly provided, \nnothing within the Site shall be construed as conferring any license under our or \nany third party's intellectual property rights, whether by estoppel, \nimplication, waiver, or otherwise. Without limiting the generality of the foregoing, you acknowledge and agree \nthat all content available through and used to operate the Site and \nits services is protected by copyright, trademark, patent, or other proprietary rights. You agree not to: \n(a) modify, alter, or deface any of the trademarks, service marks, trade dress (collectively Trademarks) or other intellectual \nproperty made available by us in connection with the Site; (b) hold yourself out as in any way sponsored by, affiliated with, or \nendorsed by us, or any of our affiliates or service providers; \n(c) use any of the Trademarks or other content accessible through the Site for any purpose other than the \npurpose for which we have made it available to you; (d) defame or disparage us, our Trademarks, or \nany aspect of the Site; and (e) adapt, translate, modify, decompile, disassemble, or reverse engineer \nthe Site or any software or programs used in connection with it or its products and services.The framing, \nmirroring, scraping or data mining of the Site or any of its content in any form and by any \nmethod is expressly prohibited. RELIABILITY OF ANY ADVICE, OPINION, STATEMENT OR OTHER INFORMATION DISPLAYED OR \nDISTRIBUTED THROUGH THE SITE. YOU EXPRESSLY UNDERSTAND AND AGREE THAT: (i) YOUR USE OF THE SITE, INCLUDING ANY \nRELIANCE ON ANY SUCH OPINION, ADVICE, STATEMENT, MEMORANDUM, OR INFORMATION CONTAINED HEREIN, SHALL BE AT YOUR SOLE RISK; (ii) THE SITE IS PROVIDED ON AN AS \nIS AND AS AVAILABLE BASIS; (iii) EXCEPT AS EXPRESSLY PROVIDED HEREIN WE DISCLAIM ALL WARRANTIES OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO IMPLIED WARRANTIES OF \nMERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, WORKMANLIKE EFFORT, \nTITLE AND NON-INFRINGEMENT; (iv) WE MAKE NO WARRANTY WITH RESPECT TO THE RESULTS THAT MAY BE OBTAINED FROM THIS SITE, \nTHE PRODUCTS OR SERVICES ADVERTISED OR OFFERED OR MERCHANTS INVOLVED; (v) \nANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF THE SITE IS DONE \nAT YOUR OWN DISCRETION AND RISK; and (vi) YOU WILL BE SOLELY RESPONSIBLE FOR ANY DAMAGE TO YOUR COMPUTER SYSTEM \nOR FOR ANY LOSS OF DATA THAT RESULTS FROM THE DOWNLOAD OF ANY SUCH MATERIAL.B. YOU UNDERSTAND AND \nAGREE THAT UNDER NO CIRCUMSTANCES, INCLUDING, BUT NOT LIMITED TO, \nNEGLIGENCE, SHALL WE BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, PUNITIVE OR CONSEQUENTIAL DAMAGES \nTHAT RESULT FROM THE USE OF, OR THE INABILITY TO USE, ANY OF OUR SITES OR MATERIALS OR FUNCTIONS \nON ANY SUCH SITE, EVEN IF WE HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. THE FOREGOING LIMITATIONS SHALL APPLY NOTWITHSTANDING ANY FAILURE \nOF ESSENTIAL PURPOSE OF ANY LIMITED REMEDY.", font=Small_Font)
        back = ttk.Button(self, text="Go back to Selection Page", command=lambda: controller.show_frame(SelectionPage))
        label1.pack()
        back.pack()


class RetrievalPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #combo box for selection of the condition
#        v = StringVar()
#        def get_condition():
#            cb_str = cb4.get()
#            s = ""
#            if cb_str=='GRE Score':
#                s = '>mark OR <mark'
#            elif cb_str=='TOEFL Score':
#                s = '>mark OR <mark'
#            elif cb_str=='University Rating':
#                s = '>rate OR <rate'
#            elif cb_str=='SOP':
#                s = '>rate OR <rate'
#            elif cb_str=='LOR':
#                s = '>rate OR <rate' 
#            elif cb_str=='CGPA':
#                s = '>grade OR <grade'  
#            elif cb_str=='Research':
#                s = '1 OR 0'
#            elif cb_str=='Chance of Admit':
#                s = '>chance OR <chance'
#            v.set(s)
#            retrieve_data(s)
        
        def retrieve_data():
          client = MongoClient("mongodb://analytics:analytics-password@analytics-shard-00-00-dccgh.mongodb.net:27017,analytics-shard-00-01-dccgh.mongodb.net:27017,analytics-shard-00-02-dccgh.mongodb.net:27017/test?ssl=true&replicaSet=analytics-shard-0&authSource=admin&retryWrites=true")
          z = cb4.get()
          x = text1.get()
          pipeline = [
                  {
                          '$match': {z : x}
                          }
                  ]
          
          S = tk.Scrollbar(self)
          T = tk.Text(self, height=30, width=100)
          S.grid()
          T.grid()
          S.config(command=T.yview)
          T.config(yscrollcommand=S.set)
          
          text = (list(client.analytics.Graduate_Admission.aggregate(pipeline)))
          for each_doc in text:
             textx = each_doc['_id'] 
             T.insert(tk.END, textx)
             T.insert(tk.END, "\n")
          
        def sort():
          client = MongoClient("mongodb://analytics:analytics-password@analytics-shard-00-00-dccgh.mongodb.net:27017,analytics-shard-00-01-dccgh.mongodb.net:27017,analytics-shard-00-02-dccgh.mongodb.net:27017/test?ssl=true&replicaSet=analytics-shard-0&authSource=admin&retryWrites=true")
          z = "$"+cb4.get()
          print(str(z))
          pipeline =[
                  {
                     '$sortByCount': z
                  }
                  ]
          
          S = tk.Scrollbar(self)
          T = tk.Text(self, height=30, width=100)
          S.grid()
          T.grid()
          S.config(command=T.yview)
          T.config(yscrollcommand=S.set)
          
          text = (list(client.analytics.Graduate_Admission.aggregate(pipeline)))
          for each_doc in text:
             textx = each_doc 
             T.insert(tk.END, textx)
             T.insert(tk.END, "\n")
         
        
        def text83():
          client = MongoClient("mongodb://analytics:analytics-password@analytics-shard-00-00-dccgh.mongodb.net:27017,analytics-shard-00-01-dccgh.mongodb.net:27017,analytics-shard-00-02-dccgh.mongodb.net:27017/test?ssl=true&replicaSet=analytics-shard-0&authSource=admin&retryWrites=true")
          z = "$"+cb4.get()
          print(str(z))
          pipeline =[
                  {
                     '$sortByCount': z
                  }
                  ]
          
          text1 = list(client.analytics.Graduate_Admission.aggregate(pipeline)['_id'])
          return text1
        
        label = ttk.Label(self, text='Select the Condition', font=Small_Font)
        cb4 = ttk.Combobox(self, values=('GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA', 'Research', 'Chance of Admit'))
        label1 = ttk.Label(self, text="Enter the Constraint:", font=Small_Font)
        text1 = ttk.Entry(self)
        sort_button = ttk.Button(self, text="Sort", command=lambda: sort())
        b1 = ttk.Button(self, text="Find!", command=lambda: retrieve_data())
        back = ttk.Button(self, text="Go back to Selection Page", command=lambda: controller.show_frame(SelectionPage))
        
        label.grid(row=0, column=0)
        b1.grid(row=10, column=20)
        back.grid(row=10, column=10)
        cb4.grid(row=0, column=10)
        sort_button.grid(row=10, column=15)
        label1.grid(row=5, column=10)
        text1.grid(row=5, column=20)
        #will be printed on the console because text are isn't available.
        
        
class UpdatePage(tk.Frame):

    def __init__(self, parent, controller):
      tk.Frame.__init__(self, parent)
      option1 = StringVar()
      
      label1 = ttk.Label(self, text='Enter the GRE Score(out of 340): ', font=Small_Font)
      t1 = ttk.Entry(self)
      label2 = ttk.Label(self, text='Enter the TOEFL Score(out of 120): ', font=Small_Font)
      t2 = ttk.Entry(self)
      label3 = ttk.Label(self, text='Enter the University Rating: ', font=Small_Font)
      r1 = ttk.Radiobutton(self, text='1', value='one', variable=option1)
      r2 = ttk.Radiobutton(self, text='2', value='two', variable=option1) 
      r3 = ttk.Radiobutton(self, text='3', value='three', variable=option1)
      r4 = ttk.Radiobutton(self, text='4', value='four', variable=option1)
      r5 = ttk.Radiobutton(self, text='5', value='five', variable=option1)
      label4 = ttk.Label(self, text='SOP: ', font=Small_Font)
      t4 = ttk.Entry(self)
      label5 = ttk.Label(self, text='LOR: ', font=Small_Font)
      t5 = ttk.Entry(self)
      label6 = ttk.Label(self, text='CGPA: ', font=Small_Font)
      t6 = ttk.Entry(self)
      label7 = ttk.Label(self, text='Research: ', font=Small_Font)
      option2 = IntVar()
      c1 = ttk.Checkbutton(self, text='Yes', variable=option2)
      option3 = IntVar()
      c2 = ttk.Checkbutton(self, text='No', variable=option3)
      label8 = ttk.Label(self, text='Chances of admission are: ', font=Small_Font)
      t7 = ttk.Entry(self)
     
      
      def calc_chances():
          gre_score = int(t1.get())
          toefl_score = int(t2.get())
          sop = int(t4.get())
          lor = int(t5.get())
          cgpa = int(t6.get())
          univ_str=option1.get()
          univ=0
          if univ_str=='one':
              univ=1
          elif univ_str=='two':
              univ=2
          elif univ_str=='three':
              univ=3
          elif univ_str=='four':
              univ=4
          elif univ_str=='five':
              univ=5
          res_str=option2.get()
          res=0
          if res_str==0:
              res=0
          elif res_str==1:
              res=1
          z = [gre_score, toefl_score, univ, sop, lor, cgpa, res]
          z = np.array(z).reshape(1, -1)
          y = (clf.predict(z)*100)
          y = str(y)
          
          t7.insert(0, y)
      
      def enter_record():
          messagebox.askquestion(title='Confirmation', message='Are you sure to proceed?')
          client = MongoClient("mongodb://analytics:analytics-password@analytics-shard-00-00-dccgh.mongodb.net:27017,analytics-shard-00-01-dccgh.mongodb.net:27017,analytics-shard-00-02-dccgh.mongodb.net:27017/test?ssl=true&replicaSet=analytics-shard-0&authSource=admin&retryWrites=true")
          db = client["analytics"]
          coll = db["Graduate_Admission"]
          
          univ_str=option1.get()
          univ=0
          if univ_str=='one':
              univ=1
          elif univ_str=='two':
              univ=2
          elif univ_str=='three':
              univ=3
          elif univ_str=='four':
              univ=4
          elif univ_str=='five':
              univ=5
          
          res_str=option2.get()
          res=0
          if res_str==0:
              res=0
          elif res_str==1:
              res=1  
            
          doc = {"GRE Score":int(t1.get()), 
                 "TOEFL Score":int(t2.get()), 
                 "University Rating":univ, 
                 "SOP":int(t4.get()), 
                 "LOR":int(t5.get()), 
                 "CGPA":int(t6.get()), 
                 "Research":res, 
                 "Chance of Admit":t7.get()
                  }
          
          x = coll.insert_one(doc)
          messagebox.showinfo('You have successfully performed the transaction. The transaction id is', x)
      
      
      back = ttk.Button(self, text="Go back to Selection Page", command=lambda: controller.show_frame(SelectionPage))
      calculate = ttk.Button(self, text='Get Chances!', command=lambda: calc_chances())
      submit = ttk.Button(self, text='Submit', command=lambda: enter_record())
      
      label1.grid(row=0, column=1)
      label2.grid(row=2, column=1)
      label3.grid(row=4, column=1)
      label4.grid(row=6, column=1)
      label5.grid(row=8, column=1)
      label6.grid(row=10, column=1)
      label7.grid(row=12, column=1)
      label8.grid(row=17, column=1)
      t1.grid(row=0, column=2)
      t2.grid(row=2, column=2)
      r1.grid(row=4, column=2)
      r2.grid(row=4, column=4)
      r3.grid(row=4, column=6)
      r4.grid(row=4, column=8)
      r5.grid(row=4, column=10)
      t4.grid(row=6, column=2)
      t5.grid(row=8, column=2)
      t6.grid(row=10, column=2)
      c1.grid(row=12, column=2)
      c2.grid(row=12, column=4)
      t7.grid(row=17, column=2)
      back.grid(row=20)
      calculate.grid(row=20, column=2)
      submit.grid(row=20, column=120)
      
app = main_class()
app.mainloop()              