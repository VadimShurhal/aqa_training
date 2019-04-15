
def dataFileProcessing(path_to_source_file, path_to_destination_file):
    with open(path_to_source_file) as f:
        xml = f.read()
