import os
packages_file = open("./packages.txt", "r")
packages = ""
for package in packages_file.readlines():
    package = package.replace("\n", "")
    packages += package
    packages += " "
packages_file.close()
#install aur repos
os.system(""" 
          cd ~ && mkdir gitclone && cd gitclone && pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si 
          """)

#install all needed packages and some personal softwares
os.system("yay -S --needed --no-confirm" + packages)

#mount partitions from another disks
#os.system("""
#          echo "UUID=2591c752-ceec-4691-8606-ad4d29bfd0d9/home/okarin/media/datas	ext4	defaults	0 2\nUUID=55a5a22d-eade-42e7-bd95-b1e86a8323ad	/home/okarin/media/programming	ext4	defaults	0 2\nUUID=eb48a74f-93e9-4bec-87d5-b4fe6ecb79a3	/home/okarin/media/school-subjects	ext4	defaults	0 2" >> /etc/test
#          """)


##done installation then reboot
print("installation has been done, reboot to complete install")
