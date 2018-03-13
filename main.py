def bar_plot(
    data, 
    x, 
    y,
    hue='',
    title='',
    x_label='', 
    y_label=''):
   
    ax = sns.barplot(
        x=x,
        y=y,
        data=data, 
        palette=['steelblue'], 
        #hue=hue,
    )
      
    plt.title(title, fontsize=10)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    sns.set_style("white")
    plt.tight_layout() 
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_position(('outward', 5))
    ax.spines['bottom'].set_position(('outward', 5))

    # ax.legend(loc='upper left')
    # plt.xticks(rotation=90)
    # plt.set_xlim=(0,4)
    # plt.xticklabels=[]

    return plt.gcf(), ax
