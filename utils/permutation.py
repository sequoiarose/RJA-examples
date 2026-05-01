from cryptorandom.cryptorandom import SHA256
from cryptorandom.sample import random_sample
from permute.core import two_sample
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

sns.set_theme()

reps = int(10**4)


def sample_indices(inds, k, s): # for permutation
    return(random_sample(inds, k, prng=s))

def get_lists(df, col, cond1, cond2, res_col):
    l1 = df.loc[df[col]==cond1][res_col].to_list()
    l2 = df.loc[df[col]==cond2][res_col].to_list()
    return l1, l2

def prop_test(n, df, test_stat_func, obs_stat, prng, tail, reps = reps, ind_col="Docket", plot=True, plot_title=""):
    test_stats = []
    for i in range(0, reps):
        inds = sample_indices(df[ind_col].to_list(), n, prng)
        test_stats.append(test_stat_func(df.loc[df[ind_col].isin(inds)])) 
    if tail == "greater":
        p_val = sum([stat >= obs_stat for stat in test_stats])/len(test_stats)
    if tail == "less":
        p_val = sum([stat <= obs_stat for stat in test_stats])/len(test_stats)
    if plot: 
        plot_prop_test(test_stats, plot_title, obs_stat)
    print(f"p-value: {round(p_val,5)}, test stat: {round(obs_stat, 5)}")
    return p_val, test_stats

def plot_prop_test(test_stats, title, obs_stat):
    sns.histplot(test_stats, stat="probability", bins=15) 
    plt.title(f"Permutation Distribution of Proportion {title} Under the Null")
    plt.axvline(x=obs_stat, color='red')
    plt.xlabel('Statistic Value')
    plt.ylabel('Count')
    plt.show()

def t_test(group_1, group_2, alternative, prng, plot=True, title="Test Statistic", bins=15):
    p, t, distr = two_sample(group_1, group_2, stat='t', reps=reps, alternative=alternative, keep_dist=True, seed=prng)
    df = len(group_1) + len(group_2) - 2 
    if plot:
        plot_t_test(df, t, distr, title, bins)
    print(f"p-value: {round(p,5)}, test stat: {round(t,5)}")
    return p, t, distr

def plot_t_test(df, t, distr, title, bins):
    plt.hist(distr, density=True, bins=bins, color='blue', alpha=0.6)
    plt.axvline(x=t, color='red')
    plt.title(f"Permutation Distribution of {title} Under the Null")
    plt.grid(True, alpha=0.3)
    plt.show()