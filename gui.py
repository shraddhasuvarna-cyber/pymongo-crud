import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

#All Code Logic Is Running Properly - Created GUI Using Python Tkinter FrameWork / Library  
# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["CollegeData"]
collection = db["students"]

#window Ceated 
root = tk.Tk()
root.title("NGD Assignment-1")
root.geometry("600x400")

# Title 
tk.Label(root, text="534- Shraddha Suvarna -- CRUD Operation Using GUI", font=("Arial", 16)).pack(anchor="w", padx=20, pady=10)

# College ID
tk.Label(root, text="College ID:").pack(anchor="w", padx=20)
id_entry = tk.Entry(root, width=40)
id_entry.pack(anchor="w", padx=20)

# Name
tk.Label(root, text="Name:").pack(anchor="w", padx=20)
name_entry = tk.Entry(root, width=40)
name_entry.pack(anchor="w", padx=20)

# Age
tk.Label(root, text="Age:").pack(anchor="w", padx=20)
age_entry = tk.Entry(root, width=40)
age_entry.pack(anchor="w", padx=20)

# Country
tk.Label(root, text="Country:").pack(anchor="w", padx=20)
country_entry = tk.Entry(root, width=40)
country_entry.pack(anchor="w", padx=20)


# Insert Function
def insert():
    id = id_entry.get().strip()
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    country = country_entry.get().strip()

    if not (id and name and age and country):
        messagebox.showwarning("Missing Data", "Please fill all fields.")
        return

    try:
        collection.insert_one({
            "id": id,
            "name": name,
            "age": age,
            "country": country
        })
        messagebox.showinfo("Success", "Data inserted successfully!")
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        country_entry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Failed to insert data.")

# Display Function
def read():
    try:
        documents = collection.find()
        result = ""
        for doc in documents:
            result += f"Id: {doc['id']}\nName: {doc['name']}\nAge: {doc['age']}\nCountry: {doc['country']}\n\n"
        result_label.config(text=result)
    except:
        messagebox.showerror("Error", "Failed to display data.")



result_label = tk.Label(root, text="", justify="left", anchor="w")
result_label.pack(anchor="w", padx=20, pady=0)
result_label.place(x=20, y=300)

# Update Operation :

def update():
        
        name_label = tk.Label(root,text="Name Should Be Same as Previous One to Update Age - Country ").pack(anchor="w",pady=65)
        name_input = tk.Entry(root,width=40)
        name_input.pack(anchor="w",padx=20,pady=0)

        age_label = tk.Label(root,text="Update Your Age : ").pack(anchor="w")
        age_input= tk.Entry(root,width=40)
        age_input.pack(anchor="w",padx=20,pady=10)

        country_label = tk.Label(root,text="Update Your Country : ").pack(anchor="w")
        country_input = tk.Entry(root,width=40)
        country_input.pack(anchor="w",padx=20,pady=10)

        def updateinfo():
            old_name = name_input.get()
            new_age = age_input.get()
            new_country = country_input.get()

            if not (old_name and new_age and new_country):
                messagebox.showwarning(root,text="Empty Can not be Updated")
                return

            result = collection.update_one({"name":old_name},{"$set" : {"age":new_age , "country":new_country}})
            if result.modified_count > 0:
                messagebox.showinfo("Success", "Record updated successfully!")
                name_input.delete(0, tk.END)
                age_input.delete(0, tk.END)
                country_input.delete(0, tk.END)
            else:
                messagebox.showinfo("No Match", "No matching record found.")
        tk.Button(root,text="Confirm Update",command=updateinfo).pack(anchor="w",padx=20,pady=10)

#Delete Operation

def delete():
    
        tk.Label(root, text="College ID:").pack(anchor="w", padx=20,pady=70)
        id_entry = tk.Entry(root, width=40)
        id_entry.pack(anchor="w", padx=20)
                

        def deleteInfo():
            
            old_id = id_entry.get()
            old_name = name_entry.get()
            new_age = age_entry.get()
            new_country = country_entry.get()
            

            result = collection.delete_many({"id":old_id})
            
            if result :
                messagebox.showinfo("Success", "Record Deleted successfully!")
                name_entry.delete(0, tk.END)
                age_entry.delete(0, tk.END)
                country_entry.delete(0, tk.END)
            else:
                messagebox.showinfo("No Match", "No matching record found.")
        tk.Button(root,text="Confirm Delete",command=deleteInfo).pack(anchor="w",padx=20,pady=10)
        
# Buttons in one line, spaced out
tk.Button(root, text="Insert", command=insert).place(x=20, y=250)
tk.Button(root, text="Display Users", command=read).place(x=100, y=250)
tk.Button(root, text="Update", command=update).place(x=220, y=250)
tk.Button(root, text="Delete", command=delete).place(x=320, y=250)


root.mainloop()

