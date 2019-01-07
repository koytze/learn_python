#Scope of this script is to generate delete commands for aggregation_link, in order to clear it up to today - 6 months
#Declare min, max and step values
min_id = 17676720822
max_id = 18720879186
step_id = 4000000
log_file = "delete_aggregation_IDs_dec2016.log" #Should be modified based on month where deletion is done

#initialize a,b variables
a = min_id
b = 0

#Create command template for start and end
cmd_tpl_start= "sqlplus -s / as sysdba <<EOF >> " + log_file + """ \n
set linesize 500 \n
col SUM_UDR_PART_ID for 999999999999999999 \n
col BIGGEST_ID for 999999999999999999 \n
col  LOWEST_ID for 999999999999999999 \n
SELECT TO_CHAR(SYSDATE, 'MM-DD-YYYY HH24:MI:SS') "JOB_START" FROM DUAL; \n"""

cmd_tpl_end = """SELECT TO_CHAR(SYSDATE, 'MM-DD-YYYY HH24:MI:SS') "JOB_FINISH" FROM DUAL;\n
quit\n
EOF"""

#Start constructing command batch


print(cmd_tpl_start)

#Constructing delete commands in the given range and step
while b < max_id:
    if a >= min_id and b < max_id and (a + step_id) < max_id:
        b = (a+step_id)-1
        print ("PROMPT " + "\"DELETE FROM AGGREGATION_LINK WHERE SUM_UDR_PART_ID BETWEEN %s AND %s;\"" % (a,b))
        print ("DELETE FROM AGGREGATION_LINK WHERE SUM_UDR_PART_ID BETWEEN %s AND %s;\n"
               "COMMIT;" % (a,b))
        a = b + 1
    elif a < max_id and (a + step_id) > max_id:
        b = max_id
        print ("PROMPT " + "\"DELETE FROM AGGREGATION_LINK WHERE SUM_UDR_PART_ID BETWEEN " + str(a) + " AND " + str(b) + ";\"")
        print ("DELETE FROM AGGREGATION_LINK WHERE SUM_UDR_PART_ID BETWEEN " + str(a) + " AND " + str(b) + ";\n"
               "COMMIT;")
    else:
        print ("Values out of range!")
        break

print(cmd_tpl_end)