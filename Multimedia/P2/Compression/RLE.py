s = "aaabbccc"


def encode_text(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


def decode_text(frequency):
    decoded_text = ""
    for char, freq in frequency.items():
        for i in range(freq):
           decoded_text += char
    return decoded_text


encoded_text = encode_text(s)
print(encoded_text)
decoded_text = decode_text(encoded_text)
print(decoded_text)