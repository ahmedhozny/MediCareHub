CREATE DATABASE IF NOT EXISTS MediCareHub;
USE MediCareHub;

-- Patients table
CREATE TABLE IF NOT EXISTS Patient (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,
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
CREATE TABLE IF NOT EXISTS RoomType (
    TypeID INT AUTO_INCREMENT PRIMARY KEY,
    TypeDescription VARCHAR(30)
);

-- Room table
CREATE TABLE IF NOT EXISTS Room (
    RoomID INT AUTO_INCREMENT PRIMARY KEY,
    RoomNumber INT UNIQUE,
    RoomCapacity INT,
    RoomTypeID INT,
    FOREIGN KEY (RoomTypeID) REFERENCES RoomType(TypeID)
);

-- Doctor table
CREATE TABLE IF NOT EXISTS Doctor (
    DoctorID INT AUTO_INCREMENT PRIMARY KEY,
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
CREATE TABLE IF NOT EXISTS Nurse (
    NurseID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    PhoneNumber VARCHAR(11),
    EmailAddress VARCHAR(320),
    RoomNumber INT,
    Salary DECIMAL(10, 2),
    FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber)
);

-- Ward Boys table
CREATE TABLE IF NOT EXISTS WardBoy (
    WardBoyID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    PhoneNumber VARCHAR(11),
    RoomNumber INT,
    Salary DECIMAL(10, 2),
    FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber)
);

-- Disease Record table
CREATE TABLE IF NOT EXISTS DiseaseRecord (
    RecordID INT ,
    PatientID INT,
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
CREATE TABLE IF NOT EXISTS Bill (
    BillID INT AUTO_INCREMENT PRIMARY KEY,
    PatientID INT,
    BillAmount DECIMAL(10, 2),
    BillingDate DATE,
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
);

DELIMITER //
CREATE TRIGGER IF NOT EXISTS BillInsertTrigger
AFTER INSERT ON Bill FOR EACH ROW
BEGIN
    UPDATE Patient
    SET Balance = Balance + NEW.BillAmount
    WHERE PatientID = NEW.PatientID;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER IF NOT EXISTS RecordInsertTrigger
AFTER INSERT ON DiseaseRecord FOR EACH ROW
BEGIN
    UPDATE Patient
    SET Balance = Balance - NEW.TreatmentCost
    WHERE PatientID = NEW.PatientID;
END;
//
DELIMITER ;


DELIMITER //
CREATE TRIGGER IF NOT EXISTS BeforeInsertDiseaseRecord
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
//
DELIMITER ;