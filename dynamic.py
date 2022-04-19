class person:
    name="suchita"
    age=27
pobj=person()
pobj2=person()
print("gender",getattr(pobj,'gender','female'))
person.age=person.age+1
print("age",person.age)
setattr(pobj,'age',28)
print("age",getattr(pobj,'age'))
for att in dir(pobj):
    print (att, getattr(pobj,att))

