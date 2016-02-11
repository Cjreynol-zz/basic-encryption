
class Permutation():
    """
    Encrypts the plaintext by shuffling blocks of text using the key as a
    pattern for block length and the mapping for positions.
    """
    
    def pad(plaintext, key):
        """
        Return the plaintext padded to be a length that divides evenly by 
        the length of the key.
        """
        remainder = len(plaintext) % len(key)
        plaintext += remainder * "q"

        return plaintext

    def encrypt_block(plaintext, plaintext_index, key):
        """
        Permute the block of plaintext at plaintext_index using the key.
        """
        ciphertext = ""
        for index in key:
            ciphertext += plaintext[plaintext_index + index]

        return ciphertext

    def decrypt_block(ciphertext, ciphertext_index, key):
        """
        Permute the block of ciphertext at ciphertext_index using the key.
        """
        pass

    def encrypt_message(plaintext, key):
        """
        Permute the plaintext block-by-block.
        """
        plaintext = self.pad(plaintext, key)
        plaintext_index = 0
        
        ciphertext = ""
        while plaintext_index < len(plaintext):
            ciphertext += encrypt_block(plaintext, plaintext_indext, key)
            plaintext_index += len(key)

        return ciphertext

    def decrypt_message(ciphertext, key):
        """
        Permute the ciphertext block-by-block.
        """
        pass

