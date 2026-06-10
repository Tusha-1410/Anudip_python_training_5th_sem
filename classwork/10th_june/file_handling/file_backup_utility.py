# --------------------------------------------------
# File Backup Utility
# --------------------------------------------------

# Function to copy content from source file
# to destination file

def copy_file(source_file, destination_file):

    # Open source file in read mode
    file = open(source_file, "r")

    # Read complete content
    content = file.read()

    # Close source file
    file.close()

    # Open destination file in write mode
    file = open(destination_file, "w")

    # Write content into destination file
    file.write(content)

    # Close destination file
    file.close()

    # Display success message
    print("\nFile copied successfully.")
    print("All contents from '" + source_file +
          "' have been copied to '" +
          destination_file + "'.")


# --------------------------------------------------
# Main Program
# --------------------------------------------------

# Take file names from user

source_file = input("Enter Source File Name      : ")
destination_file = input("Enter Destination File Name : ")

# Call function
copy_file(source_file, destination_file)
