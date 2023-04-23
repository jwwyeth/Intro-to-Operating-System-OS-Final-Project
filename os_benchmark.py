import time 
import os

#start timer
start_time = time.perf_counter()


#will create 100 folders with 1000 files and write "cs3800 is the best class" to them
folder_num = 0
while folder_num < 50: 
    file_num = 0
    output_dir = "Directory" + str(folder_num)
    os.mkdir(output_dir)
    while file_num < 100: 
        path = str(output_dir) + "/text_file" +str(file_num)
        f = open(path,"w")
        f.write("CS3800 is the best class")
        f.close()
        file_num += 1
    folder_num += 1

end_time = time.perf_counter()
elasped_time = end_time - start_time 
f = open("output.txt","w")
f.write(str(elasped_time) + " time")
f.close()