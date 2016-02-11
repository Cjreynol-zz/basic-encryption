"""
Implementation of ciphers for CS:4640 Computer Security
Chad Reynolds
February 9, 2016
"""


if __name__ == "__main__":
    from helpers import *

    parser = parser_setup() 
    args = parser.parse_args()

    input_text = pre_process(args.input_text, args.no_spaces)
    algorithm = load_algorithm(args.algorithm, args.decrypt)
    key = load_key(args.key_file, args.algorithm)

    output_text = algorithm(input_text, key)

    print(output_text)
