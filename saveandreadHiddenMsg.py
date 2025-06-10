# Save secret
with open("secret.txt", "w") as f:
    f.write("USTCtf{Hidden_Message}")

# Read secret
with open("secret.txt", "r") as f:
    print("Secret:", f.read())
