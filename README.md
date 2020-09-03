# Python-Financial-Statements
Library written in Python to assist DCF calculations. Processes historical financial statements pulled from SimFin and UniBit APIs. Helps to skip some processing steps.

This is a personal project to brush up on my Python so please feel free to give feedback! I will be adding new functions to automate more parts of the process along the way.

**Some Key Info**

-Statements from SimFin sometimes lack interest expense, gross ppe, and accumulated depreciation, hence these are obtained from UniBit

-UniBit only allows 50k credits for API calling per month (which is why I use them only for specific items)

-SimFin allows 2k API calls per day

-SimFin is not perfectly standardised so calculation of categories on pro forma has to be manually done

-Assumptions are all based on average commmon size by default

-Remember to add your api keys to the codes

### Packages used: ###
-pandas

-requests

-datetime

-io

