
# BATANGAS SAFETY CALL 

# I. PROJECT OVERVIEW

The Batangas Safety Call App GUI is a friendly users' platform developed to present solutions for some of the most significant problems associated with emergency response and mental care in the Batangas community. The primary factors that contribute to crisis issues include delayed reporting of incidents, lack of access to mental health tools, and inadequate coordination from response teams. The app's interface has fully integrated reporting of safety issues so a user can file it when needed, as well as connect with the authorities from the police and the department of fire and medical services or access mental health services ranging from crisis lines and counselling. Its intuitive design ensures users are at ease navigating through this kind of system, even at times of emergencies and when under mental health distress.

The app allows users to report incidents even about possible dangers, and access mental health support services, such as crisis helplines and professional counseling. By doing this, the app seeks to promote a more comprehensive approach to community well-being while gathering essential data to assist authorities and mental health professionals in enhancing future responses.


# System Boundaries
Included Features:

# Hotline Directory for Emergency

A listing of hotlines for the services of emergency care, mental health counseling, disaster relief services, and support lines for domestic violence victims and children at risk, etc.
Localized directory by district according to the user's location in Batangas.

# Quick-Dial Feature
Direct access to emergency services through quick-dial buttons for services such as police, fire, ambulance, and health services.
 Mental Health Support and Crisis Text Lines
Hotlines that cater for mental health support, suicide prevention, and crisis counseling.

# Educational Resources 
Resources on first aid, emergency preparedness, and trauma care.
A set of FAQs and guidance on different emergencies.

# Anonymous Reporting Options
A mechanism by which users can anonymously report an emergency, such as a case of domestic violence or child abuse, directly to the relevant authorities.

#User-Suggested Updates and Verification
 Facility for users to submit updates or verify the accuracy of emergency contact information to ensure the directory is current.


Excluded Features: 
 Medical Diagnosis or Treatment
The system will not provide medical diagnoses or recommend specific treatments. It will only provide contact information for healthcare providers.

Real-Time Emergency Response or Field Support
The system will not directly handle or dispatch emergency personnel. It will only connect users to the relevant services.

Advanced Reporting or Case Management
 Detailed case files or case follow-ups on reported cases such as abuse or violence would not be managed. Only enablement of communication and reporting shall be the core business.

Non-Emergency Services
Non-urgent services such as a routine appointment in any of the health facilities, asking about a government service, or simply general information on things about the public shall not feature in this system.

Direct Integration with Non-Emergency Mobile Applications
The system shall not integrate with third-party applications and services outside the emergency response network, focusing exclusively on urgent needs.

    Target Users: The system is solely designed for residents in Batangas.


The Batangas Safety Call App aims to achieve the following outcomes based on the SMART criteria, focusing on its current status as a GUI prototype:

    1. Specific
The app is designed to provide a clear and interactive interface where users can simulate actions such as submitting safety hazard reports, accessing emergency contact information, and navigating through safety-related updates.

    2. Measurable
Success during the GUI development phase will be measured by:

Completion of the GUI design for all core features (target: 100% completion within the development timeline). User testing results showing intuitive navigation and user-friendly design (target: 85% positive feedback). The ability to run at least 50 simulated safety-related interactions without errors or crashes.

    3. Achievable:
The app will focus on delivering a fully functional GUI by leveraging established development tools and frameworks. By concentrating solely on the front-end design, the project ensures feasible progress within the available time and resources, creating a prototype that effectively showcases the intended functionality and user experience.

    4. Relevant:
The GUI prototype is directly relevant to the goal of creating a platform for public safety in Batangas. It serves as a foundational step for visualizing and testing the app’s potential functionality, ensuring readiness for future full-scale development

    5. Time-bound:
The GUI prototype is expected to achieve the following within the first year:

Finalize the design and development of the GUI within the first 6 months. Conduct at least 3 rounds of user testing to refine the interface by the 8th month. Prepare a finalized prototype ready for demonstration or further development by the end of the 12th month.





## II. PYTHON CONCEPTS AND LIBRARIES

Python Concepts:

These are core features of Python that help me achieve the functionality in my program. Here’s how I’m using them:

    Functions: 
In my code, I define functions like open_ringing_window(), open_district_window(), and submit_report(). These functions allow me to group related tasks (like opening windows or submitting reports) into reusable blocks of code.

    Lambda Functions: 
I use lambda functions to pass arguments to event handlers. For instance, when I create buttons, I use a lambda function to pass specific data when the button is clicked, like this: command=lambda: submit_report(report_text.get("1.0", tk.END).strip()). It lets me define a small function without having to explicitly name it.

    Event Handling:
In GUI programming, events are actions triggered by the user, like clicking a button or moving the mouse. I bind events to widgets in my code. For example, I bind hover events to buttons to change their color when the mouse enters or leaves the button.

    Conditionals: 
I use conditional logic to check whether certain conditions are met before executing certain actions. For example, before submitting a report, I check if there’s any text entered in the report field: if report_text.strip().

    Loops: 
While I don’t have direct loops like for or while, I do loop through data structures like dictionaries or lists. For instance, I loop over the dictionary hotlines_by_district to generate buttons for each district dynamically.

    Variable Types:
I define variables like district_window, report_text, and button_send, which store references to Tkinter widgets. These are objects that represent the GUI elements (like buttons, labels, and windows).
            
Python Libraries:
       These are external pre-written pieces of code that I import and use in my program to add functionality without having to write everything from scratch. Here’s what I’m using:

    Tkinter:
Tkinter is the main library I use to create the GUI. It’s a standard Python library for building windows, buttons, text fields, and other graphical elements. In my code, I use it to create windows, labels, buttons, entry fields, and more.

For example, tk.Toplevel() creates a new window, tk.Label() creates a label, and tk.Button() creates a button. I also use methods like .pack() and .grid() to position the widgets in the window.

    tkinter.messagebox:
The messagebox module is part of Tkinter, and it allows me to show pop-up dialog boxes with messages. For instance, when submitting a report or showing a warning, I use messagebox.showinfo() to show an info message and messagebox.showwarning() to display a warning.

    tkinter.Scrollbar:
The Scrollbar widget is used to add scrollbars to windows or frames. In my code, I use it in windows like district_window and hotline_window to display emergency contacts in a scrollable area.

    tkinter.Text:
The Text widget allows me to create a multi-line text input area. I use it in the anonymous report window so users can type longer text inputs.












## III. SUSTAINABLE DEVELOPMENT GOALS

The Batangas Safety Call system is an effective new tool to address this challenge within the most important community contexts, showcasing its great alignment with several Sustainable Development Goals.

Mainly, it supports “SDG 3: Good Health and Well-being” by enabling immediate access to healthcare, mental health resources, and emergency services. The system ensures the availability of crucial contact information to ensure prompt action during any form of medical emergency or mental health-related crisis. This will immediately serve the need for easy access to health care and emergency services in reducing further crises by delaying the response.

Regarding “SDG 11: Sustainable Cities and Communities,” the website contributes to safer and more resilient urban and rural environments. Given that the system allows a community to easily access an emergency hotline and report on hazards or disasters, a community can act proactively with such power. It builds disaster readiness and increases safety measures with sustainable living environments, enabling them to face disasters or accidents or a failure in infrastructure.

The Batangas Safety Call system also advances “SDG 17: Partnerships for the Goals” by serving as a bridge that unites various stakeholders, including government agencies, local organizations, healthcare providers, and community members. By fostering collaboration and leveraging shared resources, the system enhances collective capacity to address emergencies effectively. These partnerships ensure that services are seamlessly coordinated, amplify community outreach, and strengthen the overall impact of safety initiatives.

Through its multifaceted functions, the Batangas Safety Call system addresses immediate needs for safety and health while establishing a foundation for long-term resilience, inclusivity, and sustainable development. Aligning with the SDGs, it is a research-backed solution to community challenges, making sure that it is relevant and effective in achieving a safer and healthier society.













## IV. PROGRAM/SYSTEM INSTRUCTIONS
    
    1. Running the Program
Execute the Python script in an environment with the Tkinter library installed; it could be IDLE, terminal, or an IDE like PyCharm.The program will launch a Login Window as the entry point.

    2. Logging In
Steps:
  Enter your Username and Password in the provided fields.
 Click the Login button to proceed.

What Happens Next:
  If the credentials match an existing account, you’ll be directed to the Main Application Window.

  If something is wrong (e.g., incorrect username or password), you’ll see an error message. Make sure to double-check your login details.

Note: If you don’t have an account yet, click the Register button to create one.

     3. Registering a New Account
Steps:
  Click the Register button on the Login Window to open the Registration screen.

Fill out the form with:
 A Username of your choice.
 A Password that is secure and easy for you to remember.
 Confirm Password to make sure there are no typos.

 Click the Register button to submit.

What to Expect:
If everything is filled out correctly and the passwords match, your account will be created successfully. A confirmation message will let you know.

If there’s an issue (e.g., username already taken or mismatched passwords), you’ll see a message explaining what went wrong so you can fix it.

    4. Main Application Window
Once logged in, you’ll enter the Main Application Window, where you’ll see a welcome message and options to continue. The main window contains several buttons for different services you can access. Each button will open a different feature of the app, such as emergency hotlines, first aid resources, mental health support, and more. Below are the key features:

Emergency Hotlines:
Access a list of important emergency contact numbers, such as police, fire, and medical services. When you click the "Emergency Hotlines" option, a new window opens displaying a list of districts. This window provides an option to choose a district.

District Selection: Upon selecting a district, a new window opens, showing a list of places within that district along with their respective emergency contact numbers.

Calling Simulation: If you click on any contact (e.g., Mayor's Office..), the program simulates a call. A "Calling..." window will appear, showing the contact being dialed and eventually connecting the call. A button allows you to end the simulation.

Scrollable Interface: Both the district and hotline selection windows feature a scrollable interface, which makes it easy to navigate through a long list of districts or contacts.

To use it:
 Open the "Emergency Hotlines" window, select your district, and then choose the specific contact you want to call.
 The simulation of the call gives you a feedback loop with a slight delay before showing that you're connected or ending the call.

 First Aid Resources: Below this, a list of six first aid steps is provided. Each step explains a key action to take in various emergency situations, such as CPR, choking, bleeding, burns, and unconsciousness. The steps are formatted clearly, with easy-to-read text aligned to the left.

Close Button: At the bottom of the window, there's a prominent "Close" button with an orange background and white text. Clicking this button will close the first aid resources window.

Mental Health Support:
After you click this button a new window will appear titled "Mental Health Support."Scroll through the content using the vertical scrollbar on the right side of the window.
Read about: “Why mental health matters.” and different resources for mental health support.

View Mental Health Contacts
Click the "View Contacts" button located near the bottom of the window. A new window will open with a list of mental health contacts, including: Organization names and phone numbers.

Each contact has a "Call" button beside it.

Simulate Dialing a Contact
Select the organization you wish to contact and click the "Call" button. A pop-up window will appear, simulating the call.
It will display a message such as "Dialing Batangas Medical Center - Psychiatry Department... 0437408307."

Wait a few seconds as the simulation updates:

The message changes to "Connecting..." and then to "Connected!" to indicate a successful call.

End the call by clicking the "OK" button, or let the simulation close automatically after 10 seconds.


Educational Resources & Guidance:
Learn about safety procedures, disaster preparedness, and general health tips.Inside the window, you'll find the following sections:

First Aid Resources
Learn essential steps to handle emergencies like CPR, choking, burns, and bleeding.

Emergency Preparedness Resources
Discover how to create a family emergency plan, prepare for natural disasters, and build an emergency kit.
 
Trauma Care Resources
Gain knowledge about handling severe trauma, controlling bleeding, and managing shock.

Frequently Asked Questions (FAQs)
Find answers to common questions.

Anonymous Reporting:
Submit anonymous safety reports about hazards, incidents, or other concerns without revealing your identity.Use the large text box provided to type out the details of your report.Ensure the content is clear and complete before submission. You can describe any issue, concern, or observation you want to report.By default, the report will be submitted anonymously. If you wish to include your details, uncheck the "Report Anonymously" checkbox.

Update Emergency Contacts:
Update your emergency contact information, ensuring that the app has the most current and accurate details for emergency services.

Look for the text box labeled "Name:" and enter your full name.  Example: "Juan Dela Cruz"

Find the text box labeled "District:" and type the name of your district.  Example: "District 1"

Select Contact Type

Use the dropdown menu labeled "Type of Emergency Contact:" to select the category of the contact you want to update. Once you select a contact type, a description of its purpose will appear below the dropdown for your reference.

Locate the text box labeled "Contact Details:" and enter the phone number or other necessary details for the selected contact.   Example: "0917-123-4567"

A note below the fields reminds you that the information you provide will be verified before being updated.

Double-check all fields for accuracy before proceeding.

Click the "Send SMS" Button. The button changes to dark green when hovered over, indicating it's ready to be clicked.

If your submission is complete, a pop-up will confirm: "Your SMS request has been sent. The details will be verified first before being sent."

Handle Missing Information
If you try to submit without filling out all required fields, a warning will appear: "Please fill out all fields before submitting."
     
     5. Logging Out
If you're done using the app, you can log out by clicking the Logout button at the bottom-right corner of the window.
What Happens When You Log Out:
Clicking Logout will close the main window.












