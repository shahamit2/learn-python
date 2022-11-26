import logging
logging.basicConfig(filename="N_Logging.log", level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d-%m-%Y::%H-%M-%S')
#logging.basicConfig(filename="Logging.txt", level=logging.DEBUG)
logging.info("At line 5.")
logging.warning("At line 6.")
logging.debug("At line 7.")
logging.critical("At line 8.")
logging.error("At line 9.")
print("Complete")