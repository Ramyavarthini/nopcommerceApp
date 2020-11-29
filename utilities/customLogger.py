import logging


class LogGen:

    @staticmethod
    def loggen():
        print('***************INSIDE LOGGER*********')
        logging.basicConfig(filename='automation.log',
                            format='%(ascitime)s: %(levelname)s: %(message)s',
                            datefmt='%m%d%y %I%m%s %p',
                            filemode='w')
        print('** ** ** ** ** ** ** *INSIDE LOGGER1111 ** ** ** ** * ')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        print('** ** ** ** ** ** ** *INSIDE LOGGER22222 ** ** ** ** * ')
        return logger