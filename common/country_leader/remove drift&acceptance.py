import tkinter as tk
from tkinter import filedialog, messagebox
import os

def comment_drift_lines():
    # 隐藏主窗口
    root = tk.Tk()
    root.withdraw()

    # 文件选择对话框
    file_path = filedialog.askopenfilename(
        title="选择要处理的TXT文件",
        filetypes=[("Text files", "*.txt")]
    )

    if not file_path:
        messagebox.showinfo("提示", "未选择文件")
        return

    try:
        # 生成新文件路径
        base_name = os.path.splitext(file_path)[0]
        new_file_path = f"{base_name}_commented.txt"

        # 定义目标关键词列表
        keywords = ["democratic_drift", "communism_drift", 
                   "fascism_drift", "neutrality_drift", 
                   "democratic_acceptance", "communism_acceptance", 
                   "fascism_acceptance", "neutrality_acceptance"]

        # 逐行处理文件
        with open(file_path, 'r', encoding='utf-8') as infile, \
             open(new_file_path, 'w', encoding='utf-8') as outfile:
            
            for line in infile:
                # 检查是否包含任意关键词（不区分大小写）
                if any(keyword in line.lower() for keyword in keywords):
                    # 在行首添加#号注释
                    commented_line = f"#{line}"
                else:
                    commented_line = line
                outfile.write(commented_line)

        # 显示完成提示
        messagebox.showinfo(
            "完成", 
            f"处理完成！新文件已保存为：\n{new_file_path}"
        )

    except Exception as e:
        messagebox.showerror("错误", f"处理文件时发生错误：\n{str(e)}")

if __name__ == "__main__":
    comment_drift_lines()