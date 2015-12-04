__author__ = 'F4RZ4N'

python_methods_blacklist = ['eval' , 'exec', 'open', 'file', 'sys', 
                            'subprocess', 'os', 'shutil', 'execfile', 'compile'
                            'reload', ]


java_methods_blacklist = ['Runtime', 'PrintWriter' ,'Process', 'SystemUtils',
                          'ProcessBuilder', 'BufferedReader', 'File', 
                          'Path', 'Paths','FileReader',
                          'FileWriter', 'BufferedWriter' ]

cpp_methods_blacklist = [ 'system', 'ofstream', 'ifstream', 'fstream', 'CreateProcess',
                           'clone', 'fork'] 
