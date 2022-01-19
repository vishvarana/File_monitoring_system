import asyncio
import random
import string
from xml.dom import WrongDocumentErr

async def string_maker():
    n = 6
    s1 = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = n))
    list = [s1,"MARUTI"]
    return random.choice(list)

async def file_writer():
    f1 = open("file1.txt","a+")
    f2 = open("file2.txt","a+") 

    for i in range(100):
        result = await string_maker()
        f1.write(result + " ")
        result = await string_maker()
        f2.write(result+ " ")

    
async def worker_class():
    
    while(True):
        await file_writer()        

        file1 = open("file1.txt","r")
        file2 = open("file2.txt","r")
        file3 = open("count.log","w")
        data1 = file1.read()
        data2 = file2.read()

        n1 = data1.count("MARUTI")
        file3.write("Count for 'MARUTI' in file1 is " + str(n1) + "\n")

        n2 = data2.count("MARUTI")
        file3.write("Count for 'MARUTI' in file2 is " + str(n2))

        await asyncio.sleep(1)

if __name__=="__main__":
    asyncio.run(worker_class())
