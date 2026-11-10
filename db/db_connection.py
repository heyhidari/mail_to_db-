"""
This file contains the connection string and 
other necessary elements for the data base in MongoDB to
function properly along with this app. 
"""
from os import getenv
from pymongo import MongoClient
from dotenv import load_dotenv

# Connection requirements
load_dotenv()

DB_CLIENT = getenv("CONNECTION_STR")

if not DB_CLIENT:
    raise ValueError("La variable de entorno DB_CLIENT no pudo ser asignada.")

myClient = MongoClient(DB_CLIENT)

db = myClient.expedientes_profesionales # Modify myClient.<db> to the desired database

def main():
    if connection_verificator():
        try: db.command("serverStatus")
        except Exception as e: print("\nHubo un error al conectarse debido a:\n\n", e)
        else:
            print("Connection test succesful, starting Client Connection:\n")
            
            # TEMPORARY CLOSE FOR DEVELOPING. Remove
            myClient.close()
    else:
        print("Falló la conexión al servidor de la DB")
        return


# Database connection verification function
def connection_verificator():
    try: db.command("serverStatus")
    except Exception as e: print("\nNo pudimos conectarnos debido a:\n\n", e)
    else: print("Estás conectado a MongoDB!\n These are the collections available:")

    # Print all collections
    print(db.list_collection_names())
    myClient.close
    return True


if __name__ == '__main__':
    main()
