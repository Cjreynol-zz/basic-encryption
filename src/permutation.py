"""
Implementation of ciphers for CS:4640 Computer Security
Chad Reynolds
Due:  February 22, 2016
"""


class Permutation():
    """
    Permutation cipher encrypt/decrypt.
    """
    def __init__(self):
        from string import ascii_lowercase
        self.alphabet = ascii_lowercase

    def encrypt_block(self, plaintext_block, key):
        """
        Permute the block of plaintext at plaintext_index using the key.
        """
        ciphertext = ""
        for index in key:
            ciphertext += plaintext_block[index]

        return ciphertext

    def decrypt_block(self, ciphertext_block, key):
        """
        Permute the block of ciphertext at ciphertext_index using the key.
        """
        plaintext = ""
        for index in range(len(key)):
            plaintext += ciphertext_block[key.index(index)]

        return plaintext
    
    def encipher_message(self, input_text, key, cipher_function):
        """
        Permute the input text block-by-block.
        """
        input_text = self.pad(input_text, key)
        input_text_index = 0
        
        output_text = ""
        while input_text_index < len(input_text):
            # get len(key) characters that are not spaces to encipher
            to_encipher = ""
            temp_index = input_text_index
            while len(to_encipher) < len(key):
                if input_text[temp_index] in self.alphabet:
                    to_encipher += input_text[temp_index]
                temp_index += 1

            # actual encipher step
            enciphered = cipher_function(to_encipher, key)

            # add the enciphered characters to the output string
            # go back through un-enciphered text to find space locations
            while input_text_index < temp_index:
                if input_text[input_text_index] in self.alphabet:
                    output_text += enciphered[0]
                    enciphered = enciphered[1:]
                else:
                    output_text += input_text[input_text_index]
                input_text_index += 1

        return output_text

    def encrypt_message(self, plaintext, key):
        """
        Permute the plaintext block-by-block.
        """
        ciphertext = self.encipher_message(plaintext, key, self.encrypt_block)
        return ciphertext

    def decrypt_message(self, ciphertext, key):
        """
        Permute the ciphertext block-by-block.
        """
        plaintext = self.encipher_message(ciphertext, key, self.decrypt_block)
        return plaintext

    def pad(self, plaintext, key):
        """
        Return the plaintext padded to be a length that divides evenly by 
        the length of the key.
        """
        remainder = (len(plaintext) - plaintext.count(' ')) % len(key)
        if remainder != 0:
            plaintext += (len(key) - remainder) * "q"

        return plaintext
