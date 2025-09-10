import streamlit as st
import base64
import urllib.parse
import hashlib

# -------------------------------
# Encoder / Decoder Functions
# -------------------------------
def base64_encoder(data):
    try:
        return base64.b64encode(data.encode("utf-8")).decode("utf-8")
    except Exception as e:
        return f" Error: {e}"

def base64_decoder(data):
    try:
        return base64.b64decode(data).decode("utf-8")
    except Exception as e:
        return f" Error: {e}"

def hex_encoder(data):
    try:
        return data.encode().hex()
    except Exception as e:
        return f" Error: {e}"

def hex_decoder(data):
    try:
        return bytes.fromhex(data).decode()
    except Exception as e:
        return f" Error: {e}"

def url_encoder(data):
    try:
        return urllib.parse.quote(data)
    except Exception as e:
        return f" Error: {e}"

def url_decoder(data):
    try:
        return urllib.parse.unquote(data)
    except Exception as e:
        return f" Error: {e}"

def caesar_cipher(data, shift):
    result = ""
    for char in data:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def vigenere_encoder(keyword, data):
    result = []
    keyword = keyword.lower()
    k_len = len(keyword)
    for i, char in enumerate(data):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(keyword[i % k_len]) - ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def vigenere_decoder(data, keyword):
    result = []
    keyword = keyword.lower()
    k_len = len(keyword)
    for i, char in enumerate(data):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(keyword[i % k_len]) - ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def MD5_encoder(data):
    return hashlib.md5(data.encode()).hexdigest()

def SHA1_encoder(data):
    return hashlib.sha1(data.encode()).hexdigest()

# -------------------------------
# Streamlit App
# -------------------------------
st.title("CipherVerse")

menu = [
    "Base64",
    "Hex",
    "URL",
    "ROT13",
    "Caesar Cipher",
    "Vigenere Cipher",
    "MD5",
    "SHA1",
    #"All at once",
]

choice = st.sidebar.selectbox("Choose an option", menu)
text = st.text_area("Enter your text here:")

if choice == "Base64":
    if st.button("Encode Base64"):
        st.code(base64_encoder(text))
    if st.button("Decode Base64"):
        st.code(base64_decoder(text))

elif choice == "Hex":
    if st.button("Encode Hex"):
        st.code(hex_encoder(text))
    if st.button("Decode Hex"):
        st.code(hex_decoder(text))

elif choice == "URL":
    if st.button("Encode URL"):
        st.code(url_encoder(text))
    if st.button("Decode URL"):
        st.code(url_decoder(text))

elif choice == "ROT13":
    if st.button("Apply ROT13"):
        st.code(caesar_cipher(text, 13))

elif choice == "Caesar Cipher":
    shift = st.slider("Shift", 1, 25, 3)
    if st.button("Apply Caesar Cipher"):
        st.code(caesar_cipher(text, shift))

elif choice == "Vigenere Cipher":
    keyword = st.text_input("Enter keyword:")
    if st.button("Encrypt with Vigenere"):
        st.code(vigenere_encoder(keyword, text))
    if st.button("Decrypt with Vigenere"):
        st.code(vigenere_decoder(text, keyword))

elif choice == "MD5":
    if st.button("Generate MD5"):
        st.code(MD5_encoder(text))

elif choice == "SHA1":
    if st.button("Generate SHA1"):
        st.code(SHA1_encoder(text))

# "Coming Soon"
# elif choice == "All at once":
#    if st.button("Run Encoding"):
#        st.markdown("### Encoding Results")
#        st.write("**Base64 Encode:**", base64_encoder(text))   
#       st.write("**Hex Encode:**", hex_encoder(text))    
#        st.write("**URL Encode:**", url_encoder(text))
#        st.write("**ROT13:**", caesar_cipher(text, 13))
#        st.write("**MD5:**", MD5_encoder(text))
#        st.write("**SHA1:**", SHA1_encoder(text))
#    if st.button("Run Decoding"):
#        st.markdown("### Decoding Results")
#        st.write("**Base64 Decode:**", base64_decoder(base64_encoder(text)))
#        st.write("**Hex Decode:**", hex_decoder(hex_encoder(text)))
#        st.write("**URL Decode:**", url_decoder(url_encoder(text)))
#        st.write("**ROT13:**", caesar_cipher(text, 13))







