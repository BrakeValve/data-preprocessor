# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 16:16:41 2016

@author: SISQUAKE
"""
from optparse import OptionParser
import os
from Game import Game

def listFilePath(path):
    file_path = [];
    file_name = [];
    for (dirpath, dirnames, filenames) in os.walk(path):
        for name in filenames:
            tmp = os.path.join(dirpath, name);
            file_path.append(tmp);
            file_name.append(name);
        break

    return {'file_path':file_path,'file_name':file_name}

#def main():

METADATA_DIRECTORY = '../../new_meta';
PRICE_DATA_DIRECTORY='../../price_data';
TRAINING_OUTPUT_DIRECTORY = '../../traing_data';

TARGET_COUNTRY = 'us';
    
parser = OptionParser();
parser.add_option("-m",dest = "METADATA_DIRECTORY");
parser.add_option("-p",dest="PRICE_DATA_DIRECTORY");
parser.add_option("-t",dest="TRAINING_OUTPUT_DIRECTORY");
(options, args) = parser.parse_args();

if options.METADATA_DIRECTORY != None:
    METADATA_DIRECTORY = options.METADATA_DIRECTORY;
if options.PRICE_DATA_DIRECTORY != None:
    PRICE_DATA_DIRECTORY = options.PRICE_DATA_DIRECTORY;
if options.TRAINING_OUTPUT_DIRECTORY != None:
    TRAINING_OUTPUT_DIRECTORY = options.TRAINING_OUTPUT_DIRECTORY;

# Store for Binary feature needs
 
developer_set = {};
publisher_set = {};
genres_set = {};

# Store ID to Game Object

game_set = {};

list_meta = listFilePath(METADATA_DIRECTORY);

# Create Game Object form metadata

for meta_path in list_meta['file_path']:
    g = Game(meta_path,TARGET_COUNTRY);
    print g.id
    game_set[g.id] = g;
    


        
        

#if __name__ == "__main__":
#    main();
