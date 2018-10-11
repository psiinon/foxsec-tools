#!/usr/bin/env python3

import argparse
import collections
import datetime
import json
import fnmatch
import os
import re
import time
'''
TODO
    Loop through all files in directory (option for one file)
    Read each line as json
    Output one line per field(?):
        category, event, timestamp, day
'''

def clean_name(name):
    return name.replace('.', '_').replace('-', '_').replace(':', '_')

def handle_file(src_file, dest_dir):
    with open(src_file) as f:
        for line in f:
            data = json.loads(line.replace('\'', '"'))
            startts = data['startts']
            day = str(datetime.date.fromtimestamp(startts))
            output_file = open(dest_dir + '/' + day, 'a')
            for field in data:
                if isinstance(data[field], dict):
                    for f2 in data[field]:
                        resDict = {}
                        resDict['startts'] = startts
                        resDict['day'] = day
                        resDict['category'] = field
                        resDict['field'] = clean_name(f2)
                        resDict['value'] = data[field][f2]

                        output_file.write(json.dumps(resDict) + '\n')
            output_file.close()

            '''
            # Print # results?
            if not "results" in data:
              print("No results in " + src_dir + '/' + account + '/' + acc_file)
              continue
            if len(data["results"]) == 0:
              print("Zero results in " + src_dir + '/' + account + '/' + acc_file)
              continue
            for res in data["results"]:
              resDict = {}
              resDict['day'] = day_str;
              resDict['account'] = account
              resDict['ami_name'] = optional(res['metadata'], 'ImageId')
              resDict['test_name'] = res['test_name']
              resDict['status'] = res['status']
              resDict['value'] = res['value']
              # Extract all of the metadata tags
              tags = {}
              for tagpair in res['metadata']['Tags']:
                tags[tagpair['Key']] = tagpair['Value']

              resDict['instance_name'] = optional(tags, 'Name')
              resDict['instance_owner'] = optional(tags, 'Owner')
              resDict['instance_stack'] = optional(tags, 'Stack')
              resDict['instance_type'] = optional(tags, 'Type')
              resDict['instance_app'] = optional(tags, 'App')
    
              output_file.write(json.dumps(resDict) + '\n')
        
          output_file.close()
          '''


def handle_all_files(src_dir, dest_dir):
    # the earliest date
    date = datetime.datetime(2018, 9, 14)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    while True: 
        day_str = date.strftime("%Y-%m-%d")
        handle_day_files(src_dir, dest_dir, day_str)
        if day_str == today:
            break;  
        date += datetime.timedelta(days=1)


def get_args():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-s', '--source-dir',
                        required=True,
                        help='source directory')
    
    parser.add_argument('-d', '--dest-dir',
                        required=True,
                        help='destination directory')
    
    parser.add_argument('-D', '--day',
                        help='date, as YYYY-MM-dd')
    
    return parser.parse_args()


def main():
    args = get_args()
    if args.day:
        handle_file(args.source_dir + '/' + args.day, args.dest_dir)
    else:
        handle_all_files(args.source_dir, args.dest_dir)


if __name__ == '__main__':
    main()
