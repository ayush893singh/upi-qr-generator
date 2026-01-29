# upi-qr-generator
import qrcode

upi_id = "7080308932@naviaxis"        
name = "Ayush Singh"          
note = "Payment for Bill"  
upi_url = (
    f"upi://pay?"
    f"pa={upi_id}&"
    f"pn={name}&"
    f"cu=INR&"
    f"tn={note}")

qr = qrcode.make(upi_url)
qr.save("upi_payment_qr.png")

print("UPI qr for Ready: upi_payment_qr.png")
