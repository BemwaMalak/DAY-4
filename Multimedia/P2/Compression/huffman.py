def frequency_analysis(data):
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequency):
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return heapq.heappop(priority_queue)

def generate_codes(node, current_code="", codes={}):
    if node is not None:
        if node.char is not None:
            codes[node.char] = current_code
        generate_codes(node.left, current_code + "0", codes)
        generate_codes(node.right, current_code + "1", codes)
    return codes

def encode_data(data, codes):
    encoded_data = ""
    for char in data:
        encoded_data += codes[char]
    return encoded_data

def decode_data(encoded_data, root):
    decoded_data = ""
    current_node = root
    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = root
    return decoded_data

# Example usage
text = "this is an example for huffman encoding"
frequency = frequency_analysis(text)
huffman_tree_root = build_huffman_tree(frequency)
codes = generate_codes(huffman_tree_root)

encoded_text = encode_data(text, codes)
print("Encoded Text:", encoded_text)

decoded_text = decode_data(encoded_text, huffman_tree_root)
print("Decoded Text:", decoded_text)
