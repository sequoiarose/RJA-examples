from scipy.stats import chi2_contingency
from scipy.stats import PermutationMethod
import matplotlib.pyplot as plt
import polars as pl
import numpy as np

def calculate_residuals(expected, observed): # reused residual calculation code I previously had
    total = sum(expected.drop("Race").sum())
    residual = expected.clone().to_pandas().set_index("Race")
    cols = expected.columns
    cols.remove("Race")
    for r in expected["Race"]:
        for c in cols:
            row_sum = expected.filter(pl.col("Race") == expected["Race"][0]).drop("Race").sum_horizontal()[0]
            col_sum = expected[c].sum()#sum([expected[ind, c] for ind in expected["Race"]])
            ob = observed.filter((pl.col("Race") == r))[c][0]
            exp = expected.filter((pl.col("Race") == r))[c][0]
            residual.at[r,c] = (ob-exp)/np.sqrt(exp*(1-row_sum/total)*(1-col_sum/total))[0]
    return residual
def test(contingency_table):
    res = chi2_contingency(contingency_table.drop("Race").transpose().to_numpy(), method=PermutationMethod(10*4, 123), correction=False)
    print(f"p-value: {res.pvalue}, test stat: {res.statistic}, dof: {res.dof}")

    expected = pl.DataFrame({"Race":contingency_table["Race"].to_list(),
                              contingency_table.columns[1]: res.expected_freq[0],
                              contingency_table.columns[2]: res.expected_freq[1]})
    expected.columns.remove("Race")
    observed = contingency_table
    calculate_residuals(expected, observed)

    display("EXPECTED", expected)
    display("OBSERVED", observed)
    display("RESIDUALS", calculate_residuals(expected,observed))
    return expected, observed

def graph_chi2(expected, observed):
    fig, axs = plt.subplots(1, 3, figsize=(14,4))
    observed.to_pandas().set_index("Race").T.plot.bar(ax=axs[0], width=0.75, #color=color_dict, 
                                                    title="Observed Charge Distribution").legend(bbox_to_anchor=(1,1))
    expected.to_pandas().set_index("Race").T.plot.bar(ax=axs[1], width=0.75,
                                                    #color=color_dict, 
                                                    title= "Expected Charge Distribution").legend(bbox_to_anchor=(1,1))
    calculate_residuals(expected,observed).T.plot.bar(ax=axs[2], width=0.75, #color=color_dict,
                                                    title="Normalized Residuals")
    axs[2].axhline(y = 2, color = 'b', linestyle = '--')
    axs[2].axhline(y = -2, color = 'b', linestyle = '--')
    axs[2].axhline(y = 3, color = 'r', linestyle = '--')
    axs[2].axhline(y = -3, color = 'r', linestyle = '--')
    axs[2].axhline(y = 0, color = 'black')

    plt.legend(bbox_to_anchor=(1,1))
    fig.subplots_adjust(hspace=0.5)
    plt.tight_layout()
    plt.show()