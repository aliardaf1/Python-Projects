file = input("File name:")
file_new = file.lower()

if ".jpg" in file_new:
    print("image/jpeg")
elif ".jpeg" in file_new:
    print("image/jpeg")
elif ".gif" in file_new:
    print("image/gif")
elif ".png" in file_new:
    print("image/png")
elif ".pdf" in file_new:
    print("application/pdf")
elif ".txt" in file_new:
    print("text/plain")
elif ".zip" in file_new:
    print("application/zip")
else :
    print("application/octet-stream")
