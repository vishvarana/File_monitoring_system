import asyncio
import random
import string

class File_writer:

    def __init__(self,file):
        self.file = file

    async def string_maker(self):
        n = 6
        s1 = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = n))
        list = [s1,"MARUTI"]
        return random.choice(list)


    async def writer(self):
        f = open(self.file,"a+")

        for i in range(100):
            result = await self.string_maker()
            f.write(result + " ")
    
class Counter:

    def __init__(self,file1,file2):
        self.file1 = file1
        self.file2 = file2

    def counter_class(self):
        f1 = open(self.file1,"r")
        f2 = open(self.file2,"r")
        counter = open("count.log","w")

        data1 = f1.read()
        data2 = f2.read()

        n1 = data1.count("MARUTI")
        n2 = data2.count("MARUTI")
        counter.write("Count for 'MARUTI' in {} is ".format(self.file1) + str(n1) + "\n")
        counter.write("Count for 'MARUTI' in {} is ".format(self.file2) + str(n2) + "\n")

if __name__=="__main__":

    while(True):
        writer1 = File_writer("file1.txt")
        writer2 = File_writer("file2.txt")
        counter = Counter("file1.txt","file2.txt")

        asyncio.run(writer1.writer())
        asyncio.run(writer2.writer())

        counter.counter_class()
