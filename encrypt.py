from PIL import Image
import numpy as np

def convert_to_rgb(image):

    if image.mode in ['RGB', 'RGBA']:
        return image.convert('RGB')
    elif image.mode == 'L':  # Grayscale
        return image.convert('RGB')
    else:
        raise ValueError(f"Unsupported image mode: {image.mode}")

def encode_message(image, message):
    
    binary_message = ''.join([format(ord(char), '08b') for char in message])
    binary_message += '00000000'  # End-of-message delimiter (null character)

    pixels = np.array(image)
    h, w, _ = pixels.shape

    binary_index = 0
    for i in range(h):
        for j in range(w):
            for k in range(3):  # Iterate over R, G, B
                if binary_index < len(binary_message):
                    pixels[i, j, k] = (pixels[i, j, k] & 0xFE) | int(binary_message[binary_index])
                    binary_index += 1
                else:
                    break
    
    encoded_image = Image.fromarray(pixels)
    return encoded_image


def encrypt_image(input_image_path, scrambled_image_path, key_image_path, message=None):

    try:
        
        original_image = Image.open(input_image_path)
        original_image = convert_to_rgb(original_image)
        
        
        if message:
            original_image = encode_message(original_image, message)
        
        original_data = np.asarray(original_image)

        # Set a random key
        np.random.seed(42)
        key_data = np.random.randint(0, 256, size=original_data.shape, dtype=np.uint8)
        
        scrambled1_data = np.bitwise_xor(original_data, key_data)
        
        # Reversing RGB values
        scrambled1_data = 255 - scrambled1_data
        key_data = 255 - key_data
        
        # Save the images
        scrambled1_image = Image.fromarray(scrambled1_data)
        key_image = Image.fromarray(key_data)
        
        scrambled1_image.save(scrambled_image_path, "PNG")
        key_image.save(key_image_path, "PNG")
        print("Encryption complete. Images saved.")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_image_path}' was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":

    # Get message to hide from user
    message = input("Enter a message to hide in the image (leave blank for no message): ")
    encrypt_image("./Resources/input.png", "./Resources/scrambled1.png", "./Resources/scrambled2.png", message)
