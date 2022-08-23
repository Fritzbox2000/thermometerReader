import thermReader
import time
import os

fname = "data.csv"
if __name__ == "__main__":
    # check if the file exits, if it doesn't create it
    if not os.path.exists(fname):
        print(f"Creating {fname}")
        f = open(fname,"w")
        f.write("time,heat\n")
        f.close()
    try:
        while True:
            f = open(fname, "a")
            t = time.gmtime()
            time_temp = f"{t[3]}:{t[4]},{thermReader.read_temp()}\n"
            f.write(time_temp)
            print(time_temp)
            f.close()
            time.sleep(60 * 1)
    finally:
        print("Successfully safely closed")
        f.close()


