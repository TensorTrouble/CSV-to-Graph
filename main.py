import customtkinter as ctk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt 
import os
from PIL import Image

class grapher:
    def __init__(self, root):
        self.root = root
        self.root.geometry('650x650')
        self.root.title('CSV to Graph')
        self.build_ui()
    
    def build_ui(self):
        self.upload_button()
        self.filename = ctk.CTkLabel(self.root, text="No CSV files selected")
        self.filename.pack(pady=5)
        self.img_lbl = ctk.CTkLabel(self.root, text='Your Graph will generate here!')
        self.img_lbl.pack(pady=5)
        
    def upload_button(self):
        self.upload_btn = ctk.CTkButton(self.root, text="Upload CSV file", command=self.upload_file)
        self.upload_btn.pack(pady=10)

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        if self.file_path:
            # global rows
            self.rows = pd.read_csv(self.file_path)
            self.file_path = self.file_path.split('/')
            self.filename.configure(text=self.file_path[-1])
            self.upload_btn.configure(state='disabled')
            self.combo_menu()
            
        else:
            self.filename.configure(text="Please select a .csv file")

    def combo_menu(self):
        self.col = self.rows.columns.to_list()


        self.lbl_x = ctk.CTkLabel(self.root, text='Select X axis')
        self.combobox_x = ctk.CTkComboBox(self.root, values=self.col)
        self.lbl_x.pack()
        self.combobox_x.pack()
        # self.pickedx = self.combobox_x.get()

        # self.col.remove(self.pickedx)

        self.lbl_y = ctk.CTkLabel(self.root, text='Select Y axis')
        self.combobox_y = ctk.CTkComboBox(self.root, values=self.col)
        self.lbl_y.pack()
        self.combobox_y.pack()
        self.generate_graph_btn()

        # self.combobox_y.configure(value=self.col)
        # print(self.col)
    


    def generate_graph_btn(self):

        self.graph_btn = ctk.CTkButton(self.root, text='Generate Graph', command=self.generate_graph)
        self.graph_btn.pack(pady=10)
    
    def generate_graph(self):

        self.x = self.rows[self.combobox_x.get()]
        self.y = self.rows[self.combobox_y.get()]
        plt.plot(self.x,self.y)
        plt.savefig('graph', dpi=300)
        self.show_imgg()

    def show_imgg(self):
        try:
            plt.clf()
            self.img = Image.open('graph.png')
            self.ctk_img = ctk.CTkImage(light_image=self.img, size =(480, 360))
            self.img_lbl.configure(image=self.ctk_img, text='')
        except:
            print('image not found')


def main():
    root = ctk.CTk()
    app = grapher(root)
    root.mainloop()


if __name__ == "__main__":
    main()