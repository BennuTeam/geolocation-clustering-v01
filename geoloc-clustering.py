
'''
read geoloc data file from same git repo
file type: json
'''

# imports
import git
import json
import os

# define repo url and local path for saving data
repo_url = "https://github.com/BennuTeam/geolocation-clustering-v01.git"
local_path = "D:\Ponisha Projects\Clustering based on Geolocation data\data" # local path should be an empty folder

# clone repo to local path
git.Repo.clone_from(repo_url,local_path)

# open, read, and display file from cloned repo
f = open(os.path.join(local_path,"GeoLocData.json"))
geoloc = json.load(f)
print(geoloc)