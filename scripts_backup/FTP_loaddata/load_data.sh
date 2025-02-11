cd /homes/chunchieh/brain/data
lftp -e "set ftp:ssl-force true; set ssl:verify-certificate no" -u lee,AhLee7chacai ftp://140.114.95.82

# download entire folder:
mirror 20250120

bye