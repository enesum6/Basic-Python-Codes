try:
    f=open("demofile.txt")
    try:
        f.write()
except:
        print("something went wrong when write to the file")
except:
        f.close()
except:
    print("something went wrong when open to the file")        
    