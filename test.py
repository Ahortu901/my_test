def decode(message_file):
    # Define the decoding algorithm
    def caesar_cipher_decode(text, shift):
        decoded_message = ""
        for char in text:
            if char.isalpha():
                # Calculate the shift amount
                shift_amount = shift % 26
                # Perform the decoding based on the Caesar cipher
                if char.islower():
                    decoded_char = chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
                elif char.isupper():
                    decoded_char = chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
            else:
                # Non-alphabetic characters remain unchanged
                decoded_char = char
            decoded_message += decoded_char
        return decoded_message

    # Assuming a shift of 3 for the Caesar cipher
    shift = 3

    try:
        # Open the file in read mode
        with open(message_file, 'r') as file:
            # Read the contents of the file
            encoded_message = file.read()
    except FileNotFoundError:
        return "File not found."

    # Decode the message using the Caesar cipher
    decoded_message = caesar_cipher_decode(encoded_message, shift)
    
    return decoded_message

# Example usage:
decoded_text = decode('encoded_message.txt')
print(decoded_text)
