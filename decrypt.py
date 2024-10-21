from PIL import Image
import numpy as np

def convert_to_rgb(image):
    if image.mode in ['RGB', 'RGBA']:
        return image.convert('RGB')
    elif image.mode == 'L':  # Grayscale
        return image.convert('RGB')
    else:
        raise ValueError(f"Unsupported image mode: {image.mode}")

def decode_message(image):

    pixels = np.array(image)
    h, w, _ = pixels.shape
    
    binary_message = ""
    for i in range(h):
        for j in range(w):
            for k in range(3):  # Iterate over R, G, B
                binary_message += str(pixels[i, j, k] & 1)
    
    binary_chunks = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ""
    for chunk in binary_chunks:
        if chunk == '00000000':  # End of message delimiter (null)
            break
        message += chr(int(chunk, 2))
    
    return message


def decrypt_image(scrambled_image_path, key_image_path, output_image_path):
    try:
        # Load and convert the scrambled images
        scrambled1_image = Image.open(scrambled_image_path)
        key_image = Image.open(key_image_path)
        scrambled1_image = convert_to_rgb(scrambled1_image)
        key_image = convert_to_rgb(key_image)
        
        scrambled1_data = np.asarray(scrambled1_image)
        key_data = np.asarray(key_image)
        
        # Reverse the RGB values back to original form
        scrambled1_data = 255 - scrambled1_data
        key_data = 255 - key_data
        
        # Decrypt the original image by XORing the two scrambled images
        original_data = np.bitwise_xor(scrambled1_data, key_data)
        
        # Save the restored image
        original_image = Image.fromarray(original_data)
        original_image.save(output_image_path, "PNG")
        
        # Decode and display the hidden message
        message = decode_message(original_image)
        print(f"Decryption complete. Image saved. Hidden message: {message}")
        
    except FileNotFoundError:
        print(f"Error: The file '{scrambled_image_path}' or '{key_image_path}' was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    decrypt_image("scrambled1.png", "scrambled2.png", "recovered.png")
