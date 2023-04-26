import time 
import os

#start timer
start_time = time.perf_counter()

#will create 50 folders with 100 files and write "cs100800 is the best class" to them
folder_num = 0
while folder_num < 50: 
    file_num = 0
    output_dir = "Directory" + str(folder_num)
    os.mkdir(output_dir)
    while file_num < 100: 
        path = str(output_dir) + "/text_file" +str(file_num)
        f = open(path,"x")
        ''' f.write("CS100800 is the best class") '''
        f.close()
        file_num += 1
    folder_num += 1

end_time = time.perf_counter()
elasped_time = end_time - start_time 
f = open("output.txt","w")
f.write(str(elasped_time) + " time \n")
f.close()

start_write_time = time.perf_counter()
#write out to all files 
folder_num = 0
while folder_num < 50: 
    file_num = 0
    output_dir = "Directory" + str(folder_num)
    while file_num < 100: 
        path = str(output_dir) + "/text_file" +str(file_num)
        f = open(path,"w")
        f.write("CS3800 is the best class")
        f.close()
        file_num += 1
    folder_num += 1

end_write_time = time.perf_counter()
elasped_write_time = end_write_time - start_write_time 
f = open("output.txt","a")
f.write(str(elasped_write_time) + " write time \n")
f.close()


start_delete_time = time.perf_counter()
folder_num = 0
while folder_num < 50: 
    file_num = 0
    output_dir = "Directory" + str(folder_num)
    while file_num < 100: 
        path = str(output_dir) + "/text_file" +str(file_num)
        os.remove(path)
        file_num += 1
    folder_num += 1
    os.rmdir(output_dir)

end_delete_time = time.perf_counter() 
elasped_delete_time = end_delete_time - start_delete_time
f = open("output.txt","a")
f.write(str(elasped_delete_time) + " delete time")
f.close()
