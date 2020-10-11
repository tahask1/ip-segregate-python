print """

It is preferred if IP list is in same directory as script. Else specify the absolute path
of the IP list without any "" even if there is a space between words in directory path.

"""
total_ips = input("Total no. of IPs: ")
ips_list = input("No. of IPs per list: ")
ip_list =  raw_input("Name of list consisting all IPs: ")
list_name = raw_input("Prefix for new list: ")

total_lists = (total_ips/ips_list) + (total_ips % ips_list > 0) + 1 #total lists to be created

with open(ip_list) as file1:                                        #open file1
    c = 0                                                           #initialize c to 0 so list ends at total no. of IPs provided
    for a in range(1, total_lists):                                 #for loop to create total_lists no. of lists
        with open("%s_%d.txt"%(list_name,a),"w+") as file2:         #open file2
            for b in range(ips_list):                               #for loop to create list with no. of ips_list
                output = file1.readline()                           
                if c < (total_ips):                                 #if condition to break loop when total no. of IPs is reached
                    file2.write(output)
                    c += 1
                else:
                    quit()