import requests,re,yaml
from bs4 import BeautifulSoup
from lxml import etree, html
def find_methods(pattern,pattern2, html_content):
    match = re.findall(pattern, html_content)
    match2=re.findall(pattern2, html_content)
    #print(match)
    methods=[]
    methods_name=[]
    dict={}
    #print(match2)
    if match:
        #print(match.groups())
        i=0
        for group in match:
            #print(group)
            methods_name.append(group[0])
            methods.append( [f'{group[0]}({group[1]})'])
            group1=group[1].replace("\xa0","")
            
            try:
                des=match2[i]
                des=des[1]
            except:
                des='None'
            dict[group[0]]=[f'{group[0]}({group1})',des]
            i+=1
        return dict

def get_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        response = requests.get(url)
        tree = html.fromstring(response.content)
        xml_content = etree.tostring(tree, pretty_print=True, encoding='unicode')
        #print(xml_content)
        pattern = r'<span class="pre">(.*?)</span></code></a>\((.*?)\)'
        pattern2=r'<\/p><\/td>(\n?)<td><p>(.*?)<\/p><\/td>'
        methods=find_methods(pattern,pattern2,xml_content)
        return methods
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
dict2={}
file1_name="API_DRIVER.P4UTIL_CLASS.txt"
file_out=file1_name.split(".txt")[0]
file1=open(file1_name,"r").readlines()
base_url = 'https://psicode.org/psi4manual/master/api/psi4.%s.'%file1_name.split("_")[1].lower()

#https://psicode.org/psi4manual/master/api/psi4.core.AOShellCombinationsIterator.html#psi4.core.AOShellCombinationsIterator
#https://psicode.org/psi4manual/master/api/psi4.CORE.AOShellCombinationsIterator.html#psi4.CORE.AOShellCombinationsIterator
line_number=0
class_name=[]
dict1={}
for line in file1:
    if line_number%2==0:
        k=line.strip().split("(")[0]
        class_name.append(k)
        print(k)
    if line_number%2==1:
        dict1[k]={"description":line.strip()}
        k=1
    line_number+=1
print(dict1)
for name in class_name:
    url=base_url+name+'.html#'+'psi4.%s.%s'%(file1_name.split("_")[1].lower(),name)
    print(url)
    dict1[name]['element']=get_api(url)
    print(dict1)
dict2[file1_name.split(".txt")[0]]=dict1
with open(file_out+'.yaml', 'w') as file:
    yaml.dump(dict2, file, default_flow_style=False, allow_unicode=True)