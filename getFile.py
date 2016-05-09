class getFile():
    _data_dir_file = []
    _corpus_size = []
    _test_lines = []
    _data_lines = []
    def __init__(self, arg_dir_file):
        self.readArgument(arg_dir_file)
        self.splitFile()
    def readArgument(self, arg_dir_file):
        with open(arg_dir_file, encoding = 'utf8') as f:
            lines = f.readlines()
            self._data_dir_file = lines[0].split()
            self._corpus_size = lines[1].split()
            self._corpus_size = [int(val) for val in self._corpus_size]
            numb_lines = 0
            for size in self._corpus_size:
                self._test_lines.append([numb_lines, int(numb_lines+size/10)])
                self._data_lines.append([int(numb_lines+size/10), numb_lines+size]) 
                numb_lines+= size
    def splitFile(self):
        for data_file in self._data_dir_file:
            self.writeData(data_file)
    def writeData(self, data_dir_file):
        test_lines = []
        data_lines = []
        
        with open(data_dir_file, encoding = 'utf8') as f:
            lines = f.readlines()
            for slices in self._test_lines:
                test_lines += lines[slices[0]:slices[1]]
            for slices in self._data_lines:
                data_lines += lines[slices[0]:slices[1]]
                
        with open('test.'+data_dir_file, 'w', encoding = 'utf8') as f:
            f.write(''.join(test_lines))
        with open('data.'+data_dir_file, 'w', encoding = 'utf8') as f:
            f.write(''.join(data_lines))
            
if __name__ == '__main__':
    a = getFile('arg.txt')