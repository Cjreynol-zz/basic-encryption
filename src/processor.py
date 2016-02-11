
class Processor():
    """
    Processes text for encryption.
    """
    def __init__(self):
        from string import ascii_lowercase
        self.letters = ascii_lowercase

    def preprocess_text(self, text):
        """
        1) Replace capital letters with lowercase letters.
        2) Remove punctuation marks
        3) Keep spaces
        """
        # 1
        text = text.lower()

        # 2
        new_text = ""
        for char in text:
            # only append lowercase letters+spaces to the processed plaintext
            if char in self.letters + ' ':
                new_text += char

        return new_text

    def preprocess_text_nospace(self, text):
        """
        Same as preprocess_text() but with no spaces
        """

        text = preprocess_text(text)
        new_text = ""
        for char in text:
            # only append lowercase letters to the processed plaintext
            if char in self.letters:
                new_text += char

        return new_text
