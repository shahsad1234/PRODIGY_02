Image Encryption Tool

This is a simple image encryption tool that uses pixel manipulation to encrypt and decrypt images. It allows users to select an image, apply a basic mathematical operation to each pixel using a key, and save the encrypted or decrypted image.
Features

    Encrypt Images: Encrypts an image by adjusting RGB values of each pixel based on a user-provided key.
    Decrypt Images: Decrypts an encrypted image using the same key to retrieve the original image.
    User Interface: Built with Tkinter for a simple, interactive user experience.

How It Works

The program encrypts and decrypts images by modifying each pixel’s RGB values using a basic shift determined by the encryption key. This approach provides a basic level of security by scrambling the color values.
Prerequisites

    Python 3.6 or later
    Pillow: Python Imaging Library (PIL) to handle image processing.
    Tkinter: Standard Python library for creating graphical interfaces.

Installation

Clone this repository:

git clone https://github.com/shahsad1234/-PRODIGY_02-.git
cd -PRODIGY_02-

Install required packages:

pip install pillow

Usage

Run the program:

python image_encryption_tool.py

    Encrypt an Image:
        Enter a numeric key for encryption.
        Click "Encrypt Image" and choose an image file to encrypt.
        Choose the location and name for the output encrypted image file.

    Decrypt an Image:
        Enter the same numeric key used for encryption.
        Click "Decrypt Image" and select the encrypted image file.
        Choose the location and name for the output decrypted image file.

Example

    Encryption Example:
        Original image file: example.jpg
        Encryption key: 10
        Encrypted file saved as: encrypted_image.png

    Decryption Example:
        Encrypted image file: encrypted_image.png
        Decryption key: 10
        Decrypted file saved as: decrypted_image.png

Error Handling

    Invalid Key: If a non-integer key is entered, the program will display an error message.
    File Not Found: If an invalid file is selected or the file path does not exist, the program will alert the user.

Project Structure
Contributing

    Fork the repository.
    Create your feature branch (git checkout -b feature/YourFeature).
    Commit your changes (git commit -am 'Add new feature').
    Push to the branch (git push origin feature/YourFeature).
    Create a new Pull Request.

License

This project is licensed under the MIT License.
Acknowledgments

    Pillow (PIL) - Python Imaging Library
    Tkinter - Standard GUI library for Python
