try:
    file = open("school.txt", "r")
    print("File content:")
    print(file.read())

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected error:", e)

finally:
 
    try:
        file.close()
        print("File closed successfully.")
    except:
        print("File was not opened, so nothing to close.")
    print("Thank you for using the file reader program.")