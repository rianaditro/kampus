import re
import pandas as pd


sample_text = """
    John Doe can be contacted via email at john.doe@example.com or call him at 8000-1234-4567.
    Jane Smith prefers to use jane.smith@mycompany.org and can be reached at 5555-3987-6543.
"""

def search_and_validate_updated(text):
    # Regular expression patterns
    name_pattern = r'[A-Z][a-z]+\s[A-Z][a-z]+'  # Assumes names are in the format: First Last
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    phone_pattern = r'\d{4}-\d{4}-\d{4}'  # Updated pattern to match XXXX-XXXX-XXXX format

    # Search for all matches of names, emails, and phone numbers in the text
    names = re.findall(name_pattern, text)
    emails = re.findall(email_pattern, text)
    phone_numbers = re.findall(phone_pattern, text)

    # Ensure all lists are of the same length by padding missing data with None
    max_len = max(len(names), len(emails), len(phone_numbers))
    names += [None] * (max_len - len(names))
    emails += [None] * (max_len - len(emails))
    phone_numbers += [None] * (max_len - len(phone_numbers))

    # Populate data into a pandas DataFrame
    data = {'Name': names, 'Email': emails, 'Phone': phone_numbers}
    df = pd.DataFrame(data)
    
    return df

df_updated = search_and_validate_updated(sample_text)
print(df_updated)
