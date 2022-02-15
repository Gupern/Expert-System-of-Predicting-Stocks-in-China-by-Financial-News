# encoding: utf-8
"""
    author: Gupern 
    description:  this is the main file, which can using command line  
                  to call modules' function, such as engine, etc. 
    using: 
           1. execute crawler script outside /src dir:  
             `python main.py --script=<target_file> --crawler_component=<target_component>` 
           2. 
"""

import configparser
import os, sys, argparse
import importlib

# add local module, abspath is outside the /src
root_dir = os.path.abspath('.')
engine_dir = root_dir + "/src/engine"
script_dir = root_dir + "/src/script"
sys.path.append(engine_dir)
sys.path.append(script_dir)

from db import MongoDBSteward
from crawler import Crawler

# read from config.ini
cf = configparser.ConfigParser()
cf.read(root_dir + "/src/resource/config.ini")

# recieve parameter
parser = argparse.ArgumentParser(description="esps's main.py, author: Gupern.")
parser.add_argument("--script", type=str, default=None, help="appoint your crawler's script file name")
parser.add_argument("--crawler_component", type=str, default=None, help="appoint your crawler component, split by ','")
parser.add_argument("--collection", type=str, default="info_detail", help="appoint your mongodb collection, default is info_detail")
args = parser.parse_args()

if __name__ == "__main__":
    print("args is: %s" % args)
    # generate crawler instance
    print(args.crawler_component)
    crawler = Crawler(args.crawler_component)

    # if script is been appointed, import target script
    script_str = args.script

    # setting mongo collection
    mongodb_steward = MongoDBSteward(cf)
    mongo_collection = mongodb_steward.get_collection("esps", args.collection)

    if script_str is not None:
        crawler_script = importlib.import_module(script_str)
        crawler_script.func(mongo_collection, crawler)
