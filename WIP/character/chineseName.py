from pypinyin import lazy_pinyin
from pathlib import Path
import pyradox, glob, os

def main():
    files = readFiles()
    tags = readTags()
    character_list_menu = []
    character_list = []
    check = False

    for i in range(len(files)):
        character_list_menu.clear()
        character_list.clear()
        with open(files[i], "r+", encoding="utf-8") as f:
            content = f.read()
            pyradox_content = pyradox.parse(content)
            character_key = [k for k, v in pyradox_content.items() if k == "create_country_leader" or k == "create_field_marshal" or k == "create_corps_commander" or k == "create_navy_leader"]
            character_value = [v for k, v in pyradox_content.items() if k == "create_country_leader" or k == "create_field_marshal" or k == "create_corps_commander" or k == "create_navy_leader"]
        for kv in range(len(character_key)):
            english_name = convertName(character_value[kv]["name"])
            if english_name not in character_list_menu:
                character_list_menu.append(english_name)
                index = -1
                character_info = f"""
                    {tags[i]}_{english_name} = {{
                        name = {english_name}
                        portraits = {{
                            civilian = {{
                                large = GFX_Portrait_{tags[i]}_{english_name}
                                #small = GFX_idea_advisor_{tags[i]}_{english_name}
                            }}
                            army = {{
                                large = GFX_Portrait_{tags[i]}_{english_name}
                                #small = GFX_idea_advisor_{tags[i]}_{english_name}
                            }}
                        }}
                    }}
                """
                pyradox_character_info = pyradox.parse(character_info)
                character_list.append(pyradox_character_info)
            else:
                index = int(character_list_menu.index(english_name))
            match character_key[kv]:
                case "create_country_leader":
                    character_info_add = character_list[index][f"{tags[i]}_{english_name}"]
                    character_info_add["country_leader"] = { "ideology": f"{character_value[kv]['ideology']}" }
                    character_info_add_country_leader = character_info_add["country_leader"]
                    character_info_add_country_leader.append("traits", f"{character_value[kv]['traits']}", in_group = True)
                    character_info_add_country_leader.append("desc", f"PORTRAIT_{tags[i]}_{english_name.upper()}_DESC")
                case "create_field_marshal":
                    character_info_add = character_list[index][f"{tags[i]}_{english_name}"]
                    character_info_add["field_marshal"] = { "#": f"#" }
                    character_info_add_field_marshal = character_info_add["field_marshal"]
                    character_info_add_field_marshal.append("traits", f"{character_value[kv]['traits']}", in_group = True)
                    character_info_add_field_marshal.append("skill", f"{character_value[kv]['skill']}")
                    character_info_add_field_marshal.append("attack_skill", f"{character_value[kv]['attack_skill']}")
                    character_info_add_field_marshal.append("defense_skill", f"{character_value[kv]['defense_skill']}")
                    character_info_add_field_marshal.append("planning_skill", f"{character_value[kv]['planning_skill']}")
                    character_info_add_field_marshal.append("logistics_skill", f"{character_value[kv]['logistics_skill']}")
                case "create_corps_commander":
                    character_info_add = character_list[index][f"{tags[i]}_{english_name}"]
                    character_info_add["corps_commander"] = { "#": f"#" }
                    character_info_add_corps_commander = character_info_add["corps_commander"]
                    character_info_add_corps_commander.append("traits", f"{character_value[kv]['traits']}", in_group = True)
                    character_info_add_corps_commander.append("skill", f"{character_value[kv]['skill']}")
                    character_info_add_corps_commander.append("attack_skill", f"{character_value[kv]['attack_skill']}")
                    character_info_add_corps_commander.append("defense_skill", f"{character_value[kv]['defense_skill']}")
                    character_info_add_corps_commander.append("planning_skill", f"{character_value[kv]['planning_skill']}")
                    character_info_add_corps_commander.append("logistics_skill", f"{character_value[kv]['logistics_skill']}")
                case "create_navy_leader":
                    character_info_add = character_list[index][f"{tags[i]}_{english_name}"]
                    character_info_add["navy_leader"] = { "#": f"#" }
                    character_info_add_navy_leader = character_info_add["navy_leader"]
                    character_info_add_navy_leader.append("traits", f"{character_value[kv]['traits']}", in_group = True)
                    character_info_add_navy_leader.append("skill", f"{character_value[kv]['skill']}")
                    character_info_add_navy_leader.append("attack_skill", f"{character_value[kv]['attack_skill']}")
                    character_info_add_navy_leader.append("defense_skill", f"{character_value[kv]['defense_skill']}")
                    character_info_add_navy_leader.append("maneuvering_skill", f"{character_value[kv]['maneuvering_skill']}")
                    character_info_add_navy_leader.append("coordination_skill", f"{character_value[kv]['coordination_skill']}")
        with open(f"{tags[i]}.txt", "w+" ,encoding="utf-8") as f:
            for j in range(len(character_list)):
                print(str(character_list[j]))
                f.write(str(character_list[j]))

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

def convertName(names):
    zh_name = (names)
    name_list = lazy_pinyin(zh_name)
 
    xin = name_list[0]
    ming_list = name_list[1:]
    ming = ""
    for y in ming_list:
        ming = ming + y
 
    en_name = xin + "_" + ming
    en_name = en_name.title().lstrip()
    
    return en_name

main()