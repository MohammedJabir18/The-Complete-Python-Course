import logging
import os
import google.generativeai as genai


def log_info():
    DIR_NAME = "Logs"
    FILE_NAME = "Application.log"

    os.makedirs(DIR_NAME, exist_ok=True)
    path = os.path.join(DIR_NAME, FILE_NAME)

    logging.basicConfig(
        format="[ %(asctime)s ] - %(levelname)s - %(message)s",  # Log format
        level=logging.INFO,  # Set the minimum log level to INFO
        datefmt="%d-%m-%Y %I:%M:%S %p",
        handlers=[
            logging.FileHandler(path),  # Log to a file
            logging.StreamHandler()  # Log to the console
        ]
    )

class NLPModel:
    def get_model(self):
        self.GOOGLE_API_KEY = "Here Give your API Key"
        try:
            genai.configure(api_key=self.GOOGLE_API_KEY)
            self.model = genai.GenerativeModel("gemini-1.5-flash")
            logging.info("Model initialized successfully.")
            return self.model
        except Exception as e:
            logging.error(f"An error occurred during API configuration {e}")
    
class NLPApp(NLPModel):
    def __init__(self):
        log_info()
        self.__database = {}
        self.model = self.get_model()
        logging.info("NLP app initialized.")
        self.first_menu()

    def first_menu(self):
        first_menu = input("""
                           Hi! How would you like to proceed?
                           
                            1. Not a member? Register
                            2. Already a member? Login
                            3. Exit
                           """).strip()
        if first_menu == "1":
            # Register
            self.__register()

        elif first_menu == "2":
            # Login
            self.__login() 

        elif first_menu == "3":
            logging.info("User choice to exit the application.")
            exit()
            
        else:
            logging.warning("Invalid entry in the first menu.")
            print("Invalid Entry!!!")
            self.first_menu()


    def __register(self):
        name = input("Enter your Name: ")
        email = input("Enter your Email: ")
        password  = input("Enter your Password: ")

        if email not in self.__database:
            self.__database[email] = [name, password]
            logging.info(f'New user registered {email}')
            print("Registration Successful!")
            self.first_menu()
        else:
            logging.warning(f"Registration failed: Email already exists - {email}")  # Log duplicate email
            print("Email is already exists.")
            self.first_menu()

    def __login(self):
        email = input("Enter your Email: ")
        password = input("Enter your password: ")

        if email in self.__database:
            if self.__database[email][1] == password:
                logging.info(f"User logged in: {email}")  # Log successful login
                print("Login Successful!")
                self.second_menu()

            else:
                logging.warning(f"Login failed: Incorrect password for {email}")  # Log incorrect password
                print("Incorrect Password!")
                self.__login()
        else:
            logging.warning(f"Login failed: Email not found - {email}")  # Log non-existent email
            print("Sorry! This Email not existing")
            register = input("Would you like to go registration page (y/n): ").lower()
            
            if register == "y":
                self.__register()
            else:
                self.first_menu()

    def second_menu(self):
        second_input = input("""
                            Hi! How would you like to proceed?
                            
                             1. Sentiment Analysis
                             2. Language Translation
                             3. Language Detection
                             4. Exit
                             """)
        
        if second_input == "1":
            self.__sentiment_analysis()
        
        elif second_input == "2":
            self.__language_translation()

        elif second_input == "3":
            self.__language_detect()
        
        elif second_input == "4":
            logging.info("User returned to the main menu.")  # Log return to main menu
            print("Returning to the main menu.")
            self.first_menu()

        else:
            logging.warning("Invalid entry in the second menu.")  # Log invalid entry
            print("Invalid Entry!!!")
            self.second_menu()

    def __sentiment_analysis(self):
        try:
            user_prompt = input("Enter your prompt: ")
            response = self.model.generate_content(f"Give me the sentiment of this sentence: \"{user_prompt}\"")
            print(response.text)
            logging.info(f"Sentiment analysis completed for: {user_prompt}")  # Log successful detection
            self.second_menu()

        except Exception as e:
            logging.error(f"Error during sentiment analysis: {e}")  # Log errors
            print("An error occurred during sentiment analysis.")
            self.second_menu()

    def __language_translation(self):
        try:
            user_prompt = input("Enter your prompt: ")
            translate = input("Which language to you want to translate: ")
            response = self.model.generate_content(f"Give me {translate} translation of this sentence: \"{user_prompt}\"")
            logging.info(f"Language translation completed for: {user_prompt}")  # Log successful detection
            print(response.text)
            self.second_menu()

        except Exception as e:
            logging.error(f"Error during language translation: {e}")  # Log errors
            print("An error occurred during language translation.")
            self.second_menu()

    def __language_detect(self):
        try:
            user_prompt = input("Enter your prompt: ")
            response = self.model.generate_content(f"Give me the language of this sentence: \"{user_prompt}\"")
            print(response.text)
            logging.info(f"Language detection completed for: {user_prompt}")  # Log successful detection
            self.second_menu()

        except Exception as e:
            logging.error(f"Error during language detection: {e}")  # Log errors
            print("An error occurred during language detection.")
            self.second_menu()


if __name__ == "__main__":
    nlp = NLPApp()
