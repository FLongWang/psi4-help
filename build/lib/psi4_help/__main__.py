from .psi4_help import Psi4KeywordsCLI
from .psi4_api_help import Psi4APICLI
import sys
def run_psi4_help():
    try:
        arg=sys.argv[1]
        print(arg)
        if "api" in arg.lower():
            cli = Psi4APICLI()
            cli.cmdloop()
        else:
            cli = Psi4KeywordsCLI()
            cli.cmdloop()
    except:
        cli = Psi4KeywordsCLI()
        cli.cmdloop()
if __name__ == "__main__":
    run_psi4_help()