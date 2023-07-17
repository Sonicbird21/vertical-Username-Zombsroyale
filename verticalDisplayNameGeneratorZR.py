import winreg


print("""
    :::::::::         ::::::::        :::   :::        :::::::::       :::::::: 
          :+:       :+:    :+:       :+:+: :+:+:      :+:    :+:     :+:    :+: 
        +:+        +:+    +:+      +:+ +:+:+ +:+     +:+    +:+     +:+         
      +#+         +#+    +:+      +#+  +:+  +#+     +#++:++#+      +#++:++#++   
    +#+          +#+    +#+      +#+       +#+     +#+    +#+            +#+    
  #+#           #+#    #+#      #+#       #+#     #+#    #+#     #+#    #+#     
#########       ########       ###       ###     #########       ########       
    """)

print("-" * 97)
print("Sonic's Vertical name Generator v.2.1")
print("-" * 97)
print("""Options: 
      1. EOL Method
      2. Line Seperator Method
      3. Both""")


def setDisplayName(name):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Yang Liu\\Zombs Royale", 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, "displayName_h2033418264", 0, winreg.REG_BINARY, name)
    key.Close()


while True:
    try:
        method = int(input(">> "))
        if method == 1:
            name_input = input("Enter your display name: ")
            binary_data = bytes(f"{name_input}\x03", "utf-8")

            setDisplayName(binary_data)
            print(f"Your name has been updated to {name_input}" + " using the End of Line method.")

            break
        elif method == 2:
            name_input = input("Enter your display name: ")

            ls_char = b"\xE2\x80\xA8"
            displayName = b""

            for i, char in enumerate(name_input.encode('utf-8')):
                displayName += bytes([char])
                if i < len(name_input) - 1:
                    displayName += ls_char
            
            setDisplayName(displayName)
            print(f"Your name has been updated to {name_input}" + " using the Line Seperator method. \n(Note: This method significantly reduces the amount of characters you can use in your name.)")

            break
        elif method == 3:
            name_input = input("Enter your display name: ")

            ls_char = b"\xE2\x80\xA8"
            displayName = b""

            for i, char in enumerate(name_input.encode('utf-8')):
                displayName += bytes([char])
                if i < len(name_input) - 1:
                    displayName += ls_char
            
            setDisplayName(displayName + b"\x03")
            print(f"Your name has been updated to {name_input}" + " using both methods. \n(Note: The Line Separator method significantly reduces the amount of characters you can use in your name.)")
            break

        else:
            print("Invalid input, please try again.")
    except ValueError:
        print("Invalid input, please try again.")

input("\nPress enter to exit...")
