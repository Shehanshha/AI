def rule1(symptoms):
    if 'fever' in symptoms and 'cough' in symptoms and 'runnyNose' in symptoms:
        return 'You may have a cold.'
    return None

def rule2(symptoms):
    if 'fever' in symptoms and 'headache' in symptoms and 'vomiting' in symptoms:
        return 'You may have food poisoning. Drink plenty of fluids and rest.'
    return None

    
def rule3(symptoms):
    if 'nausea' in symptoms and 'weakness' in symptoms:
        return 'You may have Stomach upset.'
    return None
    
def rule4(symptoms):
    if 'headache' in symptoms or 'restlessness' in symptoms:
        return 'You may have Acid reflex.'
    return None

def rule5(symptoms):
    if 'fatigue' in symptoms and 'muscle pain' in symptoms:
        return 'You may have flu.'
    return None    

def rule6(symptoms):
    if 'chestpain' in symptoms and 'shortnessofbreath' in symptoms:
        return 'You may be experiencing a heart attack. Seek emergency medical attention immediately.'
    return None 
def medical_diagnosis(symptoms):
    rules = [rule1, rule2,rule3,rule4,rule5,rule6]
    
    for rule in rules:
        diagnosis = rule(symptoms)
        if diagnosis:
            return diagnosis
    
    return 'No specific diagnosis could be made.'

while True:
    user_symptoms = input("Enter your symptoms : ")

    diagnosis_result = medical_diagnosis(user_symptoms)
    print(diagnosis_result)
