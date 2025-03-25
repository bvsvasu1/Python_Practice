import re
text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern = r'https://twitter\.com/([a-z0-9_]+)' # todo: type your regex here

match = re.findall(pattern, text, flags=re.IGNORECASE)
print("From 1st text",match)


text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''
pattern = r'Concentration of Risk: ([^\n]+)' # todo: type your regex here

match = re.findall(pattern, text, flags=re.IGNORECASE)
print("From 2nd text",match)


text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''
pattern = r'FY([0-9]+ [a-zA-Z][0-9])' # todo: type your regex here

match = re.findall(pattern, text, flags=re.IGNORECASE)
print("From 3rd text",match)

pattern = 'FY(\d{4} (Q[1-4]|S[1-2]))'

match = re.findall(pattern, text)
print("From 4th text",match)

match = re.findall('FY(\d{4} (?:Q[1-4]|S[1-2]))', text)
print("From 4th text",match)

text = '''
the year is 2025-03-03
'''
pattern = r'\d{4}-\d{1,2}-\d{1,2}' # todo: type your regex here

match = re.findall(pattern, text, flags=re.IGNORECASE)
print("From 5th text",match)

pattern = r'(\d{4})([-.\\\/])(\d{1,2})\2(\d{1,2})' # todo: type your regex here

match = re.findall(pattern, text, flags=re.IGNORECASE)
print("From 6th text",match)
print(map(str,match))
print(''.join(map(str,match)))