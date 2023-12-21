import datetime

from src.models.model import Model


class MedicalRecord(Model):
    patient_id: int
    room_id: int
    doctor_id: int
    admission_date: datetime.date
    disease_description: str | None
    priority: int | None
    treatment_description: str | None
    treatment_cost: float | None
    discharge_date: datetime.date | None
    status: int | None

    @staticmethod
    def relation_attribute_name() -> dict:
        return (Model.relation_attribute_name() |
                {
                    'PatientID': 'patient_id',
                    'RoomID': 'room_id',
                    'DoctorID': 'doctor_id',
                    'AdmissionDate': 'admission_date',
                    'DiseaseDescription': 'disease_description',
                    'Priority': 'priority',
                    'TreatmentDescription': 'treatment_description',
                    'TreatmentCost': 'treatment_cost',
                    'DischargeDate': 'discharge_date',
                    'Status': 'status'
                })

    def __init__(self, record_id: int | None, patient_id: int, room_id: int, doctor_id: int,
                 admission_date: datetime.date | None, disease_description: str | None = None,
                 priority: int | None = None, treatment_description: str | None = None,
                 treatment_cost: float | None = None, discharge_date: datetime.date | None = None,
                 status: int | None = None) -> None:
        super().__init__(record_id)
        self.patient_id = patient_id
        self.room_id = room_id
        self.doctor_id = doctor_id
        self.admission_date = admission_date
        self.disease_description = disease_description
        self.priority = priority
        self.treatment_description = treatment_description
        self.treatment_cost = treatment_cost
        self.discharge_date = discharge_date
        self.status = status

    def set_disease(self, disease_description: str, priority: int):
        self.disease_description = disease_description
        self.priority = priority
        self.status = 1

    def set_treatment(self, treatment_description: str, treatment_cost: float):
        self.treatment_description = treatment_description
        self.treatment_cost = treatment_cost
        self.status = 2

    def set_discharge(self, discharge_date: datetime.date):
        self.discharge_date = discharge_date
        self.status = 3

    def __str__(self):
        return (
            f"{super().__str__()}, Patient ID: {self.patient_id}, Record ID: {self.id}, Room ID: {self.room_id}, Doctor ID: {self.doctor_id},"
            f"Admission date: {self.admission_date}, Disease: {self.disease_description}, Priority level: {self.priority},"
            f"Treatment: {self.treatment_description}, Treatment cost: {self.treatment_cost}, Discharge date: {self.discharge_date}"
            f"Status: {self.status}")

    def __dict__(self) -> dict:
        return {
            'PatientID': self.patient_id,
            'ID': self.id,
            'RoomID': self.room_id,
            'DoctorID': self.doctor_id,
            'AdmissionDate': self.admission_date,
            'DiseaseDescription': self.disease_description,
            'Priority': self.priority,
            'TreatmentDescription': self.treatment_description,
            'TreatmentCost': self.treatment_cost,
            'DischargeDate': self.discharge_date,
            'Status': self.status
        }
