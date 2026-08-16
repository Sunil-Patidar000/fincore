# Entity Relationship Diagram (ERD)
## Project: FinCore — Integrated Banking & Insurance Backend System

**Version:** 1.0
**Related Documents:** [BRD.md](./BRD.md), [SRS.md](./SRS.md)

---

## 1. Diagram (Mermaid format — renders directly on GitHub)

```mermaid
erDiagram
    USER ||--o| CUSTOMER_PROFILE : "has"
    CUSTOMER_PROFILE ||--o{ ACCOUNT : "owns"
    ACCOUNT ||--o{ TRANSACTION : "has"
    CUSTOMER_PROFILE ||--o{ LOAN : "applies for"
    LOAN ||--o{ EMI_SCHEDULE : "has"
    LOAN }o--|| ACCOUNT : "linked to"
    CUSTOMER_PROFILE ||--o{ POLICY : "owns"
    POLICY ||--o{ PREMIUM_PAYMENT : "has"
    POLICY ||--o{ CLAIM : "has"
    CUSTOMER_PROFILE ||--o{ NOTIFICATION : "receives"

    USER {
        int id PK
        string username
        string email
        string password
        string role
        datetime created_at
    }

    CUSTOMER_PROFILE {
        int id PK
        int user_id FK
        string full_name
        string pan_number
        string aadhar_number
        date dob
        string address
        datetime created_at
    }

    ACCOUNT {
        int id PK
        int customer_id FK
        string account_number
        string account_type
        decimal balance
        string status
        string branch
        datetime created_at
    }

    TRANSACTION {
        int id PK
        int account_id FK
        int related_account_id FK
        string transaction_type
        decimal amount
        decimal balance_after
        string status
        datetime timestamp
    }

    LOAN {
        int id PK
        int customer_id FK
        int account_id FK
        decimal amount
        decimal interest_rate
        int tenure_months
        string status
        datetime created_at
    }

    EMI_SCHEDULE {
        int id PK
        int loan_id FK
        int installment_number
        date due_date
        decimal amount
        string status
    }

    POLICY {
        int id PK
        int customer_id FK
        string policy_type
        decimal sum_assured
        decimal premium_amount
        int tenure_years
        string status
        date start_date
    }

    PREMIUM_PAYMENT {
        int id PK
        int policy_id FK
        decimal amount
        date payment_date
        string status
    }

    CLAIM {
        int id PK
        int policy_id FK
        decimal amount
        string reason
        string status
        date filed_date
        date resolved_date
    }

    NOTIFICATION {
        int id PK
        int customer_id FK
        string message
        string type
        string status
        datetime sent_at
    }
```

---

## 2. Entity Descriptions (Simple English)

### USER
The base login account. Every person (customer, bank employee, insurance agent, admin) has one User record with a role field that decides what they can access.

### CUSTOMER_PROFILE
Extra details for users with role = "customer" — like their KYC info (PAN, Aadhar, address). Linked one-to-one with USER.

### ACCOUNT
A bank account belonging to a customer. One customer can have many accounts (savings, current, etc.).

### TRANSACTION
Every deposit, withdrawal, or transfer creates one transaction record. For a transfer, `related_account_id` stores the other account involved, so we can trace money movement both ways.

### LOAN
A loan applied for by a customer, linked to one of their accounts (where the loan amount gets credited and EMIs get deducted from).

### EMI_SCHEDULE
Each loan is broken into monthly installments. One loan has many EMI_SCHEDULE records (installment 1, 2, 3...).

### POLICY
An insurance policy (life/health/vehicle) owned by a customer.

### PREMIUM_PAYMENT
Every time a customer pays a premium for their policy, one record is created here. One policy can have many payments over its lifetime.

### CLAIM
A claim filed by a customer against their policy. One policy can have multiple claims over time.

### NOTIFICATION
A log of every email/SMS sent to a customer (transaction alerts, premium reminders, claim updates).

---

## 3. Relationship Summary

| Relationship | Type |
|---|---|
| User → Customer Profile | One-to-One |
| Customer Profile → Account | One-to-Many |
| Account → Transaction | One-to-Many |
| Loan → EMI Schedule | One-to-Many |
| Customer Profile → Loan | One-to-Many |
| Customer Profile → Policy | One-to-Many |
| Policy → Premium Payment | One-to-Many |
| Policy → Claim | One-to-Many |
| Customer Profile → Notification | One-to-Many |

---

## 4. Notes for Implementation

- `role` field on USER will use choices: `customer`, `bank_employee`, `insurance_agent`, `admin`
- `account_type` choices: `savings`, `current`
- `transaction_type` choices: `deposit`, `withdrawal`, `transfer_in`, `transfer_out`
- `status` fields (account/loan/policy/claim) will each have their own choice list, defined when building that specific model
- All money fields (`balance`, `amount`, `premium_amount`, `sum_assured`) will use Django's `DecimalField`, never `FloatField` — this avoids rounding errors in financial calculations

---

## 5. Next Document

The **API Design Document** will map each of these entities to actual REST API endpoints (URL, method, request, response) for every functional requirement listed in SRS.md.
