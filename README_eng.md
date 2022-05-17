# Kata Unittest for ML
This is a small kata putting unittest into practice on DataFrame and saving model. 

## Instructions
First of all, checkout on the branch that gives an empty skeleton :
```
git checkout start
```
Then, the goal is to create a __process__ function that takes a DataFrame as input and :
1. Deletes the desired columns
2. Fills in the missing values: the mean for the numbers and the most present modality for the categories.
3. Handles categories with one-hot encoding

As an input, we can consider the following DataFrame : 
![dataframe_entree](images/dataframe_entree.png)

As an output, we can consider the following DataFrame : 
![dataframe_sortie](images/dataframe_sortie.png)

## Prerequisite

Install the package using this command (for more compliance, you may need to use a `virtualenv`)

```
pip install -r requirements.txt
```

## Test

To test using  `pytest`

```
python -m pytest
```

To test using `unittest`

```
python -m unittest
```

## Solution
To see the proposed solution : 
```
git checkout solution
```
The TIPS.md file also gives advice.