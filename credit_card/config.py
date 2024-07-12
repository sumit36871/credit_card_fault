from dataclasses import dataclass
import os
import astra

@dataclass


class EnvironmentVariable:
    ASTRA_DB_URL:str = os.getenv("ASTRA_DB_URL")




env_var = EnvironmentVariable()

astra_client = astra.AstraClient(env_var.astra_db_url)