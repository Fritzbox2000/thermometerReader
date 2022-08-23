import thermReader
import time
import os
import logging
import WebController

if __name__ == "__main__":

    logging.basicConfig(filename="./Crashlog.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger = logging.getLogger(__name__)
    fname = "data.csv"
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
            try:
                time_temp = f"{t[3]}:{t[4]},{thermReader.read_temp()}\n"
                f.write(time_temp)
                print(time_temp)
            except IndexError as e:
                logger.error(e)
            f.close()
            WebController.makePage()
            time.sleep(60 * 1)
    except Exception as e:
        print(e)
        logger.error(e)
    finally:
        print("Successfully safely closed")
        f.close()


