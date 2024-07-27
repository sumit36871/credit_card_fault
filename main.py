from credit_card.exception import CreditCardException
import os
import sys
from credit_card.logger import logging



def test_exception():
    try:
        logging.info("complete test")
        a=1/0
    except Exception as e:
        raise CreditCardException(e,sys)
    


if __name__ == "__main__":

    try:
        test_exception()
    except Exception as e:
        print(e)