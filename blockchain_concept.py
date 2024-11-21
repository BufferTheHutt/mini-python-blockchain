#!/bin/python3

import hashlib
import json
import time
import os

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """
        Erzeugt den Hash des Blocks basierend auf seinem Inhalt.
        """
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        """
        Erstellt den ersten Block der Blockchain.
        """
        return Block(0, time.time(), "Genesis Block", "0")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        """
        Fügt einen neuen Block zur Blockchain hinzu.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        """
        Überprüft die Integrität der Blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print(f"Block {i} wurde manipuliert!")
                return False
            
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {i} hat eine falsche previous_hash!")
                return False
        
        return True

def hash_file(filepath):
    """
    Erzeugt den SHA-256-Hash einer Datei.
    """
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"Datei {filepath} nicht gefunden.")
        return None

# Beispielanwendung
if __name__ == "__main__":
    blockchain = Blockchain()
    filepath = "example.txt"  # Name der zu überprüfenden Datei

    # Erzeuge oder überprüfe die Datei
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            f.write("Dies ist ein Testinhalt.")
        print(f"Datei '{filepath}' erstellt.")
    
    # Erzeuge einen Block basierend auf dem Datei-Hash
    file_hash = hash_file(filepath)
    if file_hash:
        print(f"Hash der Datei '{filepath}': {file_hash}")
        blockchain.add_block(Block(1, time.time(), file_hash, blockchain.get_latest_block().hash))
    
    # Blockchain überprüfen
    print("Blockchain überprüfen...")
    if blockchain.is_chain_valid():
        print("Blockchain ist gültig!")
    else:
        print("Blockchain ist ungültig!")
