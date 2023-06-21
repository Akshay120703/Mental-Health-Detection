#Mental Health Detection
import pandas as pd

from google.colab import files
upload = files.upload()

dataset = pd.read_csv("/content/dataset.csv")

# Get the questions from the header row
questions = dataset.columns[:24]

# Function to interact with the chatbot
def chatbot():
    print("Welcome to the chatbot! Please answer the following questions with 'yes' or 'no'.")
    answers = []

    # Ask questions and gather user input
    for question in questions:
        answer = input(question + " (yes/no): ")
        while answer.lower() not in ["yes", "no"]:
            answer = input("Please answer with 'yes' or 'no': ")
        answers.append(answer.lower())

    # Count the number of "no" answers
    num_no = answers.count("no")

    # Check the 14th question to calculate Positivity
    if answers[13] == "yes":
        positivity = (num_no / 0.24) + 4.166
    else:
        positivity = (num_no / 0.24) - 4.166

    # Convert the user input into a single-row dataframe
    input_data = pd.DataFrame([answers], columns=questions)

    # Retrieve the corresponding output from the dataset
    output = dataset.iloc[:, 24][dataset.iloc[:, :24].eq(input_data.loc[0]).all(axis=1)]

    if len(output) > 0:
        print("Chatbot output: You are suffering from ", output.values[0])
    else:
        print("No matching output found.")

    print("Positivity:", positivity)
    print("%")

# Run the chatbot
chatbot()
