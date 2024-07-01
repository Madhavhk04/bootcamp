x=[1,2,3,4,5,6]
y=[4,5,6,3,2,3]
plt.plot(x,y,linestyle='-.',marker='*')
#linestyle is used to change the formatting of line so that we can easily identify the lije

x1=[2,4,6,8,10]
y1=[1,2,3,4,5]
plt.plot(x1,y1,color="red",marker="o")

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Multiple plot")
plt.show()


plt.subplot(2,2,1) #2 row and 2 column . ist postion i want the graph 
plt.plot(x,y,'y')

plt.subplot(2,2,2) #2 row and 2 column . 2nd postion i want the graph 
plt.plot(x1,y1,color="red",marker="o")

plt.subplot(2,2,3) #2 row and 2 column . 3rd postion i want the graph 
plt.plot(x,y,'g')