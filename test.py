def decode(message_file):
    try:
        # Read the contents of the file
        with open(message_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        return "File not found."

    # Initialize a dictionary to store words corresponding to pyramid numbers
    pyramid_words = {}

    # Populate the pyramid_words dictionary with words corresponding to pyramid numbers
    for line in lines:
        number, word = line.split()
        pyramid_words[int(number)] = word.strip()

    # Get the maximum number in the pyramid
    max_number = max(pyramid_words.keys())

    # Construct the decoded message using words corresponding to pyramid numbers
    decoded_message = " ".join(pyramid_words[num] for num in range(1, max_number + 1))
    # Write the decoded message to the output file
    with open(output_file, 'w') as file:
        file.write(decoded_message)
    return decoded_message

# Example usage:
decoded_message = decode('codng_qual_input.txt')
print(decoded_message)
