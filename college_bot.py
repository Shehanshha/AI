# Importing necessary dependencies
import nltk
from nltk.chat.util import Chat, reflections

# Downloading NLTK data if not already downloaded
# nltk.download('punkt')

# Define the chatbot responses for hotel-related inquiries
pairs = [
    [
        r"hi|hello|hey|greetings",
        ["Hello! Welcome to our College. How may I assist you?",]
    ],
    [
        r"my name is (.*)",
        ["Hello %1! How can I assist you today?",]
    ],
    [
        r"(.*)how are you ?",
        ["I'm just a chatbot programmed to assist you. How can I help you?",]
    ],
    [
        r"(.*) your name?",
        ["You can call me CollegeBot.",]
    ],
    [
        r"(.*) your age?",
        ["I am just a chatbot, I don't have an age.",]
    ],
    [
        r"(.*) (pune|colleges) (.*)",
        ["COEP,PICT,VIT,CUMMINS,PCCOE",]
    ],
    [
        r"(.*) (engineering|branches) (.*)",
        [ "Computer Engineering,IT Engineering,ENTC Engineering",]
    ],
    [
        r"(.*) (coep|cut-offs) (.*)",
        ["COEP Cut-offs - Computer Engineering : 99.8 percentile,Does not have IT branch,ENTC Engineering: 99.2 percentile",]
    ],
    [
        r"(.*) (pict|cut-offs) (.*)",
        ["PICT Cut-offs - Computer Engineering : 99.4 percentile,IT Engineering : 98.6 percentile,ENTC Engineering: 97.2 percentile",],  

    ],
    [
        r"(.*) (vit|cut-offs) (.*)",
        ["VIT Cut-offs - Computer Engineering : 99.8 percentile,IT Engineering: 97.1 percentile",]
    ],
    [
        r"(.*) (cummins|cut-offs) (.*)",
        [
        "Cummins Cut-offs - Computer Engineering : 99.8 percentile,Does not have IT branch,ENTC Engineering: 99.2",],  
    ],
    [
        r"(.*) (pccoe|cut-offs) (.*)",
        [
        "PCCOE Cut-offs - Computer Engineering : 99.8 percentile,Does not have IT branch,ENTC Engineering: 99.2",], 
    ],
    [
        r"(.*) (entrance|exam)",
        ["CET and JEE is requried to take admission in the college",],
    ],
    [
        r"(.*) (admissions|start) (.*)",
        ["Admissions generally start around August",], 
    ],
    [
        r"thank you|thanks",
        ["You're welcome! If you need any further assistance, feel free to ask.",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I'm not sure how to assist you with that. Could you please provide more details?",]
    ]
]


hotel_chatbot = Chat(pairs, reflections)

# Defining the conversation loop
def hotel_chat():
    print("Hello! Welcome to our College. How may I assist you?")
    print("Type 'quit' to exit.")
    print()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("\nThank you for visiting us. Have a great day!")
            break
        response = hotel_chatbot.respond(user_input)
        print("\nCollegeBot: ", response)
        print()

# Starting the conversation with the hotel chatbot
if __name__ == "__main__":
    hotel_chat()
