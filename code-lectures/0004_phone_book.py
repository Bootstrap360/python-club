number = 1234
address = "12 sdfsa street"
email = "123@sdfas.com"

# %%

glen_number = 1234
glen_email = "123@sdfas.com"

tanya_number = 53145
tanya_email = "12sdf3@sdfas.com"

print("glen", glen_number, glen_email)
print("tanya", tanya_number, tanya_email)

# How do we add attributes

# %%

class Contact:
    def __init__(self, firstname, lastname, number, email) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.email = email

glen = Contact("Glen", "Turner", 1234, "sdfsk@sdfalkj.com")
tanya = Contact("Tanya", "Tang", 1234, "sdfsk@sdfalkj.com")

print(glen)
print(tanya)

# %%

class Contact:
    def __init__(self, firstname, lastname, number, email) -> None:

        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.email = email.lower()

    def __str__(self):
        return f"Contact(firstname={self.firstname}, lastname={self.lastname}, number={self.number}, email={self.email})"

glen = Contact("Glen", "Turner", 1234, "sdfsk@sdfalkj.com")
tanya = Contact("Tanya", "Tang", 1234, "sdfsk@sdfalkj.com")

print(glen)
print(tanya)


# %%

# add some more checks inside the constructor to make sure data is valid

class Contact:
    def __init__(self, firstname, lastname, number, email) -> None:

        assert "@" in email, f"Invalid email address {email}"
        assert isinstance(number, int), f"Invalid phone number {number}. Must be an integer."

        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.email = email.lower()  # convert to lower case to make it look better
    
    def _setup_(self):
        pass

    def __str__(self):
        return f"Contact(firstname={self.firstname}, lastname={self.lastname}, number={self.number}, email={self.email})"


glen = Contact("Glen", "Turner", 1234, "glen@motionmetrics.com")
tanya = Contact("Tanya", "Tang", 1234, "tanya@motionmetrics.com")

# %%
# Use inheritance to get free behavior. MotionMetricsContact is a specific version of a contact

class MotionMetricsContact(Contact):
    
    def __init__(self, firstname, lastname, number) -> None:
        email = f"{firstname}@motionmetrics.com"

        super().__init__(
            firstname=firstname, lastname=lastname, number=number, email=email,
        )
    
    def __str__(self):
        return "MotionMetrics" + super().__str__()



glen = MotionMetricsContact("Glen", "Turner", 12123)

import inspect

print(Contact.__str__)
print(MotionMetricsContact.__str__)

print(glen)
print(tanya)

# %%



    

# %%
