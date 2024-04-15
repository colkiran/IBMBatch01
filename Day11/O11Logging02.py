

import logging

logging.basicConfig(filename="mylogfile.log", filemode="a",
                    level=logging.DEBUG,
                format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

def diff(x, y):
    return x - y

a = 10
b = 20
logging.debug(f"the difference of {a} and {b} is :{a - b}")
logging.info(f"the difference of {a} and {b} is :{a - b}")

a = 10
b = 20
logging.warning(f"the difference of {a} and {b} is :{a - b}")

a = 10
b = 20
logging.error(f"the difference of {a} and {b} is :{a - b}")
logging.critical(f"the difference of {a} and {b} is :{a - b}")