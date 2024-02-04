import operator as op
# opens and reads in trace.config file
def read_config(config_file = 'trace.config'):
    section = {}
    try:
        # help taken from https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
        with open(config_file, 'r') as config:
            lines = config.readlines()
            for line in lines:
                line = line.strip()

                # help taken from https://www.geeksforgeeks.org/check-if-string-contains-substring-in-python/
                if line:
                    if op.contains(line, "configuration"):
                        current_section = line
                        section[current_section] = []
                    else:
                        section[current_section].append(line)
        return section
                

    except Exception as e:
        print(f'Error while reading config file: {e}')

# help taken from https://stackoverflow.com/questions/39875629/how-to-use-strip-in-map-function
    # https://medium.com/@kelvinsang97/split-and-strip-function-in-python-18e741c0bb75
        # https://stackoverflow.com/questions/28097057/how-to-split-a-line-and-map-it-in-pairs
        
def parse_section(section_lines):
    section_data = {}
    for line in section_lines:
        key, value = map(str.strip, line.split(':'))
        section_data[key] = value
    return section_data