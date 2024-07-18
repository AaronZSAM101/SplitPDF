# Credit: Mengqiu Liu S240010 刘孟秋
# 2024.2.3
import os

# 函数定义：提取数字部分。该部分针对提取后的文件中包含数字的进行处理。
def extract_number(filename):
    # 从文件名中提取数字部分
    return int(''.join(filter(str.isdigit, filename)))

# 读取list.txt文件内容，生成列表
NAMElistpath = r'C:\Users\Capta\Desktop\SplitPDF\name_list.txt' # 在引号中输入list文件的路径
with open(NAMElistpath, 'r', encoding='utf-8') as list_file:
    pdf_list = [line.strip() for line in list_file.readlines()]

# 获取目标文件夹中的PDF文件列表，并按数字顺序排序
pdf_folder = r'C:\Users\Capta\Desktop\SplitPDF\output' # pdf存在的文件夹路径
pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith('.pdf')]
pdf_files.sort(key=extract_number)

# 使用字典构建映射关系，根据list.txt的顺序与PDF文件对应
pdf_mapping = {}
for i, pdf_filename in enumerate(pdf_files):
    if i < len(pdf_list):
        pdf_mapping[pdf_list[i]] = pdf_filename
    else:
        print("list.txt 中的行数不足以覆盖目标目录中的所有PDF文件。")

# 遍历list.txt中的名称，并根据映射关系重命名PDF文件
for name in pdf_list:
    if name in pdf_mapping:
        old_pdf_path = os.path.join(pdf_folder, pdf_mapping[name])
        new_pdf_path = os.path.join(pdf_folder, name + '.pdf')
        
        os.rename(old_pdf_path, new_pdf_path)
        print("处理文件 {0}".format(new_pdf_path))
    else:
        print("无法找到与 {0} 相关的PDF文件。".format(name))