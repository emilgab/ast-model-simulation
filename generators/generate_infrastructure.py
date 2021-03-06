import csv

# Contains number of individual cores/workers for the infrastructure scenario
cores = 8

# Name of the resulting .csv file
csv_filename = "INFRASTRUCTUREFILE.csv"

with open(csv_filename,"w") as csv_file:
    infra_writer = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    infra_writer.writerow(["CoreID","StartTimeAvailable","PerformanceRating","AvailabilityTime"])
    for x in range(1,cores+1):
        infra_writer.writerow(["I"+str(x).zfill(4),"00.00","1","1440"])
