# --------------------------------------------------
# Email Validation & Domain Analytics System
# --------------------------------------------------

# Dictionary to store domain counts for valid email addresses
domain_count = {}

# List to store invalid emails for later review
invalid_emails = []

# --------------------------------------------------
# Take 20 email addresses as input
for i in range(1, 21):

    print("\nEmail", i)
    email = input("Enter Email Address: ")

    print("\nEmail Analysis")

    # ------------------------------------------
    # Validation Check
    # A valid email must contain exactly one '@', contain at least one '.',
    # and must not include any spaces.
    valid = True

    if email.count("@") != 1:
        valid = False

    if "." not in email:
        valid = False

    if " " in email:
        valid = False

    # ------------------------------------------
    # If valid, perform analysis and update domain statistics
    if valid:

        # Extract username and domain from the email address
        username = email.split("@")[0]
        domain = email.split("@")[1]

        # Extract the file extension from the domain portion
        extension = domain.split(".")[-1]

        print("Username  :", username)
        print("Domain    :", domain)
        print("Extension :", extension)

        # --------------------------------------
        # Count digits in the username portion
        digit_count = 0

        for ch in username:
            if ch.isdigit():
                digit_count += 1

        print("Digits in Username :", digit_count)

        # --------------------------------------
        # Count special characters in the username portion
        special_count = 0

        for ch in username:
            if not ch.isalnum():
                special_count += 1

        print("Special Characters :", special_count)
        print("Email Status : Valid")

        # --------------------------------------
        # Count domain users for report generation
        if domain in domain_count:
            domain_count[domain] += 1
        else:
            domain_count[domain] = 1

    else:
        print("Email Status : Invalid")
        invalid_emails.append(email)

# --------------------------------------------------
# Display Invalid Emails
print("\n================================")
print("INVALID EMAILS")
print("================================")

for email in invalid_emails:
    print(email)

# --------------------------------------------------
# Domain Report
print("\n================================")
print("DOMAIN REPORT")
print("================================")

for domain in domain_count:
    print(domain, "->", domain_count[domain], "users")
