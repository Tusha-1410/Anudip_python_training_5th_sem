#program for battery level charging
charging_level = 20
electricity_status = True
while(charging_level <= 100):
    if(electricity_status):
        print("Battery level is at", charging_level, "%")
        charging_level += 10
    else:
        print("Electricity is not available. Please check the connection.")
        break
print("Battery is fully charged!") 