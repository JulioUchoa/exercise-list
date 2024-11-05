file_name = input("File name: ")

file_name = file_name.strip(' ').lower()

if '.gif' in file_name:
    print("image/gif")

elif '.jpg' in file_name:
    print("image/jpeg")

elif '.jpeg' in file_name:
    print("image/jpeg")

elif '.png' in file_name:
    print("image/pgn")

elif '.pdf' in file_name:
    print("application/pdf")

elif '.txt' in file_name:
    print("text/plain")

elif '.zip' in file_name:
    print("application/zip")

else:
    print("application/octet-stream")