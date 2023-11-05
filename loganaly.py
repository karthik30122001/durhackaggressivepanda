import time
from glob import glob
from testfile import sort_by,search_by_re
import argparse
from datetime import datetime

class LogAnalyzer:
    def __init__(self, log_file_path, live=False, method=False, wordser="" ):
        self.log_file_path = log_file_path
        self.logfile_lines = []
        self.dc = 0
        self.ec = 0
        self.wc = 0
        self.ic = 0
        self.cc = 0
        self.oc = 0
        self.live = live
        self.method= method
        self.wordser=wordser

    def readlin(self):
        with open(self.log_file_path, 'r') as file:
            self.logfile_lines = file.readlines()
            # for line in lines:
            #     self.logfile_lines.append(line.split(' ', 3))

    def tail(self):
        while True:
            try:
                with open(self.log_file_path, 'r') as file:
                    file.seek(0, 2)
                    while True:
                        line = file.readline()
                        if not line:
                            time.sleep(0.1)
                            continue
                        yield line
            except FileNotFoundError:
                time.sleep(1)

    def sort_by(self, log_type, log):
        # Implement your log sorting logic here
        pass

    def search_by_re(self, word, log):
        # Implement your regular expression search logic here
        pass

    def counter(self):
        live = self.live
        if live:
            print("{:5}{:5}{:4}{:4}{:4}{:5}".format('Debug','Error','Warn','Info','Crit','Other'))
            for line in self.tail():
                print("\r{:5}{:5}{:4}{:4}{:4}{:5}".format(self.dc, self.ec, self.wc, self.ic, self.cc, self.oc), end='')
                if sort_by("debug", log=line):
                    self.dc += 1
                if sort_by("error", log=line):
                    self.ec += 1
                if sort_by("warn", log=line):
                    self.wc += 1
                if sort_by("info", log=line):
                    self.ic += 1
                if sort_by("crit", log=line):
                    self.cc += 1
                if sort_by("other", log=line):
                    self.oc += 1
        else:
            print("{:5}{:5}{:4}{:4}{:4}{:5}".format('Debug', 'Error', 'Warn', 'Info', 'Crit', 'Other'))
            for line in self.logfile_lines:
                # print(line)
                if sort_by("debug", log=line):
                    self.dc += 1
                if sort_by("error", log=line):
                    self.ec += 1
                if sort_by("warn", log=line):
                    self.wc += 1
                if sort_by("info", log=line):
                    self.ic += 1
                if sort_by("crit", log=line):
                    self.cc += 1
                if sort_by("other", log=line):
                    self.oc += 1
            print("\r{:5}{:5}{:4}{:4}{:4}{:5}".format(self.dc, self.ec, self.wc, self.ic, self.cc, self.oc), end='')

    def ret_stats(self):
        self.counter()
        
        
    def word_search(self, word):
        live = self.live
        if live:
            for line in self.tail():
                if search_by_re(word=word, log=line):
                    print(line)
        else:
            for line in self.logfile_lines:
                if search_by_re(word=word, log=line):
                    print(line)

    def ping(self):
        for i in range(len(self.logfile_lines)):
            if i <= 5:
                ping =self.time_diff(self.logfile_lines[i], self.logfile_lines[i-1])
                print(ping)


    def time_diff(self, log1, log2):
        log1_parts= log1.strip().split(" ",3)
        # print(log1_parts)
        log2_parts= log2.strip().split(" ",3)
        
        time1 = float(log1_parts[1].split(":")[-1])
    
        
        time2 = float(log2_parts[1].split(":")[-1])
            
        if time2 > time1:
            time_difference = time2 - time1
        else:
            time_difference = time1 - time2
        return(round(time_difference, 4))

    def main(self):
        if self.live != True:
            self.readlin()
        if self.method == "counter":
            self.counter()
        elif self.method == "ping":
            self.ping()
        elif self.wordser != "":
            self.word_search(self.wordser)
       
        
        

    

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--log_path',
                        required=True,
                        help=' path to the log file: /...')
    parser.add_argument('-l', '--live',
                        required=False,
                        action='store_true',
                        help=' Flag for real time monitoring: /...')
    parser.add_argument('-m', '--method',
                        required=False,
                        help=' Returns counter: /...')
    parser.add_argument('-w', '--wordser',
                        required=False,
                        help=' Word search (Possibly Regex): /...')
    
    
    args = parser.parse_args()
    log_file_path = args.log_path
    live = args.live
    method = args.method
    wordser= args.wordser


    log_file_path = glob("logfile5*")[-1]
    

    analyzer = LogAnalyzer(log_file_path,live, method, wordser)
    analyzer.main()
    # analyzer.word_search("Dragon")