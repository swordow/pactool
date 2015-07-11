#!/usr/bin/python
import sys;
import base64;

def getSitesFromGFWList():
	# Decode the GFWList
	f = file("gfwlist.txt","rt");
	of = file("convertedgfwlist.txt","wt");
	str = "";
	while True:
		str = f.readline();
		if str == -1 or str == "":
			break;
		ree = base64.standard_b64decode(str);
		of.write(ree);
	of.close()
	f.close();

	# Get the useful site list
	siteSet = {};
	count = 0;
	f = file("convertedgfwlist.txt",'rt');
	while True:
		str = f.readline();
		if str == -1 or str == "":
			break;
		# Ignore the comment
		if str.startswith("@"):
			continue;
		if str.startswith("!"):
			continue;
		if str.startswith("["): # "[Auto Config]"
			continue;

		if str.startswith("||"):
			str = str[2:];
		if str.startswith("."):
			str = str[1:];
		if str.startswith("|"):
			str = str[1:];
		if str.startswith("http://"):
			str = str[7:];
		if str.startswith("https://"):
			str = str[8:];
		if str.startswith("www."):
			str = str[4:];

		siteSet[count] = str;
		count = count + 1;
		#if re.match(r".*google.*",str):
			#print str;
		#of.write("\n");
	f.close();
	return siteSet;

def cleanUpSiteSet(siteSet):
	for i in siteSet:
		# Ignore xxx.xxx/ignored ...
		firstSplash = siteSet[i].find("/");
		if firstSplash != -1:
			siteSet[i] = siteSet[i][:firstSplash];

		# Ignore xxxx.xxx*ignored search content
		firstStar = siteSet[i].find("*");
		if firstStar != -1:
			siteSet[i] = siteSet[i][:firstStar];
		
		# Ignore the newline
		firstNL = siteSet[i].find("\n");
		if firstNL != -1:
			siteSet[i] = siteSet[i][:firstNL];

		# Ignore the string contains no dot
		firstDot = siteSet[i].find(".");
		if firstDot == -1:
			siteSet[i] = "";

	return siteSet;

def genPACFile(siteSet):
	f = file("gfwlist.pac","wt");
	f.write("\
		var strProxy = \"SOCKS5 127.0.0.1:7070;SOCKS 127.0.0.1:7070\";\n\
		function regExpMatch(url, patter) \n\
		{ \n\
			try { \n\
				return new RegExp(pattern).test(url); \n\
			} catch (ex) { \n\
				return false; \n\
			} \n\
		} \n\
		function FindProxyForURL(url, host) \n\
		{\n\
	");
	for i in siteSet:
		if siteSet[i]!="":
			f.write("\t");
			f.write("if (shExpMatch(url, \"");
			f.write("http*://*.");
			f.write(siteSet[i]);
			f.write("*\")) return strProxy;\n");
	
	f.write("\telse return \"DIRECT\";\n}");
	f.close();
	
def main():
	siteSet = getSitesFromGFWList();
	siteSet = cleanUpSiteSet(siteSet);
	genPACFile(siteSet);
	
if __name__ == '__main__':
	main();
