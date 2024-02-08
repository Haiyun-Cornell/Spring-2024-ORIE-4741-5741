# Project Ideas

1. **COVID-19 Symptom Data Challenge**
   - Can you identify symptoms to help with early detection of COVID-19?
   - [The COVID-19 Symptom Challenge](https://www.symptomchallenge.org/) can connect you to symptom data for this task; top prize is $50,000!

2. **Who's Ready to Leave? Medical Edition**
   - Hospitals often find that patients take a turn for the worse and return to the hospital right after being released.
   - The percentage of patients who return (within a short time window) is called the *re-admission rate*.
   - Your goal is to help the hospital understand which patients are likely to return, and to recommend which patients are ready for release.
   - *Example data:* [MIMIC III](https://mimic.physionet.org/) is an openly available dataset developed by the MIT Lab for Computational Physiology, comprising deidentified health data associated with >40,000 critical care patients. It includes demographics, vital signs, laboratory tests, medications, and more.

3. **Who's Ready to Leave? Criminal Edition**
   - Prisoners are often released on *parole* for good behavior, but some immediately commit crimes and return to prison.
   - The percentage of prisoners who return (within a short time window) is called the *recidivism rate*.
   - Your goal is to help the government understand which inmates are likely to commit a subsequent crime, and which inmates are ready for parole.
   - Your solution must not discriminate on the basis of a protected class, such as race, sex, or national origin.
   - *Example data:* [COMPAS](https://github.com/propublica/compas-analysis/)

4. **Which Hospital Should I Visit?**
   - Different hospitals can have startlingly different success rates for the same medical problem, and can have startlingly different costs for performing the same procedure.
   - But remember that the best hospitals often attract the most sick patients, and so can appear to have the worst outcomes.
   - Given a particular health condition, which hospital should I visit?
   - *Example data:*
     - [SPARCS Hospital Inpatient Discharges](https://health.data.ny.gov/Health/Hospital-Inpatient-Discharges-SPARCS-De-Identified/u4ud-w55t) record treatment and cost details for a large number of hospitals in NY State.
     - [Medical Expenditure Panel Survey (MEPS)](https://meps.ahrq.gov/mepsweb/) is a set of large-scale surveys of families and individuals, their medical providers, and employers across the United States. MEPS is the most complete source of data on the cost and use of health care and health insurance coverage.
     - [Practice Fusion](https://www.kaggle.com/c/pf2012) is America's fastest-growing Electronic Health Record (EHR) community, with more than 170,000 medical professional users treating 34 million patients in all 50 states. Practice Fusion’s EHR-driven research dataset is used to detect disease outbreaks, identify dangerous drug interactions and compare the effectiveness of competing treatments.

5. **Beat Nate Silver**
   - The 2024 US presidential election is coming. One of the most critical tasks for any electoral campaign is to get out the vote --- and that means getting out the vote for *your* candidate.
   - Predict which districts (or better, which individuals) are likely to support your candidate so that you can route resources to get out *their* vote.
   - *Example data:*
     - The [Ohio Voter File](http://www6.sos.state.oh.us/ords/f?p=111:1) lists every registered voter in Ohio and which elections they've voted in.
     - [Kaggle](https://www.kaggle.com/benhamner/2016-us-election) has data on votes in the 2016 primary election.
     - The [Voting Information Project](https://votinginfoproject.org/) has a list of all polling places in the US.
     - The [Census](http://www.census.gov/topics/income-poverty/poverty/guidance/data-sources/acs-vs-cps.html) administers two surveys each year (the ACS and CPS) covering a range of economic and demographic questions.

6. **Who Gets Credit?**
   - Decide which applications should be approved for credit. The goal for a financial firm would be to offer credit to customers who will pay back their loans.
   - But how can you tell if your model is unfair, either to individuals or to (disadvantaged) groups?
   - *Example data:* [HDMA](https://www.consumerfinance.gov/data-research/hmda/explore) mortgage dataset.

<!-- 7. **Which Algorithm Should I Use?**
   - Meta-learning, or learning-to-learn, is the process of borrowing knowledge from past similar learning tasks to improve performance on a new task in the future.
   - It is an active area in modern-day machine learning research and has strong ties to automated machine learning (AutoML).
   - One important subproblem is to predict how long it will take for a given model (like linear regression) to train on a given dataset.
   - This would help us decide which models to try out when the time budget is limited, which is often the case in practice.
   - *Example data:* We can collect data about how long it takes models to run on a variety of datasets, in order to fit a "meta-model" to predict how long a given model will run on a new dataset.
   - Here is [one such collection of data on runtimes](https://cornell.box.com/s/78x6kt9698ponn3dwkpdhwyikxc7ftoz) (Cornell NetID login required).
   - Talk to TA Chengrun Yang cy438 to discuss.
-->

7. **More Interesting Data Sets and Project Ideas:**
   - [DrivenData](https://www.drivendata.org/competitions/): Data science competitions to build a better world.
   - [InnoCentive](https://www.innocentive.com/): Problem-solving competitions: some with data, some for which you'll need to be creative in hunting down your own datasets!
   - [Dream Challenges](http://dreamchallenges.org/): Biomedical data science challenges (including one with access to a US hospital's COVID data)
   - [Data.gov](https://www.data.gov) The US Federal Government's compendium of data, tools, and resources to conduct research, develop web and mobile applications, design data visualizations, and more. More than 200,000 datasets!
   - [Kaggle data sets](https://www.kaggle.com/datasets): Everything from peer-to-peer lending to speed dating to climate change to university rankings...!
   - [Resource Watch](http://resourcewatch.org/): An open data platform under the [World Resources Institute](http://wri.org/), a global environmental research nonprofit. This platform features over 250 datasets in 10 thematic areas: food, forests, water, energy, climate, cities, biodiversity, conflict, society, and commerce from sources such as NASA, NOAA, the UN, the World Band, the FAO, and more.
   - [Data Science for Social Good](https://dssg.uchicago.edu/projects/): Compiles a list of projects that use data to make the world a better place.
   - [CornellTech Health Hack 2016](https://github.com/imbenzene/datascience2016/blob/master/datasets.pdf): Data sets from a recent hackathon.
   - A curated list of [weather and climate data sources](https://github.com/datacarpentry/NEON-R-Spatio-Temporal-Data-and-Management-Intro/blob/gh-pages/00-spatio-temporal-science-questions.Rmd\#find-temperature-and-precipitation-data), courtesy of [NEON](http://www.neonscience.org/science-design/collection-methods/flux-tower-measurements).
   - [New York State data portal](https://data.ny.gov/)
   - [National Longitudinal Survey of Youth](https://www.bls.gov/nls/nlsy79.htm): A yearly survey dating back to 1979. You might use it to explore how public opinion changes over time.
