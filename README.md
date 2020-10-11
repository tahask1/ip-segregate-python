# ip-segregate-python
A python script to help segregate a large list of IPs into smaller and better manageable lists

The idea for this came when I heard from a colleague that he was facing difficulty in segregating a large list of IPs into smaller lists to perform scanning with nmap. He had to manually copy paste the large IP list into smaller IP lists. This was an issue for many, including me.

Script is written using Python 2, running with Python 3 executable will give error.

It is preferred if the IP list is in the same directory as script. Else, specify the absolute path of the IP list without any "" even if there is a space between words in directory path. The same goes if the script is being run from the same directory as the IP list.

<h2>In short, DON'T use double quotes in "Name of list consisting all IPs: "</h2>


Example below:

C:\Python27>python.exe "C:\Users\test\Desktop\Python Scripts\Segregate IPs into list.py"

It is preferred if IP list is in same directory as script. Else specify the absolute path
of the IP list without any "" even if there is a space between words in directory path.


Total no. of IPs: 100

No. of IPs per list: 10

Name of list consisting all IPs: C:\Users\test\Desktop\Python Scripts\IP list.txt

Prefix for new list: list
