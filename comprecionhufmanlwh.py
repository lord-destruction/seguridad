import heapq
from collections import Counter, namedtuple
import sys
import time

# ========== HUFFMAN IMPLEMENTATION ==========

class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_counter = Counter(text)
    heap = [Node(char, freq, None, None) for char, freq in freq_counter.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_codes(node, prefix="", codebook={}):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encode(text, codebook):
    return ''.join(codebook[char] for char in text)

def huffman_decode(encoded_text, tree):
    decoded = []
    node = tree
    for bit in encoded_text:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            decoded.append(node.char)
            node = tree
    return ''.join(decoded)

# ========== LZW IMPLEMENTATION ==========

def lzw_compress(uncompressed):
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}
    w = ""
    result = []

    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    if w:
        result.append(dictionary[w])
    return result

def lzw_decompress(compressed):
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}
    w = chr(compressed.pop(0))
    result = [w]

    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError("Código inválido: %s" % k)

        result.append(entry)
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry

    return ''.join(result)

# ========== MAIN COMPARISON SCRIPT ==========

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python compare_huffman_lzw.py <ruta_archivo>")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    print("\n📂 Archivo leído:", file_path)
    print("📏 Tamaño original (caracteres):", len(text))

    # --- HUFFMAN ---
    start_huffman = time.time()
    tree = build_huffman_tree(text)
    codebook = build_codes(tree)
    encoded_huff = huffman_encode(text, codebook)
    decoded_huff = huffman_decode(encoded_huff, tree)
    end_huffman = time.time()

    print("\n🔷 Huffman Compression")
    print("   ➡️ Tamaño comprimido (bits):", len(encoded_huff))
    print("   ✅ Coincide decodificado con original:", decoded_huff == text)
    print("   ⏱️ Tiempo de ejecución: {:.4f} segundos".format(end_huffman - start_huffman))

    # --- LZW ---
    start_lzw = time.time()
    compressed_lzw = lzw_compress(text)
    decompressed_lzw = lzw_decompress(compressed_lzw.copy())
    end_lzw = time.time()

    print("\n🔶 LZW Compression")
    print("   ➡️ Tamaño comprimido (número de códigos):", len(compressed_lzw))
    print("   ✅ Coincide decodificado con original:", decompressed_lzw == text)
    print("   ⏱️ Tiempo de ejecución: {:.4f} segundos".format(end_lzw - start_lzw))

    # --- CONCLUSION ---
    print("\n✅ Comparación final completada.\n")
