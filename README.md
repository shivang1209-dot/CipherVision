# CipherVision - Image Encryption & Steganography

**CipherVision** is a powerful Python-based tool that lets you securely encrypt your images by splitting them into two noise-like grayscale images. It also adds an extra layer of secrecy by allowing you to hide a steganographic message inside the image, making it perfect for situations where secure and covert communication is required.

### How it works:
1. **Image Encryption:** CipherVision converts an input PNG or JPEG image into two seemingly random grayscale images that, when combined, can be used to recover the original image.
2. **Steganography:** Optionally, you can hide a secret message within the image during encryption. This message is encrypted in the least significant bits (LSB) of the pixel data.
3. **Decryption:** The two scrambled images are XORed together to recover the original image. Any hidden message can also be extracted during decryption.

---

## Features

- **Noise-looking Grayscale Splitting:** Your input image is split into two encrypted files, which look like random noise and provide no visual clue about the original image.
- **Secure Message Hiding:** Hide a message inside the image during encryption using steganography.
- **Lossless Recovery:** Decrypt the image by combining the two grayscale images, allowing for perfect recovery of the original image.
- **Flexible Formats:** Supports both PNG and JPEG image formats.

---

## How to Use

### Encryption

The encryption process breaks down your input image into two noise-like grayscale images. Optionally, you can also hide a message inside the encrypted images.

**Command:**
```bash
python encrypt.py
```

When prompted, enter the message you want to hide (or leave it blank if you don't want to hide any message). The program will generate two output images:

- **scrambled1.png/scrambled1.jpeg**: Contains part of the encrypted data.
- **scrambled2.png/scrambled2.jpeg**: Contains the key used to encrypt the image.

### Decryption

To recover the original image and reveal the hidden message (if one exists), run the decryption script.

**Command:**
```bash
python decrypt.py
```

This will regenerate the original image and reveal the hidden message (if provided) in the terminal.

---

## Setup

### Prerequisites

Make sure you have Python 3.x installed. You will also need the following Python libraries:

- **Pillow:** For image manipulation.
- **NumPy:** For pixel manipulation.

You can install the dependencies using pip:

```bash
pip install -r requirements.txt
```

### File Structure

Your project folder should have the following structure:

```
CipherVision/
│
├── Resources/
│   ├── input.jpeg             # Your input image
│   ├── scrambled1.jpeg         # First scrambled image (output)
│   ├── scrambled2.jpeg         # Second scrambled image (key) (output)
│   ├── recovered.jpeg          # Decrypted image (output)
│
├── encrypt.py                  # Encryption script
├── decrypt.py                  # Decryption script
├── README.md                   # You're here!
├── requirements.txt            # Required Python libraries

```

---

## Workflow

### Encryption

1. Convert your input image (PNG/JPEG) into RGB format, regardless of the original mode (grayscale, RGBA, etc.).
2. Optionally, embed a message using steganography (encoded in the least significant bits of the pixel values).
3. Generate a random key and scramble the image data using bitwise XOR.
4. Invert the pixel values to add an extra layer of visual obfuscation.
5. Save the scrambled image and the key image as grayscale PNG files.

### Decryption

1. Load the two grayscale images and invert the pixel values to restore their original form.
2. XOR the two scrambled images to reconstruct the original image.
3. Optionally, extract and display the hidden message from the image.

---

## Steganography - Encoding & Decoding

### Encoding

The steganographic message is hidden in the least significant bits (LSB) of the pixel data. Each character of the message is converted to its binary form and embedded into the image.

### Decoding

During decryption, the LSBs are scanned and the binary message is reassembled. The message ends when the delimiter `00000000` (null character) is found.

---

## Example

Let's walk through a simple example.

### 1. Encrypt an Image with a Secret Message

```bash
python encrypt.py
```
**Input:**  
- Input image: `input.jpeg/input.png`
- Message: "Top secret"

**Output:**  
- Encrypted images: `scrambled1.jpeg/scrambled1.png` and `scrambled2.jpeg/scrambled2.png`

### 2. Decrypt the Images

```bash
python decrypt.py
```

**Input:**  
- Scrambled images: `scrambled1.jpeg/scrambled1.png` and `scrambled2.jpeg/scrambled1.png`

**Output:**  
- Recovered image: `recovered.jpeg/recovered.png`
- Hidden message: "Top secret"

---

## Known Issues and Limitations
- **Image Size:** Larger images may take more time to process.
- **Message Size:** The maximum message length depends on the size of the image.
- **File Format:** Only works with PNG and JPEG formats.

---

## Future Enhancements
- **Support for More Image Formats:** Expand to other formats such as BMP, TIFF, etc.
- **Improved Message Encoding:** Implement stronger encoding schemes to increase message capacity.
- **Error Correction:** Add error correction to ensure that minor changes or corruption in the images don’t disrupt message decoding.

---

## Contribute

Found a bug? Want to improve the project? Feel free to open a pull request or an issue on GitHub. Contributions are welcome!

---

Enjoy the power of CipherVision!