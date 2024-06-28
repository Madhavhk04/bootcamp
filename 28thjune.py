import matplotlib.pyplot as plt

# NUMBER OF EMPLOYEE 
dept=["HR","SALES","TECHNICAL","SERVICE"]   #labels
cnt=[23,17,34,21]  #x values 

plt.pie(cnt,labels=dept,autopct="%1.2f%%")
plt.show()


labels=['ML','DS','AI','POWERBI']
sizes=[30,70,50,80]
colors=['lightblue','red','green','yellow']
explode=[0,0,0.3,0]   #exploding only the third slice
plt.pie(sizes,labels=labels,colors=colors,explode=explode,autopct='%1.2f%%',shadow=True,startangle=90)
plt.show()