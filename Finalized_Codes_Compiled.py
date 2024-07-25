## Beginning of Receptionist Part
#1 register customer
def Register_New_Customer():
    print("Add New Customer Here")
    f = open ("userpasslistrec.txt", "a")
    cun = input("Add Customer's Username: ")
    cpa = input("Add Customer's Password: ")
    rol = 'CUSTOMER'.upper()
    f.write(cun+","+cpa+","+rol+"\n")
    g = open("Basic_Customer_Details.txt", "a")
    h = open("More_Customer_Details.txt", "a")
    cfn = input("Enter Customer First Name: ")
    cln = input("Enter Customer Last Name: ")
    em = input("Enter Email:")
    ccn = input("Enter customer contact number (01x-xxxxxxx): ")
    sercat = input("Enter service category (1-NORMAL,2-URGENT): ")
    datereq = input("Enter date of request (dd-mm-yyyy): ")
    stat = 'PENDING'
    doc = '-'
    description = '-'
    price = input("Enter total price (RM): ")
    print("Services Offered")
    print("[1] Remove virus, malware or spyware")
    print("[2] Troubleshot and fix computer running slow")
    print("[3] Laptop screen replacement")
    print("[4] Laptop battery replacement")
    print("[5] Operating System Format and Installation")
    print("[6] Data backup and recovery")
    csr = input("Service Requested (S1, S2, ...)(Only one service allowed at a time): ").upper()
    g.write(cfn+","+cln+","+ccn+","+em+","+sercat+","+csr+"\n")
    h.write(cfn+","+csr+","+sercat+","+datereq+","+stat+","+doc+","+description+","+price+"\n")
    f.close()
    g.close()
    h.close()
    print("Customer have been recorded")



#2 payment and receipt
# Function to generate and display a formatted receipt
def generate_receipt():
    # Define the company information
    company_name = 'FloppaTech Pte. Ltd.'
    company_address = 'Lot 13, Bangunan CBD 2 Cyberjaya, 43100, Sepang, Selangor'
    company_contact = '016-9696969'

    # Read data from the text file 'More_Customer_Details.txt' while skipping the header
    data = []
    try:
        with open('More_Customer_Details.txt', 'r') as file:
            # Skip the header row
            next(file)
            for line in file:
                name, service, service_category, date_of_request, status, date_of_completion, description, price = line.strip().split(",")
                if service_category.isnumeric():
                    service_category = int(service_category)
                if price.isnumeric():
                    price = int(price)
                entry = {
                    'Name': name,
                    'Service': service,
                    'Service Category': service_category,
                    'Price': price,
                    'Date of Completion': date_of_completion
                }
                data.append(entry)
    except FileNotFoundError:
        print("Error: The file 'More_Customer_Details.txt' was not found.")
        return

    # Get user's name input
    user_name = input("Enter your name: ")

    # Filter data based on the user's name
    filtered_data = [entry for entry in data if entry['Name'] == user_name]

    # Check if there is data for the user
    if not filtered_data:
        print(f"No data found for user: {user_name}")
        return

    for entry in filtered_data:
        # Message to generate receipt
        print("\nReceipt generating...")
        # Receipt header with company information
        print(f'\n{"="*50}')
        print(f'{company_name}\n{company_address}\nContact: {company_contact}\n')
        print(f'{"-"*50}\n')

        # Middle section with service details
        print(f"{'Service:':<20} {entry['Service']}")
        print(f"{'Service Category:':<20} {entry['Service Category']}")
        print(f"{'Price:':<20} RM{entry['Price']}\n")

        # Bottom section with transaction information
        print(f'{"-"*50}\n')
        print(f'Total: RM{entry["Price"]}')
        print(f'Date of Completion: {entry["Date of Completion"]}')

        # Receipt footer
        print(f'{"="*50}')
        print("\n")
        print("Returning to main menu...")

#3 update profile
def update_receptionist_profile():
    if __name__ == "__main__":
        receptionist_id = input("Enter Receptionist ID: ")
        new_address = input("Enter new Address (Street Postcode State): ")
        new_language1 = input("Enter new Language 1: ")
        new_language2 = input("Enter new Language 2: ")

    with open('ftreceptionrec.txt', 'r') as file:
        lines = file.readlines()

    updated_data = []
    found = False

    for line in lines:
        data = line.strip().split(',')
        if data[0] == receptionist_id:
            data[4] = new_address
            data[5] = new_language1
            data[6] = new_language2
            found = True
        updated_data.append(data)

    if found:
        with open('ftreceptionrec.txt', 'w') as file:
            for line in updated_data:
                updated_line = ','.join(line)
                file.write(updated_line + '\n')
        print("Data updated successfully. Returning to the main menu...")
    else:
        print("Receptionist ID not found. Returning to the main menu...")


#1 Login
def receptionist_menu_page():
    while True:
        print("[1] Register New Customers")
        print("[2] Payment and Receipt Generator")
        print("[3] Update Profile")
        print("[0] Log Out")
        option = int(input("Enter your Option: "))
        match option:
            case 1:
                Register_New_Customer()
            case 2:
                generate_receipt()
            case 3:
                update_receptionist_profile()
            case 0:
                break
            case _:
                ("Invalid option. Please try again.")
    print("Thank you for logging in. Have a wonderful day!")
## End of Receptionist Part

## Beginning of Technician Part
#create technician page menu
def technician_menu_page():
    while True :
            print("\n【【【 Welcome to Floppa Tech Technician Page 】】】")
            print('''[1] View Service Requested by customers.
[2] Add Customer Description
[3] Update Technician Profile
[0] Log Out''')

            option = int(input("Enter your option:"))
            print("")
            match option:
                case 1:
                    view_service()
                    update_status_date_completed()
                case 2:
                    add_description()
                case 3:
                    update_technician_details()
                case 0:
                    exit()
                case _:
                    print("Invalid input. Please retry again.")

# View requested service by customers
def view_service():
    print("\n【 List of Pending Customers 】\n")
    found = False
    with open("More_Customer_Details.txt", "r") as f:
        header = next(f)
        for line in f:
            # Split the line into individual values
            u_name, service_number, service_category, date_request, status, date_completed, description, price = line.strip().split(",")
            if "Completed" not in status:
                if service_category.isnumeric():
                    service_category = int(service_category)
                print("{:<25}{:^8}".format("Customer Name", u_name))
                print("{:<27}{:<4}{:<0}".format("Service Type Requested", service_number,show_service_type(service_number)))
                print("{:<27}{:<40}".format("Service Category", service_category,show_service_category(service_category)))
                print("{:<27}{:<40}".format("Date Requested:", date_request))
                print("{:<27}{:^8}".format("Status", status))
                print("{:<27}{:<40}".format("Date Completion:", date_completed))
                print("{:<27}{:<40}".format("Description:", description))
                print("{:<27}{:<40}".format("Price:", price))
                print("")
                found = True
    if not found:
        print("No service pending.")
        technician_menu_page()

#show service type according to service ID
def show_service_type(service_number):
    service_type = None
    if service_number == 'S1':
        service_type = "Remove virus, malware, or spyware"
    elif service_number == 'S2':
                service_type = "Troubleshoot and fix computer running slow"
    elif service_number == 'S3':
                service_type = "Laptop screen replacement"
    elif service_number == 'S4':
                service_type = "Laptop battery replacement"
    elif service_number == 'S5':
                service_type = "Laptop keyboard replacement"
    elif service_number == 'S6':
                service_type = "Data backup and recovery"
    return service_type

#show service category according to category number
def show_service_category(service_category):
    service_cat = None
    if service_category == 1:
                service_cat = "URGENT"
    elif service_category == 2:
                service_cat = "NORMAL"
    return service_cat

#update statues and date completed
def update_status_date_completed():
    print("\n【 To Update Customer Status and Completion Date 】\n")
    name = input("Enter Customer Name: ")
    user = False
    # Open the file in read-write mode ('r+')
    with open("More_Customer_Details.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)  # Reset the file pointer to the beginning of the file

        for line_number, line in enumerate(lines):
            u_name, service_number, service_category, date_request, status, date_completed, description,price = line.strip().split(",")

            if name == u_name:
                user = True
                print("{:<25}{:^8}".format("Customer Name:", u_name))
                print("{:<27}{:<4}{:<0}".format("Service Type Requested:", service_number,
                                                show_service_type(service_number)))
                print("{:<27}{:<40}".format("Service Category:", service_category,
                                            show_service_category(int(service_category))))
                print("{:<27}{:<40}".format("Date Requested:", date_request))
                print("{:<27}{:^8}".format("Status:", status))
                print("{:<27}{:<40}".format("Date Completion:", date_completed))
                print("{:<26}{:<38}".format("Description:", description))
                print("{:<27}{:<40}".format("Price:", price))
                print("")

                c = input("Enter New Status (Completed): ").capitalize()
                b = input("Enter Completion Date (dd-mm-yyyy): ")
                updated_line = ",".join([u_name, service_number, service_category, date_request, c, b,description,price])
                print(updated_line)
                f.write(updated_line + '\n')  # Write the updated line back to the file
                print("Status and Date of completion UPDATED successfully.\n")
            else:
                f.write(line)  # Write the original line back to the file

        # If the customer was not found, print a message
    if not user:
        print("Customer NOT FOUND, please try again.")


#add description for customers
def add_description():
    print("【 Add Customer's Service Description 】")
    name = input("Enter Customer Name: ")
    user = False

    f = open("More_Customer_Details.txt","r+")
    lines = f.readlines()
    f.seek(0)

    for line_number, line in enumerate(lines):
            u_name, service_number, service_category, date_request, status, date_completed, description,price = line.strip().split(
                ",")

            if name == u_name:
                user = True
                print("{:<25}{:^8}".format("Customer Name:", u_name))
                print("{:<27}{:<4}{:<0}".format("Service Type Requested:", service_number,
                                                show_service_type(service_number)))
                print("{:<27}{:<40}".format("Service Category:", service_category,
                                            show_service_category(int(service_category))))
                print("{:<27}{:<40}".format("Date Requested:", date_request))
                print("{:<27}{:^8}".format("Status:", status))
                print("{:<27}{:<40}".format("Date Completion:", date_completed))
                print("{:<26}{:<40}".format("Description:", description))
                print("{:<27}{:<40}".format("Price:", price))
                print("")

                d = str(input("Description: "))
                updated_line = ",".join([u_name, service_number, service_category, date_request, status,date_completed,d,price])
                print(updated_line)
                f.write(updated_line + "\n")
                print("")
                print("Description UPDATED successfully.\n")
            else:
                f.write(line)
    if not user:
        print("Customer NOT found. Please try again.")
    f.close()



#update_technician details
def update_technician_details():
    def update_detail(tech_ID, detail_name, prompt_message, update_message):
        with open("fttechnicianrec.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)

            for line_number, line in enumerate(lines):
                technician_ID, first_name, last_name, DoB, contact_number, address, service_specialty = line.strip().split(",")

                if tech_ID == technician_ID:
                    print(f"【 Update {detail_name} 】")
                    new_detail = str(input(f" {prompt_message}"))
                    if detail_name == "Contact Number":
                        updated_line = ",".join(
                            [technician_ID, first_name, last_name, DoB, new_detail, address, service_specialty])
                    elif detail_name == "Address":
                        updated_line = ",".join(
                            [technician_ID, first_name, last_name, DoB, contact_number, new_detail, service_specialty])
                    elif detail_name == "Service Specialty":
                        updated_line = ",".join(
                            [technician_ID, first_name, last_name, DoB, contact_number, address, new_detail])
                    else:
                        updated_line = line  # If the detail_name is not recognized, don't change the line
                    print(updated_line)
                    f.write(updated_line)
                    print("")
                    print(f"{update_message} Succesfully Updated.\n")
                else:
                    f.write(line)




    def show_current_detail(tech_ID):
        with open("fttechnicianrec.txt", "r") as f:
            lines = f.readlines()

            for line_number, line in enumerate(lines):
                technician_ID, first_name, last_name, DoB, contact_number, address, service_specialty = line.strip().split(",")

                if tech_ID == technician_ID:
                    print("{:<26}{:^8}".format("Technician ID:", technician_ID))
                    print("{:<27}{:<4}".format("First Name:", first_name))
                    print("{:<27}{:<40}".format("Last Name:", last_name))
                    print("{:<27}{:<40}".format("Date of Birth:", DoB))
                    print("{:<27}{:^8}".format("Contact Number:", contact_number))
                    print("{:<27}{:<40}".format("Home Address:", address))
                    print("{:<27}{:<40}".format("Service Specialty:", service_specialty))

                    print('''\nChoose Update Details Option:
[1] Contact Number
[2] Address
[3] Service Specialty
[0] Back to Techinician Menu''')

                    update_option = int(input("Enter your Option: "))
                    match update_option:
                        case 1:
                            update_detail(tech_ID, "Contact Number", "Enter your New Contact Number(012-3456789): ", "Contact Number")
                        case 2:
                            update_detail(tech_ID, "Address", "Enter your New Address (Street, Postcode, State): ", "Address")
                        case 3:
                            update_detail(tech_ID, "Service Specialty", "Enter your New Service Specialty (S1): ", "Service Specialty")
                        case 0:
                            technician_menu_page()
                    break
    max_attempt = 3
    for attempt in range(1, max_attempt + 1):
        print(f"Attempt #{attempt}")
        verify_tech_ID = str(input("Verify Technician ID: "))
        verify_tech_pw = str(input("Verify Technician Password: "))

        f = open("userpasslistrec.txt", "r")
        for line in f:
            tech_ID, tech_pw, role = line.strip().split(',')
            if verify_tech_ID == tech_ID and verify_tech_pw == tech_pw:
                print("")
                print("Verification Successful.\n")
                show_current_detail(verify_tech_ID)
                return
        print("Log in Failed.")
    print("Maximum attempts reached.\n")
## End of Technician Part

## Beginning of Customer Part
from tabulate import tabulate
table_data = [
        ['1', 'Remove virus, malware or spyware', 'RM 50', 'RM 80'],
        ['2', 'Troubleshoot and fix computer running slow', 'RM 60', 'RM 90'],
        ['3', 'Laptop screen replacement', 'RM 380', 'RM 430'],
        ['4', 'Laptop battery replacement', 'RM 180', 'RM 210'],
        ['5', 'Operating System Format and Installation', 'RM 100', 'RM 150'],
        ['6', 'Data backup and recovery', 'RM 80', 'RM 130']]

header = ["No", "Service type", "Service(Normal)", "Service Fee(Urgent)"]

# Function to read customer details from a file
def read_customer_details(filename):
    with open("Basic_Customer_Details.txt", "r") as file:
        lines = file.readlines()
        details = [line.strip().split(",") for line in lines]
    return details

def read_customer_requests(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        requests = [line.strip().split(",") for line in lines]
    return requests

def write_customer_requests(filename, requests):
    with open(filename, "w") as file:
        for request in requests:
            file.write(",".join(request) + "\n")

def get_customer_request_by_name(name, requests):
    for request in requests:
        if request[0] == name:
            return request
    return None

def change_service_request():
    filename = "More_Customer_Details.txt"
    requests = read_customer_requests(filename)

    # Step 1: Ask for customer name
    name = input("Enter your name: ")
    customer_request = get_customer_request_by_name(name, requests)

    if not customer_request:
        print("Name not found!")
        return

    # Step 2: Display their current request
    print(f"******** Current service request for {name}: {customer_request[1]} ********\n-------------------------------------------------------")

    # Step 3: Let them choose a new service
    print("Available services: S1, S2, S3, S4, S5, S6\n-------------------------------------------------------")
    new_service = input("Enter new service request: ")
    while new_service not in ["S1", "S2", "S3", "S4", "S5", "S6"]:
        print("Invalid choice. Please choose from S1 to S6.")
        new_service = input("Enter new service request: ")

    # Update the service in the request
    customer_request[1] = new_service

    # Step 4: Save changes back to the file
    write_customer_requests(filename, requests)
    print(f"Service request for {name} has been updated to {new_service}.")



# Function to write customer details to a file
def write_customer_details(filename, details):
    with open(filename, "w") as file:
        for detail in details:
            file.write(",".join(detail) + "\n")


# Function to change customer details
def change_customer_details():
    filename = "Basic_Customer_Details.txt"
    details = read_customer_details(filename)

    # Step 1: Ask for customer name
    name = input("Enter your name: ")

    # Find the customer's details by name
    customer_detail = None
    for detail in details:
        if detail[0] == name:
            customer_detail = detail
            break

    if not customer_detail:
        print("Customer not found!")
        return

    # Step 2: Display their current details
    current_name, current_lastname, current_phone, current_email, _, _ = customer_detail
    print(f"Current details for {name}:")
    print(f"First Name: {current_name}")
    print(f"Last Name: {current_lastname}")
    print(f"Phone: {current_phone}")
    print(f"E-mail:{current_email}")

    # Step 3: Update the customer's details
    new_name = input("Enter new first name: ")
    new_lastname = input("Enter new last name: ")
    new_phone = input("Enter new phone number: ")
    new_email = input("Enter new e-mail address: ")

    customer_detail[0] = new_name
    customer_detail[1] = new_lastname
    customer_detail[2] = new_phone
    customer_detail[3] = new_email

    # Step 4: Save changes back to the file
    write_customer_details(filename, details)
    print(f"Details for {name} have been updated. Returning to the main menu...")


# Function to display service descriptions
def view_service_description():
    # Specify the path to your text file
    file_path = "More_Customer_Details.txt"
    nm = input("Enter your name:")

    found = False  # Flag to check if the name was found in the file

    # Open the text file for reading
    with open(file_path, 'r') as f:
        # Read the contents of the file
        for line in f:
            customer_detail = line.strip().split(",")
            if customer_detail[0] == nm:
                found = True
                print(f"....................................................\nService Description: {customer_detail[6]}, Price (RM): {customer_detail[7]}")
                if customer_detail[4] == "Pending":
                    print("Your computer is still in service. Check again soon!")
                else:
                    print(f"Collection date:{customer_detail[5]}\n....................................................")
    if not found:
        print(f"{nm} is not found in the file. Returning to the main menu...")
# Main menu
def customer_menu_page():
    if __name__ == "__main__":
        while True:
            print("********** Menu ************\n----------------------------\n1. Change service request\n2. View service description\n3. Update profile\n4. Exit\n----------------------------")
            option = int(input("Please enter an option:"))

            if option == 1:
                print(tabulate(table_data, header, tablefmt="fancy_grid"))
                change_service_request()
            elif option == 2:
                view_service_description()
            elif option == 3:
                # Implement profile update functionality here
                change_customer_details()
                pass
            elif option == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
## End of Customer Part

## Beginning of Administrator Part
# ID generator for new technicians
def technician_id_generator():
    try:
        f = open("technician_id_counter.txt", "r")
        technician_id_generator_string = f.read().strip()
        if technician_id_generator_string:
            technician_id = int(technician_id_generator_string)
        else:
            technician_id = 1
    except FileNotFoundError:
        technician_id = 1

    technician_id_format = f"FTTC{technician_id:02}"
    g = open("technician_id_counter.txt", "w")
    g.write(str(technician_id + 1))

    return technician_id_format

# Function to execute technician registration
def add_technician():
    print("\nAdd a new technician's details here.")
    technician_id = technician_id_generator()
    technician_password = input("Add a technician password: ")
    technician_role = "technician".upper()
    f = open ("userpasslistrec.txt", "a")
    f.write(technician_id+","+technician_password+","+technician_role+"\n")
    g = open("fttechnicianrec.txt", "a")
    technician_first_name = input("Enter technician's first name: ")
    technician_last_name = input("Enter technician's last name: ")
    technician_date_of_birth = input("Enter technician's date of birth (e.g. dd-mm-yyyy): ")
    technician_contact_number = input("Enter technician's contact number (e.g. 01x-xxxxxxx): ")
    technician_house_address = input("Enter technician's address (street,postcode,state): ")
    print("***Services Offered***")
    print("[S1] Remove virus, malware, or spyware")
    print("[S2] Troubleshoot and fix computer running slow")
    print("[S3] Laptop screen replacement")
    print("[S4] Laptop battery replacement")
    print("[S5] Operating System Format and Installation")
    print("[S6] Data backup and recovery")
    service_specialty = input("Enter Technician's Service Specialty: ")
    g.write(technician_id+","+technician_first_name+","+technician_last_name+","+technician_date_of_birth+","
            +technician_contact_number+","+technician_house_address+","+service_specialty+"\n")
    f.close()
    g.close()
    print("\nTechnician Record Added! Returning to the main menu...")

# ID generator for new receptionists
def receptionist_id_generator():
    try:
        f = open("reception_id_counter.txt", "r")
        generate_receptionist_id_string = f.read().strip()
        if generate_receptionist_id_string:
            receptionist_id = int(generate_receptionist_id_string)
        else:
            receptionist_id = 1
    except FileNotFoundError:
        receptionist_id = 1

    receptionist_id_format = f"FTRC{receptionist_id:02}"
    g = open("reception_id_counter.txt", "w")
    g.write(str(receptionist_id + 1))

    return receptionist_id_format

# Function to execute receptionist registration
def add_receptionist():
    print("\nAdd a new receptionist's details here.")
    receptionist_id = receptionist_id_generator()
    receptionist_password = input("Add a receptionist password: ")
    receptionist_role = "RECEPTIONIST"
    f = open("userpasslistrec.txt", "a")
    f.write(receptionist_id+","+receptionist_password+","+receptionist_role+"\n")
    receptionist_first_name = input("Enter receptionist's first name: ")
    receptionist_last_name = input("Enter receptionist's last name: ")
    receptionist_date_of_birth = input("Enter receptionist's date of birth (e.g. dd-mm-yyyy): ")
    receptionist_contact_number = input("Enter receptionist's contact number (e.g. 01x-xxxxxxx): ")
    receptionist_address = input("Enter receptionist's address (street,postcode,state): ")
    primary_language_of_communication = input("Enter receptionist's primary language of communication (e.g. English, Malay, etc.): ")
    secondart_language_of_communication = input("Enter receptionist's secondary language of communication (e.g. English, Malay, etc.): ")
    g = open("ftreceptionrec.txt", "a")
    g.write(receptionist_id+","+receptionist_first_name+ ","+receptionist_last_name+","+receptionist_date_of_birth+","
            +receptionist_contact_number+","+receptionist_address+","+primary_language_of_communication+","
            +secondart_language_of_communication+"\n")
    f.close()
    g.close()
    print("\nReceptionist Record Added! Returning to the main menu...")

# View service reports that has happened throughout a specific month and year
def view_monthly_service_report():
    import csv

    # Read the data from the text file and store it in a list of dictionaries
    data = []
    f = open("More_Customer_Details.txt", "r")
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

    # Prompt the admin to input the year and month
    print("\n***FloppaTech Monthly Service Report Viewing***")
    year = int(input("Enter the year of choice (e.g., 2023): "))
    month = int(input("Enter the month of choice (e.g., input 10 for the month October): "))

    # Initialize a list to store data for the specified month and year with 'Status' as 'Completed'
    matching_rows = []

    # Iterate through the data and filter rows based on the specified criteria
    for row in data:
        date_request = row['Date of Request'].split('-')
        if int(date_request[2]) == year and int(date_request[1]) == month and row['Status'] == 'Completed':
            # Modify 'Service Category' based on the values
            if row['Service Category'] == '1':
                row['Service Category'] = 'URGENT'
            elif row['Service Category'] == '2':
                row['Service Category'] = 'NORMAL'

            matching_rows.append({
                'Name': row['Name'],
                'Services': row['Services'],
                'Service Category': row['Service Category'],
                'Date of Completion': row['Date of Completion'],
                'Service Description': row['Description'],
                'Price': row['Price']
            })

    # Display the data rows for the specified month and year with 'Status' as 'Completed' in a table
    if matching_rows:
        print(f"\nData for Service Descriptions within {month}-{year}:")
        headers = ['Name', 'Services', 'Service Category', 'Date of Completion', 'Service Description', 'Price']

        # Create a format string for the table
        string_format = ' | '.join(f'{{:<{len(header)}}}' for header in headers)

        # Print the header row
        print(string_format.format(*headers))

        # Print the data rows
        for row in matching_rows:
            price_in_ringgit = "RM{:.2f}".format(float(row['Price']))
            row_data = [row['Name'], row['Services'], row['Service Category'], row['Date of Completion'],
                        row['Service Description'], price_in_ringgit]
            print(string_format.format(*row_data))
        print("\nReturning to the main menu...")
    else:
        print("\nNo data matches your request. Returning to the main menu...")

# View the total monthly income, along with the involved data in a table format
def view_monthly_income():
    import csv

    # Read the data from the text file and store it in a list of dictionaries
    data = []
    f = open("More_Customer_Details.txt", "r")
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

    # Prompt the admin to input the year and month
    print("\n***FloppaTech Monthly Income Viewing***")
    year = input("Enter the year of choice (e.g., 2023): ")
    month = input("Enter the month of choice (e.g., input 10 for the month October): ")

    # Initialize the total income for the specified month and year
    total_income = 0

    # Initialize a list to store data rows for the specified month and year with 'Status' as 'Completed'
    matching_rows = []

    # Iterate through the data and sum the prices for the specified month and year
    for row in data:
        date_request = row['Date of Request'].split('-')
        if date_request[2] == year and date_request[1] == month and row['Status'] == 'Completed':
            total_income += float(row['Price'])
            # Modify 'Service Category' based on the values
            if row['Service Category'] == '1':
                row['Service Category'] = 'NORMAL'
            elif row['Service Category'] == '2':
                row['Service Category'] = 'URGENT'
            matching_rows.append(row)

    # Display the total income for the specified month and year
    print(f"\nTotal income for {month}-{year}: RM{total_income:.2f}")

    # Display the data rows for the specified month and year with 'Status' as 'Completed' in a table
    if matching_rows:
        print(f"\nTable Display of Completed Transactions within {month}-{year}:")
        headers = ['Name', 'Services', 'Service Category', 'Date of Request', 'Status', 'Date of Completion',
                   'Description', 'Price']

        # Calculate the maximum width for each column
        column_widths = [max(len(header), max(len(row[header]) for row in matching_rows)) for header in headers]

        # Create a format string for the table
        format_string = ' | '.join(f'{{:<{width}}}' for width in column_widths)

        # Print the header row
        print(format_string.format(*headers))

        # Print the data rows
        for row in matching_rows:
            price_in_ringgit = "RM{:.2f}".format(float(row['Price']))
            row_data = [row['Name'], row['Services'], row['Service Category'], row['Date of Request'], row['Status'],
                        row['Date of Completion'], row['Description'], price_in_ringgit]
            print(format_string.format(*row_data))
        print("\nReturning to the main menu...")
    else:
        print("\nNo data matches your request. Returning to the main menu...")

# Password update codes
def update_password():
    def read_id_password_file():
        id_password_records = {}
        f = open("userpasslistrec.txt", "r")
        for line in f:
            id, password, roles = line.strip().split(",")
            id_password_records[id] = {'password': password, 'roles': roles}
        return id_password_records

    def id_password_verification(id_password_records, id_username, current_password, new_password):
        if id_username in id_password_records and id_password_records[id_username]['password'] == current_password:
            id_password_records[id_username]['password'] = new_password
            return True
        return False

    def new_password_alteration(id_password_records):
        f = open("userpasslistrec.txt", "w")
        for id_username, data in id_password_records.items():
            password = data['password']
            roles = data['roles']
            f.write(f"{id_username},{password},{roles}\n")

    def password_change_execution():
        if __name__ == "__main__":
            id_password_records = read_id_password_file()
            print("\nUpdate your password here.")
            id_username = input("Verify Employee ID or username: ")
            current_password = input("Verify current password: ")
            new_password = input("Enter new password: ")
            if id_password_verification(id_password_records, id_username, current_password, new_password):
                new_password_alteration(id_password_records)
                print("\nPassword updated successfully. Returning to main menu...")
            else:
                print("\nInvalid username or password. Returning to main menu...")
    password_change_execution()


# Administrator Main Menu Page Function
def administrator_menu_page(id_username):
    while True:
        print("\n***FloppaTech Administrator Menu***")
        print("[1] Register a new technician.")
        print("[2] Register a new receptionist.")
        print("[3] View monthly service report.")
        print("[4] View monthly total income.")
        print("[5] Update password.")
        print("[0] Log Out")

        option = int(input("Enter your option :"))
        match option:
            case 1:
                # Directs the administrator to add technician
                add_technician()
            case 2:
                # Directs the administrator to add receptionist
                add_receptionist()
            case 3:
                # Able to view monthly service report
                view_monthly_service_report()
            case 4:
                # Able to view monthly income
                view_monthly_income()
            case 5:
                # Directs the administrator to update password
                update_password()
            case 0:
                # Logs the administrator out and terminates the program
                break
            case _:
                # Asks the administrator to redo the input again as they've input an invalid value
                print("Invalid input. Please redo the input.")
    print(f"Thank you for logging in, {id_username}. Have a nice day!")
## End of Administrator Part

## Unified Login Page
# Prompts the user to either of these four based on their roles
def mainmenuprompt(id_username, username_password_record):
    if username_password_record[2] == "RECEPTIONIST":
        print(f"Welcome to FloppaTech Receptionist Menu, {id_username}!")
        receptionist_menu_page()
    elif username_password_record[2] == "TECHNICIAN":
        print(f"Welcome to FloppaTech Technician Menu, {id_username}!")
        technician_menu_page()
    elif username_password_record[2] == "CUSTOMER":
        print(f"Welcome to FloppaTech Customer Menu, {id_username}!")
        customer_menu_page()
    elif username_password_record[2] == "ADMINISTRATOR":
        print(f"Welcome to FloppaTech Administrator Menu, {id_username}!")
        administrator_menu_page(id_username)

# Login Page
def login():
    attemptmax = 3

    for attempt in range(1, attemptmax + 1):
        print("Welcome to FloppaTech.com! Please Login below.")
        print(f"*********Attempt #{attempt} *********")
        id_username = input("Please Enter your ID or Username: ")
        password = input("Please enter your Password: ")

        f = open("userpasslistrec.txt", "r")
        for line in f:
            username_password_record = line.strip().split(",")
            if id_username == username_password_record[0] and password == username_password_record[1]:
                print("Login Successful!")
                mainmenuprompt(id_username, username_password_record)
                return
        print("Login Failed!")
    print("You have reached the maximum login attempts allowed. Access is denied.")
login()