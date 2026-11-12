import sys, yaml; print(yaml.load(sys.stdin.read(), Loader=yaml.FullLoader))
