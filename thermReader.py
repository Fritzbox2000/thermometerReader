import time
import os
import glob

os.system("modprobe w1-gpio")
os.system("modprobe w1-therm")

base_dir = '/sys/bus/w1/devices/'
# get all the files names
device_folder = glob.glob(base_dir+'28*')[0]
device_file = device_folder + '/w1_slave'

def read_rom(device_folder) -> str:
    name_file=device_folder
    f=open(name_file,'r')
    return f.readline()

def read_temp_raw() -> list[str]:
    f=open(device_file,'r')
    lines=f.readlines()
    f.close()
    return lines

def read_temp() -> float:
    lines = read_temp_raw()
    try:
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
    except Exception as e:
        print(f"Oh no, something really broke \n{e}")
        return 0
    equal_pos = lines[1].find('t=')
    if equal_pos != -1:
        temp_string = lines[1][equal_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

if __name__ == "__main__":
    print('rom: '+ read_rom(device_file))
    while True:
        print(' C=%3.3f' % read_temp())
        time.sleep(1)

