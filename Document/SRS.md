# Software Requirement Specification (SRS)
## Project: FinCore — Integrated Banking & Insurance Backend System

**Version:** 1.0
**Status:** Draft
**Date:** 17-08-2026
**Related Document:** [BRD.md](./BRD.md)

---

## 1. Purpose

This document converts the business requirements (from BRD) into clear technical requirements. It lists exactly what the system should do (Functional Requirements) and how well it should perform (Non-Functional Requirements). Developers will use this document to build features, and testers will use it to write test cases.

---

## 2. User Roles

| Role | What they can do |
|---|---|
| **Customer** | Manage own bank account and insurance policies |
| **Bank Employee** | View and manage banking operations (accounts, loans) |
| **Insurance Agent** | View and manage insurance policies and claims |
| **Admin** | Full access to the whole system |

---

## 3. Functional Requirements

Each requirement has a unique ID. These IDs will later be used to link test cases and track progress.

### 3.1 Authentication & User Management

| ID | Requirement |
|---|---|
| FR-01 | System shall allow a new user to register with email, password, and role |
| FR-02 | System shall allow a registered user to log in and receive a JWT access token and refresh token |
| FR-03 | System shall allow a user to refresh their access token using the refresh token |
| FR-04 | System shall store customer KYC details (name, PAN, Aadhar number, address, date of birth) |
| FR-05 | System shall restrict each role to only the actions they are allowed to perform |

### 3.2 Banking

| ID | Requirement |
|---|---|
| FR-06 | System shall allow a customer to open a bank account (savings or current) |
| FR-07 | System shall allow a customer to have more than one bank account |
| FR-08 | System shall allow a customer to deposit money into their account |
| FR-09 | System shall allow a customer to withdraw money, but only if the balance is enough |
| FR-10 | System shall allow a customer to transfer money from one account to another |
| FR-11 | System shall record every deposit, withdrawal, and transfer as a transaction |
| FR-12 | System shall allow a customer to view their transaction history, filtered by date range |
| FR-13 | System shall allow a customer to apply for a loan |
| FR-14 | System shall generate an EMI (installment) schedule when a loan is approved |
| FR-15 | System shall allow an admin or bank employee to freeze or unfreeze an account |

### 3.3 Insurance

| ID | Requirement |
|---|---|
| FR-16 | System shall allow a customer to apply for an insurance policy (life, health, or vehicle) |
| FR-17 | System shall allow a customer to pay a premium for their policy |
| FR-18 | System shall record the history of all premium payments for a policy |
| FR-19 | System shall allow a customer to file a claim against their policy |
| FR-20 | System shall allow an insurance agent to update the status of a claim (pending, approved, rejected) |
| FR-21 | System shall notify the customer when their claim status changes |

### 3.4 Cross-Module (Dashboard)

| ID | Requirement |
|---|---|
| FR-22 | System shall provide a single dashboard API that shows a customer's bank accounts, insurance policies, recent transactions, and claim status together |

### 3.5 Notifications (External API)

| ID | Requirement |
|---|---|
| FR-23 | System shall send an email or SMS alert when a transaction happens |
| FR-24 | System shall send a reminder when a premium payment is due |

### 3.6 Reporting (Admin)

| ID | Requirement |
|---|---|
| FR-25 | System shall allow an admin to view total deposits, active accounts, and active policies |

---

## 4. Non-Functional Requirements

| ID | Requirement | Why it matters |
|---|---|---|
| NFR-01 | API response time should be under 500ms for normal requests | Good user experience |
| NFR-02 | Passwords must be stored in encrypted (hashed) form | Security |
| NFR-03 | All money transactions must be atomic (either fully complete or fully fail, never half-done) | Prevents money loss or duplication |
| NFR-04 | System should have at least 80% test coverage | Code reliability |
| NFR-05 | API should follow REST conventions and return proper HTTP status codes | Easy for other developers to use |
| NFR-06 | System should log all failed login attempts | Security monitoring |
| NFR-07 | API documentation must be available and kept up to date | Easy onboarding for other developers |

---

## 5. Basic Use Cases (Simple Flow Examples)

**Use Case 1: Customer transfers money**
1. Customer logs in
2. Customer selects "transfer money" and enters receiver account + amount
3. System checks if balance is enough
4. If yes, system deducts from sender and adds to receiver, and creates a transaction record
5. If no, system returns an error message

**Use Case 2: Customer files an insurance claim**
1. Customer logs in
2. Customer selects their policy and files a claim with amount and reason
3. System creates the claim with status "pending"
4. Insurance agent reviews and updates status to "approved" or "rejected"
5. Customer receives a notification about the update

---

## 6. What is Not Covered (Out of Scope)

Same as mentioned in BRD.md:
- Mobile app
- Real payment gateway (mock/test mode only)
- Multi-currency support
- Document OCR/upload verification (mock verification API only)

---

## 7. Next Step

After this SRS, the next document will be the **API Design Document** and **ERD (Entity Relationship Diagram)** — these will define the exact database tables, their relationships, and the exact API endpoints (URL, method, request, response) for each functional requirement listed above.
