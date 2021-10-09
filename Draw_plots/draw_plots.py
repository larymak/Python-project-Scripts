import matplotlib.pyplot as plt


colors = ["pink","c","lightblue","lavender","lightcoral","wheat","beige"]

def draw_donut(title,values,names,file_name):
    plt.pie(values, autopct='%.2f',colors=colors, rotatelabels =True,labels=names,startangle=150)
    circle = plt.Circle(xy=(0,0),radius=0.75,facecolor='white')
    plt.gca().add_artist(circle)
    plt.title(title)
    plt.savefig('/home/ruth/NFT-study/Ruth/Plots/{}.png'.format(file_name))

def draw_pie(title,values,names,file_name):
    plt.pie(values, autopct='%.2f',colors=colors)
    plt.legend(labels=names)
    plt.title(title)
    plt.savefig('/home/ruth/NFT-study/Ruth/Plots/{}.png'.format(file_name))

def draw_plot(x_values,y_values,x_label,y_label,title,file_name):
    plt.plot(x_values, y_values)
    plt.xlabel (x_label)
    plt.ylabel (y_label)
    plt.title(title)
    plt.xticks(x_values)
    plt.yticks(y_values)
    plt.savefig('/home/ruth/NFT-study/Ruth/Plots/{}.png'.format(file_name))
