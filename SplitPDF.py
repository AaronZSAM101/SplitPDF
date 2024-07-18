
# Credit: Mengqiu Liu S240010 刘孟秋
# 2024.2.3
import fitz
import os

def split_pdf(input_path, output_folder):
    pdf_document = fitz.open(input_path)
    total_pages = pdf_document.page_count
    page_counter = 1

    for start_page in range(0, total_pages, 5):
        end_page = min(start_page + 4, total_pages)

        pdf_writer = fitz.open()
        pdf_writer.insert_pdf(pdf_document, from_page=start_page, to_page=end_page)

        output_file_path = os.path.join(output_folder, f"output_pages_{start_page + 1}_{end_page}.pdf")
        pdf_writer.save(output_file_path)

        print(f"Created: {output_file_path}")
        page_counter += 5

    pdf_document.close()

def rename_files(name_list_path, output_folder):
    with open(name_list_path, 'r') as name_file:
        names = name_file.readlines()

    for i, name in enumerate(names):
        input_file_path = os.path.join(output_folder, f"output_pages_{i * 5 + 1}_{(i + 1) * 5}.pdf")
        output_file_path = os.path.join(output_folder, f"{name.strip()}.pdf")

        try:
            os.rename(input_file_path, output_file_path)
            print(f"Renamed: {input_file_path} to {output_file_path}")
        except FileNotFoundError:
            print(f"Error: {input_file_path} not found.")


input_pdf_path = r'C:\Users\Capta\OneDrive\顺科\WORK\WIP\开发\SplitPDF\S30C-0i24020217260 - 副本.pdf'  # 替换为你的实际文件路径
output_pdf_folder = r'C:\Users\Capta\OneDrive\顺科\WORK\WIP\开发\SplitPDF\output'  # 替换为你的输出文件夹路径

split_pdf(input_pdf_path, output_pdf_folder)
print('Done.')