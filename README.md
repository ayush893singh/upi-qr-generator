# UPI QR Code Generator
A simple Python script that generates a UPI QR code for instant payments.

## Technologies Used
Python 
qrcode library

## Installation
pip install qrcode[pil]

## How to Run
python upi_qr_generator.py

## How it Works
1. UPI ID, Name aur Note set hota hai
2. UPI URL generate hoti hai
3. Us URL ka QR code banta hai
4. QR code `upi_payment_qr.png` file mein save ho jaata hai

## Code
```Python
import qrcode

upi_id = "7080308932@naviaxis"
name = "AYUSH SINGH"
note = "Payment for Bill"

upi_url = (
    f"upi://pay?"
    f"pa={upi_id}&"
    f"pn={name}&"
    f"cu=INR&"
)

qr = qrcode.make(upi_url)
qr.save("upi_payment_qr.png")

print("UPI Payment Ready QR generated")
print("Save to file")
```
## ---- Output ----
Ek upi_payment_qr.png` file generate hoti hai
 Koi bhi UPI app (GPay, PhonePe, Paytm) se scan karke payment kar sakta hai

## Author
**Ayush Singh**  
GitHub: [@ayush893singh](https://github.com/ayush893singh)
