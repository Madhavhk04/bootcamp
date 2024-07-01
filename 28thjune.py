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


x = [1, 2, 3, 4, 5, 6]  # x-values
y = [4, 5, 6, 3, 2, 3]  #y-values

plt.plot(x, y, color="green")
plt.title("x vs y")   #to show the title of the visual
plt.xlabel("x axis")  #to set the label of a axix
plt.ylabel("y axis")  #to set the label of y axis
plt.show()