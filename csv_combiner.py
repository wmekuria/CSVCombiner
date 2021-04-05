import sys
import csv

class FileCombiner(object):
    def __init__(self, includ_filename = True):
        self.includ_filename = includ_filename #show filename column flag

    def display_csv(self, filename):
        if filename.endswith('.csv'):
            with open(filename) as csv_file: # different variable
                csv_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
                next(csv_reader, None) # skip header 
                for row in csv_reader:
                    #option to use without adding a new col
                    if self.includ_filename == True:
                        row.append('"'+filename+'"') 
                    print(",".join(row))
        else:
            raise TypeError("File must be csv")

    def display_header(self):
        headers = ["email_hash", "category"]
        if self.includ_filename == True:
            headers.append("filename") 
        print (",".join(f'"{s}"' for s in headers))

    def display_combined(self, filelist):
        self.display_header()
        if isinstance(filelist, list):
            for filename in filelist:
                self.display_csv(filename)
        else:
            raise TypeError("Argument must be a list")
       
def main():
    filename = sys.argv #get input arguments 
    if len(filename) > 1:
        filename.pop(0) #remove first element 
        combiner = FileCombiner() #Instance of class
        combiner.display_combined(filename)

if __name__ == '__main__':
    main()
