# Importing necessary dependencies
import nltk
from nltk.chat.util import Chat, reflections

# Downloading NLTK data if not already downloaded
# nltk.download('punkt')

# Define the chatbot responses for hotel-related inquiries
pairs = [
    [
        r"hi|hello|hey|greetings",
        ["Hello! Welcome to our hotel. How may I assist you?",]
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
        ["You can call me HotelBot.",]
    ],
    [
        r"(.*) your age?",
        ["I am just a chatbot, I don't have an age.",]
    ],
    [
        r"(.*) (book|reservation|reserve|room) (.*)",
        ["Sure, I can help you with that. Please provide your check-in and check-out dates and the type of room you prefer.",]
    ],
    [
        r"(.*) (types|available|availability) (.*)",
        ["We have various room types available including standard, deluxe, and suite rooms. Please let me know your preferences.",]
    ],
    [
        r"(.*) (price|cost) (.*)",
        ["The price depends on the type of room and the duration of your stay. Would you like me to provide specific pricing details?",]
    ],
    [
        r"(.*) (amenities|facilities) (.*)",
        ["Our hotel offers various amenities such as complimentary breakfast, gym access, and free Wi-Fi. Is there anything specific you would like to know about?",]
    ],
    [
        r"(.*) (restaurant|dining|food) (.*)",
        ["We have an on-site restaurant that serves a variety of cuisines. Would you like to make a reservation?",]
    ],
    [
        r"(.*) (location|address) (.*)",
        ["Our hotel is located at Near the Pune station. Is there anything else you would like to know?",]
    ],
    [
        r"(.*) (feedback|complaint) (.*)",
        ["We appreciate your feedback. Please let us know how we can improve our services.",]
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

# Creating the hotel chatbot
hotel_chatbot = Chat(pairs, reflections)

# Defining the conversation loop
def hotel_chat():
    print("Hello! Welcome to our hotel. How may I assist you?")
    print("Type 'quit' to exit.")
    print()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("\nThank you for visiting us. Have a great day!")
            break
        response = hotel_chatbot.respond(user_input)
        print("\nHotelBot: ", response)
        print()

# Starting the conversation with the hotel chatbot
if __name__ == "__main__":
    hotel_chat()
