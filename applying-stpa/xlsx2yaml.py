import yaml
import pandas as pd

def convert_UCAs_to_yml(xlsx_file, uca_sheet):
    uca_categories = ["Providing", "Not Providing", "Timing", "Duration"]
    cc_labels = {"Providing":"P", "Not Providing":"NP", "Timing": "T", "Duration": "D"}
    uca_df = pd.read_excel(xlsx_file, engine='openpyxl', sheet_name=uca_sheet)
    components = []
    component = {}
    control_action = {}
    for row in uca_df.iterrows():
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

    return yaml.dump({"Components": components}, sort_keys=False)

def convert_purpose_to_yml(xlsx_file, purpose_sheet):
    purpose_df = pd.read_excel(xlsx_file, engine='openpyxl', sheet_name=purpose_sheet)
    purpose_dict = {
        "Losses": [],
        "Hazards": [],
        "Constraints": []
    }
    necessary_identifiers = {
        "Losses": [],
        "Hazards": [],
    }
    for index,loss in purpose_df['Losses'].items():
        if type(loss) is str:
            split_loss = loss.split(": ")
            purpose_dict["Losses"].append({
                "Identifier": split_loss[0].strip(),
                "Text": split_loss[1].strip()
            })
            necessary_identifiers["Losses"].append(split_loss[0].strip())
    for index, hazard in purpose_df['Hazards'].items():
        if type(hazard) is str:
            split_hazard = hazard.split(": ")
            losses = []
            for loss in necessary_identifiers["Losses"]:
                if loss in split_hazard[1]:
                    losses.append(loss)
            text = split_hazard[1].strip().split(losses[0])[0][:-1].strip()
            purpose_dict["Hazards"].append({
                "Identifier": split_hazard[0].strip(),
                "Text": text,
                "Losses": losses
            })
            necessary_identifiers["Hazards"].append(split_hazard[0].strip())
    for index, constraint in purpose_df['Scenario Constraints'].items():
        if type(constraint) is str:
            split_constraint = constraint.split(": ")
            hazards = []
            for hazard in necessary_identifiers["Hazards"]:
                if hazard in split_constraint[1]:
                    hazards.append(hazard)
            text = split_constraint[1].strip().split(hazards[0])[0][:-1].strip()
            purpose_dict["Constraints"].append({
                "Identifier": split_constraint[0].strip(),
                "Text": text,
                "Hazards": hazards
            })
    return yaml.dump(purpose_dict, sort_keys=False)

# Shefali function, to be continued
def add_scenarios_to_yml(xlsx_file, scenario_sheet_name, yml_file):
    scenario_df = pd.read_excel(xlsx_file, engine='openpyxl', sheet_name=scenario_sheet_name)


print(convert_UCAs_to_yml('/home/milanlakhani/vsc/openaps-stpa.xlsx', 'Level 1 UCAs'))
print(convert_purpose_to_yml('/home/milanlakhani/vsc/openaps-stpa.xlsx', 'Losses, Hazards and SCs'))

