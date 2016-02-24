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
        Permute the text, without spaces, block-by-block, then add spaces 
        back.
        """
        input_nospace_copy = input_text.replace(' ', '')
        input_nospace_copy = self.pad(input_nospace_copy, key)
        
        input_copy_index = 0

        output_nospace_text = ""
        while input_copy_index < len(input_nospace_copy):
            output_nospace_text += cipher_function(input_nospace_copy[input_copy_index:input_copy_index + len(key)] , key)
            input_copy_index += len(key)

        output_text = self.re_space(input_text, output_nospace_text)

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

    def re_space(self, input_text, output_nospace_text):
        """
        Return the output text with spaces in the same positions as in the 
        input text.
        """

        output_index = 0
        output_text = ""
        for char in input_text:
            if char == ' ':
                output_text += ' '
            else:
                output_text += output_nospace_text[output_index]
                output_index += 1

        return output_text
