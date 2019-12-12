import requests
import json
import os

# Sandbox URL
sandbox_url = os.environ.get('SMART_URL')

# Get Request
def get_request(url_parameter, patient_id=""):
    response = requests.get(sandbox_url + url_parameter + patient_id)
    response_json = json.loads(response.text)
    return response_json

# Search Number of Patients in Database and Retrieve IDs
def get_patients():
    response_json = get_request("/Patient")
    patients = response_json['entry']
    patient_id_list = []
    for patient in range(len(patients)):
        patient_id = patients[patient]['resource']['id']
        patient_id_list.append(patient_id)
    print(patient_id_list)

# Search Patient by ID in Sandbox
def search_patient(patient_id):
    response_json = get_request("/Patient/" + patient_id)
    resource_type = response_json['resourceType']
    last_name = response_json['name'][0]['family'][0]
    first_name = response_json['name'][0]['given'][0]
    full_name = first_name + " " + last_name
    gender = response_json['gender']
    dob = response_json['birthDate']
    print("Resource Type: {} \n"
          "Patient: {} \n"
          "Gender: {} \n"
          "Birthdate: {}".format(resource_type, full_name, gender, dob))

# Obtain RXNORM codes and Medication List via Patient ID
def get_med_list(patient_id):
    response_json = get_request("/MedicationOrder?patient=", patient_id)
    medications = response_json['entry']
    rxnorm_code_list = []
    medications_list = []
    status_list = []
    for med in range(len(medications)):
        rxnorm_code = medications[med]['resource']['medicationCodeableConcept']['coding'][0]['code']
        medication = medications[med]['resource']['medicationCodeableConcept']['text']
        status = medications[med]['resource']['status']
        rxnorm_code_list.append(rxnorm_code)
        medications_list.append(medication)
        status_list.append(status)
    print(rxnorm_code_list)
    print(medications_list)
    print(status_list)

# Obtain SNOMED-CT Concepts and Medical Conditions via Patient ID
def get_medical_conditions(patient_id):
    response_json = get_request("/Condition?patient=", patient_id)
    conditions = response_json['entry']
    snomed_code_list = []
    conditions_list = []
    for condition in range(len(conditions)):
        snomed_code = conditions[condition]['resource']['code']['coding'][0]['code']
        med_condition = conditions[condition]['resource']['code']['text']
        snomed_code_list.append(snomed_code)
        conditions_list.append(med_condition)
    print(snomed_code_list)
    print(conditions_list)

# Obtain CVX codes and Immunization History via Patient ID
def get_immunizations(patient_id):
    try:
        response_json = get_request("/Immunization?patient=" + patient_id)
        immunizations = response_json['entry']
        cvx_code_list = []
        immunizations_list = []
        for vaccine in range(len(immunizations)):
            cvx_code = immunizations[vaccine]['resource']['vaccineCode']['coding'][0]['code']
            immunization = immunizations[vaccine]['resource']['vaccineCode']['text']
            cvx_code_list.append(cvx_code)
            immunizations_list.append(immunization)
        print(cvx_code_list)
        print(immunizations_list)
    except Exception as e:
        print(e)
        yes_or_no = input("No immunizations on file. Would you like recommendations based on patient factors? (y or n): ")

























