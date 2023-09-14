# SPDX-FileCopyrightText: 2023 ELISA <medical-devices@lists.elisa.tech>
# SPDX-License-Identifier: LGPL-2.1-or-later

import yaml
import pandas as pd
import pprint
from functools import cmp_to_key

filter_out_list = ["above", "Either", "EIther", "Fallback", "scope", "overed"]

def compare_items(item1, item2):
    item1_number = int(item1[0].split("-")[-1])
    item2_number = int(item2[0].split("-")[-1])
    return item1_number - item2_number

def gen_requirements(xlsx_file, loss_scenarios_sheet):
    scenario_df = pd.read_excel(xlsx_file, engine='openpyxl', sheet_name=loss_scenarios_sheet)
    requirement_columns = 0
    all_requirements = {}
    identifier = 1

    for row in scenario_df.iterrows():
        data = row[1]
        for i in range(1, 9):
            if f"Requirement {str(i)}" in data and type(data[f"Requirement {str(i)}"]) is str:
                requirements = data[f"Requirement {str(i)}"].split("\n")
                for requirement in requirements:
                    if requirement and requirement not in all_requirements.values() and requirement != "-":
                        if all(word not in requirement for word in filter_out_list):
                            all_requirements[f"REQ-{identifier}"] = requirement
                            identifier += 1

    return sorted(all_requirements.items(), key=cmp_to_key(compare_items))

pprint.pprint(gen_requirements('xlsx_file.xlsx', 'Level 2 Loss Scenario Analysis'), width=800)
