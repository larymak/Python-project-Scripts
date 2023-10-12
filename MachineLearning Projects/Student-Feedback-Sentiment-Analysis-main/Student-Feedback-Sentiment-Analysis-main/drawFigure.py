import matplotlib.pyplot as plt
import numpy as np



def make(value , label , category_no):

    fig = plt.figure(figsize=(8,8) , edgecolor='red' , linewidth=10)

    plt.bar(x = ['Positive' , 'Neutral' , 'Negative'] , height = value , color=['blue','gold','red'])
    plt.title(label, fontsize = 24, weight = 'demibold', pad = 15, fontstyle = 'italic' , family = 'cursive')
    plt.xticks(rotation=0 , fontsize=16)
    plt.yticks([])
    plt.xlabel('Feedback Type',fontsize = 18, labelpad=17, weight= 550 , family = 'cursive')
    plt.ylabel('')

    fig.subplots_adjust(bottom = 0.14)
    ax = plt.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)

    for p in ax.patches:
        ax.annotate("%.1f%%" % (100*float(p.get_height()/sum(value))), (p.get_x() + p.get_width() / 2., abs(p.get_height())),
        ha='center', va='bottom', color='black', xytext=(0, 5),rotation = 'horizontal',
        textcoords='offset points', fontsize = 16 , fontweight = 'medium')
        
    plt.savefig(f'./static/plot{category_no}.jpg')

    return
