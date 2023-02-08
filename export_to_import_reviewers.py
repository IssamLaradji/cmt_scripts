import pandas as pd 

# Import exported data from Excel
fname = "ReviewerInvites.txt"

# read tab delimited .txt file as list of dictionaries
with open(fname, "r") as f:
    lines = f.readlines()
    lines = [line.split("\t") for line in lines]
    # lines = [line[:2] for line in lines]
    # lines = [line for line in lines if len(line) == 2]
    # lines = [line for line in lines if line[1] != ""]   

# convert list of lists to list of dictionaries
lines = [dict(zip([ "First Name", "Last Name", "Email", "Organization"], line)) for line in lines]

# convert list of dictionaries to pandas dataframe
df = pd.DataFrame(lines[1:])

# add "Middle Initial" column between "First Name" and "Last Name"
df.insert(1, "Middle Initial", "")

# save as tab delimited csv file using utf encoding and tab separator
df.to_csv("ReviewerInvites.csv", sep="\t", encoding="UTF-8", index=False)
