import serial
def get_card():
    port = 465 
    ser = serial.Serial('COM3',9600)
    #time.sleep(2)
    b = ser.readline()
    str_rn = b.decode()
    str_rn = str_rn.strip()
    b = int(b)
    ser.close()
    return b
