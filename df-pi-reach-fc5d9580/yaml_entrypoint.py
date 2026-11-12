"""A small YAML parsing entrypoint for reachability evaluation."""
        import sys
        import yaml


        def parse_document(raw: str):
            return yaml.load(raw, Loader=yaml.FullLoader)


        if __name__ == "__main__":
            print(parse_document(sys.stdin.read()))
        
