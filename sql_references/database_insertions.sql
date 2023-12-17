USE medicarehub;

-- Inserting data into RoomType table
INSERT INTO RoomType (TypeID, TypeDescription) VALUES
(1, 'Normal'),
(2, 'ICU'),
(3, 'Operation Theater');

-- Inserting data into Room table
INSERT INTO Room (RoomNumber, RoomCapacity, RoomTypeID) VALUES
(101, 2, 1),
(201, 1, 2),
(301, 1, 3);

-- Inserting data into Doctor table
INSERT INTO Doctor (DoctorID, FirstName, LastName, PhoneNumber, EmailAddress, JobTitle, Salary) VALUES
(1, 'John', 'Doe', '1234567890', 'john.doe@example.com', 'Cardiologist', 120000),
(2, 'Jane', 'Smith', '9876543210', 'jane.smith@example.com', 'Orthopedic Surgeon', 150000);

-- Inserting data into Nurse table
INSERT INTO Nurse (NurseID, FirstName, LastName, PhoneNumber, EmailAddress, Salary) VALUES
(1, 'Alice', 'Johnson', '5551112222', 'alice.johnson@example.com', 60000),
(2, 'Bob', 'Williams', '5553334444', 'bob.williams@example.com', 55000);

-- Inserting data into WardBoy table
INSERT INTO WardBoy (WardBoyID, FirstName, LastName, PhoneNumber, Salary) VALUES
(1, 'Charlie', 'Brown', '5555555555', 40000),
(2, 'David', 'Wilson', '5556666666', 38000);

-- Inserting data into Patient table
INSERT INTO Patient (PatientID, FirstName, LastName, PhoneNumber, Gender, DateOfBirth, HomeAddress, ChronicDiseases, Balance, NumberOfRecords) VALUES
(1, 'Patient1', 'Lastname1', '1234567890', 1, '1990-01-01', '123 Main St', 'Hypertension', 0, 0),
(2, 'Patient2', 'Lastname2', '9876543210', 2, '1985-05-15', '456 Oak St', 'Diabetes', 0, 0);

-- Inserting data into DiseaseRecord table
INSERT INTO DiseaseRecord (PatientID, AssignedRoomNumber, AssignedDoctorID, DiseaseDescription, PriorityLevel, AdmissionDate, DischargeDate, TreatmentCost, Treatment, Status) VALUES
(1, 101, 1, 'Heart Disease', 2, '2023-01-15', '2023-02-01', 5000, 'Medication', 'Recovered'),
(2, 201, 2, 'Fractured Leg', 1, '2023-02-01', '2023-02-10', 8000, 'Surgery', 'In Treatment');

-- Inserting data into Bill table
INSERT INTO Bill (BillID, PatientID, BillAmount, BillingDate) VALUES
(1, 1, 3000, '2023-02-01'),
(2, 2, 12000, '2023-02-10');
