import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    "CustomerID": ["C-26247", "C-35067", "C-34590", "C-16668", "C-12196", "C-2600", "C-9047", "C-2206", "C-25607", "C-11606"],
    "Name":["Adwaid Krishna","Madhav Hemakumar","Ananjay Pampalli","Abhishek Jain","Arpita Mahapatra","Namritha Mani","Pinchu Alok","Tanya Nair","Gurkirat Singh","Adhil Kareem"],
    "Gender":["M","M","M","M","F","F","M","F","M","M"],
    "Age":[19,18,18,19,18,19,19,18,19,19],
    "Income (USD)": [3472.69, 1184.84, 1266.27, 1369.72, 1939.23, 2944.81, 1957.31, 1403.63, 1604.65, 949.17],
    "Income Stability": ["Low", "Low", "Low", "High", "High", "Low", "Low", "High", "Low", "Working"],
    "Profession": ["Commercial associate", "Working", "Working", "Pensioner", "Pensioner", "Working", "Working", "Pensioner", "Working", "Working"],
    "Type of Employment": ["Managers", "Sales staff", "", "", "", "Sales staff", "Sales staff", "", "", "Laborers"],
    "Location": ["Semi-Urban", "Rural", "Semi-Urban", "Rural", "Urban", "Semi-Urban", "Rural", "Semi-Urban", "Semi-Urban", "Rural"],
    "Loan Amount Request (USD)": [137088.98, 104771.59, 176684.91, 97009.18, 109980, 31465.78, 150334.11, 121029.27, 39475.31, 24703.89]
}
df = pd.DataFrame(data)
df.head()

df.isnull()