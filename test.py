
import time
from glob import glob
from testfile import sort_by,search_by_re



# with open('qrt_data_extraction_analysis_04-11-2023_130618.log', 'r') as f:
#     for line in f:
#         line = line.split(" ", 3)
#         if line[2] == 'DEBUG:':
#             print(line[3])
            
# file = open(glob("logfile*.log")[0],"r")

# while 1:
#     where = file.tell()
#     line = file.readline()
#     if not line:
#         time.sleep(1)
#         file.seek(where)
#     else:
#         print(line)

import time

def tail(file_path):
    while True:
        try:
            with open(file_path, 'r') as file:
                file.seek(0, 2)  # Move the file pointer to the end of the file
                while True:
                    line = file.readline()
                    if not line:
                        time.sleep(0.1)  # Sleep for a short interval before checking again
                        continue
                    yield line
        except FileNotFoundError:
            time.sleep(1)  # Sleep for a longer interval if the file doesn't exist yet


# Example usage:
dc=0
ec=0
wc=0
ic=0
cc=0
oc=0
log_file_path = glob("logfile5*")[-1]
with open(log_file_path, 'r') as file:
    loglines=  file.readlines

def counter(live=False):
    if live:
        print("{:5}{:5}{:4}{:4}{:4}{:5}".format('Debug','Error','Warn','Info','Crit','Other'))
        for line in tail(log_file_path):
        
            print("\r","{:5}{:5}{:4}{:4}{:4}{:5}".format(dc,ec,wc,ic,cc,oc), end='')
            if sort_by("debug", log=line):

                # print(line, end='')
                dc = dc+1
            if sort_by("error", log=line):

                # print(line, end='')
                ec = ec+1
            if sort_by("warn", log=line):

                # print(line, end='')
                wc = wc+1
            if sort_by("info", log=line):

                # print(line, end='')
                ic = ic+1
            if sort_by("crit", log=line):

                # print(line, end='')
                cc = cc+1

            if sort_by("other", log=line):

                # print(line, end='')
                oc = oc+1

    else:
        for line in loglines:
            print(line)
            if sort_by("debug", log=line):

                # print(line, end='')
                dc = dc+1
            if sort_by("error", log=line):

                # print(line, end='')
                ec = ec+1
            if sort_by("warn", log=line):

                # print(line, end='')
                wc = wc+1
            if sort_by("info", log=line):

                # print(line, end='')
                ic = ic+1
            if sort_by("crit", log=line):

                # print(line, end='')
                cc = cc+1

            if sort_by("other", log=line):

                # print(line, end='')
                oc = oc+1
        


def ret_stats():
    counter()
    print("{:5}{:5}{:4}{:4}{:4}{:5}".format('Debug','Error','Warn','Info','Crit','Other'))
    print("{:5}{:5}{:4}{:4}{:4}{:5}".format(dc,ec,wc,ic,cc,oc), end='')


def word_search(word, live= False):
    if live:
        for line in tail(log_file_path):
            if search_by_re(word=word, log=line):
                print(line)
    else:
        for line in loglines:
            if search_by_re(word=word, log=line):
                print(line)


word_search("ping")
ret_stats()