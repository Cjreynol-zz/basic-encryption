"""                                                                               
Implementation of ciphers for CS:4640 Computer Security                           
Chad Reynolds                                                                     
Due:  February 22, 2016                                                           
"""  


class Vigenere():
    """
    Vigenere cipher for encryption/decryption
    """
    def __init__(self):
        from string import ascii_lowercase
        self.alphabet = ascii_lowercase

    def encrypt_char(self, plaintext_index, key_letter_index):
        """
        Ci = (Pi + Ki) % 26
        """
        return (plaintext_index + key_letter_index) % 26

    def decrypt_char(self, ciphertext_index, key_letter_index):
        """
        Pi = (Ci - Ki) % 26
        """
        return (ciphertext_index - key_letter_index) % 26
    
    def encrypt_message(self, plaintext, key):
        """
        Runs encrypt_char in a loop on the plaintext.
        """
        ciphertext = self.encipher_message(plaintext, key, self.encrypt_char)
        return ciphertext

    def decrypt_message(self, ciphertext, key):
        """
        Runs decrypt_char in a loop on the ciphertext.
        """
        plaintext = self.encipher_message(ciphertext, key, self.decrypt_char)
        return plaintext

    def encipher_message(self, input_text, key, cipher_function):
        """
        Manages calling cipher_function() repeatedly on entire input 
        to either encrypt of decrypt it.
        """
        key_index = 0
        output_text = ""

        for char in input_text:
            in_index = self.alphabet.find(char)
            if in_index == -1:
                output_text += char
            else:
                kl_index = self.alphabet.find(key[key_index])
                key_index = self.increment(key_index, key)
                output_text += self.alphabet[cipher_function(in_index, kl_index)]

        return output_text

    def increment(self, i, text):
        """
        Wrap around incrementing, defaults back to 0 if it falls off the
        end of the text.
        """
        i += 1
        if i >= len(text):
            i = 0
        return i
