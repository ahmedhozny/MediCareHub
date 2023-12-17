CREATE DATABASE IF NOT EXISTS MediCareHub;
USE MediCareHub;

-- Patients table
CREATE TABLE Patient (
    PatientID INT PRIMARY KEY,
    FirstName VARCHAR(30) NOT NULL,
    LastName VARCHAR(30) NOT NULL,
    PhoneNumber VARCHAR(11) NOT NULL,
    Gender TINYINT NOT NULL,
    DateOfBirth DATE,
    HomeAddress VARCHAR(255),
    ChronicDiseases VARCHAR(1023),
    Balance DECIMAL(10, 2) DEFAULT 0,
    NumberOfRecords INT DEFAULT 0
);

-- Room Type table
CREATE TABLE RoomType (
    TypeID INT PRIMARY KEY,
    TypeDescription VARCHAR(30)
);

-- Room table
CREATE TABLE Room (
    RoomNumber INT PRIMARY KEY,
    RoomCapacity INT,
    RoomTypeID INT,
    FOREIGN KEY (RoomTypeID) REFERENCES RoomType(TypeID)
);

-- Doctor table
CREATE TABLE Doctor (
    DoctorID INT PRIMARY KEY,
    FirstName VARCHAR(30),
    LastName VARCHAR(30),
    PhoneNumber VARCHAR(11),
    EmailAddress VARCHAR(320),
    JobTitle VARCHAR(255),
    OfficeNumber INT,
    Salary DECIMAL(10, 2),
    FOREIGN KEY (OfficeNumber) REFERENCES Room(RoomNumber)
);

-- Nurse table
CREATE TABLE Nurse (
    NurseID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    PhoneNumber VARCHAR(11),
    EmailAddress VARCHAR(320),
    RoomNumber INT,
    Salary DECIMAL(10, 2),
    FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber)
);

-- Ward Boys table
CREATE TABLE WardBoy (
    WardBoyID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    PhoneNumber VARCHAR(11),
    RoomNumber INT,
    Salary DECIMAL(10, 2),
    FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber)
);

-- Disease Record table
CREATE TABLE DiseaseRecord (
    PatientID INT,
    RecordID INT,
    AssignedRoomNumber INT,
    AssignedDoctorID INT,
    DiseaseDescription VARCHAR(255),
    PriorityLevel INT,
    AdmissionDate DATE,
    DischargeDate DATE,
    TreatmentCost DECIMAL(10, 2),
    Treatment VARCHAR(255),
    Status VARCHAR(50),
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    PRIMARY KEY (PatientID, RecordID),
    FOREIGN KEY (AssignedRoomNumber) REFERENCES Room(RoomNumber),
    FOREIGN KEY (AssignedDoctorID) REFERENCES Doctor(DoctorID)
);

-- Bill table
CREATE TABLE Bill (
    BillID INT PRIMARY KEY,
    PatientID INT,
    BillAmount DECIMAL(10, 2),
    BillingDate DATE,
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
);

CREATE TRIGGER BillInsertTrigger
AFTER INSERT ON Bill FOR EACH ROW
BEGIN
    UPDATE Patient
    SET Balance = Balance + NEW.BillAmount
    WHERE PatientID = NEW.PatientID;
END;

CREATE TRIGGER RecordInsertTrigger
AFTER INSERT ON DiseaseRecord FOR EACH ROW
BEGIN
    UPDATE Patient
    SET Balance = Balance - NEW.TreatmentCost
    WHERE PatientID = NEW.PatientID;
END;

CREATE TRIGGER BeforeInsertDiseaseRecord
BEFORE INSERT ON DiseaseRecord FOR EACH ROW
BEGIN
    DECLARE numRecords INT;

    -- Get the number of records for the patient
    SELECT NumberOfRecords INTO numRecords FROM Patient WHERE PatientID = NEW.PatientID;

    -- Increment the count to get the new RecordID
    SET NEW.RecordID = numRecords;
    UPDATE Patient
    SET NumberOfRecords = NumberOfRecords + 1
    WHERE PatientID = NEW.PatientID;
END;
