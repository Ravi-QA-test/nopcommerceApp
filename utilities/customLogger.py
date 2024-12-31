import logging

class LogGenerate:

    @staticmethod
    def loggen():
        # logging.basicConfig(filename=".\\Logs\\automation.Log",
        #                     filemode="w",
        #                     format='%(asctime)s: %(levelname)s: %(message)s',
        #                     datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='w')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger

# In above; inside, basicConfig() method, if filename is not explicitly specified,
# it means, by-default filemode ='a',
# Since we need to Re-Write the 'automation.log' file each time whenever test cases run,
# we specified filemode ='w'.

# Instead of, logging.basicConfig(), we can use logging.FileHandler()

# logging.FileHandler(filename=".\\Logs\\automation.Log",
#                     mode="w",
#                     format='%(asctime)s: %(levelname)s: %(message)s',
#                     datefmt='%m/%d/%Y %I:%M:%S %p')
