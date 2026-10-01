from distro import name
import qrcode

url = input("Enter the URL to generate QR code: ")
data = name() + " " + url  # Combine the name and URL into a single string

# Create a QR code instance
file_path = "C:\\Users\\musta\\OneDrive\\Desktop\\py\\qr_images\\qr_code.png"  # Specify the file path to save the QR code image

qr = qrcode.QRCode()
qr.add_data(data)

img = qr.make_image(fill_color="black", back_color="white")
img.save(file_path)

print(f"QR code generated and saved as {file_path}") 
