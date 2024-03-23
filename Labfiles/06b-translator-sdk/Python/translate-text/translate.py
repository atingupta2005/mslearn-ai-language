from dotenv import load_dotenv
import os

# import namespaces



def main():
    try:
        # Get Configuration Settings
        dotenv_path = os.path.expanduser('~/.env') 

        load_dotenv(dotenv_path)
        translatorRegion = os.getenv('TRANSLATOR_REGION')
        translatorKey = os.getenv('TRANSLATOR_KEY')

        # Create client using endpoint and key
        


        ## Choose target language



        # Translate text



    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()