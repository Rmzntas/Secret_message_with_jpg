# Hidden Message With JPG

This project contains a sample application written in Python. This application allows you to embed a hidden message into a JPEG (JPG) file and extract the hidden message from the file.

## Usage

1. First, create a file named `main.py` in the same directory where the `secret.py` file containing the `Message` class is located.

2. Before using the application, ensure that the `PIL` (Python Imaging Library) library is installed. If it's not installed, you can install it using the following command:

    ```
    pip install pillow
    ```

3. Open the `main.py` file and follow these steps:

    a. Import the `Message` class from the `secret` module:

    ```python
    from secret import Message
    ```

    b. Create an instance of the `Message` class, specifying the path of the JPG file where you want to store the hidden message:

    ```python
    message = Message("image.jpg")  # Path to the JPG file
    ```
    
    c. Use the `read` method to extract the hidden message from the file:

    ```python
    message.read()
    ```

    d. Use the `write` method to embed the hidden message into the file:

    ```python
    message.write("Your Hidden Message")
    ```

    e. Use the `ReSeT` method to reset the file and delete the hidden message:

    ```python
    message.ReSeT()
    ```

4. After read, write or deleting message, you can use the application by running the `main.py` file:

    ```
    python main.py
    ```

## Notes

- Writing this message does not harm the jpg file.
- It only works on images in jpg format.


## License

This project is licensed under the [MIT License](LICENSE). For more information, you can refer to the license file.

---

Feel free to edit and customize this README template to fit your project's needs. By providing important information and instructions related to your project in the README file, you can help users understand and use your project more easily.
