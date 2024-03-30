"""
Process different files that contain transaction histories.

"""
# import csv
import pandas as pd


class AppleCSV():
    fields = [
        "Transaction Date",
        "Clearing Date",
        "Description",
        "Merchant",
        "Category",
        "Type",
        "Amount (USD)",
        "Purchased By"
    ]

    def to_blip(self, bank_data: dict) -> BankBlip:
        pass

class ElanCSV():
    fields = [
        "Date",
        "Transaction",
        "Name",
        "Memo",
        "Amount"
    ]

    def to_blip(self, bank_data: dict) -> BankBlip:
        pass

class DesertFinCSV():
    fields = [
        "Transaction ID",
        "Posting Date",
        "Effective Date",
        "Transaction Type",
        "Amount",
        "Check Number",
        "Reference Number",
        "Description",
        "Transaction Category",
        "Type",
        "Balance",
        "Memo",
        "Extended Description"
    ]

    def to_blip(self, bank_data: dict) -> BankBlip:
        pass

CSV_TYPES: list[class] = {
        AppleCSV,
        DesertFinCSV,
        ElanCSV
}
def importCSV(filename: str) -> pd.DataFrame:
    """Parse a bank file and place the data into the generic Dataframe."""
    # Open the file
	transactions = pd.read_csv(filename)

	# Determine type of imported file


	# Convert to bank_standard headers

def elan_2_blip(bank_data: dict) -> BankBlip:
    pass




def df_2_blip(bank_data: dict) -> BankBlip:
    pass


def compare_lists(this_list: list, that_list: list):
    """Return true if all items in this_list match those in that_list."""
    for element in this_list:
        if element not in that_list:
            return False
    # Inverse to be sure two lists are exactly the same
    for element in that_list:
        if element not in this_list:
            return False
    return True


def get_csv_type(field_list: list) -> str:
    """Determine what type of csv file matches the list of fields.

    Args:
        field_list (list): Normally the first row from a csv file.

    Returns:
        str: a key from the dictionary of csv types
    """
    # Compare field list to all lists in csv types
    for csv_type, columns in CSV_TYPES.items():
        if compare_lists(columns, field_list):
            return csv_type
    return 'NO_MATCH'
