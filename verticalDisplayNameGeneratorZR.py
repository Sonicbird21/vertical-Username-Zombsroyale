import winreg


print('''
    :::::::::         ::::::::        :::   :::        :::::::::       :::::::: 
          :+:       :+:    :+:       :+:+: :+:+:      :+:    :+:     :+:    :+: 
        +:+        +:+    +:+      +:+ +:+:+ +:+     +:+    +:+     +:+         
      +#+         +#+    +:+      +#+  +:+  +#+     +#++:++#+      +#++:++#++   
    +#+          +#+    +#+      +#+       +#+     +#+    +#+            +#+    
  #+#           #+#    #+#      #+#       #+#     #+#    #+#     #+#    #+#     
#########       ########       ###       ###     #########       ########       
    ''')

print("-" * 97)
print("Sonic's Vertical name Generator v.2.0")
print("-" * 97)
print("Please enter the name you want to have vertically: ")

name_input = input()
binary_data = bytes(f"{name_input}\x03", "utf-8")

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Yang Liu\\Zombs Royale", 0, winreg.KEY_ALL_ACCESS)

def setDisplayName(name):
    winreg.SetValueEx(key, "displayName_h2033418264", 0, winreg.REG_BINARY, name)

setDisplayName(binary_data)
print(f"Your name has been updated to {name_input}" + ".")
