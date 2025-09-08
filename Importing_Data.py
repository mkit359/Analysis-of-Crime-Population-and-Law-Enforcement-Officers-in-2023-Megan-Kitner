import pandas as pd
import openpyxl
import os

##Creating a definition to call to upload
def upload_info():

    ## Part 1: Create a dataframe to keep the state referencing across tables clean and uniform with a nationally recognized coding system
    FIPS_data = {
        "01": ["Alabama"],
        "02": ["Alaska"],
        "04": ["Arizona"],
        "05": ["Arkansas"],
        "06": ["California"],
        "08": ["Colorado"],
        "09": ["Connecticut"],
        "10": ["Delaware"],
        "11": ["District of Columbia"],
        "12": ["Florida"],
        "13": ["Georgia"],
        "15": ["Hawaii"],
        "16": ["Idaho"],
        "17": ["Illinois"],
        "18": ["Indiana"],
        "19": ["Iowa"],
        "20": ["Kansas"],
        "21": ["Kentucky"],
        "22": ["Louisiana"],
        "23": ["Maine"],
        "24": ["Maryland"],
        "25": ["Massachusetts"],
        "26": ["Michigan"],
        "27": ["Minnesota"],
        "28": ["Mississippi"],
        "29": ["Missouri"],
        "30": ["Montana"],
        "31": ["Nebraska"],
        "32": ["Nevada"],
        "33": ["New Hampshire"],
        "34": ["New Jersey"],
        "35": ["New Mexico"],
        "36": ["New York"],
        "37": ["North Carolina"],
        "38": ["North Dakota"],
        "39": ["Ohio"],
        "40": ["Oklahoma"],
        "41": ["Oregon"],
        "42": ["Pennsylvania"],
        "44": ["Rhode Island"],
        "45": ["South Carolina"],
        "46": ["South Dakota"],
        "47": ["Tennessee"],
        "48": ["Texas"],
        "49": ["Utah"],
        "50": ["Vermont"],
        "51": ["Virginia"],
        "53": ["Washington"],
        "54": ["West Virginia"],
        "55": ["Wisconsin"],
        "56": ["Wyoming"]
    }

    ##Load the data that is currently a dictionary into a DataFrame
    fips = pd.DataFrame.from_dict(FIPS_data,orient='index', columns = ["State"])
    fips.reset_index(inplace=True)
    fips.columns = ["FIPS_ID", "State"]

    ##Part 2.0: File paths to upload the tables from local computer
    paths = {
        '08': r'C:\\Users\\megan\\Documents\\CAPSTONE\\Need\\Ready to Use\\NIBRS_08_2023.xlsx',
        '10': r'C:\\Users\\megan\\Documents\\CAPSTONE\\Need\\Ready to Use\\NIBRS_10_2023.xlsx',
        '26': r'C:\\Users\\megan\\Documents\\CAPSTONE\\Need\\Ready to Use\\NIBRS_26_2023.xlsx',
        '27': r'C:\\Users\\megan\\Documents\\CAPSTONE\\Need\\Ready to Use\\NIBRS_27_2023.xlsx',
        '28': r'C:\\Users\\megan\\Documents\\CAPSTONE\\Need\\Ready to Use\\NIBRS_28_2023.xlsx',
        '29': r'C:\\Users\\megan\\Documents\\CAPSTONE\\Need\\Ready to Use\\NIBRS_29_2023.xlsx',
        '69': r'C:\\Users\\megan\\Documents\\CAPSTONE\\Need\\Ready to Use\\NIBRS_69_2023.xlsx',
        '76': r'C:\\Users\\megan\\Documents\\CAPSTONE\\Need\\Ready to Use\\NIBRS_76_2023.xlsx',
        '77': r'C:\\Users\\megan\\Documents\\CAPSTONE\\Need\\Ready to Use\\NIBRS_77_2023.xlsx',
        '78': r'C:\\Users\\megan\\Documents\\CAPSTONE\\Need\\Ready to Use\\NIBRS_78_2023.xlsx',
        '80': r'C:\\Users\\megan\\Documents\\CAPSTONE\\Need\\Ready to Use\\NIBRS_80_2023.xlsx',
        '81': r'C:\\Users\\megan\\Documents\\CAPSTONE\\Need\\Ready to Use\\NIBRS_81_2023.xlsx',
    }
    ## Part 2.1: Pulls in the datasets while testing to provide info if properly loaded
    NIBRS_dataset = {}

    for id, path in paths.items():
        if os.path.exists(path):
            try:
                NIBRS_dataset[id] = pd.read_excel(path)
                print(f"Successfully uploaded: NIBRS_{id}_2023.xlsx")
            except Exception as ex:
                print(f"Failed to upload NIBRS_{id}_2023.xlsx")
        else:
            print(f"File not located: NIBRS_{id}_2023.xlsx")

    return fips, NIBRS_dataset

# Validating that the datasets uploaded properly
# if __name__ == "__main__":
#     fips, datasets = upload_info()
#     print("\nSummary:")
#     print(f"States DataFrame shape: {fips.shape}")
#     print(f"Number of datasets loaded: {len(datasets)}")
#     for key in datasets:
#         print(f" - Dataset {key} shape: {datasets[key].shape}")
