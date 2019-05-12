s="201811123028"
count = 0
with open(r'C:\Users\92507\Desktop\text-file-process-ProgramLove7\log_files/201811123028.log',encoding='utf8') as f :
     for line in f:
         line =line[14:26]
         if s==line:
             count =count +1

print(count)        