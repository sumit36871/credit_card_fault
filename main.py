from credit_card.exception import CreditCardException
import os
import sys
from credit_card.logger import logging
from credit_card.utils2 import dump_csv_file_to_mongodb_collection



    


if __name__ == "__main__":
    file_path="C:/Projects/credit_card_fault/UCI_Credit_Card.csv"
    database_name="intern"
    collection_name ="credit_card_fault"
    dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

    