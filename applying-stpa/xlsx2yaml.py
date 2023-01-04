import yaml
import pandas as pd

def convertUcaToJson(sheets_file, uca_sheet):
    uca_categories = ["Providing", "Not Providing", "Timing", "Duration"]
    cc_labels = {"Providing":"P", "Not Providing":"NP", "Timing": "T", "Duration": "D"}
    l1_uca_df = pd.read_excel(sheets_file, engine='openpyxl', sheet_name=uca_sheet)
    components = []
    component = {}
    control_action = {}
    for row in l1_uca_df.iterrows():
        data = row[1]
        if type(data['Controller']) is str:
            if component:
                component["Control Actions"].append(control_action)
                components.append(component)
            component = {
                "Text": data['Controller'],
                "Control Actions": [],
                "Controller Constraints": []
            }
            control_action = {}
        if type(data['Control Action']) is str:
            if control_action:
                component["Control Actions"].append(control_action)
            split_control_action = data['Control Action'].split(": ")
            control_action = {
                "Identifier": split_control_action[0].strip(),
                "Text": split_control_action[1].strip(),
                "Unsafe Control Actions": []
            }
        for category in uca_categories:
            if type(data[category]) is str:
                if not data[category].strip():
                    continue
                split_uca = data[category].split(": ")
                control_action["Unsafe Control Actions"].append({
                    "Identifier": split_uca[0].strip(),
                    "Text": split_uca[1].strip(),
                    "Reason": category
                })
                if type(data[cc_labels[category]+" Controller Constraints"]) is str:
                    if not data[cc_labels[category]+" Controller Constraints"].strip():
                        continue
                    controller_constraints = data[cc_labels[category]+" Controller Constraints"].split("\n")
                    for constraint in controller_constraints:
                        split_cc = constraint.split(": ")
                        component["Controller Constraints"].append({
                            "Identifier": split_cc[0].strip(),
                            "Text": split_cc[1].strip(),
                            "Unsafe Control Actions": [split_uca[0].strip()]
                        })

    return yaml.dump({"Components": components})

print(convertUcaToJson('/home/milanlakhani/vsc/openaps-stpa.xlsx', 'Level 1 UCAs'))

