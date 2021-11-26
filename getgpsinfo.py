import serial
import time

def getinfo():
    i =0 
    while i<8:
        try:
            ser = serial.Serial("/dev/serial0",9600) 
            line = str(ser.readline())
            print(line)
            print('successfully got info')
            if line.startswith("b\'$GPGLL"):
                print('GPGLL get >>>>>>>>>>>>>>>>>>>>>>>')
                data = str(line).split(',')
                print(data)
                if data[1] != '' and data[3] != '':
                    longitude = float(data[3])/100
                    latitude = float(data[1])/100
                    gpsdata=[longitude,latitude]
                    return gpsdata
        except:
            return []
        i=i+1


         