import argparse,os

parser = argparse.ArgumentParser()

parser.add_argument('-s', '--source', choices=('staging', 'integration', 'prod','skill-edge'), help='source directory from which you copy the json files')
parser.add_argument('-d', '--destination', choices=('staging', 'integration', 'prod','skill-edge'), help='destination directory to which you paste the json files')



args = parser.parse_args()



if (args.source is None) or (args.destination is None):
    ##print the file name
    print("try "+os.path.basename(__file__)+" --help")
else:
    print(args.source)
    print (args.destination)
