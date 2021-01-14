"""
Main.py imports scrape and allows users to input the number of pages they would like to scrape on the command line and then call functions of scrape.py accordingly, then prints out values.

$ python3 main.py num
"""
import sys
import scrape
import pprint

pprint.pprint(scrape.num_of_pages_to_scrape(int(sys.argv[1])))