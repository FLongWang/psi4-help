import yaml,cmd,os,sys,re
from colorama import Fore, Back, Style, init
from pkg_resources import resource_filename
init(autoreset=True)
def print_tree(data, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{Colors.BOLD}{' ' * indent}{key}{Colors.RESET}")
            print_tree(value, indent + 2)
    elif isinstance(data, list):
        for item in data:
            print_tree(item, indent + 2)
    else:
        print(f"{' ' * (indent + 2)}{data}")
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
def read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def print_top_keys(yaml_data):
    top_keys=list(yaml_data.keys())
    print(f"{Colors.RED}keys number: %s{Colors.RESET}"%len(top_keys))
    for i, keyword in enumerate(top_keys, 1):
        l1="%10s"%keyword
        print(f"{Colors.BOLD}{Colors.BG_RED}{l1}{Colors.RESET}", end="\t")
        if i % 6 == 0:
            print()

def print_top3_keys(file, top_keys, top2_keys, des=False):
    print(f"\n{Colors.UNDERLINE}{Colors.BOLD}{Colors.RED}{top2_keys}{Colors.RESET}",end='\n')
    top3_element=list(file[top_keys][top2_keys]["element"].keys())
    if not des:
        for i, keyword in enumerate(top3_element):
            l1="%20s"%keyword
            print(f"{Colors.UNDERLINE}{Colors.WHITE}{l1}{Colors.RESET}",end='\t')
            if i % 5 == 4:
                print()
        print()
    else:
        for i, keyword in enumerate(top3_element, 1):
            ele=file[top_keys][top2_keys]["element"][keyword]
            l1="%20s"%keyword.strip()
            l2="%20s"%ele[0]
            print(f"{Colors.UNDERLINE}{l1}{Colors.RESET}",end='\t')
            print(f"{Colors.GREEN}{ele[0]}{Colors.RESET}",end='\t')
            print(f"{Colors.BLUE}{ele[1]}{Colors.RESET}",end='\t')
            print("\n")

def print_top2_keys(file, top_keys, des=False):
    top2_keys=list(file[top_keys].keys())
    print(f"{Colors.BOLD}{Colors.BG_RED}{top_keys}{Colors.RESET}")
    for i, keyword in enumerate(top2_keys, 1):
        #print(file[top_keys])
        l1="%30s"%keyword
        print(f"{Colors.UNDERLINE}{Colors.RED}{l1}{Colors.RESET}",end="\t")
        if i % 3 == 0:
            print()
    print()

def print_top2_keys_all(file, des=False):
    for top_keys in ["psi4.core","ps4.driver","psi4.driver.p4util"]:
        top2_keys=list(file[top_keys].keys())
        print(f"{Colors.BOLD}{Colors.BG_RED}{top_keys}{Colors.RESET}")
        for i, keyword in enumerate(top2_keys, 1):
            #print(file[top_keys])
            l1="%30s"%keyword
            print(f"{Colors.UNDERLINE}{Colors.RED}{l1}{Colors.RESET}",end="\t")
            if i % 3 == 0:
                print()
        print()

def search_keys(file,keys,des=True):
    pattern = r'\b%s'%keys
    #print_top3_keys(file, "psi4.core", keys)
    for top_keys in ["psi4.core","ps4.driver","psi4.driver.p4util"]:
        for top2_keys in list(file[top_keys].keys()):
            if re.search(pattern, top2_keys):
                print_top3_keys(file, top_keys, top2_keys)
                break
           
        
class Psi4APICLI(cmd.Cmd):
    intro = "\nWelcome to the Psi4 Keywords CLI. Type help or ? to list commands.\n Type \"show <module>\" like \"show ADC\".  \n \
Or use \"show <module> d\" to show description \n \"top\" or \"mod\" for module keys.\n"
    prompt = "(psi4-api-cli) $ "
    def __init__(self):
        super().__init__()
        #file_path = resource_filename('psi4_help', 'api_class.yaml')
        file_path='psi4_api_class.yaml'
        self.yaml_data = read_yaml(file_path)
        print_top_keys(self.yaml_data)
    def do_exit(self, arg):
        """Exit the CLI."""
        print("Exiting...")
        return True
    def do_e(self, arg):
        """Exit the CLI."""
        print("Exiting...")
        return True
    def do_mod_api(self, arg):
        """List all top-level PSI4 keys."""
        print_top2_keys_all(self.yaml_data)
    def do_module_api(self, arg):
        """List all top-level PSI4 keys."""
        print_top2_keys_all(self.yaml_data)
    def do_mod_api(self, arg):
        """List all top-level PSI4-API keys."""
        print_top2_keys_all(self.yaml_data)
    def do_top_api(self, arg):
        """List all top-level PSI4-API keys."""
        print_top2_keys_all(self.yaml_data)
    def do_all_api(self, arg):
        """List all PSI4-API keys."""
        print_top2_keys_all(self.yaml_data)
    def do_s(self, arg):
        """search PSI4-API keys."""
        args = arg.lower()
        print(args)
        search_keys(self.yaml_data,args)
    def do_ss(self,arg):
        """Search PSI4-API keys."""
        args = arg.split()
        if not args:
            print("Usage: ss <top_key> <top2_key>")
            return
        top_keys = args[0].lower()
        top2_keys = args[1].lower()
        pattern = r'\b%s'%top_keys
        match = re.search(pattern, ["core","driver","p4util"])
        if match:
            top_keys="psi4."+match.group(0)
        pattern = r'\b%s'%top2_keys
        for top2_keys in list(self.yaml_data[top_keys].keys()):
            if re.search(pattern, top2_keys):
                print_top3_keys(self.yaml_data, top_keys, top2_keys)
                break
    def do_score(self,arg):
        """Search psi4.core PSI4-API keys."""
        args = arg.split()
        if not args:
            print("Usage: score <top2_key>")
            return
        top2_keys = args[0].lower()
        pattern = r'\b%s'%top2_keys
        for top2_keys in list(self.yaml_data["psi4.core"].keys()):
            if re.search(pattern, top2_keys):
                print_top3_keys(self.yaml_data, "psi4.core", top2_keys)
                break
    def do_core(self,arg):
        """List all psi4.core PSI4-API keys."""
        args = arg.split()
        if not args:
            print("Usage: show <top_key>")
            return
        top2_keys = args[0].lower()
        print_top2_keys(self.yaml_data, "psi4.%s"%top2_keys, des=False)
    def do_show(self,arg):
        """List all psi4.core PSI4-API keys."""
        print_top2_keys(self.yaml_data, "psi4.core", des=False)
    def do_driver(self,arg):
        """List all psi4.diver PSI4-API keys."""
        print_top2_keys(self.yaml_data, "psi4.driver", des=False)    
    def do_p4util(self,arg):
        """List all psi4.diver.p4util PSI4-API keys."""
        print_top2_keys(self.yaml_data, "psi4.driver.p4util", des=False)       
    def do_tree(self, arg):
        """Print the tree structure of the YAML file."""
        print_tree(self.yaml_data)

if __name__ == "__main__":
#    print_top2_keys( read_yaml('api_class.yaml'), "psi4.core")
#    print_top3_keys( read_yaml('api_class.yaml'), "psi4.core","wavefunction")
    Psi4APICLI().cmdloop()