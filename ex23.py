import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    # Read a single line of the file language_file
	line = language_file.readline()
	
    # If line has something in it, continue (readline() returns empty string at EOF)
	if line:
		print_line(line, encoding, errors)
        
        # Rerun the main function, this time moving to the next line
		return main(language_file, encoding, errors)
	
	
def print_line(line, encoding, errors):
    # Strip() out the trailing \n on the line string
	next_lang = line.strip()
    
    # Encode language received from language_file into raw bytes
	raw_bytes = next_lang.encode(encoding, errors=errors)
    
    # Decode raw_bytes string back (same as next_lang)
	cooked_string = raw_bytes.decode(encoding, errors=errors)
	
	print(raw_bytes, "<===>", cooked_string)
	
	
# Functions have been defined. Now open the languages.txt file"
languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

#DBES - Decode Bytes Encode Strings