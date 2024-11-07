from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def encrypt_image(input_image_path, output_image_path, key):
    try:
        image = Image.open(input_image_path)
        pixels = image.load()

        width, height = image.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                encrypted_r = (g + key) % 256
                encrypted_g = (r + key) % 256
                encrypted_b = (b + key) % 256

                pixels[x, y] = (encrypted_r, encrypted_g, encrypted_b)

        image.save(output_image_path)
        messagebox.showinfo("Success", f"Image encrypted and saved as {output_image_path}")

    except FileNotFoundError:
        messagebox.showerror("Error", f"The file {input_image_path} was not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def decrypt_image(input_image_path, output_image_path, key):
    try:
        image = Image.open(input_image_path)
        pixels = image.load()

        width, height = image.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                original_r = (g - key) % 256
                original_g = (r - key) % 256
                original_b = (b - key) % 256

                pixels[x, y] = (original_r, original_g, original_b)

        image.save(output_image_path)
        messagebox.showinfo("Success", f"Image decrypted and saved as {output_image_path}")

    except FileNotFoundError:
        messagebox.showerror("Error", f"The file {input_image_path} was not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def choose_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg"), ("All Files", "*.*")]
    )
    if file_path:
        label_selected_file.config(text=f"Selected File: {os.path.basename(file_path)}")
    return file_path

def handle_encrypt():
    input_image = choose_image()
    if input_image:
        output_image = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")]
        )
        try:
            key = int(entry_key.get())
            if 0 <= key <= 255:
                encrypt_image(input_image, output_image, key)
            else:
                messagebox.showerror("Error", "Please enter a key between 0 and 255.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for the encryption key.")

def handle_decrypt():
    input_image = choose_image()
    if input_image:
        output_image = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")]
        )
        try:
            key = int(entry_key.get())
            if 0 <= key <= 255:
                decrypt_image(input_image, output_image, key)
            else:
                messagebox.showerror("Error", "Please enter a key between 0 and 255.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for the decryption key.")

window = tk.Tk()
window.title("Image Encryption Tool")
window.geometry("450x300")
window.config(bg="#f7f7f7")

label_key = tk.Label(window, text="Enter Encryption Key (0-255):", font=("Arial", 12, "bold"), bg="#f7f7f7", fg="#333")
label_key.pack(pady=10)

entry_key = tk.Entry(window, font=("Arial", 12), width=20, bd=2, relief="solid", justify="center")
entry_key.pack(pady=10)

label_selected_file = tk.Label(window, text="No file selected", font=("Arial", 10), bg="#f7f7f7", fg="#666")
label_selected_file.pack(pady=10)

button_encrypt = tk.Button(window, text="Encrypt Image", font=("Arial", 12), width=20, height=2, bg="#4CAF50", fg="white", command=handle_encrypt, relief="raised", bd=2)
button_encrypt.pack(pady=10)

button_decrypt = tk.Button(window, text="Decrypt Image", font=("Arial", 12), width=20, height=2, bg="#FF6347", fg="white", command=handle_decrypt, relief="raised", bd=2)
button_decrypt.pack(pady=10)

window.mainloop()
