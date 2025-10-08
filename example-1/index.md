# Example 1

This directory contains example analysis notebooks and data for an example based off of a real life case. The dataset has been scrubbed to remove any identifying information, however the cases are real. For this example, consider the following case facts:

- Latino Male defendant with no prior convictions
- Defendant was in a fight with the victim, shot the victim, and the victim survived
- The defendant is being charged with felony attempted murder 
- The defendant is being charged with a great bodily injury with a firearm enhancement
- The defendant is being offered a plea deal of over 10 years
- The defendant faces potential of life in prison if the case goes to trial due to the charge and enhancements

The defendant's counsel believes the plea offer is very high for this case and that the defendant is being charged as severly as possible. This conduct can be seen as a "wobbler" - under the same conduct, the defendant could have been charged with misdemenor assult with a firearm instead of the felony. The pursual of the enhancement also increases the maximum sentance length. Both the choice of felony charge and enhancement are discretion points that could have racial bias.

As a statistical expert, we are tasked with analyzing if there are racial disparities between our clients case and other "similarly situated" cases. The dataset and definition of "similarly situated" for this case were provided by the counsel. In this case, similarly situated was defined as:

- Case where someone was shot but did not die
- Cases without domestic violence

The counsel identified which cases should be excluded for these reasons. The cousel presented the following specific questions for analysis:

1. When looking at shooting cases (i.e., the cases in our list in which someone was actually shot), how does the rate at which Latino defendants were charged with attempted murder compare to the rate at which White and non-Latino defendants were charged with attempted murder?

2. When looking at shooting cases (i.e., the cases in our list in which someone was actually shot), how does the rate at which Latino defendants were charged with an enhancement pursuant to section 12022.53(d) compare to the rate at which White or non-Latino defendants were charged with that enhancement?

3. When looking at disposed of (i.e. closed/not pending) shooting cases in which someone was shot, how do outcomes and sentences compare for Latino defendants versus for white or non-Latino defendants?
    - In disposed of cases, are Latino defendants more frequently sentenced to prison compared to white or non-latino defendants?
    - In disposed of cases, are Latino defendants less frequently sentenced to probation compared to white or non-latino defendants?
    - In disposed of cases, do Latino defendants less frequently obtain a dismissal of their case as compare to white or non-Latino defendants?
    - On average, are Latino defendants sentenced to prison sentenced to a longer prison term compared to white defendants sentenced to prison?
    - How does the average sentence for Latino defendants charged with a shooting compare to the average sentence for white or non-Latino defendants charged with a shooting?

We take a non-parametric statistical approch to these questions, with analyses present in the corresponding notebooks


