import time #time module
import random

sentences = [
    "This is the typing test code.",
    "A journey of a thousand miles begins with a single step.",
    "This is the way for us to reference the object of the class."
]

def measure_accuracy(user_input, test_sentence):
    if not test_sentence:
        return 0.0
    correct_chars = 0
    for i, char in enumerate(user_input):
        if i < len(test_sentence) and char == test_sentence[i]:
            correct_chars += 1
    return (correct_chars / len(test_sentence)) * 100


def typing_test():
    test_sentences = random.choice(sentences)
    print("Type the following sentences as fast as you can:")
    print(test_sentences)
    input("Press Enter when ready, then type: ")
    start_time = time.time() #Measures start time
    user_input = input("\nStart typing\n")
    end_time = time.time()
    time_taken = end_time - start_time
    time_taken_in_minutes = time_taken / 60
    word_count = len(test_sentences.split(" "))
    
    print("Results")
    print(f"Time taken: {time_taken} seconds")
    print(f"Words typed: {word_count}")
    typing_speed = word_count / time_taken_in_minutes
    print(f"Typing Speed: {typing_speed} words per minute")
    accuracy = measure_accuracy(user_input, test_sentences)
    print(f"Accuracy: {accuracy:.2f}%")
typing_test()