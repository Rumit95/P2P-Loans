# Lending Club Loan Data

This Project is Dataquest's Monthly Challenge.
Data is from year 2007-2019.

LendingClub is a US peer-to-peer lending company, headquartered in San Francisco, California. It was the first peer-to-peer lender to register its offerings as securities with the Securities and Exchange Commission (SEC), and to offer loan trading on a secondary market. LendingClub is the world's largest peer-to-peer lending platform.

Solving this case study will give us an idea about how real business problems are solved using EDA and Machine Learning. In this case study, we will also develop a basic understanding of risk analytics in banking and financial services and understand how data is used to minimise the risk of losing money while lending to customers.

In this challenge, we are to explore using past loan data from Lending Club to build models that can predict if a loan will be paid off on time or not.

## Approach :
We are looking at the problem from the conservative investor's standpoint -- we are more interested in a low False Positive Rate(FPR) than a high True Positive Rate(TPR)

## Goal:
Construct a machine learning model that achieves a TPR greater than 50% while maintaining a FPR less than 7%.

## There are a few variables that are good targets for Loan predictive modelling:

    1. Application outcome (accepted or rejected)
    2. Interest rate (int_rate)
    3. Grade of the loan (grade)
    4. The loan status, if paid or defaulted (loan_status)
Picking Loan Status because it can give a overall Idea on how the borrower's nature is:

If he has defaulted or delayed then it tells us that loan should'nt be given out to such people.
If he pays it back, it means he is trust worthy and indirectly it increases his credit score, Capable of getting a loan.

ref- http://cs229.stanford.edu/proj2015/199_report.pdf
