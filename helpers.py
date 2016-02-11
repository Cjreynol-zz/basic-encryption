
def parser_setup():
    """
    Creates the argument parser.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="Encrypt/Decrypt text")

    parser.add_argument("input_text", type=str, 
                help="the filename of the input text")
    parser.add_argument("algorithm", type=str,
                help="the algorithm to use for encryption",
                choices=["vigenere", "permutation"])
    parser.add_argument("key_file", type=str,
                help="the file containing the key to use for the encryption")
    parser.add_argument("-n", "--no-spaces", 
                help="indicate if preprocessor should remove spaces", 
                action="store_true")
    parser.add_argument("-d", "--decrypt",
                help="indicate decryption instead of encryption",
                action="store_true")

    return parser

def pre_process(input_filename, no_spaces):
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

def load_algorithm(algorithm_name, decrypt):
    """
    Load the proper encryption/decryption function.
    """
    from vigenere import Vigenere
    from permutation import Permutation

    if algorithm_name == "vigenere":
        algorithm = Vigenere()
    elif algorithm_name == "permutation":
        algorithm = Permutation()
    else:
        raise RuntimeError("Chosen algorithm does not exist.")

    if decrypt:
        function = algorithm.decrypt_message
    else:
        function = algorithm.encrypt_message

    return function

def load_key(key_filename, algorithm_name):
    """
    Load the key and check to make sure the key is within parameters.
    """
    key = ""
    with open(key_filename, 'r') as key_file:
        key = key_file.read().strip()
        
        if algorithm_name == "permutation":
            key = key_to_permute_key(key)

    if len(key) > 7:
        raise RuntimeError("Key is too long, must be <= 7 characters.")

    return key

def key_to_permute_key(key):
    """
    Change key string to a list of integers like the permuation expects.
    """
    key = list(key)
    key_list = []
    for i in key:
        key_list.append(int(i))

    return key_list
