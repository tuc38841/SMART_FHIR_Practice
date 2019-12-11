import requests
import json
import os


# Sandbox URL
sandbox_url = os.environ.get('SMART_URL')

#test patient = smart-1288992

# Search Number of Patients in Database and Retrieve IDs
def get_patients():
    response = requests.get(sandbox_url + "/Patient")
    response_json = json.loads(response.text)
    patients = response_json['entry']
    patient_id_list = []
    for patient in range(len(patients)):
        patient_id = patients[patient]['resource']['id']
        patient_id_list.append(patient_id)
    print(patient_id_list)

# Search Patient by ID in Sandbox
def search_patient(patient_id):
    response = requests.get(sandbox_url + "/Patient/" + patient_id)
    response_json = json.loads(response.text)
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

# Search Patient's Med List via ID in Sandbox
def get_med_list(patient_id):
    response = requests.get(sandbox_url + "/MedicationOrder?patient=" + patient_id)
    response_json = json.loads(response.text)
    num_of_meds = response_json['entry']
    rxnorm_code_list = []
    medications_list = []
    status_list = []
    for i in range(len(num_of_meds)):
        rxnorm_code = response_json['entry'][i]['resource']['medicationCodeableConcept']['coding'][0]['code']
        medication = response_json['entry'][i]['resource']['medicationCodeableConcept']['text']
        status = response_json['entry'][i]['resource']['status']
        rxnorm_code_list.append(rxnorm_code)
        medications_list.append(medication)
        status_list.append(status)
    print(rxnorm_code_list)
    print(medications_list)
    print(status_list)

