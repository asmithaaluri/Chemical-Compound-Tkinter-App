import tkinter as tk
from tkinter import messagebox, Label
import chemical_compound_web_scraper as ccws

def process_user_input():
    user_input = user_entry.get()

    try:
        cid = ccws.get_cid(user_input)
        compound_name, molecular_formula, molecular_weight, structure_image = ccws.execute(user_input, cid)
        display_compound_info(cid, compound_name, compound_name_label_result, molecular_formula, molecular_formula_label_result, molecular_weight, molecular_weight_label_result, structure_image)
    except ccws.UnableToFindCompoundError:
        #print(f'ERROR: Invalid compound.')
        messagebox.showerror("Error", "You entered an invalid compound.")

def display_compound_info(cid, compound_name, compound_name_label_result, molecular_formula, molecular_formula_label_result, molecular_weight, molecular_weight_label_result, structure_image):
    compound_name_label_result.config(text=f"{compound_name}")
    molecular_formula_label_result.config(text=f"{molecular_formula}")
    molecular_weight_label_result.config(text=f"{molecular_weight}")

    global image_label_result
    image_label_result.config(image=structure_image, bg='#728a80')
    image_label_result.image = structure_image

root = tk.Tk()
root.title("Chemical Compound Info")
root.resizable(False, False)
root.config(bg='#dcf5df')
root.geometry("435x700")

prompt_label = Label(root, 
                     text="Enter a compound name:", 
                     bg='#dcf5df', 
                     fg='#728a80', 
                     font=("Helvetica", 17, 'bold')) 
user_entry = tk.Entry(root, 
                      fg='#fff', 
                      font=("Helvetica", 16, 'bold'),
                      bg='#728a80', 
                      bd=2, 
                      highlightthickness=0, 
                      highlightbackground='#346beb', 
                      highlightcolor='#fff')
search_button = tk.Button(root,
                          text="Search",
                          bg='#728a80',
                          fg='#000',
                          activebackground='#000',
                          activeforeground='#728a80',
                          borderwidth=0,
                          highlightthickness=0,
                          relief='raised',
                          font=("Helvetica", 15, "italic"),
                          padx=5,
                          pady=10,
                          command=process_user_input)
compound_name_label = tk.Label(root, 
                  text="Name:",
                  bg='#dcf5df', 
                  fg='#728a80',
                  font=("Helvetica", 17, 'bold'))
compound_name_label_result = tk.Label(root,
                                      bg='#98b5a9',
                                      fg='#fff',
                                      width=40,
                                      height=2,
                                      highlightbackground='#728a80',
                                      highlightthickness=3,
                                      font=("Helvetica", 17, "italic"))
molecular_formula_label = tk.Label(root, 
                  text="Molecular Formula:",
                  bg='#dcf5df', 
                  fg='#728a80',
                  font=("Helvetica", 17, 'bold'))
molecular_formula_label_result = tk.Label(root,
                                      bg='#98b5a9',
                                      fg='#fff',
                                      width=40,
                                      height=2,
                                      highlightbackground='#728a80',
                                      highlightthickness=3,
                                      font=("Helvetica", 17, "italic"))
molecular_weight_label = tk.Label(root, 
                  text="Molecular Weight:",
                  bg='#dcf5df', 
                  fg='#728a80',
                  font=("Helvetica", 17, 'bold'))
molecular_weight_label_result = tk.Label(root,
                                      bg='#98b5a9',
                                      fg='#fff',
                                      width=40,
                                      height=2,
                                      highlightbackground='#728a80',
                                      highlightthickness=3,
                                      font=("Helvetica", 17, "italic"))
image_label = tk.Label(root, 
                  text="Image:",
                  bg='#dcf5df', 
                  fg='#728a80',
                  font=("Helvetica", 17, 'bold'))
image_label_result_template = tk.Label(root,
                            bg='#98b5a9',
                            fg='#fff',
                            width=45,
                            height=17,
                            highlightbackground='#728a80',
                            highlightthickness=3)
image_label_result = tk.Label(root, borderwidth=2, bg='#98b5a9')


prompt_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
user_entry.grid(row=0, column=1, padx=0, pady=0)
search_button.grid(row=1, column=0, columnspan=2, padx=15, pady=10, sticky='nsew')
compound_name_label.grid(row=2, column=0, columnspan=2, padx=10, pady=2, sticky='nesw')
compound_name_label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=2)
molecular_formula_label.grid(row=4, column=0, columnspan=2, padx=10, pady=2, sticky='nesw')
molecular_formula_label_result.grid(row=5, column=0, columnspan=2, padx=10, pady=2)
molecular_weight_label.grid(row=6, column=0, columnspan=2, padx=10, pady=2, sticky='nesw')
molecular_weight_label_result.grid(row=7, column=0, columnspan=2, padx=10, pady=2)
image_label.grid(row=8, column=0, columnspan=2, padx=10, pady=2, sticky='nesw')
image_label_result_template.grid(row=9, column=0, columnspan=2, padx=10, pady=2)
image_label_result.grid(row=9, column=0, columnspan=2, padx=10, pady=2)

root.mainloop()