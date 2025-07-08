import hashlib
import json
import time

class Block:
    def __init__(self, index, participants, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.participants = participants
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        self.winner = self.pick_winner()

    def calculate_hash(self):
        block_data = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'participants': self.participants,
            'previous_hash': self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_data).hexdigest()

    def pick_winner(self):
        if not self.participants:
            return None
        winner_index = int(self.hash, 16) % len(self.participants)
        return self.participants[winner_index]

    def __repr__(self):
        return (
            f"🎲 Round #{self.index} | Participants: {len(self.participants)} | "
            f"Winner: {self.winner}\nHash: {self.hash[:20]}...\n"
        )

class LotteryBlockchain:
    def __init__(self):
        genesis = Block(0, [], "0")
        self.chain = [genesis]

    def add_block(self, participants):
        prev_hash = self.chain[-1].hash
        new_block = Block(len(self.chain), participants, prev_hash)
        self.chain.append(new_block)
        return new_block

    def print_chain(self):
        print("\n🧱 Full Lottery History:")
        for block in self.chain[1:]:  # Skip genesis block
            print(block)

# --- Interactive mode ---
if __name__ == "__main__":
    blockchain = LotteryBlockchain()

    while True:
        print("\n🎟️ Enter participant names for a new round (comma-separated), or type 'exit' to quit:")
        user_input = input("> ")

        if user_input.strip().lower() == "exit":
            break

        participants = [name.strip() for name in user_input.split(",") if name.strip()]

        if not participants:
            print("⚠️ No participants entered. Try again.")
            continue

        block = blockchain.add_block(participants)
        print(block)

    blockchain.print_chain()
