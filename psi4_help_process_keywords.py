import requests
import yaml,lxml
from lxml import etree
import yaml
def is_number(s):
    try:
        # 尝试将字符串转换为浮点数
        float(s)
        return True
    except ValueError:
        # 如果转换失败，检查是否是科学计数法
        if 'D' in s or 'd' in s:
            try:
                # 替换 'D' 或 'd' 为 'e'
                s = s.replace('D', 'e').replace('d', 'e')
                float(s)
                return True
            except ValueError:
                return False
        return False
def is_letters(s):
    for char in s:
        if not (char.isalpha() or char.isspace() or char=="_"):
            return False
    return True
file_path = "psi4_keywords.txt"

module_name=[]
module_keys=[]
keywords_dict={}

with open(file_path, 'r', encoding='utf-8') as file:
    while True:
        line=file.readline()
        l=line.replace("(","").replace(")","")
        if "(" in line and ")" in line and len(line.split())==2 \
            and l.split()[1].isupper() and l.split()[0].isupper():
            module_name=l.split()[1]
            module_keys=line.split()[0]

            if module_name not in keywords_dict.keys():
                keywords_dict[module_name]={}
            keywords_dict[module_name][module_keys]={}
        if not line:
            break
print(keywords_dict["DETCI"])
with open(file_path, 'r', encoding='utf-8') as file:
    while True:
        line=file.readline()
        l=line.replace("(","").replace(")","")
        if "(" in line and ")" in line and len(line.split())==2 \
            and l.split()[1].isupper() and l.split()[0].isupper():
            module_name=l.split()[1]
            module_keys=line.split()[0]
        if " —" in line:
            keywords_dict[module_name][module_keys]["description"]=line.split("—")[-1].strip()
        if "Type:" in line:
            keywords_dict[module_name][module_keys]["type"]=line.split()[-1]  
        if "Default:" in line: 
            keywords_dict[module_name][module_keys]["default"]=line.split()[-1]
        if "Possible Values:" in line:
            keywords_dict[module_name][module_keys]["optional"]=line.split(":")[-1].strip()
        if not line:
            break
import yaml
with open("psi4_keywords.yaml", 'w', encoding='utf-8') as file:
    yaml.safe_dump(keywords_dict, file, sort_keys=True)
print(keywords_dict)