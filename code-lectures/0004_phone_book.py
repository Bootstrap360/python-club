# %%

# We will create a phone book to record contacts name, phone number and email by using OOP in this tutorial.

glen_number = 1234
glen_email = "123@sdfas.com"

tanya_number = 53145
tanya_email = "12sdf3@sdfas.com"

print("glen", glen_number, glen_email)
print("tanya", tanya_number, tanya_email)

# %%

# How do we add attributes

class Contact:
    def __init__(self, firstname, lastname, number, email):

        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.email = email.lower()

    # We use a dunder method __str__ here, then we could call this function by using str(<object>) and get the return
    def __str__(self):                 
        return f"Contact(firstname={self.firstname}, lastname={self.lastname}, number={self.number}, email={self.email})"

glen = Contact("Glen", "Turner", glen_number, glen_email)
tanya = Contact("Tanya", "Tang", tanya_number, tanya_email)

print(glen)      # print function will run str(glen) inside, which is the same as glen.__str__()
print(tanya)


# %%

# Add some more checks inside the constructor to make sure data is valid

class Contact:
    def __init__(self, firstname, lastname, number, email):
        
        # assert <condition>, "<message>". If condition return False, assert will drop error message "<message>"
        assert "@" in email, f"Invalid email address {email}"
        # isinstance method will return True if variable number is int type
        assert isinstance(number, int), f"Invalid phone number {number}. Must be an integer."

        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.email = email.lower()  # convert to lower case to make it look better
    
    def _setup_(self):
        pass

    def __str__(self):
        return f"Contact(firstname={self.firstname}, lastname={self.lastname}, number={self.number}, email={self.email})"

# Both of the two lines below will return error
glen = Contact("Glen", "Turner", "1234", glen_email)
tanya = Contact("Tanya", "Tang", tanya_number, "tanya_1234")

# %%

# Use inheritance to get free behavior. MotionMetricsContact is a specific version of a contact

class MotionMetricsContact(Contact):
    
    def __init__(self, firstname, lastname, number):
        email = f"{firstname}@motionmetrics.com"

        # super() here is the same thing as Contact. super().__init__() will initialize the variables for parent class.
        super().__init__(
            firstname=firstname, lastname=lastname, number=number, email=email,
        )
    
    def __str__(self):
        # super().__str__() here is the same as Contact.__str__()
        return "MotionMetrics " + super().__str__()


glen = MotionMetricsContact("Glen", "Turner", glen_number)

print(glen)
