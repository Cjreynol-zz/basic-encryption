
class Permutation():
    """
    Permutation cipher encrypt/decrypt.
    """
    def encrypt_block(self, plaintext, plaintext_index, key):
        """
        Permute the block of plaintext at plaintext_index using the key.
        """
        ciphertext = ""
        for index in key:
            ciphertext += plaintext[plaintext_index + index]

        return ciphertext

    def decrypt_block(self, ciphertext, ciphertext_index, key):
        """
        Permute the block of ciphertext at ciphertext_index using the key.
        """
        plaintext = ""
        for index in range(len(key)):
            plaintext += ciphertext[ciphertext_index + key.index(index)]

        return plaintext
    
    def encipher_message(self, input_text, key, cipher_function):
        """
        Permute the input text block-by-block.
        """
        input_text = self.pad(input_text, key)
        input_text_index = 0
        
        output_text = ""
        while input_text_index < len(input_text):
            output_text += cipher_function(input_text, input_text_index, key)
            input_text_index += len(key)

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
        remainder = len(plaintext) % len(key)
        plaintext += (len(key) - remainder) * "q"

        return plaintext
