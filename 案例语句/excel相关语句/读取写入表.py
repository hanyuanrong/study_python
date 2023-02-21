# import pandas as pd
# path = r"C:\Users\user\Desktop\结算报表.xlsx"   #路径名
# df1 = pd.read_excel(path)      #读取路径名
# print(df1)
# print(df1.shape[0])     #读取表的行数
# path1=r"C:\Users\user\Desktop\test.xlsx"
# df1.to_excel(path1, sheet_name="按大库分类统计", index=False)    #把df1文件写入到path1中，更改为指定的sheet名
#
# df1 = pd.read_excel(path,sheet_name = 0)  #读取path路径中指定sheet，0为索引，可以改为文件名

import pandas as pd
path = r"C:\Users\user\Desktop\结算报表.xlsx"   #路径名
df1 = pd.read_excel(path)      #读取路径名
# df1 = pd.read_excel(path,sheet_name = None) #不知道sheet的名字，然后读取所有的sheet
# for i in df1.keys():
#     df2 = pd.read_excel(path,sheet_name = i)
#     print(i)

#合并两列
df1["是否托管"] = df1["修理类型"] + df1["修理厂名称"]
print(df1)
df1.to_excel(r"C:\Users\user\Desktop\jiesuan.xlsx" , sheet_name="按大库分类统计", index=False)

#筛选
df2 = df1[df1["修理类型"] == "自费维修 "]    #筛选出修理类型为自费维修
df2.to_excel(r"C:\Users\user\Desktop\jiesuan1.xlsx" , sheet_name="按大库分类统计", index=False)

df3 = df1[df1["修理类型"].str.contains("进")]    #筛选出修理类型含“自”
df3.to_excel(r"C:\Users\user\Desktop\jiesuan2.xlsx" , sheet_name="按大库分类统计", index=False)

#拼接
list=[]
list.append(df2)
list.append(df3)
df4 = pd.concat(list)
# df4=df4.iloc[:,0]    #iloc取数，取所有行的第一列
# df4=df4.iloc[:,1]  #取所有行的第二列
# df4=df4.iloc[:,0:3]  #取所有行的0列，即第一列、第二列、第三列
df4=df4.iloc[0:2,0:3]  #取所有行的第一行、第二行，即第一列、第二列、第三列
df4.to_excel(r"C:\Users\user\Desktop\jiesuan3.xlsx" , sheet_name="按大库分类统计", index=False)

