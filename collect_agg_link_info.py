#Scope of this script is to generate select command for aggregation_link, in order to use it as base for aggregation_link deletion
#Declare min, max date
min_date = "to_date('01/02/2017 00:00:00','dd/mm/yyyy hh24:mi:ss')"
max_date = "to_date('01/03/2017 00:00:00','dd/mm/yyyy hh24:mi:ss')"
log_file = "count_aggregation_IDs_Feb2017.log" #Should be modified based on month where deletion is done

#Create command template for start and end
cmd_tpl_start= "sqlplus -s / as sysdba <<EOF > " + log_file + """
set linesize 500
col SUM_UDR_PART_ID for 999999999999999999
col BIGGEST_ID for 999999999999999999
col  LOWEST_ID for 999999999999999999
SELECT TO_CHAR(SYSDATE, 'MM-DD-YYYY HH24:MI:SS') "JOB_START" FROM DUAL;"""

cmd_tpl_end = """SELECT TO_CHAR(SYSDATE, 'MM-DD-YYYY HH24:MI:SS') "JOB_FINISH" FROM DUAL;
quit
EOF"""

#Start constructing command batch


print(cmd_tpl_start)

#Constructing delete commands in the given range and step


cmd_tpl_mid = "select count(SUM_UDR_PART_ID) as TOTAL_IDs, min(SUM_UDR_PART_ID) as LOWEST_ID, max(SUM_UDR_PART_ID) as BIGGEST_ID, trunc(ENTRY_DATE) as DATE_DAY from AGGREGATION_LINK where ENTRY_DATE > %s and ENTRY_DATE < %s group by trunc(ENTRY_DATE) order by trunc(ENTRY_DATE);"


#while b < max_id:
#    if a >= min_id and b < max_id and (a + step_id) < max_id:
#        b = (a+step_id)-1
#        print ("PRINT " + "\"DELETE FROM AGGREGATION_LINK WHERE SUM_UDR_PART_ID BETWEEN " + str(a) + " AND " + str(b) + ";\"")
#        print ("DELETE FROM AGGREGATION_LINK WHERE SUM_UDR_PART_ID BETWEEN " + str(a) + " AND " + str(b) + ";\n"
#               "COMMIT;")
#        a = b + 1
#    elif a < max_id and (a + step_id) > max_id:
#        b = max_id
#        print ("PRINT " + "\"DELETE FROM AGGREGATION_LINK WHERE SUM_UDR_PART_ID BETWEEN " + str(a) + " AND " + str(b) + ";\"")
#        print ("DELETE FROM AGGREGATION_LINK WHERE SUM_UDR_PART_ID BETWEEN " + str(a) + " AND " + str(b) + ";\n"
#               "COMMIT;")
#    else:
#        print ("Values out of range!")
#        break

print("PROMPT " + "Command used: " + cmd_tpl_mid % (min_date,max_date))
print(cmd_tpl_mid % (min_date,max_date))
print(cmd_tpl_end)