import glob
import re
import yaml
import json
import os

filePaths = [f for f in glob.glob("../**/*.md", recursive=True)]

yamlStart = re.compile(r'\s*---\s')
yamlTag = re.compile(r'\s*---\s')

cache = {}
cacheFile = open('./Obsidian-Dataview-Cache.json', 'w')

for path in filePaths:
	with open(path) as file:

		filename = os.path.basename(path)
		trimfilename = filename.replace('.md', '')
		content = file.read()

		cache[trimfilename] = {}

		# ------------------------------
		#  Get YAML data
		# ------------------------------
		if yamlStart.match(content):
			yamlTags = [(m.span(0)) for m in yamlTag.finditer(content)]

			if len(yamlTags) > 1:
				yamlString = content[
					yamlTags[0][1]:
					yamlTags[1][0]
				]

				if yamlString:
					yamlFrontMatter = yaml.safe_load(yamlString)
					if type(yamlFrontMatter) is dict:
						cache[trimfilename].update(yamlFrontMatter)
		# ------------------------------
		#  Get file data
		# ------------------------------
		filedata = {}
		filedata['name'] = filename
		filedata['folder'] = os.path.dirname(path)
		filedata['path'] = path
		filedata['link'] = trimfilename

		cache[trimfilename]['file'] = filedata

json.dump(cache, cacheFile, indent=4)
cacheFile.close()
