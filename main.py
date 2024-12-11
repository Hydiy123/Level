from pychat import PyChat


# Create an instance of the PyChat class
window = PyChat()

# Set the title
window.title("My Custom PyChat Window")

# Set the size of the window
window.size(500, 500)

# Create and display the window
window.create_window()
