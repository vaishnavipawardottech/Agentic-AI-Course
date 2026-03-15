device_status = "active"
tempreature = 38

if device_status == "active":
    if tempreature > 35:
        print("High tempreature alert!")
    else:
        print("Tempreature is normal.")
else:
    print("Device is offline.")