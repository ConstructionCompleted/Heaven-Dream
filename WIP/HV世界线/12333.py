import os
import sys
import pyradox as pyx

def append_to_txt_files():
    # 获取当前目录下所有txt文件
    txt_files = [f for f in os.listdir() if f.lower().endswith('.txt')]
    
    if not txt_files:
        print("⚠️ 未找到任何TXT文件")
        return

    # 处理每个文件
    for file_name in txt_files:
        file_path = os.path.abspath(file_name)
        try:
            with open(file_path, 'r+', encoding='utf-8') as f:
                content = f.read()
            pyxContent = pyx.parse(content)
            strContent = str(pyxContent)
            with open(file_path, 'w+', encoding='utf-8') as f:
                f.write(strContent)
            print(f"✅ 成功处理: {file_name}")
            
        except PermissionError:
            print(f"⛔ 无权限修改文件: {file_name}")
        except UnicodeDecodeError:
            print(f"⚠️ 文件编码异常（非UTF-8）: {file_name}")
        except Exception as e:
            print(f"❌ 处理 {file_name} 时发生错误: {str(e)}")

if __name__ == "__main__":
    append_to_txt_files()