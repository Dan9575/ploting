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


def facet(data, 
         col, 
         hue,
          values
         ):
    
    g = sns.FacetGrid(data, 
                     col=col,
                     hue=hue, 
                     col_wrap=4, 
                     #palette=['steelblue', 'silver'], 
                      size=2
                      )
    
    g.map(
        plt.hist, 
        values, 
        bins=np.arange(1, 7), 
        normed=True,
        fill=True,
        alpha=0.7, 
        align='left', 
        stacked=True, 
        histtype='stepfilled', 
        )

    g.set_titles("{col_name}")
    g.add_legend()
    
    g.set(
        xlim=(.5, 6), 
        ylim=(0,1), 
        xticks=np.arange(1, 6), 
        #xlabels=(['']),
        #ylabels=(['']), 
        yticklabels=(['']),
        xticklabels=(['1 (low)', 2, 3, 4, 5])
        )
    return 
