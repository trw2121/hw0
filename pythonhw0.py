counter = 0
searchfile = open('iowa-liquor-sample.csv', 'r')
for line in searchfile:
	if 'single malt scotch' in line.lower(): counter += 1
print counter
searchfile.close()
