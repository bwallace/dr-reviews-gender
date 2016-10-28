import matplotlib as plt
import pylab
import seaborn as sns


'''
print('Parameters: ', res.params)
print('Standard errors: ', res.bse)
print('Predicted values: ', res.predict())
'''

def point_ests_and_CIs(point_estimates, lowers, uppers, names, colors, outf_name, xtitle="title", pval="p<0.001"):
    pylab.clf()
    sns.set_style("white")
    
    #ys = [2.25,1.75,1.25,.75]
    y0 = .75 # lowest point on y-axis
    ys = [y0]
    for _ in names:
        ys.append(ys[-1]+.1)

    ys.reverse() 

    for i in range(len(names)):
        lower = lowers[i]
        upper = uppers[i]
        pylab.plot([lower, upper], [ys[i], ys[i]], alpha=.5, color=colors[i])
        pylab.scatter([point_estimates[i]], [ys[i]], color=colors[i], s=200, alpha=.75)

    #pylab.ylim((0.5,max(ys)))


    lower_x = min(lowers)-.15
    upper_x = max(uppers)+.15
    pylab.xlim((lower_x, upper_x))
    

    locs, labels = pylab.yticks(ys, names)
    pylab.ylim((.8, max(ys)+.05))
    pylab.xlabel(xtitle)
    pylab.text(upper_x-.05, max(ys)+.025, pval)
    prettify_canvas()
    pylab.savefig(outf_name)

def prettify_canvas(big_font=True, turn_off_y=False):
    ax1 = pylab.axes()
    if big_font:
        pylab.setp(ax1.get_xticklabels(), size=14)
        pylab.setp(ax1.get_yticklabels(), size=14)
        pylab.setp(ax1.xaxis.label, size=16)
        pylab.setp(ax1.yaxis.label, size=16)

    if turn_off_y:
        pylab.axes().get_yaxis().set_visible(False)

    #pylab.rcParams['font.family'] = 'sans-serif'
    #pylab.rcParams['font.sans-serif'] = ['Helvetica']
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    pylab.axes().xaxis
    pylab.axes().yaxis
    pylab.tight_layout()

