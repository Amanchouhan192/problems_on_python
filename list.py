def listC(mylist):
    "it is the function which help to modify the lit"
    mylist.append([1,2,3,4]);
    print"list inside the function " ,mylist
    return

mylist = [1,2,3,4,5]
listC(mylist);
print "Values outside the function: ", mylist
