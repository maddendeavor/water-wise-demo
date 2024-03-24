#!/bin/env python3
import sys
import yaml
import copy
# import logging

# log = logging.getLogger()
# Initialize an empty list to collect lines
input_lines = []

for line in sys.stdin:
  # Collect the lines
  input_lines.append(line)

# Join the collected lines into a single string
yaml_input = ''.join(input_lines)

try:
  # Parse the entire YAML input
  data = yaml.safe_load(yaml_input)

  if isinstance(data, list):
    # If input is a list, modify each item in the list
    outputs = []
    for item in data:
      imp = copy.deepcopy(item)
      # imp['energy'] = 1
      imp['energy'] = item["cpu/energy"] * 8
      imp["item"] = str(item)
      imp["item_type"] = str(type(item))
      outputs.append(imp)
    # print(yaml.dump(outputs, default_flow_style=False))
      
    print(yaml.dump(outputs, default_flow_style=True))
  else:
    print("Input data is not a list. Please provide YAML data in list format.")
except yaml.YAMLError as e:
  print("Error parsing YAML:", e)
