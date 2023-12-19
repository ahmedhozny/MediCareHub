CREATE DATABASE IF NOT EXISTS MediCareHub;
USE MediCareHub;

-- Patients table
CREATE TABLE IF NOT EXISTS Patient (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(30) NOT NULL,
    LastName VARCHAR(30) NOT NULL,
    Phone VARCHAR(11) NOT NULL,
    Gender TINYINT NOT NULL,
    DOB DATE,
    HomeAddress VARCHAR(255),
    ChronicDiseases VARCHAR(1023),
    Balance DECIMAL(10, 2) DEFAULT 0,
    NumberOfRecords INT DEFAULT 0,
    INDEX phone(Phone)
);

-- Room Type table
CREATE TABLE IF NOT EXISTS RoomType (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    TypeDescription VARCHAR(30) NOT NULL,
    INDEX description(TypeDescription)
);

-- Room table
CREATE TABLE IF NOT EXISTS Room (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    RoomNumber INT UNIQUE NOT NULL,
    TypeID INT NOT NULL,
    FOREIGN KEY (TypeID) REFERENCES RoomType(ID),
    INDEX Room(RoomNumber)
);

-- Doctor table
CREATE TABLE IF NOT EXISTS Doctor (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(30) NOT NULL,
    LastName VARCHAR(30) NOT NULL,
    Phone VARCHAR(11) NOT NULL,
    Email VARCHAR(320) NOT NULL,
    JobTitle VARCHAR(30) NOT NULL,
    OfficeID INT NOT NULL,
    Salary DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (OfficeID) REFERENCES Room(ID),
    INDEX phone(Phone)
);

-- Nurse table
CREATE TABLE IF NOT EXISTS Nurse (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(30) NOT NULL,
    LastName VARCHAR(30) NOT NULL,
    Phone VARCHAR(11) NOT NULL,
    Email VARCHAR(320) NOT NULL,
    RoomID INT NOT NULL,
    Salary DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (RoomID) REFERENCES Room(ID),
    INDEX phone(Phone)
);

-- Ward Boys table
CREATE TABLE IF NOT EXISTS WardBoy (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(30) NOT NULL,
    LastName VARCHAR(30) NOT NULL,
    Phone VARCHAR(11) NOT NULL,
    RoomID INT NOT NULL,
    Salary DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (RoomID) REFERENCES Room(ID),
    INDEX phone(Phone)
);

-- Disease Record table
CREATE TABLE IF NOT EXISTS MedicalRecord (
    PatientID INT,
    ID INT,
    RoomID INT NOT NULL,
    DoctorID INT NOT NULL,
    AdmissionDate DATE,
    DiseaseDescription VARCHAR(1023),
    Priority INT,
    TreatmentDescription VARCHAR(1023),
    TreatmentCost DECIMAL(10, 2),
    DischargeDate DATE,
    Status VARCHAR(50),
    FOREIGN KEY (PatientID) REFERENCES Patient(ID),
    PRIMARY KEY (ID, PatientID),
    FOREIGN KEY (RoomID) REFERENCES Room(ID),
    FOREIGN KEY (DoctorID) REFERENCES Doctor(ID)
);

-- Bill table
CREATE TABLE IF NOT EXISTS Bill (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    PatientID INT NOT NULL,
    BillAmount DECIMAL(10, 2) NOT NULL,
    BillingDate DATETIME DEFAULT NOW(),
    FOREIGN KEY (PatientID) REFERENCES Patient(ID),
    INDEX patient(PatientID)
);

DELIMITER //
CREATE TRIGGER  BillInsertTrigger
AFTER INSERT ON Bill FOR EACH ROW
BEGIN
    UPDATE Patient
    SET Balance = Balance + NEW.BillAmount
    WHERE Patient.ID = NEW.PatientID;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER  RecordInsertTrigger
AFTER UPDATE ON MedicalRecord FOR EACH ROW
BEGIN
    UPDATE Patient
    SET Balance = Balance - NEW.TreatmentCost + OLD.TreatmentCost
    WHERE Patient.ID = NEW.PatientID;
END;
//
DELIMITER ;


DELIMITER //
CREATE TRIGGER  BeforeInsertDiseaseRecord
BEFORE INSERT ON MedicalRecord FOR EACH ROW
BEGIN
    DECLARE numRecords INT;

    -- Get the number of records for the patient
    SELECT NumberOfRecords INTO numRecords FROM Patient WHERE Patient.ID = NEW.PatientID;

    -- Increment the count to get the new RecordID
    SET NEW.ID = numRecords + 1;
    UPDATE Patient
    SET NumberOfRecords = NumberOfRecords + 1
    WHERE Patient.ID = NEW.PatientID;
END;
//
DELIMITER ;