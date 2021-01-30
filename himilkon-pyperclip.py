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
    parser.add_argument("-db", "--djangoblock", help="generuje nam block będący w djangowych htmlu block-iem jako pierwszy wyraz - nazwa pliku, drugi jako nazwa bloku rozdzielana niemieckim ß")
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

def generateBlock(blok, plik):
    text="{% block "+ str(blok) + " %}"+"\n"+\
            "<!-- "+ str(blok)+ " " +str(plik) + " -->"+"\n"+\
            "{% endblock "+ str(blok) + " %}"
    return text

def djangoblockFunction(djangoblock):
    lst=djangoblock.split("ß")
    print("lst : "+ str(lst))
    blok=lst[0]
    plik=lst[1]
    text=generateBlock(blok, plik)
    print(text)
    pc.copy(str(text))

def main():
    args=def_params()
    if args.geturl:
        gurlsfunction()
    elif args.djangoblock:
        djangoblock=args.djangoblock
        djangoblockFunction(djangoblock)

if __name__ == "__main__":
    main()
