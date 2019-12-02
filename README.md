# How to Teach and Learn on the Internet
We examine a [dataset](https://analyse.kmi.open.ac.uk/open_dataset)
from the Open University in the UK. The dataset has granular activity data for
students in 6 classes over a period of 2 years (2013-2014).

- We find statistically significant correlations between specific types of
activities and activity patterns and learning outcomes (class grade).

## Contributors
Ravi Charan ([github](https://github.com/rcharan/))
Gabriel Seeman ([github](https://github.com/gseemann))

## Background
This is our third Flatiron School project (NYC Data Science), for module 4

Se the presentation and conclusions on [Google Slides](https://docs.google.com/presentation/d/1dfHFlbCMSFO3Hv7CUhEBZI7zMS4QV0EXoaoM0IXFb7A/edit?usp=sharing)
or view the pdf in our repository.

## How to use this Repo
There are two Jupyter notebooks, feature-engineering.ipynb and analysis.ipynb.
- *feature-engineer* assembles the dataset and engineers a number of features
related to activity and attention metrics. To use this, you will have to download
the original dataset from the Open University (link above). It is about 500MB. The
directory of csvs as "anonymisedData" in the directory structure.
- *analysis* performs the analysis for the presentation. It works with the 5MB dataset
in the repository

There is also a utilities.py file that provides a number of conveniences for use in the
notebooks.

Software required: statsmodels, pandas, scipy, and seaborn, as well as their dependencies.

We ran this code with:
- Python 3.6
- statsmodels 0.10.1
- pandas 0.25.1
- scipy 1.3.1
- seaborn 0.9.0
