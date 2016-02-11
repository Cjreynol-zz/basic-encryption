
class EncryptionManager():
    """
    Contains all of the functions to load the input text, key, and algorithm.
    """
    def __init__(self):
        parser = self.parser_setup() 
        args = parser.parse_args()

        input_text = self.pre_process(args.input_text, args.no_spaces)

        system = self.load_system(args.algorithm)
        algorithm = self.load_algorithm(system, args.decrypt)

        key = self.load_key(args.key_file, args.algorithm)
        self.check_key(key, args.algorithm)

        self.output_text = algorithm(input_text, key)
        

    def parser_setup(self):
        """
        Creates the argument parser.
        """
        import argparse
        
        parser = argparse.ArgumentParser(description="Encrypt/Decrypt text")

        parser.add_argument("input_text", type=str, 
                    help="the filename of the input text")
        parser.add_argument("key_file", type=str,
                    help="the file containing the key to use for the encryption")
        parser.add_argument("algorithm", type=str,
                    help="the algorithm to use for encryption",
                    choices=["vigenere", "permutation"])
        parser.add_argument("-n", "--no-spaces", 
                    help="indicate if preprocessor should remove spaces", 
                    action="store_true")
        parser.add_argument("-d", "--decrypt",
                    help="indicate decryption instead of encryption",
                    action="store_true")

        return parser

    def pre_process(self, input_filename, no_spaces):
        """
        Load text from file and pre-process it.
        """
        from processor import Processor

        processor = Processor()

        with open(input_filename, 'r') as text:
            input_text = text.read()
    
        if no_spaces:
            input_text = processor.preprocess_text_nospace(input_text)
        else:
            input_text = processor.preprocess_text(input_text)

        return input_text

    def load_algorithm(self, algorithm, decrypt):
        """
        Load the proper encryption/decryption function.
        """
        if decrypt:
            function = algorithm.decrypt_message
        else:
            function = algorithm.encrypt_message

        return function

    def load_system(self, algorithm_name):
        """
        Load the proper class containing requested algorithms.
        """
        from vigenere import Vigenere
        from permutation import Permutation

        if algorithm_name == "vigenere":
            algorithm = Vigenere()
        elif algorithm_name == "permutation":
            algorithm = Permutation()
        else:
            raise RuntimeError("Chosen algorithm does not exist.")

        return algorithm

    def load_key(self, key_filename, algorithm_name):
        """
        Load and format the key from its file.
        """
        with open(key_filename, 'r') as key_file:
            key = key_file.read().strip()
        
            if algorithm_name == "permutation":
                key = self.key_to_permute_key(key)

        return key

    def check_key(self, key, algorithm_name):
        """
        Check the key to ensure it falls within parameters.
        """
        if len(key) > 7:
            raise RuntimeError("Key is too long, must be <= 7.")

        if algorithm_name == "permutation":
            for i in range(len(key)):
                if i not in key:
                    raise RuntimeError("Key must contain all indexes in range.")

    def key_to_permute_key(self, key):
        """
        Change key string to a list of integers like the permuation expects.
        """
        key = list(key)
        key_list = []
        for i in key:
            key_list.append(int(i))

        return key_list

    def get_output_text(self):
        """
        Return the output text.
        """
        return self.output_text
