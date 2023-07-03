import heapq
from collections import defaultdict


def build_huffman_tree(text):
    # محاسبه تعداد تکرار هر کاراکتر
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    # ساخت درخت هافمن با استفاده از صف اولویت
    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def encode_text(text, huffman_tree):
    huffman_dict = {char: code for char, code in huffman_tree}
    encoded_text = ''.join(huffman_dict[char] for char in text)
    return encoded_text


def decode_text(encoded_text, huffman_tree):
    huffman_dict = {code: char for char, code in huffman_tree}
    current_code = ""
    decoded_text = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in huffman_dict:
            decoded_text += huffman_dict[current_code]
            current_code = ""
    return decoded_text


def main():
    input_file_path = 'input.txt'
    compressed_file_path = 'input' + '.compressed'
    encoded_file_path = 'encoded.txt'

    # خواندن متن ورودی
    with open(input_file_path, 'r') as file:
        input_text = file.read()

    # ساخت کدگذار هافمن
    huffman_tree = build_huffman_tree(input_text)

    # رمزنگاری و ذخیره فایل فشرده شده
    encoded_text = encode_text(input_text, huffman_tree)
    with open(compressed_file_path, 'w') as file:
        file.write(encoded_text)

    # رمزگشایی و ذخیره فایل بازگشتی
    with open(compressed_file_path, 'r') as file:
        encoded_message = file.read()
    decoded_message = decode_text(encoded_message, huffman_tree)
    with open(encoded_file_path, 'w') as file:
        file.write(decoded_message)


if __name__ == '__main__':
    main()
