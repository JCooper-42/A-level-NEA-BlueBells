import os

def find_files(filename, search_path):
   result = []

# Recursively walks through the directory
   for root, dir, files in os.walk(search_path):
      if filename in files:
	  # If the file is found, add its full path to the result list
         result.append(os.path.join(root, filename))
   return result

print(find_files("results.txt","MICROBIT:"))