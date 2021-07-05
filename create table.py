from dbms import *
from Tkinter import *
root=Tk()
cur.execute("create table records(name varchar(30) not null,id number,lno number not null,sdate date not null,edate date,pr number,ramt number,rate number,no_intrst number,si number,primary key(id,lno))")
con.commit()
