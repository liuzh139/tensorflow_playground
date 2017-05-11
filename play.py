filename_list = ['/Users/daisy/github/sandbox/play_dataset/dataset_1.txt']
filename_output = '/Users/daisy/github/sandbox/play_dataset/output_1.txt'


def read_lines_from_file(filename_list):
    for file in filename_list:
        with open(file) as f:
            content = f.readlines()
            print(content)

def write_lines_to_file(filename_output):
    file = open(filename_output,'w')
    file.write("hello world")
    file.close()


if __name__ == "__main__":
    write_lines_to_file(filename_output)
    read_lines_from_file(filename_list)