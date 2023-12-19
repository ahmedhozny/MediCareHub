USE MediCareHub;

-- Inserting data into RoomType table
INSERT INTO RoomType (TypeDescription) VALUES
('Normal'),
('ICU'),
('Operation Theater');

-- Inserting data into Room table
INSERT INTO Room (RoomNumber, TypeID) VALUES
(101, 1),
(201, 2),
(301, 3);

-- Inserting data into Doctor table
INSERT INTO Doctor (FirstName, LastName, Phone, Email, JobTitle, OfficeID, Salary) VALUES
('John', 'Doe', '1234567890', 'john.doe@example.com', 'Cardiologist', 3, 120000),
('Jane', 'Smith', '9876543210', 'jane.smith@example.com', 'Orthopedic Surgeon', 2, 150000);

-- Inserting data into Nurse table
INSERT INTO Nurse (FirstName, LastName, Phone, Email, RoomID, Salary) VALUES
('Alice', 'Johnson', '5551112222', 'alice.johnson@example.com', 2, 60000),
('Bob', 'Williams', '5553334444', 'bob.williams@example.com', 1, 55000);

-- Inserting data into WardBoy table
INSERT INTO WardBoy (FirstName, LastName, Phone, RoomID, Salary) VALUES
('Charlie', 'Brown', '5555555555', 1, 40000),
('David', 'Wilson', '5556666666', 2, 38000);

-- Inserting data into Patient table
INSERT INTO Patient (FirstName, LastName, Phone, Gender, DOB, HomeAddress, ChronicDiseases, Balance, NumberOfRecords) VALUES
('Patient1', 'Lastname1', '1234567890', 1, '1990-01-01', '123 Main St', 'Hypertension', 0, 0),
('Patient2', 'Lastname2', '9876543210', 2, '1985-05-15', '456 Oak St', 'Diabetes', 0, 0);

-- Inserting data into MedicalRecord table
INSERT INTO MedicalRecord (PatientID, RoomID, DoctorID, AdmissionDate, DiseaseDescription, Priority, TreatmentDescription, TreatmentCost, DischargeDate, Status) VALUES
(1, 1, 1, '2023-01-15', 'Heart Disease', 2, 'Medication', 5000, '2023-02-01', 'Recovered'),
(2, 2, 2, '2023-02-01', 'Fractured Leg', 1, 'Surgery', 8000, '2023-02-10', 'In Treatment');

-- Inserting data into Bill table
INSERT INTO Bill (PatientID, BillAmount, BillingDate) VALUES
(1, 3000, '2023-02-01'),
(2, 12000, '2023-02-10');
