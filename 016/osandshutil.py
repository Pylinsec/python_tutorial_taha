import os
#_____________________________
#mkdir()  make directory  feqat dar mesir dade shode darsorat vojood
#os.mkdir("dir1/taha/pythoncourse")
#os.mkdir("h:/BBBBBB")
#os.mkdir("h:\BBBBBBA\CCCC")
#os.mkdir("../../tahaback")
#print('\')
#__________________________________________________
#makedirs nested  to ar to   yani ta akhar khodat hame ra besaz 
#os.makedirs("program\\adobe\\phtoshop1")
#dar linux va mac jodakonnadeh / ast vali dar windows \ ast ke ma az \\ estefadeh mikonim
#os.makedirs("..\\..\\program\\adobe\\phtoshop1")
#for i in range(5):
    #os.makedirs(f"jam\\taha {str(i)}")
#____________________________________________________________________
#remove file  os.remove feqat file ra hazf minemayad
#with open("test.txt","a"):
    #pass
#os.remove("H:\\BBBBBBA\\CCCC\\23.docx")  # in remove mikonad file ra albateh dae mesir dadeshode
#___________________________________________________
#rmdir() feqat dar mesir dadeshode hazf mikonad be sharti khali bashad
#os.rmdir("11\\12")
#___________________________________________________________
#removedirs()  foldaer haye to dar to ra betartib hazf mikonad albeteh khali bayad bashad
#os.removedirs("12\\11")
#_____________________________________________
#listdir() avardan temam filha va dirs
list= os.listdir("12")
print(list)
for item in list:
    print(item)
    if os.path.isfile(f"12\\{item}"):
        os.remove(f"12\\{item}")
    else:
        os.rmdir(f"12\\{item}")
#_______________________________________________________    
#path.join()
#print(os.path.join("thah","python","reza"))
#_________________________________________________
#path.exists() agar file bood true bargardan
#print(os.path.exists("12"))
#_______________________________________
#path.getsize() size file bar migardanad
#print(os.path.getsize("13.mp4"))
#________________________________________________________
#rename("sourcefile","destinationfile")  move va rename anjam midehad
#os.rename("havij.mp4","12\\havij12.mp4")
#print(list)
#for item in list:
#    os.rename(f"{item}",f"12")
#_____________________________________
#getcwd() current working directory
#print(os.getcwd())
#__________________________________

#chdir()  change directory  tagiir mesir pishfarz
#os.chdir("12")
#print(os.getcwd())
#___________________________________________________
#path.isfile() agar file bood true bargardan 
#path.isdirs() agar dir bood true bargardan

