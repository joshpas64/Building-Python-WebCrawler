# Building-Python-WebCrawler
This repo will contain drafts and updates towards making a modern, efficient webcrawler and text processor in Python.
TextProcessorRoughDraft.py contains a class and is an overall program that will read a file and store every unique word (stripping trailing punctuation and converting to the same case) into an object that will store its frequencies in the file
That object (usually a python dictionary object) will then be put into a sorted list order by frequency (HIGHEST FIRST) then alphabetically
FileComparator.py does the same but with two files and stores all the words they have in common as well as frequency, sorting in the previously stated fashion as well.
