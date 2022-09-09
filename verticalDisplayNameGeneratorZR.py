import binascii

reg_default_text = "Windows Registry Editor Version 5.00"
reg_path = "[HKEY_CURRENT_USER\Software\Yang Liu\Zombs Royale]"
reg_display_name='"displayName_h2033418264"=hex:'


print('''
    :::::::::         ::::::::        :::   :::        :::::::::       :::::::: 
          :+:       :+:    :+:       :+:+: :+:+:      :+:    :+:     :+:    :+: 
        +:+        +:+    +:+      +:+ +:+:+ +:+     +:+    +:+     +:+         
      +#+         +#+    +:+      +#+  +:+  +#+     +#++:++#+      +#++:++#++   
    +#+          +#+    +#+      +#+       +#+     +#+    +#+            +#+    
  #+#           #+#    #+#      #+#       #+#     #+#    #+#     #+#    #+#     
#########       ########       ###       ###     #########       ########       
    ''')

print("-" * 60)
print("Sonic's Vertical name Generator v.1.0 (Currently only works when killing people or being killed!)")
print("-" * 60)

print("Please enter the name you want to have vertically: ")
name = input().encode("utf-8")


hexxed = binascii.hexlify(name)
decode = hexxed.decode()
string_hexxed = str(decode)

name_split = ",".join(string_hexxed[i:i + 2] for i in range(0, len(string_hexxed),2))


with open('verticalUsername_DoubleClickMe.reg', "w") as o:
	o.write(reg_default_text + "\n" + "\n" + reg_path + "\n" + reg_display_name + name_split + ",03")

print("Created Registry File, double click it to change your Username!")
