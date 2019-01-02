#!/usr/bin/env python3
# Outputs an Athena SQL schema based on the json files passed in

import json
import os
import sys
import types


all_keys = {}

def get_type(o):
    if isinstance(o, bool):
        return "BOOLEAN"
    elif isinstance(o, float):
        return "FLOAT"
    elif isinstance(o, int):
        return "INT"
    elif isinstance(o, str):
        return "STRING"
    else:
        return "Unsupported: " + type(o)

def analyse(file):
    if not os.path.exists(file):
        print("File does not exist: " + file)
    with open(file) as fp:
        for line in fp:
            jline = json.loads(line)
            for key in jline:
                val_type = get_type(jline[key])
                if not key in all_keys:
                    all_keys[key] = val_type
                elif all_keys[key] != val_type:
                    all_keys[key] = 'Unsupported: varies'

def main(argv):
    if len(argv) == 1:
        print("Usage: " + argv[0] + " <files to analyse>")
        return
    for f in argv[1:]:
        analyse(f)
        
    # Output the SQL statement
    print("CREATE EXTERNAL TABLE IF NOT EXISTS <<TODO_replace>> (")
    key_len = len(all_keys) -1
    i = 0
    for key in sorted(all_keys):
        if i == key_len:
            print("  `" + key + "` " + all_keys[key])
        else :
            print("  `" + key + "` " + all_keys[key] + ",")
        i += 1
    print(")")
    print("ROW FORMAT  serde 'org.openx.data.jsonserde.JsonSerDe'")
    print("LOCATION 's3://foxsec-metrics/<<TODO_replace>>/';")

if __name__ == "__main__":
    main(sys.argv)