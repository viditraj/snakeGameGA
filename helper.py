import matplotlib.pyplot as plt
from IPython import display

plt.ion()


def plot(scores, mean_scores, i):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title(f'Generation-{i}')
    plt.xlabel('Chromosomes')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores) - 1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores) - 1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.savefig(f'Generation-{i}-Score.png')
    plt.pause(.1)
