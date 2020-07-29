Port1={21:"FTP" , 22:"SSH", 23:"telnet" , 80:"http"}
dict1=list(Port1.keys())
dict2=list(Port1.values())
Port2={dict2[each]:dict1[each] for each in range(len(dict1))}
print(Port2)
