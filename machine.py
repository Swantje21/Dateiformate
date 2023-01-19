text = input("Enter the text: ")
char = input("Enter the character you want to escape: ")

escaped_text = text.replace(char, "\\" + char)

print(escaped_text)
