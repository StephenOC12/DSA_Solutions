# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    _prime = 1000000007
    _multiplier = 263
    pattern_length = len(pattern)
    text_length = len(text)
    hash_pattern = 0
    hash_text = 0
    h = pow(_multiplier, pattern_length - 1) % _prime
    result = []

    for i in range(pattern_length):
        hash_pattern = (_multiplier * hash_pattern + ord(pattern[i])) % _prime
        hash_text = (_multiplier * hash_text + ord(text[i])) % _prime

    for i in range(0, text_length - pattern_length + 1):
        if hash_pattern == hash_text and text[i:i+pattern_length] == pattern:
            result.append(i)
        if i < text_length - pattern_length:
            hash_text = (_multiplier * (hash_text - ord(text[i]) * h) + ord(text[i + pattern_length])) % _prime

    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))