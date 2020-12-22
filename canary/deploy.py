from brads_badass_canary import deploy
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        data = deploy(name)
        filename = sys.argv[2]
        with open(filename, 'w') as outfile:
            print("Outputting results to {}".format(filename))
            json.dump(data, outfile)
    else:
        sys.exit()
