s="201811123028"
qiandaocishu = 0
with open('201811123028.log',encoding='utf8') as h :
     for line in h:
         line =line[14:26]
         if s==line:
             qiandaocishu =qiandaocishu +1

print(qiandaocishu)        