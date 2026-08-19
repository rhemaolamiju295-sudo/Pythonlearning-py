# Execution pipeline

# An execution pipeline is simply a sequence of state transformations. Each step reads some part of the current state, does something with it, and produces a new state for the next step.

# The word pipeline is useful because it suggests data flowing through stages. At each stage, the data is changed in a specific way, just as crude oil is refined through different stages or rice is processed through milling, bagging, transporting, and selling.

# For example, a simple user login pipeline might look like this:

#     Take the user's email and password.
#     Find the stored password for that email.
#     Compare the entered password with the stored password.
#     If they match, set login_status to success.
#     If they do not match, set login_status to failure.
#     Send the login_status back to the user interface.

# Each step transforms the state. The email and password are part of the state. The stored password is part of the state. The login_status is new state created during the process.

user_mail = "rhemaolamiju295@proton.me"
user_password = "12345678"
email= input("Enter your Login email: ")
passowrd = input("Enter your Login password: ")


if email == user_mail and passowrd == user_password:
    login_status = "Login success"
    print(login_status)

else:
    login_status = "400: Invalid email or password"
    print(login_status)