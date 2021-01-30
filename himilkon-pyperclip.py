import logging
import argparse
import pyperclip as pc
import subprocess

def def_params():
    parser = argparse.ArgumentParser(
            description="Description to fill"
    )
    parser.add_argument("-l", "--loghami", action='store_true', help="set debug")
    parser.add_argument("-gurl", "--geturl", action='store_true', help='zwraca url do repa')
    args = parser.parse_args()
    if args.loghami:
        logging.basicConfig(level=logging.DEBUG, force=True)
        print("args:" + str(args))
    return args

def gurlfunction():
    gurl=subprocess.Popen(['git', 'config', '--get', 'remote.origin.url'], stdout=subprocess.PIPE)
    output_gurl = gurl.stdout.read()
    print(output_gurl)
    pc.copy(str(output_gurl)[2:-3])

def main():
    args=def_params()
    if args.geturl:
        gurlsfunction()

if __name__ == "__main__":
    main()
