'''
Functions you only need to care:
+ readArgument
+ splitFiles
+ mergeFiles
'''

class getFile():
    def __init__(self):
        self._data_dir_file = []
        self._corpus_size = []
        self._test_lines = []
        self._data_lines = []
        self._child_dir_file = []
        self._merge_file = ''
    def readArgument(self, arg_dir_file, command = 'split'):
        if (command == 'split'):
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
        if (command == 'merge'):
            with open(arg_dir_file, encoding = 'utf8') as f:
                lines = f.readlines()
                command = lines[0].split()[0]
                if ('manual' == command):
                    self._child_dir_file = lines[1].split()
                elif ('auto' == command):
                    raw = lines[1].split()
                    prefix = raw[0]
                    self._child_dir_file = [prefix+str(index) for index in range(int(raw[1]), int(raw[2])+1)]
                self._merge_file = lines[2]
    def splitFiles(self):
        for data_file in self._data_dir_file:
            self.splitFile(data_file)
    def mergeFiles(self):
        lines = []
        for data_file in self._child_dir_file:
            with open(data_file, encoding = 'utf8') as f:
                lines += f.readlines()
        with open(self._merge_file, 'w', encoding = 'utf8') as f:
            f.write(''.join(lines))
    def splitFile(self, data_dir_file):
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
    a = getFile()
    a.readArgument('arg.txt', 'merge') 
    a.mergeFiles()
