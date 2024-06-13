# SPDX-FileCopyrightText: 2023 ELISA <medical-devices@lists.elisa.tech>
# SPDX-License-Identifier: LGPL-2.1-or-later

import yaml
import pandas as pd
import click
import pprint
from functools import cmp_to_key

# TODO: Make the xlsx_file an argument when calling this script

filter_out_list = ["Covered"]

def compare_items(item1, item2):
    item1_number = int(item1[0].split("-")[-1])
    item2_number = int(item2[0].split("-")[-1])
    return item1_number - item2_number

@click.command()
@click.option('--xlsx_file', help='OpenAPS STPA spreadsheet file')
@click.option('--loss_scenarios_sheet', help='Sheet in OpenAPS STPA spreadsheet file, eg "Level 1 Loss Scenario Analysis"')
@click.option('--output_file', help='Output txt file')
def gen_requirements(xlsx_file, loss_scenarios_sheet, output_file):
    scenario_df = pd.read_excel(xlsx_file, engine='openpyxl', sheet_name=loss_scenarios_sheet)
    requirement_columns = 0
    all_requirements = {}
    identifier = 1

    for row in scenario_df.iterrows():
        data = row[1]
        In = False
        for i in range(1, 9):
            if f"Requirement {str(i)}" in data and type(data[f"Requirement {str(i)}"]) is str:
                requirements = data[f"Requirement {str(i)}"].split("\n")
                for requirement in requirements:
                    if requirement:
                        if requirement[-1] != ".":
                    	    requirement += "."
                        if requirement not in all_requirements.values() and requirement != "-":
                            if all(word not in requirement for word in filter_out_list):
                                all_requirements[f"REQ-{identifier}"] = requirement
                                identifier += 1

    req_string = "\n".join([": ".join(req) for req in sorted(all_requirements.items(), key=cmp_to_key(compare_items))])

    with open(output_file, "w") as file:
        file.write(req_string)
    pprint.pprint(sorted(all_requirements.items(), key=cmp_to_key(compare_items)), width=800)

    return req_string

if __name__ == '__main__':
    gen_requirements()
