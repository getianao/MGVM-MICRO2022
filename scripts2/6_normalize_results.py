#!/usr/bin/python3

import sys
import csv

resultsFileName = sys.argv[1]
resultsFile = open(resultsFileName)
csvreader = csv.reader(resultsFile)

outputFileName = sys.argv[2]
outputFile = open(outputFileName, "w+")
csvwriter = csv.writer(outputFile)

header = []
header = next(csvreader)
print(header)

metric_to_row_map = dict()
i = 0
for col in header:
    if col == 'kernel_time':
        metric_to_row_map['kernel_time'] = i
    if col == 'mmu-pw-lat':
        metric_to_row_map['mmu-pw-lat'] = i
    if col == 'pw_local_num':
        metric_to_row_map['pw_local_num'] = i
    if col == 'pw_remote_num':
        metric_to_row_map['pw_remote_num'] = i
    if col == 'local-TLBHit-num-total':
        metric_to_row_map['local-TLBHit-num-total'] = i
    if col == 'remote-TLBHit-num-total':
        metric_to_row_map['remote-TLBHit-num-total'] = i
    # increase i
    i = i + 1

# print(metric_to_row_map)

rows = []
for row in csvreader:
    rows.append(row)


inputFolders = ["private", "private-ideal",
                "shared",   "shared-h1",
                # "mgvm-nobalance",
                "mgvm", "mgvm-ideal1"]

normalised_rows = ["benchmark"]

metrics = ["IPC" , "PW Latency", "L2 TLB Local Hits", "L2 TLB Remote Hits", "PW Acccess Local Hits", "PW Acccess Remote Hits"]

for i in range(len(metrics)):
    normalised_rows.append("")
    for j in range(len(inputFolders)):
        normalised_rows.append(metrics[i] + " " + inputFolders[j])
    
# normalised_rows = ["benchmark",
#         "", "IPC Private", "IPC Shared", "IPC MGVM-NoBalance", "IPC MGVM",
#         "", "PW Latency Private", "PW Latency Shared", "PW Latency MGVM-NoBalance", "PW Latency MGVM",
#         "", "L2 TLB Local Hits Private", "L2 TLB Local Hits Shared", "L2 TLB Local Hits MGVM-NoBalance", "L2 TLB Local Hits MGVM",
#         "", "L2 TLB Remote Hits Private", "L2 TLB Remote Hits Shared", "L2 TLB Remote Hits MGVM-NoBalance", "L2 TLB Remote Hits MGVM",
#         "", "PW Acccess Local Hits Private", "PW Acccess Local Hits Shared", "PW Acccess Local Hits MGVM-NoBalance", "PW Acccess Local Hits MGVM",
#         "", "PW Acccess Remote Hits Private", "PW Acccess Remote Hits Shared", "PW Acccess Remote Hits MGVM-NoBalance", "PW Acccess Remote Hits MGVM",
#         ]
csvwriter.writerow(normalised_rows)

for row in rows:
    nrow = []
    nrow.append(row[0])
    nrow.append("")
    
    # IPC
    metric_name = 'kernel_time'
    data_group = []
    for ii in range(len(inputFolders)):
        # print(row[metric_to_row_map[metric_name]+ ii + 1])
        data_group.append(float(row[metric_to_row_map[metric_name]+ ii + 1]))
    for ii in range(len(inputFolders)):
        # print(data_group[0]/data_group[ii])
        nrow.append(data_group[0]/data_group[ii])
    nrow.append("")

    # PW Latency
    # metric_name = 'mmu-pw-lat'
    # data_group = []
    # for ii in range(len(inputFolders)):
    #     # print(row[metric_to_row_map[metric_name]+ ii + 1])
    #     data_group.append(float(row[metric_to_row_map[metric_name]+ ii + 1]))
    # for ii in range(len(inputFolders)):
    #     # print(data_group[0]/data_group[ii])
    #     nrow.append(data_group[ii]/data_group[0])
    # nrow.append("")
    
    private_pwlat = float(row[metric_to_row_map['mmu-pw-lat'] + 1])
    shared_pwlat = float(row[metric_to_row_map['mmu-pw-lat'] + 2])
    mgvm_nobalance_pwlat  = float(row[metric_to_row_map['mmu-pw-lat'] + 3])
    mgvm_pwlat = float(row[metric_to_row_map['mmu-pw-lat'] + 4])
    nrow.append(private_pwlat/private_pwlat)
    nrow.append(shared_pwlat/private_pwlat)
    nrow.append(mgvm_nobalance_pwlat/private_pwlat)
    nrow.append(mgvm_pwlat/private_pwlat)
    nrow.append("")
    private_local_tlb_hit = float(row[metric_to_row_map['local-TLBHit-num-total'] + 1])
    shared_local_tlb_hit = float(row[metric_to_row_map['local-TLBHit-num-total'] + 2])
    mgvm_nobalance_local_tlb_hit  = float(row[metric_to_row_map['local-TLBHit-num-total'] + 3])
    mgvm_local_tlb_hit = float(row[metric_to_row_map['local-TLBHit-num-total'] + 4])
    private_remote_tlb_hit = float(row[metric_to_row_map['remote-TLBHit-num-total'] + 1])
    shared_remote_tlb_hit = float(row[metric_to_row_map['remote-TLBHit-num-total'] + 2])
    mgvm_nobalance_remote_tlb_hit  = float(row[metric_to_row_map['remote-TLBHit-num-total'] + 3])
    mgvm_remote_tlb_hit = float(row[metric_to_row_map['remote-TLBHit-num-total'] + 4])
    # nrow.append("")
    if((private_local_tlb_hit+private_remote_tlb_hit)==0):
        nrow.append(float('nan'))
    else:
        nrow.append(private_local_tlb_hit/(private_local_tlb_hit+private_remote_tlb_hit))
    if((shared_local_tlb_hit+shared_remote_tlb_hit)==0):
        nrow.append(float('nan'))
    else:
        nrow.append(shared_local_tlb_hit/(shared_local_tlb_hit+shared_remote_tlb_hit))
    nrow.append(mgvm_nobalance_local_tlb_hit/(mgvm_nobalance_local_tlb_hit+mgvm_nobalance_remote_tlb_hit))
    nrow.append(mgvm_local_tlb_hit/(mgvm_local_tlb_hit+mgvm_remote_tlb_hit))
    nrow.append("")
    if((private_local_tlb_hit+private_remote_tlb_hit)==0):
        nrow.append(float('nan'))
    else:
        nrow.append(private_remote_tlb_hit/(private_local_tlb_hit+private_remote_tlb_hit))
    if((shared_local_tlb_hit+shared_remote_tlb_hit)==0):
        nrow.append(float('nan'))
    else:
        nrow.append(shared_remote_tlb_hit/(shared_local_tlb_hit+shared_remote_tlb_hit))
    nrow.append(mgvm_nobalance_remote_tlb_hit/(mgvm_nobalance_local_tlb_hit+mgvm_nobalance_remote_tlb_hit))
    nrow.append(mgvm_remote_tlb_hit/(mgvm_local_tlb_hit+mgvm_remote_tlb_hit))
    nrow.append("")
    private_local_pw_num = float(row[metric_to_row_map['pw_local_num'] + 1])
    shared_local_pw_num = float(row[metric_to_row_map['pw_local_num'] + 2])
    mgvm_nobalance_local_pw_num  = float(row[metric_to_row_map['pw_local_num'] + 3])
    mgvm_local_pw_num = float(row[metric_to_row_map['pw_local_num'] + 4])
    private_remote_pw_num = float(row[metric_to_row_map['pw_remote_num'] + 1])
    shared_remote_pw_num = float(row[metric_to_row_map['pw_remote_num'] + 2])
    mgvm_nobalance_remote_pw_num  = float(row[metric_to_row_map['pw_remote_num'] + 3])
    mgvm_remote_pw_num = float(row[metric_to_row_map['pw_remote_num'] + 4])
    # nrow.append("")
    nrow.append(private_local_pw_num/(private_local_pw_num+private_remote_pw_num))
    if((shared_local_pw_num+shared_remote_pw_num)==0):
        nrow.append(float('nan'))
    else:
        nrow.append(shared_local_pw_num/(shared_local_pw_num+shared_remote_pw_num))
    nrow.append(mgvm_nobalance_local_pw_num/(mgvm_nobalance_local_pw_num+mgvm_nobalance_remote_pw_num))
    nrow.append(mgvm_local_pw_num/(mgvm_local_pw_num+mgvm_remote_pw_num))
    nrow.append("")
    nrow.append(private_remote_pw_num/(private_local_pw_num+private_remote_pw_num))
    if((shared_local_pw_num+shared_remote_pw_num)==0):
        nrow.append(float('nan'))
    else:
        nrow.append(shared_remote_pw_num/(shared_local_pw_num+shared_remote_pw_num))
    nrow.append(mgvm_nobalance_remote_pw_num/(mgvm_nobalance_local_pw_num+mgvm_nobalance_remote_pw_num))
    nrow.append(mgvm_remote_pw_num/(mgvm_local_pw_num+mgvm_remote_pw_num))
    csvwriter.writerow(nrow)

