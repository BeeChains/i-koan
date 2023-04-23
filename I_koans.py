import random

# Updated and expanded list of koans with both 'I' and 'You' koans
koans = [
    "If you want to awaken all of humanity, then awaken all of yourself.",
    "The only way to see things as they truly are is to free oneself from all conditioning.",
    "To follow the path, look to the master, follow the master, walk with the master, see through the master, become the master.",
    "Before enlightenment, chop wood and carry water. After enlightenment, chop wood and carry water.",
    "The instant you speak about a thing, you miss the mark.",
    "It is not necessary to seek for what is true, but it is necessary to seek for what is false.",
    "The only Zen you find on the tops of mountains is the Zen you bring up there.",
    "You cannot travel the path until you have become the path itself.",
    "When you realize how perfect everything is, you will tilt your head back and laugh at the sky.",
    "Zen is not some kind of excitement, but concentration on our usual everyday routine.",
    "If you wish to know the truth, then hold to no opinions for or against anything.",
    "Everything that irritates us about others can lead us to an understanding about ourselves.",
    "If you think you are too small to make a difference, try sleeping with a mosquito.",
    "Be yourself. Everyone else is already taken.",
    "You have power over your mind - not outside events. Realize this, and you will find strength.",
    "Happiness is not something ready-made. It comes from your own actions.",
    "We don't see things as they are, we see them as we are.",
    "Don't let yesterday take up too much of today.",
    "The only true wisdom is in knowing you know nothing."
]

# Define a function to print a random koan from the list
def print_random_koan(koans_list):
    """
    Function to print a random koan from the list

    Args:
    koans_list: list of koans

    """
    if not koans_list:
        print("Oops! The list of koans is empty.")
        print("Please add some koans to the list.")
    else:
        print(random.choice(koans_list))

# taking input from the user to give the user the choice of inputting their own koans or if they want to stick with default one.
while True:
    try:
        user_input = int(input('Choose an option: \n1. Get a random koan from default list.\
    \n2. Input your own koans and get a random koan from the added list. \nOption: '))
        if user_input in [1,2]:
            break
        else:
            print("Invalid input!")
    except ValueError:
        print("Invalid input!")

if user_input == 1:
    # Call the function to print a random koan
    print_random_koan(koans)

elif user_input == 2:
    while True:
        # To take inputs from user until they are done
        new_koan = input("Enter your own koan (or stop to finish adding): ")
        if new_koan == "stop":
            break
        koans.append(new_koan)

    # Call the function to print a random koan from the updated koans list
    print_random_koan(koans)
