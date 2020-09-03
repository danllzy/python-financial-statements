# Python-Financial-Statements
Basic DCF library written in Python. Processes historical financial statements pulled from SimFin and UniBit APIs. 
\n Statements from SimFin sometimes lack interest expense, gross ppe, and accumulated depreciation, hence these are obtained from UniBit
UniBit only allows 50k credits for API calling per month
Calling interest expense and gross ppe data for over 4-5 years costs around 800 credits
SimFin is not perfectly standardised so calculation of categories on pro forma has to be manually done in spreadsheet
Assumptions are all based on average commmon size by default
    
SimFin allows 2k API calls per day
from d_library import *
