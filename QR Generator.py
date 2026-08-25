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