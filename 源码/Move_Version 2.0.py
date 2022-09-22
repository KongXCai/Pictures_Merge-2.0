import os

Merge_dir = "./Merge"
if not os.path.exists(Merge_dir):
    os.makedirs(Merge_dir)
path=os.path.dirname(os.path.abspath(Merge_dir))
print(path)
i=1
print('请输入照片名称：')
name=input()
src_path1=path+'/First/'
src_path2=path+'/Second/'
target_path=path+'/Merge/'
filelist_src = os.listdir(src_path1)
format='.'+filelist_src[0].split(".")[-1]
for file in filelist_src:
    path1 = os.path.join(src_path1, file)
    path2 =os.path.join(target_path, name+str(i)+format)
    os.rename(path1,path2)
    i=i+1

filelist_src2 = os.listdir(src_path2)
format='.'+filelist_src2[0].split(".")[-1]
for file in filelist_src2:
    path1 = os.path.join(src_path2, file)
    path2 =os.path.join(target_path, name+str(i)+format)
    os.rename(path1,path2)
    i=i+1
