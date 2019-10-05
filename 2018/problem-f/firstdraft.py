# Constraints
# 1) line width >= longest word
# 2) no trailing whitespaces
# 3) words cant be split

#input format
"""
numofwords=int(raw_input())
txtinput=str(raw_input())
wordlist=list(map(str,txtinput.split()))
"""

#arrange to line width
"""
linewidth=21
line=""
linelist=[]
numoflines=0
i=0
while i!=numofwords:
    
    if len(line)+1+len(wordlist[i])>linewidth:
        numoftrailingextraspace=linewidth-len(line)
        for j in range(numoftrailingextraspace):
            line=line+"0"
        linelist.append(line)
        line=""
        numoflines=numoflines+1
        i=i-1
    else:
        if line!="":
            line=line+" "+wordlist[i]
        else:
            line=wordlist[i]
    i=i+1
    
print linelist
"""

#linewidth for loop ranging from longest word to txtinputlength(txtinputlength would not be used in an optimised script but will remain for now till troubleshooting phase passes)
"""
l=length_of_longest_word
for i in range(l,len(txtinput())):
"""

# for adding, index of whitespace coordinates(x) in a line, to a list and then adding that list(y) to a master list(x,y)
"""
line_list=["Thats w at","i me nt 00","w ile that","is what 00","she said 0","b rrpies!0","fil ed as0","that oad a"]
linewidth=10
numoflines=8
index_lines=[]
for ith_line in range(numoflines):
    current_line=line_list[ith_line]
    iteration=0
    index_values=[]
    
    for ith_word in range(linewidth):
        iteration=iteration+1
        if " "==current_line[ith_word]:
            index_values.append(iteration)
    index_lines.append(index_values)
print index_lines
"""         

#for checking the longest river from master list for both diverging(/splitting) and converging(/joining) rivers
#this part is really difficult to implement like i have formed a basic almost foolproof idea as to how to consider all cases using both the face and place values in the 2 related lists lengths and previous_line
previous_line=[6, 8]
for ithlinenumber in range(numoflines-1):
    currentline=index_lines[ithlinenumber]
    for i in previous_line:
        for j in currentline:
            if j!=i and j!=i+1 and j!=i-1:
                ind=0
                a=0
                while j>previous_line[a]:
                    ind=ind+1
                    a=a+1
                previous_line.insert(ind,j)
                lengths.insert(ind,1)
            elif j==i or j==i+1 or j==i-1:

                
                
    placevalues=ithlinenumber

  
    
    
"""
    for upperspace in currentline:
        for lowerspace in nextline:
            placevalues=c
            if upperspace==lowerspace or upperspace+1==lowerspace or upperspace-1==lowerspace:
"""

#list practice
"""
l=[]
l.append("")
a=""
l.append(a)
l.append("")
l[2]=""
print l
"""            
