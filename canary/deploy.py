from brads_badass_canary import deploy
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        filename = sys.argv[2]

        if len(sys.argv) > 2:
            data = deploy(name, sys.argv[3], sys.argv[4], sys.argv[5])
        else:
            data = deploy(name)
        with open(filename, 'w') as outfile:
            print("Outputting results to {}".format(filename))
            json.dump(data, outfile)
    else:
        sys.exit()
