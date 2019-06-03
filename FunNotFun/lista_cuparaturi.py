'''answer=raw_input("createa list ? ")
answer=answer.lower()
while (answer=='y'):
        lista=[]
        no_elem=raw_input("please give the length of the list : ")
        no_elem=int(no_elem)
        for i in range(0,no_elem):
                number=raw_input("plese give the nuber: ")
                lista.append(number)
        print lista
        answer=raw_input("create another list ? ")
        if (answer != 'y'):
                break'''

cumparaturi={}
print (" 0- adaugare \n 1-stergere \n 2-afisare \n 3-iesire \n ")
answ=int(raw_input ("make you selection: "))
while True:
        if (answ == 0):
                elem=raw_input("plese give the key: ")
                if cumparaturi.has_key(elem):
                        print "this element is already in dictionary"
                        answ=int(raw_input ("make you selection: "))
                else:
                        val=raw_input("pleaase give the value: ")
                        cumparaturi.update({elem:val})
                        answ=int(raw_input ("make you selection: "))
                
        if (answ == 1):
                elem=raw_input("plese give the key: ")
                if cumparaturi.has_key(elem):
                        cumparaturi.pop(elem)
                        answ=int(raw_input ("make you selection: "))
                else:
                        print ("the element does not exist")
                        answ=int(raw_input ("make you selection: "))
        if (answ == 2):
                for i in cumparaturi.keys():
                        print i
                for j in cumparaturi.values():
                         print j
                answ=int(raw_input ("make you selection: "))
        if (answ == 3):
                print "goodbye"
                break
                
        
