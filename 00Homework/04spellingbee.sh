#Words must be 4 or more
#Middle must be used
#Only the letters shown
#Should have 50 results
#Must run from /mcb185_homework and access data in MCB185/data

#Make a soft-link to the file found in MCB185/data and place it in mcb185_homework
#ln -s ../MCB185/data/dictionary.gz ./sldictionary.gz

#Unzip the gfile and leave the original in tact
#gunzip -c sldictionary.gz | 

#Four or more letter words
#grep -E "\w{4,}" | 

#Selection for words with the given seven letters
#grep -Ev "[bdefghjklmpqstuvwxy]" | 

#Selection for words with the required letter and printout
#grep -Ec "r" | 

#Removal of the soft link for repeated use
#rm sldictionary.gz


ln -s ../MCB185/data/dictionary.gz ./sldictionary.gz | gunzip -c sldictionary.gz | grep -E "\w{4,}" | grep -Ev "[bdefghjklmpqstuvwxy]" | grep -Ec "r"
rm sldictionary.gz
