from pypinyin import lazy_pinyin
from pathlib import Path
import pyradox, glob, os

def main():
    files = readFiles()
    tags = readTags()
    for i in range(len(files)):
        with open(files[i], "r+", encoding="utf-8") as f:
            content = f.read()
            pyradox_content = pyradox.parse(content)
            character_key = [k for k, v in pyradox_content.items() if k == "create_country_leader" or k == "create_field_marshal" or k == "create_corps_commander" or k == "create_navy_leader"]
            character_value = [v for k, v in pyradox_content.items() if k == "create_country_leader" or k == "create_field_marshal" or k == "create_corps_commander" or k == "create_navy_leader"]
        for kv in range(len(character_key)):
            match character_key[kv]:
                case "create_country_leader":
                    print(f"""
                        country_leader = {{
                            ideology = {character_value[kv]["ideology"]}
                            traits = {{  }}
                            desc = PORTRAIT_YUX_LIU_XIANG_DESC
                            expire = "1965.1.1.1"
                            id = -1
                        }}
                    """)
                case "create_field_marshal":
                    print(f"""
                        field_marshal = {{
                            traits = {{ {character_value[kv]["traits"]} }}
                            skill = {character_value[kv]["skill"]}
                            attack_skill = {character_value[kv]["attack_skill"]}
                            defense_skill = {character_value[kv]["defense_skill"]}
                            planning_skill = {character_value[kv]["planning_skill"]}
                            logistics_skill = {character_value[kv]["logistics_skill"]}
                        }}
                    """)
                case "create_corps_commander":
                    print(f"""
                        corps_commander = {{
                            traits = {{ {character_value[kv]["traits"]} }}
                            skill = {character_value[kv]["skill"]}
                            attack_skill = {character_value[kv]["attack_skill"]}
                            defense_skill = {character_value[kv]["defense_skill"]}
                            planning_skill = {character_value[kv]["planning_skill"]}
                            logistics_skill = {character_value[kv]["logistics_skill"]}
                        }}
                    """)
    print(tags)

def readFiles():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txt_files = glob.glob(os.path.join(current_dir, "*.txt"))
    return txt_files

def readTags():
    filename_prefixes = []
    current_dir = Path(__file__).parent
    txt_files = [str(p.resolve()) for p in current_dir.glob("*.txt")]
    for file_path in txt_files:
        # 获取纯文件名（不含路径）
        filename = os.path.basename(file_path)
        # 使用切片操作提取前三个字符[1,4,5](@ref)
        prefix = filename[:3] if len(filename) >= 3 else filename
        filename_prefixes.append(prefix)
    return filename_prefixes

def convertName():
    zh_name = ("黄绍竑")
    name_list = lazy_pinyin(zh_name)
 
    xin = name_list[0]
    ming_list = name_list[1:]
    ming = ""
    for y in ming_list:
        ming = ming + y
 
    en_name = xin + "_" + ming
    en_name = en_name.title().lstrip()
    print(en_name)

main()