import covid 
import matplotlib.pyplot as plt
covid=covid.Covid()
name=input("enter the country name::")
virusdata=covid.get_status_by_country_name(name)
remove=['id','country','latitude','longitude','last_update']
for i in remove:
    virusdata.pop(i)
all=virusdata.pop('confirmed')
id=list(virusdata.keys())
value=[str(i) for i in virusdata.values()]
plt.pie(value,labels=id,colors=['r','y','g','b'],autopct='%2.1f%%')
plt.title("COUNTRY:"+name.upper() +"\n TOTAL CASES : "+str(all))
plt.legend()
plt.show()
