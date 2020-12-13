from brads_badass_canary import deploy
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        deploy(sys.argv[1])
    else:
        sys.exit()
