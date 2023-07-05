#new version(version 3.0)
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
    num_no = answers.count("yes")

    # Determine the stage of illness
    stage = ""
    if num_no < 7:
        stage = "Stage 1"
    elif num_no < 12:
        stage = "Stage 2"
    elif num_no < 17:
        stage = "Stage 3"
    elif num_no < 20:
        stage = "Stage 4"
    else:
        stage = "Stage 5"

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
        print("\nChatbot output:", output.values[0])
    else:
        print("\nChatbot output: Stress")

    print("Positivity:", positivity)
    print("Stage of illness:", stage)

# Run the chatbot
chatbot()
