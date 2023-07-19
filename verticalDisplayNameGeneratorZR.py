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
print("Sonic's Vertical name Generator v.3.0")
print("-" * 97)
print("""Options: 
      1. EOL Method
      2. Line Separator Method
      3. Both""")


def setDisplayName(name):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Yang Liu\\Zombs Royale", 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, "displayName_h2033418264", 0, winreg.REG_BINARY, name)
    key.Close()

def make_ls_name(name):
    ls_char = b"\xE2\x80\xA8"
    display_name = b""

    for i, char in enumerate(name.encode('utf-8')):
                display_name += bytes([char])
                if i < len(name) - 1:
                    display_name += ls_char
    return display_name

def make_ls_name_custom(name, ls_indices):
    ls_char = b"\xE2\x80\xA8"
    display_name = b""
    index = 0

    for i, char in enumerate(name.encode('utf-8')):
        display_name += bytes([char])
        if index < len(ls_indices) and i == ls_indices[index]:
            display_name += ls_char
            index += 1
               
    return display_name

while True:
    try:
        method = int(input(">> "))
        if method == 1:
            name_input = input("Enter your display name: ")
            binary_data = bytes(f"{name_input}\x03", "utf-8")

            setDisplayName(binary_data)
            print(f"\nYour name has been updated to {name_input}" + " using the End of Line method.")

            break
        elif method == 2:
            
            print("\nOptions:")
            mode = int(input("      1. Default mode\n      2. Custom location\n>> "))
            if mode == 1:
                name_input = input("Enter your display name: ")
                ls_name = make_ls_name(name_input)
                setDisplayName(ls_name)

            elif mode == 2:
                name_input = input("Enter your display name: ")
                ls_indices_input = input("Enter the location where to put the line separator (e.g., 1,3,5): ")
                ls_indices = [int(i.strip()) for i in ls_indices_input.split(",")]

                ls_indices_diff = [num - 1 for num in ls_indices]

                ls_name = make_ls_name_custom(name_input, ls_indices_diff)
                setDisplayName(ls_name)

            else:
                print("Invalid input, please try again.")
                break
            
            print(f"\nYour name has been updated to {name_input}" + " using the Line Separator method. \n(Note: This method significantly reduces the amount of characters you can use in your name.)")

            break
        elif method == 3:
            
            name_input = input("Enter your display name: ")
            ls_name = make_ls_name(name_input)
            
            setDisplayName(ls_name + b"\x03")
            print(f"\nYour name has been updated to {name_input}" + " using both methods. \n(Note: The Line Separator method significantly reduces the amount of characters you can use in your name.)")
            break

        else:
            print("Invalid input, please try again.")
            break
    except ValueError:
        print("Invalid input, please try again.")
        break
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
        
input("\nPress enter to exit... ")
