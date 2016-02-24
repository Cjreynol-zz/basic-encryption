#!/usr/bin/env python3
"""
Implementation of ciphers for CS:4640 Computer Security
Chad Reynolds
Due:  February 22, 2016
"""


if __name__ == "__main__":
    from manager import EncryptionManager

    encryption_manager = EncryptionManager()
    output_text = encryption_manager.get_output_text()

    print(output_text)

