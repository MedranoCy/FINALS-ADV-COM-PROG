import tkinter as tk
from tkinter import messagebox, Scrollbar, Text

#================================================================== LOGIN AND REGISTER ===========================================================================
user_credentials = {}

def validate_login(username, password, login_window):
    if not username or not password:  # Check if either username or password is empty
        messagebox.showerror("Login Failed", "Username and password cannot be empty.")
        return

    #Login check
    if username in user_credentials and user_credentials[username] == password:
        login_window.destroy()  # Close the login window
        open_main_app_window()  # Open the main app window if login is successful
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_register_window():
    register_window = tk.Tk()
    register_window.title("Register")
    register_window.geometry("400x400")
    register_window.configure(bg="beige")

    label_register = tk.Label(register_window, text="Create a New Account", font=("Arial", 18), bg="beige", fg="black")
    label_register.pack(pady=20)

    label_username = tk.Label(register_window, text="Username:", font=("Arial", 12), bg="beige", fg="black")
    label_username.pack(pady=5)
    entry_username = tk.Entry(register_window, font=("Arial", 12), width=25)
    entry_username.pack(pady=5)

    label_password = tk.Label(register_window, text="Password:", font=("Arial", 12), bg="beige", fg="black")
    label_password.pack(pady=5)
    entry_password = tk.Entry(register_window, show="*", font=("Arial", 12), width=25)
    entry_password.pack(pady=5)

    label_confirm_password = tk.Label(register_window, text="Confirm Password:", font=("Arial", 12), bg="beige", fg="black")
    label_confirm_password.pack(pady=5)
    entry_confirm_password = tk.Entry(register_window, show="*", font=("Arial", 12), width=25)
    entry_confirm_password.pack(pady=5)

    def register_user():
        username = entry_username.get()
        password = entry_password.get()
        confirm_password = entry_confirm_password.get()

        # Check if any field is empty
        if not username or not password or not confirm_password:
            messagebox.showerror("Registration Failed", "All fields must be filled.")
            return
        
        # Check if passwords match
        if password != confirm_password:
            messagebox.showerror("Registration Failed", "Passwords do not match.")
            return

        # Check if username already exists
        if username in user_credentials:
            messagebox.showerror("Registration Failed", "Username already exists!")
        else:
            user_credentials[username] = password  # Add new user to credentials
            messagebox.showinfo("Registration Successful", "You have successfully registered!")
            register_window.destroy()  # Close the registration window

    register_button = tk.Button(register_window, text="Register", command=register_user, font=("Arial", 12), bg="light blue", fg="black", width=20)
    register_button.pack(pady=20)

    
    register_window.mainloop()

def open_main_app_window():
    main_window = tk.Tk()
    main_window.title("Batangas Safety Call App")
    main_window.geometry("600x600")  
    main_window.configure(bg="beige")  

    frame_main = tk.Frame(main_window, bg="beige")
    frame_main.pack(pady=20)

    label_welcome = tk.Label(frame_main, text="Welcome to Batangas Safety Call App!", font=("Arial", 16, "bold"), bg="beige", fg="black")
    label_welcome.pack(pady=20)

    button_frame = tk.Frame(main_window, bg="beige")
    button_frame.pack(pady=20)
 
    button_style = {
        'font': ("Arial", 12),
        'bg': "orange",  
        'fg': "white",  
        'width': 30,
        'relief': "flat",
        'bd': 2,
        'highlightbackground': "orange",
        'highlightcolor': "orange"
    }

    hotline_button = tk.Button(button_frame, text="Emergency Hotlines", command=open_hotlines, **button_style)
    hotline_button.grid(row=0, column=0, pady=10)

    first_aid_button = tk.Button(button_frame, text="First Aid Resources", command=open_first_aid, **button_style)
    first_aid_button.grid(row=1, column=0, pady=10)

    mental_health_button = tk.Button(button_frame, text="Mental Health Support", command=open_mental_health, **button_style)
    mental_health_button.grid(row=2, column=0, pady=10)

    educational_button = tk.Button(button_frame, text="Educational Resources & Guidance", command=open_educational_resources, **button_style)
    educational_button.grid(row=3, column=0, pady=10)

    anonymous_report_button = tk.Button(button_frame, text="Anonymous Reporting", command=open_anonymous_reporting, **button_style)
    anonymous_report_button.grid(row=5, column=0, pady=10)

    update_contacts_button = tk.Button(button_frame, text="Update Emergency Contacts", command=open_update_contacts, **button_style)
    update_contacts_button.grid(row=6, column=0, pady=10)

    
    def logout():
        main_window.destroy()  

    logout_button = tk.Button(main_window, text="Logout", font=("Arial", 10), bg="red", fg="white", width=10, relief="flat", command=logout)
    logout_button.place(relx=0.9, rely=0.95, anchor="center")  # Place it at the bottom-right corner
    

    main_window.mainloop()

def open_login_window():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x400")
    login_window.configure(bg="beige")

    label_login = tk.Label(login_window, text="Please Login to Continue", font=("Arial", 18), bg="beige", fg="black")
    label_login.pack(pady=20)

    label_username = tk.Label(login_window, text="Username:", font=("Arial", 12), bg="beige", fg="black")
    label_username.pack(pady=5)
    entry_username = tk.Entry(login_window, font=("Arial", 12), width=25)
    entry_username.pack(pady=5)

    label_password = tk.Label(login_window, text="Password:", font=("Arial", 12), bg="beige", fg="black")
    label_password.pack(pady=5)
    entry_password = tk.Entry(login_window, show="*", font=("Arial", 12), width=25)
    entry_password.pack(pady=5)

    login_button = tk.Button(login_window, text="Login", command=lambda: validate_login(entry_username.get(), entry_password.get(), login_window),
                             font=("Arial", 12), bg="light green", fg="black", width=20)
    login_button.pack(pady=20)

    register_button = tk.Button(login_window, text="Register", command=open_register_window, font=("Arial", 12), bg="light blue", fg="black", width=20)
    register_button.pack(pady=10)

    login_window.mainloop()
#================================================================== EMERGENCY HOTLINES ==============================================================================

def open_hotlines():
    hotline_window = tk.Toplevel()  
    hotline_window.title("Emergency Hotlines")
    hotline_window.geometry("800x600")  
    hotline_window.configure(bg="beige")  

   
    label_hotlines = tk.Label(
        hotline_window,
        text="Emergency Hotlines by District",
        font=("Arial", 16, "bold"),
        bg="beige",  
        fg="black"   
    )
    label_hotlines.grid(row=0, column=0, padx=20, pady=10, sticky="w")

    category_frame = tk.Frame(hotline_window, bg="beige")  # Beige background
    category_frame.grid(row=1, column=0, padx=30, pady=10, sticky="w")

hotlines_by_district = {
    "DISTRICT 1": {
    "Balayan, Batangas": ["BFP: 0915-602-2053","MSWDO: 0953-934-2485","MSWDO: 0962-518-3555","MDRRMO: 0906-636-4019","PNP: 0927-434-8008","Red Cross: 0917-133-1427"],
    "Calatagan, Batangas": ["BFP: 0926-408-4359","MDRRMO: 0909-766-5818","MDRRMO: (043)-419-7510","PNP: 0917-337-5190","PNP: 0998-598-5687","RHU: 0930-816-8484"],
    "Nasugbu, Batangas": ["BFP: 0995-448-5073","BFP: (043)-416-0125","MDRRMO: 043-233-1842","MDRRMO: 0917-508-9911","PNP: 043-276-9643","PNP: 0927-500-1199","PNP: 0998-598-5697","REDCROSS: 0917-133-1427","REDCROSS: 43-740-2356"],
    "Lian, Batangas": ["BFP: 0956-182-4272","BFP: (043)-727-6745","MDRRMO: 0965-210-5769","MDRRMO: (043)-233-1421","PNP: 0917-551-2292","PNP: 0998-598-5692"],
    "Taal, Batangas": ["BFP: 411-1550","MDRRMO: 0908-930-4167","PNP: 2142-167"],
    "Tuy, Batangas": ["BFP: 0926-773-7914","MDRRMO: 0906-623-6941","PNP: 0915-899-1931","RHU: 0926-911-1949"],
    "Calaca City, Batangas": ["BFP: (043)-424-1410","BFP: (043)-223-5514","CDRRMO: 0998-987-1251","CDRRMO: (043)-424-1379","PNP: (043)-223-5048","PNP: (043)-424-1493","RHU: 043-424-0345","RHU: 043-223-7220"],
    "Lemery, Batangas": ["BFP: 0985-979-6727","MDRRMO: 0915-676-1424","MDRRMO: 0939-146-3726","MDRRMO: 726-3223","RESCUE TEAM: 0915-676-1424","RESCUE TEAM: 0939-146-3726","PNP: 0908-352-7183","PNP: 0927-707-1191","MAYOR'S OFFICE: (043)-740-0157","MAYOR'S OFFICE: (043)-740-2618"]
    },
    "DISTRICT 2": {
    "Lobo, Batangas": ["BFP: 0915-602-2046","MDRRMO: 0917-100-4607","MDRRMO: 0955-880-5252","Mayor's Office: 0995-634-1483","Mayor's Office: 0949-913-9323","PNP: 0916-719-4906","RHU: 0965-051-7113"],
    "Mabini, Batangas": ["BFP: 0926-621-1953","BFP: (043)-425-3890","MDRRMO: 0915-201-6244","MDRRMO: (043)-774-4659","PNP: 0916-270-0837","RHU: (043)-349-2341"],
    "Bauan, Batangas": ["BFP: 0918-499-3938","BFP: 727-1140","MDRRMO: 0917-837-7608","MDRRMO: 727-2632","PNP: 0916-462-0308","RHU: 0906-438-3919","RHU: 980-9147"],
    "San Pascual, Batangas": ["BFP: 0947-893-7133","BFP: (043)-726-0254","MDRRMO: (043)-984-3629","MDRRMO: 0928-521-5113","MDRRMO: 0939-910-7681","Mayor's Office: (043)-727-3094","PNP: 0998-598-5704","PNP: 0915-534-8889","PNP: (043)-456-9032","Rescue Team: 0928-521-5113","Rescue Team: 0939-910-7681"],
    "Tingloy, Batangas": ["BFP: 0991-369-0472","LGU: 0947-246-6829","LGU: 0928-520-3836"],
    "San Luis, Batangas": ["BFP: 0915-602-0640","MDRRMO: 0908-210-9313","MSWDO: 0908-891-1407","PNP: 0926-598-5702","PNP: 0926-641-6290","RHU: 0985-039-8492"]
    },
    "DISTRICT 3": {
    "Agoncillo, Batangas": ["BFP: 0915-601-6791","MDRRMO: 0975-732-5274","MDRRMO: (043)-773-6880 loc 116","MDRRMO: (043)-773-6880 loc 121","PNP: 0915-261-9656","Mayor's Office: (043)-773-6880 loc 116"],
    "Balete, Batangas": ["BFP: 0966-746-2560","MDRRMO: 0920-592-2480","MDRRMO: 740-9638","PNP: 0915-467-2095","PNP: 781-2326","RHU: 706-9757"],
    "Cuenca, Batangas": ["BFP: 0966-693-4161","BFP: (043)-740-6367","Engineering Office: (043)-349-5010","MDRRMO: 0917-834-2607","MDRRMO: (043)-774-3376","Mayor's Office: (043)-756-4361","PNP: 0998-598-5688","PNP: 0915-954-7571","PNP: (043)-342-1887"],
    "Laurel, Batangas": ["BFP: 0915-603-4225","MDRRMO: 0950-443-4219","PNP: 0998-598-5690","PNP: 741-4031 loc 110","PNP: 0916-652-5208","RHU: 0916-652-5208"],
    "Malvar, Batangas": ["BFP: 0949-833-9974","BFP: 0927-698-7802","BFP: (043)-784-8297","MDRRMO: 0906-627-4066","MDRRMO: 0917-179-7408","MDRRMO: (043)-233-1934","MSWDO: (043)-405-3659","PNP: 0998-598-5695","PNP: 0927-698-7783"],
    "Mataas na Kahoy, Batangas": ["BFP: 0931-181-8435","Mayor's Office: 461-0107","MDRRMO: 0977-682-5025","MDRRMO: 784-1016","PNP: 0915-923-1698","RHU: 0935-378-0459","RHU: 8461-1992"],
    "San Nicolas, Batangas": ["BFP: 0943-077-2691","Coast Guard: 0917-809-4335","MDRRMO: 0982-867-4563","PNP: 0927-683-6457"],
    "Sta. Teresita, Batangas": ["BFP: 0960-810-2105","MDRRMO: 0917-520-1408","PNP: 0906-466-9222","PNP: 0998-598-5706","RHU: (043)-772-0738"],
    "Sto. Tomas City, Batangas": ["BFP: 0915-602-1987","BFP: (043)-778-3243","CDRRMO: 0917-109-1843","CDRRMO: 0917-814-3657","CDRRMO: (043)-784-8432","Emergency Operation Center: 0917-109-1843","Emergency Operation Center: 0917-814-3657","Emergency Operation Center: (043)-784-8432","PNP: 0998-598-5706","PNP: (043)-778-1610"],
    "Talisay, Batangas": ["BFP: 0967-154-2145","MDRRMO: 0919-002-6621","PNP: 0917-353-4074"],
    "Tanauan City, Batangas": ["BFP: 0922-344-8887","BFP: (043)-702-9678","CDRRMO: 0962-347-5073","PNP: 1939-322-7848","PNP: 0977-685-6947","Red Cross: 0930-358-3058"]
    },
     "DISTRICT 4": {
    "Ibaan, Batangas": ["BFP: 0930-468-9030","Engineering Office: 0917-855-1237","MDRRMO: 0917-855-8040","MSWDO: 0919-534-4348","PNP: 0927-731-3259"],
    "Padre Garcia, Batangas": ["LGU: (043)-430-0319","MDRRMO: 0977-801-1557","MDRRMO: 0919-611-6180","MDRRMO: (043)-515-7424","PNP: 0928-663-7762","PNP: 0905-292-4038","PNP: (043)-515-9209"],
    "Rosario, Batangas": ["BFP: (043)-312-112","MDRRMO: (043)-312-112","MDRRMO: 0915-624-435","PNP: 0915-254-2577","PNP: 0923-728-1366","PNP: 0917-133-9605"],
    "San Jose, Batangas": ["BFP: 0929-293-0106","MDRRMO: 0916-512-1163","PNP: 0956-476-3867","RHU: 0917-173-5818","RHU: 0985-990-0178"],
    "San Juan, Batangas": ["BFP: 0915-602-2026","BFP: 0939-713-9474","MDRRMO: 0909-623-7425","MDRRMO: 0998-590-5102","MDRRMO: 0945-841-2692","PNP: 0998-598-5701","PNP: 0915-385-0205"],
    "Taysan, Batangas": ["BFP: 0975-544-0473","MDRRMO: 0917-319-6660","PNP: 0906-242-1620"]
   },
   "DISTRICT 5": {
    "Batangas City, Batangas": ["BFP: 0915-602-1984","BFP: (043)-425-7163","BFP: 301-7996","CDRRMO: 0909-352-0485","CDRRMO: 702-3902","CSWDO: 723-2357","CSWDO: 301-7996","PNP: 0916-429-1515",
      "PNP: 0998-967-3414","PNP: (043)-723-2476","PNP: (043)-732-030","Red Cross: 723-3027"]
   },
   "DISTRICT 6": {
    "Lipa City, Batangas": ["BFP: 0927-575-8065","BFP: (043)-757-4618","CDRRMO: 0954-261-4415","CDRRMO: 0961-358-0544","CDRRMO: (043)-756-0127","CDRRMO: (043)-757-5164","Mayor's Office: 774-5169",
      "PNP: 0977-744-9692","PNP: (043)-702-3832","Red Cross: 0998-957-0443","Red Cross: (043)-740-0768","Rescue Team: 0954-261-4415","Rescue Team: 0961-358-0544","Rescue Team: (043)-756-0127","Red Cross: (043)-740-0768"]
  }
}

def open_ringing_window(contact_name, phone_number):
    """Simulates the ringing window when a call button is clicked."""
    ringing_window = tk.Toplevel()
    ringing_window.title("Calling...")
    ringing_window.geometry("300x150")
    ringing_window.configure(bg="beige")

    label = tk.Label(
        ringing_window,
        text=f"Dialing {contact_name}...\n{phone_number}",
        font=("Arial", 14, "bold"),
        bg="beige",
        fg="black",
    )
    label.pack(pady=30)

    def simulate_dialing():
        label.config(text=f"Connecting to {contact_name}...\n{phone_number}")
        ringing_window.after(3000, lambda: label.config(text=f"Connected to {contact_name}!"))

    ringing_window.after(2000, simulate_dialing)

    def end_call():
        ringing_window.destroy()

    button_ok = tk.Button(
        ringing_window,
        text="OK",
        font=("Arial", 12, "bold"),
        bg="orange",
        fg="white",
        relief="flat",
        width=10,
        height=2,
        command=end_call,
    )
    button_ok.pack(pady=10)

    ringing_window.after(10000, end_call)

def open_district_window(district_name):
    """Opens a window for the selected district showing its emergency contacts."""
    district_window = tk.Toplevel()
    district_window.title(f"{district_name} - Emergency Contacts")
    district_window.geometry("800x900")
    district_window.configure(bg="beige")

    canvas = tk.Canvas(district_window, bg="beige")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = Scrollbar(district_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = tk.Frame(canvas, bg="beige")
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    title_label = tk.Label(
        scrollable_frame,
        text=f"Emergency Contacts for {district_name}",
        font=("Arial", 16, "bold"),
        bg="beige",
        fg="black",
    )
    title_label.pack(pady=30)

    for place, numbers in hotlines_by_district[district_name].items():
        place_label = tk.Label(
            scrollable_frame,
            text=place,
            font=("Arial", 14, "bold"),
            bg="beige",
            fg="black",
        )
        place_label.pack(anchor="w", padx=20, pady=5)

        for contact in numbers:
            contact_name, phone_number = contact.split(":")
            phone_number = phone_number.strip()

            button = tk.Button(
                scrollable_frame,
                text=f"Call {contact_name.strip()} - {phone_number}",
                font=("Arial", 12),
                bg="orange",
                fg="white",
                relief="flat",
                command=lambda name=contact_name, phone=phone_number: open_ringing_window(name, phone),
            )
            button.pack(anchor="w", padx=40, pady=2)

    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def open_hotlines():
    """Main hotline selection window."""
    hotline_window = tk.Toplevel()
    hotline_window.title("Emergency Hotlines")
    hotline_window.geometry("400x500")
    hotline_window.configure(bg="beige")

    canvas = tk.Canvas(hotline_window, bg="beige")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = Scrollbar(hotline_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = tk.Frame(canvas, bg="beige")
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    label_hotlines = tk.Label(
        scrollable_frame,
        text="Select a District",
        font=("Arial", 16, "bold"),
        bg="beige",
        fg="black",
    )
    label_hotlines.pack(pady=10)

    for district_name in hotlines_by_district.keys():
        button = tk.Button(
            scrollable_frame,
            text=f" {district_name}",
            font=("Arial", 14),
            bg="orange",
            fg="white",
            width=30,
            relief="flat",
            command=lambda d=district_name: open_district_window(d),
        )
        button.pack(pady=10)

    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

#====================================================================== FIRST AID ==============================================================================
def open_first_aid():
    first_aid_window = tk.Toplevel()
    first_aid_window.title("First Aid Resources")
    first_aid_window.geometry("800x500")  
    first_aid_window.configure(bg="beige")  

    label_first_aid = tk.Label(
        first_aid_window, 
        text="First Aid Instructions", 
        font=("Arial", 16, "bold"), 
        bg="beige", 
        fg="black"  
    )
    label_first_aid.grid(row=0, column=0, padx=20, pady=10, sticky="w")

   
    instructions_frame = tk.Frame(first_aid_window, bg="beige")
    instructions_frame.grid(row=1, column=0, padx=20, pady=10)

    first_aid_steps = [
        "1. Check for responsiveness. If unresponsive, call emergency services immediately.",
        "2. Perform CPR if no pulse or breathing. Push hard and fast in the center of the chest.",
        "3. Apply pressure to stop bleeding. Use a clean cloth or bandage to apply pressure.",
        "4. If the person is choking, perform the Heimlich maneuver to clear the airway.",
        "5. In case of burns, cool the burn under running water and cover with a sterile dressing.",
        "6. If the person is unconscious but breathing, place them in the recovery position and monitor their condition."
    ]
    
    for step in first_aid_steps:
        step_label = tk.Label(
            instructions_frame,
            text=step,
            font=("Arial", 12),
            bg="beige",
            fg="black",
            anchor="w"  
        )
        step_label.pack(anchor="w", padx=10, pady=5)

    
    close_button = tk.Button(
        first_aid_window, 
        text="Close", 
        font=("Arial", 12), 
        bg="orange",  
        fg="white",   
        command=first_aid_window.destroy, 
        relief="flat", 
        bd=2
    )
    close_button.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

#===================================================================== MENTAL HEALTH ===========================================================================

def quick_dial(contact_name, phone_number):
    """Simulates a quick dial action with a pop-up window."""
    try:
        # Simulate the call
        calling_window = tk.Toplevel()
        calling_window.title("Calling...")
        calling_window.geometry("800x200")
        calling_window.configure(bg="beige")  

        # Label indicating the phone number being dialed
        calling_label = tk.Label(
            calling_window,
            text=f"Dialing {contact_name}... {phone_number}",
            font=("Arial", 14, "bold"),
            bg="beige",
            fg="black"
        )
        calling_label.pack(pady=30)

        # Function to simulate the dialing process
        def simulate_dialing():
            # Change the label text to "Connecting..."
            calling_label.config(text=f"Connecting to {contact_name}... {phone_number}")
            # Simulate the successful connection after 3 seconds
            calling_window.after(3000, lambda: calling_label.config(text=f"Connected to {contact_name}!"))

        # Start the dialing simulation after 1 second
        calling_window.after(1000, simulate_dialing)

        # Function to end the call
        def end_call():
            calling_window.destroy()

        # Orange "OK" button to end the call
        ok_button = tk.Button(
            calling_window,
            text="OK",
            font=("Arial", 12, "bold"),
            bg="orange",
            fg="white",
            relief="flat",
            command=end_call
        )
        ok_button.pack(pady=10)

        # Automatically close the window after 10 seconds
        calling_window.after(10000, end_call)  # Can be adjusted

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def display_contacts(contacts, parent_window):
    """Display the contacts in a new window with dial options."""
    contacts_window = tk.Toplevel(parent_window)
    contacts_window.title("Mental Health Support Contacts")
    contacts_window.geometry("600x600")
    contacts_window.configure(bg="beige")

    frame = tk.Frame(contacts_window, bg="beige")
    frame.pack(expand=True)

    row = 0
    for contact in contacts:
        tk.Label(
            frame,
            text=f"{contact['title']}",
            bg="beige",
            font=("Arial", 12, "bold"),
            anchor="center"
        ).grid(row=row, column=0, sticky="ew", padx=20, pady=5)
        row += 1

        tk.Button(
            frame,
            text=f"Call: {contact['number']}",
            font=("Arial", 10),
            bg="orange",
            fg="white",
            command=lambda name=contact["title"], num=contact["number"]: quick_dial(name, num)
        ).grid(row=row, column=0, sticky="ew", padx=20, pady=5)
        row += 1

    for i in range(row):
        frame.grid_rowconfigure(i, weight=1)
    
    frame.grid_columnconfigure(0, weight=1)

def open_mental_health():
    mental_health_window = tk.Tk()
    mental_health_window.title("Mental Health Support")
    mental_health_window.geometry("800x900")
    mental_health_window.resizable(False, False)
    mental_health_window.configure(bg="beige")

    canvas = tk.Canvas(mental_health_window, bg="beige")
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(mental_health_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    content_frame = tk.Frame(canvas, bg="beige", width=750)
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    info_label = tk.Label(
        content_frame,
        text="Mental Health: A Key to a Balanced and Fulfilling Life",
        bg="beige",  
        font=("Arial", 16, "bold"),
        anchor="w",
        justify="left",
        wraplength=750,
        padx=10
    )
    info_label.pack(pady=10)

    # Subsection: Why Mental Health Matters
    why_label = tk.Label(
        content_frame,
        text="Why Mental Health Matters:",
        bg="beige",  
        font=("Arial", 14, "bold"),
        anchor="w",
        justify="left",
        wraplength=750,
        padx=10
    )
    why_label.pack(pady=5)

    why_info = """
    - Good mental health fosters resilience, enhances relationships, and improves overall quality of life.
    - When mental health challenges go unaddressed, they can lead to:
    - Emotional distress and feelings of hopelessness.
    - Physical health issues, including fatigue, headaches, or weakened immunity.
    - Impaired daily functioning at work, school, or in social settings.
    - Potential development of serious mental health conditions.
    """
    why_info_label = tk.Label(
        content_frame,
        text=why_info,
        bg="beige",  
        font=("Arial", 12),
        anchor="w",
        justify="left",
        wraplength=750,
        padx=10
    )
    why_info_label.pack(pady=5)

    # Subsection: Resources for Mental Health Support
    resources_label = tk.Label(
        content_frame,
        text="Resources for Mental Health Support:",
        bg="beige",  
        font=("Arial", 14, "bold"),
        anchor="w",
        justify="left",
        wraplength=750,
        padx=10
    )
    resources_label.pack(pady=5)

    resources_info = """
    1. Professional Help:
      - Therapists and Counselors: Trained professionals who offer therapy tailored to individual needs.
      - Psychiatrists: Medical doctors who specialize in mental health and can prescribe medication when needed.
      - Community Centers: Local organizations often provide free or affordable mental health support.

    2. Online Mental Health Platforms:
      - MentalHealthPH: Offers a directory of mental health services in the Philippines and online counseling options.
      - Silakbo PH: Connects individuals to support groups and shares mental health advocacy stories.

    3. Self-Care Practices:
      - Mindfulness: Engage in activities like meditation, deep breathing, or yoga to manage stress.
      - Physical Activity: Exercise boosts mood and overall health through endorphin release.
      - Healthy Relationships: Spend time with loved ones to strengthen emotional connections.
      - Structured Routines: Maintain regular sleep patterns, eat nutritious meals, and minimize screen time.
    """
    resources_info_label = tk.Label(
        content_frame,
        text=resources_info,
        bg="beige",  
        font=("Arial", 12),
        anchor="w",
        justify="left",
        wraplength=750,
        padx=10
    )
    resources_info_label.pack(pady=5)

    # Button to view contacts
    def view_contacts():
        contacts = [
            {"title": "Batangas Medical Center - Psychiatry Department", "number": "0437408307"},
            {"title": "PMHA Lipa-Batangas Chapter", "number": "09175652036"},
            {"title": "National Center for Mental Health (NCMH) Crisis Hotline", "number": "1553"},
            {"title": "Hopeline PH", "number": "09175584673"}
        ]
        
        display_contacts(contacts, mental_health_window)

    view_contacts_button = tk.Button(
        content_frame,
        text="View Contacts",
        font=("Arial", 14, "bold"),
        bg="orange",
        fg="white",
        relief="flat",
        command=view_contacts
    )
    view_contacts_button.pack(pady=30)

   
    content_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    mental_health_window.mainloop()

#==================================================================== EDUCATIONAL RESOURCES ===================================================================
def open_educational_resources():
    educational_window = tk.Toplevel()
    educational_window.title("Educational Resources & Guidance")
    educational_window.geometry("700x600")  
    educational_window.configure(bg="beige")

    canvas = tk.Canvas(educational_window)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(educational_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    frame = tk.Frame(canvas, bg="beige")
    canvas.create_window((0, 0), window=frame, anchor="nw")


    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    label_educational = tk.Label(frame, text="Educational Resources & Guidance", font=("Arial", 18, "bold"), bg="beige")
    label_educational.grid(row=0, column=0, padx=20, pady=20, sticky="w")

    section_title_style = {"font": ("Arial", 14, "bold"), "bg": "beige", "anchor": "w"}

    frame_first_aid = tk.Frame(frame, bg="beige")
    frame_first_aid.grid(row=1, column=0, padx=20, pady=10, sticky="w", columnspan=2)

    label_first_aid = tk.Label(frame_first_aid, text="1. First Aid Resources", **section_title_style)
    label_first_aid.grid(row=0, column=0, pady=10, sticky="w")

    first_aid_content = """
    Basic First Aid Steps:
    - Check for responsiveness: Gently tap and shout, "Are you okay?" If there's no response, proceed with emergency measures.
    - Call for help: Dial emergency services (e.g., 911) immediately.

    Airway, Breathing, Circulation (ABC):
    - A: Check the airway to ensure it’s clear.
    - B: Look, listen, and feel for breathing. If absent, begin CPR.
    - C: If there’s no pulse, begin chest compressions.

    Control bleeding: Use clean cloths or gauze to apply pressure to any bleeding wounds.
    Splinting fractures: If you suspect a broken bone, immobilize it to avoid further injury.

    Common First Aid Procedures:
    - CPR (Cardiopulmonary Resuscitation): For adults, perform 30 chest compressions followed by 2 rescue breaths.
      If you’re not trained in mouth-to-mouth, perform chest compressions only.
    - Choking: Use the Heimlich maneuver for adults. For infants, turn them face down and give five back blows, followed by five chest thrusts.
    - Burns:
    - First-degree: Cool with running water, cover with a sterile bandage.
    - Second-degree: Do not pop blisters; cover loosely and seek medical care.
    - Third-degree: Call emergency services immediately, and do not remove burned clothing.
    """
    label_first_aid_content = tk.Label(frame_first_aid, text=first_aid_content, justify="left", font=("Arial", 10), bg="beige")
    label_first_aid_content.grid(row=1, column=0, pady=5, sticky="w")


    frame_preparedness = tk.Frame(frame, bg="beige")
    frame_preparedness.grid(row=2, column=0, padx=20, pady=10, sticky="w", columnspan=2)

    label_preparedness = tk.Label(frame_preparedness, text="2. Emergency Preparedness Resources", **section_title_style)
    label_preparedness.grid(row=0, column=0, pady=10, sticky="w")

    preparedness_content = """
    Creating an Emergency Plan:
    - Know your emergency exits: In case of fire, natural disaster, or other emergencies.
    - Create a family emergency plan: Establish a meeting point and ensure everyone knows how to contact one another.
    - Gather an emergency kit: Stock up on essential items like water, non-perishable food, a first aid kit, flashlight, batteries, medications, and a multi-tool.

    Types of Emergencies to Prepare For:
    - Natural disasters: Earthquakes, floods, hurricanes, tornadoes.
    - Medical emergencies: Heart attacks, strokes, allergic reactions, asthma attacks.
    - Accidents: Car crashes, falls, injuries.

    Important Emergency Supplies:
    - First aid kit (bandages, antiseptic wipes, gauze, gloves, pain relievers).
    - Flashlight, extra batteries, and a radio (preferably battery-operated or hand-crank).
    - A portable phone charger.
    - A list of important contacts and medical information for each family member.
    """
    label_preparedness_content = tk.Label(frame_preparedness, text=preparedness_content, justify="left", font=("Arial", 11), bg="beige")
    label_preparedness_content.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    frame_trauma_care = tk.Frame(frame, bg="beige")
    frame_trauma_care.grid(row=3, column=0, padx=20, pady=10, sticky="w", columnspan=2)

    label_trauma_care = tk.Label(frame_trauma_care, text="3. Trauma Care Resources", **section_title_style)
    label_trauma_care.grid(row=0, column=0, pady=10, sticky="w")

    trauma_care_content = """
    Dealing with Major Trauma:
    - Control severe bleeding: Apply direct pressure on large wounds. If the bleeding continues, elevate the legs (if no spinal injury is suspected) and apply more pressure.
    - Monitor vitals: Check for breathing, pulse, and responsiveness. If the person is not breathing, initiate CPR.
    - Immobilization: If there are signs of a serious fracture, immobilize the injured part until professional help arrives. Avoid moving the person unless there is an immediate risk (e.g., fire, explosion).
    - Shock management: Lay the person flat, elevate their feet, and cover them with a blanket to prevent hypothermia.
    - Spinal injury: Do not move the person unless absolutely necessary, as movement can cause further injury.

    Triage in Trauma Situations:
    In mass casualty events, prioritize care by the severity of injuries. The basic categories are:
    - Red (Immediate): Life-threatening but survivable with immediate intervention.
    - Yellow (Delayed): Serious injuries requiring care, but not immediately life-threatening.
    - Green (Minor): Non-life-threatening injuries; can wait for treatment.
    - Black (Deceased/Expectant): No signs of life or injuries incompatible with life.
    """
    label_trauma_care_content = tk.Label(frame_trauma_care, text=trauma_care_content, justify="left", font=("Arial", 11), bg="beige")
    label_trauma_care_content.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    frame_faq = tk.Frame(frame, bg="beige")
    frame_faq.grid(row=4, column=0, padx=20, pady=10, sticky="w", columnspan=2)

    label_faq = tk.Label(frame_faq, text="4. Frequently Asked Questions (FAQs) on Emergency Situations", **section_title_style)
    label_faq.grid(row=0, column=0, pady=10, sticky="w")


    faq_content = """
    - What should I do if someone is unconscious and not breathing?
      Start CPR immediately, beginning with chest compressions. If you're trained, perform mouth-to-mouth. Otherwise, focus on chest compressions until help arrives.

    - How do I recognize a heart attack?
      Common signs include chest pain, shortness of breath, lightheadedness, nausea, and pain radiating to the arm, jaw, or back.

    - When should I perform the Heimlich maneuver?
      If the person is choking and unable to breathe or speak, perform the Heimlich maneuver to clear the obstruction from the airway.

    - What is the best way to treat a burn?
      For minor burns, run cool water over the area for 10–20 minutes. For more serious burns, avoid using ice and cover the burn with a clean, dry cloth until medical help arrives.
    """
    
    label_faq_content = tk.Label(frame_faq, text=faq_content, justify="left", font=("Arial", 11), bg="beige")
    label_faq_content.grid(row=1, column=0, padx=10, pady=5, sticky="w")

def create_label(parent, text, font=("Arial", 12), bg="beige", fg="black", pady=10):
    label = tk.Label(parent, text=text, font=font, bg=bg, fg=fg)
    label.pack(pady=pady)
    return label


#==================================================================== ANONYMOUS REPORTING ===============================================================================
def submit_report(report_text, anonymous_window):
    if report_text.strip():  # Check if there's any text in the report
        # Simulating the sending of the anonymous report
        print(f"Anonymous report sent: {report_text}")
        messagebox.showinfo("Report Submitted", "Your anonymous report has been submitted successfully.")
        anonymous_window.destroy()  
    else:
        messagebox.showwarning("No Report", "Please enter a report before submitting.")
        anonymous_window.destroy() 

def open_anonymous_reporting():
    anonymous_window = tk.Toplevel()
    anonymous_window.title("Anonymous Reporting")
    anonymous_window.geometry("500x500")  
    anonymous_window.configure(bg="beige")

   
    frame = tk.Frame(anonymous_window, bg="beige")
    frame.pack(pady=30)

    create_label(frame, "Anonymous Reporting", font=("Arial", 16, "bold"), bg="beige", fg="black")
    
   
    create_label(frame, "Please enter your report below:", bg="beige", pady=15)

    report_text = tk.Text(frame, height=8, width=40, font=("Arial", 12), wrap=tk.WORD, bd=2, relief="solid", padx=10, pady=10, bg="white", fg="black")
    report_text.pack(pady=20)
    
    anonymous_status = tk.BooleanVar(value=True)  # Default is anonymous
    anonymous_checkbox = tk.Checkbutton(frame, text="Report Anonymously", font=("Arial", 12), variable=anonymous_status, bg="beige")
    anonymous_checkbox.pack(pady=10)

    button_report = tk.Button(
        frame, 
        text="Submit Report", 
        font=("Arial", 12, "bold"), 
        bg="light green", 
        fg="white", 
        relief="flat", 
        width=20, 
        height=2, 
        command=lambda: submit_report(report_text.get("1.0", tk.END).strip(), anonymous_window)
    )
    
    def on_enter(e):
        button_report['bg'] = "dark orange"
        
    def on_leave(e):
        button_report['bg'] = "light green"
    
    button_report.bind("<Enter>", on_enter)
    button_report.bind("<Leave>", on_leave)

    button_report.pack(pady=20)

    send_button = tk.Button(
        frame, 
        text="Send", 
        font=("Arial", 12, "bold"), 
        bg="orange", 
        fg="white", 
        relief="flat", 
        width=20, 
        height=2, 
        command=lambda: submit_report(report_text.get("1.0", tk.END).strip(), anonymous_window)
    )
    
    def on_send_enter(e):
        send_button['bg'] = "dark green"
        
    def on_send_leave(e):
        send_button['bg'] = "orange"
    
    send_button.bind("<Enter>", on_send_enter)
    send_button.bind("<Leave>", on_send_leave)

    send_button.pack(pady=10)

    anonymous_window.mainloop()
#========================================================================= UPDATE CONTACTS =============================================================================

def create_label(parent, text, font=("Arial", 12), bg="beige", fg="black", pady=10):
    label = tk.Label(parent, text=text, font=font, bg=bg, fg=fg)
    label.pack(pady=pady)
    return label

# Function to simulate sending an SMS (For demonstration purposes)
def send_sms(name, district, contact_type, contact_details):
    if contact_details.strip() and name.strip() and district.strip() and contact_type:
        messagebox.showinfo("SMS Sent", f"Your SMS request has been sent.\n\n"
                                      f"Name: {name}\nDistrict: {district}\nContact Type: {contact_type}\nContact Details: {contact_details}\n\n"
                                      "Note: The details will be verified first before being sent.")
    else:
        messagebox.showwarning("Incomplete Details", "Please fill out all fields before submitting.")

def open_update_contacts():
    update_window = tk.Toplevel()
    update_window.title("Update Emergency Contacts")
    update_window.geometry("600x600")  
    update_window.configure(bg="beige")

    frame = tk.Frame(update_window, bg="beige")
    frame.pack(pady=30)
    create_label(frame, "Update Emergency Contacts", font=("Arial", 16, "bold"), bg="beige", fg="black")
    
    create_label(frame, "Please enter your emergency contact details below:", pady=15)

    create_label(frame, "Name:", pady=5)
    name_entry = tk.Entry(frame, font=("Arial", 12), width=40)
    name_entry.pack(pady=5)

    create_label(frame, "District:", pady=5)
    district_entry = tk.Entry(frame, font=("Arial", 12), width=40)
    district_entry.pack(pady=5)

    # Dropdown menu for selecting contact type
    create_label(frame, "Type of Emergency Contact:", pady=5)
    contact_types = ["Mayor's Office", "PNP", "CDRRMO", "Rescue Team", "BFP", "Red Cross", "CSWDO", 
                     "MDRRMO", "RHU", "Emergency Operation Center", "Coast Guard", "LGU" "Mental Health"]
    contact_descriptions = {
        "Mayor's Office": "Local government office responsible for overseeing municipal or city administration.",
        "PNP": "Philippine National Police, responsible for enforcing laws and maintaining peace and order.",
        "CDRRMO": "City Disaster Risk Reduction and Management Office, responsible for disaster preparedness and response.",
        "Rescue Team": "Team trained to provide rescue operations during emergencies.",
        "BFP": "Bureau of Fire Protection, responsible for fire prevention, suppression, and rescue.",
        "Red Cross": "Humanitarian organization providing emergency assistance, disaster relief, and education.",
        "CSWDO": "City Social Welfare and Development Office, handles welfare programs for individuals in need.",
        "MDRRMO": "Municipal Disaster Risk Reduction and Management Office, responsible for disaster management at the municipal level.",
        "RHU": "Rural Health Unit, provides health services in rural areas.",
        "Emergency Operation Center": "A facility that manages and coordinates disaster response efforts.",
        "Coast Guard": "The government agency responsible for maritime law enforcement and search and rescue operations.",
        "Mental Health":"Provide a range of interventions, assessments, diagnoses, treatments, and counseling to help people maintain or improve their mental health.",
        "LGU": "Local Government Unit, administrative body responsible for managing local affairs and services."
    }
    
    contact_type_var = tk.StringVar()
    contact_type_menu = tk.OptionMenu(frame, contact_type_var, *contact_types)
    contact_type_menu.config(font=("Arial", 12), width=38)
    contact_type_menu.pack(pady=5)

    # Label to show description of the selected contact type
    description_label = tk.Label(frame, text="", font=("Arial", 10), bg="beige", fg="black", wraplength=500)
    description_label.pack(pady=5)

    # Function to update the description label based on selected contact type
    def update_description(*args):
        selected_contact = contact_type_var.get()
        description_label.config(text=contact_descriptions.get(selected_contact, ""))

    # Bind the dropdown menu change to update the description
    contact_type_var.trace("w", update_description)

    # Entry box for entering contact details with custom border and padding (same as Name input box)
    create_label(frame, "Contact Details:", pady=5)
    contact_details_entry = tk.Entry(frame, font=("Arial", 12), width=40)
    contact_details_entry.pack(pady=10)

    # Reminder about verification
    create_label(frame, "Note: The details you provide will be verified first before being updated.", fg="red", pady=15)

    # Send SMS button with a rounded design and hover effect
    button_send = tk.Button(frame, text="Send SMS", font=("Arial", 12, "bold"), bg="orange", fg="white", 
                            relief="flat", width=30, height=2, command=lambda: send_sms(
                                name_entry.get(), district_entry.get(), contact_type_var.get(), contact_details_entry.get()))
    
    def on_enter(e):
        button_send['bg'] = "dark green"
        
    def on_leave(e):
        button_send['bg'] = "green"
    
    button_send.bind("<Enter>", on_enter)
    button_send.bind("<Leave>", on_leave)

    button_send.pack(pady=20)

    update_window.mainloop()

# Start the application with the main window
open_login_window()


