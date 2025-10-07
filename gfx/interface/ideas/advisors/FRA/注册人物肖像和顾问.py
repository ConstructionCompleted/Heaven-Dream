import os
import glob
import sys
import re
import msvcrt

def get_platform_anykey():
    print("按任意键退出...")
    msvcrt.getch()

def main():
    TAG = check_dir_name()

    """收集当前目录下.dds和.png文件名（不含后缀）并写入文本文件"""
    # 获取目标文件并去除后缀
    dds_files = [os.path.splitext(f)[0] for f in glob.glob('*.dds')]
    png_files = [os.path.splitext(f)[0] for f in glob.glob('*.png')]
    all_files = dds_files + png_files

    """主菜单控制函数"""
    # 创建函数映射字典
    function_map = {
        '1': write_characters,
        '2': write_advisors
    }
    
    while True:
        # 显示菜单选项
        print("\n" + "="*30)
        print("命令行功能菜单")
        print("="*30)
        print("1. 注册角色大肖像")
        print("2. 注册顾问小肖像")
        print("="*30)
        
        # 获取用户输入
        choice = input("请选择操作 (1/2): ").strip()
        
        # 处理用户选择
        if choice in function_map:
            function_map[choice](TAG, all_files)  # 执行对应函数
            get_platform_anykey()  # 等待任意键退出
            return
        else:
            print(f"错误：无效选择 '{choice}'，请重新输入！")
    

def check_dir_name():
    # 获取当前脚本所在目录的绝对路径[2,4](@ref)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 提取当前目录的文件夹名[5](@ref)
    folder_name = os.path.basename(script_dir)
    print(f"当前目录名称: {folder_name}")
    
    # 验证目录名格式[7,8](@ref)
    if len(folder_name) != 3:
        print(f"错误：目录名长度必须为3个字符（当前长度：{len(folder_name)}）")
        sys.exit(1)
    
    # 验证字符组成（大写字母+数字）[6,7](@ref)
    if not re.fullmatch(r'[A-Z0-9]{3}', folder_name):
        invalid_chars = [c for c in folder_name if not c.isalnum()]
        print(f"错误：目录名只能包含大写字母和数字（非法字符：{invalid_chars}）")
        sys.exit(1)
    
    # 存储并输出验证通过的目录名
    TAG = folder_name
    print(f"验证成功！TAG = {TAG}")

    return TAG

def write_advisors(TAG, all_files):
    output_file=TAG+'_advisor.gfx'
    # 写入文件（确保无后缀）
    with open(output_file, 'w+', encoding='utf-8') as f:
        f.write('spriteTypes = {\n')
        f.write(f'\t#There are {len(all_files)} advisor portraits.')
        for filename in all_files:
            f.write('\n\n\tspriteType = {\n')
            f.write('\t\tname = "GFX_'+filename+'\"\n')
            f.write('\t\ttexturefile = "gfx/interface/ideas/advisors/'+TAG+'/'+filename+'.dds\"\n')
            f.write('\t}')
        f.write('\n}')
    print(f"成功写入 {len(all_files)} 个注册文件到 {output_file}")

def write_characters(TAG, all_files):
    output_file=TAG+'_character.gfx'
    # 写入文件（确保无后缀）
    with open(output_file, 'w+', encoding='utf-8') as f:
        f.write('spriteTypes = {\n')
        f.write(f'\t#There are {len(all_files)} character portraits.')
        for filename in all_files:
            f.write('\n\n\tspriteType = {\n')
            f.write('\t\tname = "GFX_'+filename+'\"\n')
            f.write('\t\ttexturefile = "gfx/leaders/'+TAG+'/'+filename+'.dds\"\n')
            f.write('\t}')
        f.write('\n}')
    print(f"成功写入 {len(all_files)} 个注册文件到 {output_file}")

if __name__ == "__main__":
    main()
