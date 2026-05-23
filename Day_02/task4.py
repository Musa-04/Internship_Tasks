status_code = int(input("Enter API status code: "))

if status_code == 200:
    print("Success")
elif status_code == 404:
    print("Resource not found")
elif status_code == 500:
    print("Server error")
else:
    print("Unknown status")
