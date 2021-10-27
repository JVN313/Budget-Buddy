import datetime

x = datetime.datetime.now()
date = f"{x.month}-{x.day}-{x.year}"

new_file = open(f"new{date}.txt","w")
new_file.write("HI")
new_file.close()