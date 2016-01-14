#-*- coding:utf-8 -*-
input_data = "adult.data"
input_names = "adult.names"
output_csv = "data.csv"

with open(input_names,"r") as f:
    attrs = [l.split(":")[0] for l in f if l[0] != "|" and ":" in l]
attrs.append("class")
print(len(attrs))
with open(input_data,"r") as input:
    with open(output_csv, "w") as output:
        output.write(",".join(attrs) + "\n")
        for line in input:
            line = ",".join([d.strip() for d in line.split(",")])
            #line = line.replace("?", "")
            output.write(line + "\n")
