# Use this script when you want to create a large number of NOIDs in batch.
# Specify how many NOIDs you want to generate in 'noidcount' variable, and it will save them to a tsv file.
#
# NOIDs include:
# - Existing collection prefix scheme (1 to 7 characters)
# - Z (universal NOID prefix) Z + year + numeric month
# - 6-digit zero-padded, ascending sequential counter
#
# For this script, you will need to provide: The desired prefix and the number of NOIDs to generate
#
# The following inputs are set by default:
# - Year/month in YYYYMM format. Default reflects the month the script runs
# - The starting number. Default is 1 but can be changed
#
# Documentation on our NOID schema is on Sharepoint here: t.ly/frkDZ


from datetime import datetime
import csv


# Input collection prefix
collection_prefix = "CYLPN"

# Input number of NOIDs to generate as interger
noidcount = 30

# Optional start count variable as interger (exclude preceding zeros)
startcount = 1

# Get date
today = datetime.today()
noiddate = today.strftime('%Y%m')

# Get consecutive count beginning with startcount
counts = range(startcount, startcount + noidcount)
count_list = []

output = f"noid_output{noiddate}.tsv"

with open(output, 'a', newline='') as f:
    csv_writer = csv.writer(f, delimiter='\t')

    for c in counts:
        pcount = str(c).rjust(6, '0')  # save c as padded string
        count_list.append(pcount)  # add each padded string to list
        noidid = collection_prefix + "Z" + noiddate + pcount
        csv_writer.writerow([noidid])

print(f"{noidcount} NOIDs printed to {output}")
