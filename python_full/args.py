import argparse as arg

def version():
    print("version is " + args.version)

if __name__ == '__main__':
    params = arg.ArgumentParser()
    params.add_argument('-v','--version',help="帮助信息")
    args = params.parse_args()
    print(args.version)
    if args.version:
        version()
