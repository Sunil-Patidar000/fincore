# API Design Document
## Project: FinCore — Integrated Banking & Insurance Backend System

**Version:** 1.0
**Related Documents:** [BRD.md](./BRD.md), [SRS.md](./SRS.md), [ERD.md](./ERD.md)

**Base URL (local):** `http://localhost:8000/api/`
**Authentication:** JWT (Bearer token in `Authorization` header, except login/register)

---

## 1. Authentication & User Management

| FR | Method | Endpoint | Who can call | Request Body | Response |
|---|---|---|---|---|---|
| FR-01 | POST | `/auth/register/` | Anyone | `username, email, password, role` | `201 Created` — user details |
| FR-02 | POST | `/auth/login/` | Anyone | `username, password` | `200 OK` — `access` and `refresh` tokens |
| FR-03 | POST | `/auth/token/refresh/` | Anyone with refresh token | `refresh` | `200 OK` — new `access` token |
| FR-04 | POST | `/customers/profile/` | Customer | `full_name, pan_number, aadhar_number, dob, address` | `201 Created` — profile details |
| FR-04 | GET | `/customers/profile/` | Customer | — | `200 OK` — own profile details |
| FR-04 | PUT | `/customers/profile/` | Customer | same as POST | `200 OK` — updated profile |

---

## 2. Banking

| FR | Method | Endpoint | Who can call | Request Body | Response |
|---|---|---|---|---|---|
| FR-06 | POST | `/banking/accounts/` | Customer | `account_type, branch` | `201 Created` — account details (auto-generated account number) |
| FR-07 | GET | `/banking/accounts/` | Customer | — | `200 OK` — list of own accounts |
| — | GET | `/banking/accounts/{id}/` | Customer (own) / Employee / Admin | — | `200 OK` — single account details |
| FR-08 | POST | `/banking/accounts/{id}/deposit/` | Customer | `amount` | `200 OK` — new balance + transaction id |
| FR-09 | POST | `/banking/accounts/{id}/withdraw/` | Customer | `amount` | `200 OK` — new balance + transaction id, or `400` if insufficient balance |
| FR-10 | POST | `/banking/accounts/transfer/` | Customer | `from_account, to_account, amount` | `200 OK` — both new balances + transaction id |
| FR-11, FR-12 | GET | `/banking/accounts/{id}/transactions/` | Customer (own) | Query params: `start_date, end_date` | `200 OK` — list of transactions |
| FR-13 | POST | `/banking/loans/` | Customer | `amount, tenure_months, account_id` | `201 Created` — loan details (status: pending) |
| FR-14 | GET | `/banking/loans/{id}/emi-schedule/` | Customer (own) | — | `200 OK` — list of EMI installments |
| FR-13 | POST | `/banking/loans/{id}/approve/` | Bank Employee/Admin | — | `200 OK` — loan approved + EMI schedule auto-generated |
| FR-15 | POST | `/banking/accounts/{id}/freeze/` | Bank Employee/Admin | — | `200 OK` — account status updated |
| FR-15 | POST | `/banking/accounts/{id}/unfreeze/` | Bank Employee/Admin | — | `200 OK` — account status updated |

---

## 3. Insurance

| FR | Method | Endpoint | Who can call | Request Body | Response |
|---|---|---|---|---|---|
| FR-16 | POST | `/insurance/policies/` | Customer | `policy_type, sum_assured, tenure_years` | `201 Created` — policy details (auto-calculated premium) |
| FR-16 | GET | `/insurance/policies/` | Customer | — | `200 OK` — list of own policies |
| FR-17 | POST | `/insurance/policies/{id}/pay-premium/` | Customer | `amount` | `200 OK` — payment confirmation |
| FR-18 | GET | `/insurance/policies/{id}/payments/` | Customer (own) | — | `200 OK` — list of past payments |
| FR-19 | POST | `/insurance/claims/` | Customer | `policy_id, amount, reason` | `201 Created` — claim details (status: pending) |
| FR-20 | GET | `/insurance/claims/` | Customer (own) / Agent (all) | — | `200 OK` — list of claims |
| FR-20 | POST | `/insurance/claims/{id}/update-status/` | Insurance Agent/Admin | `status (approved/rejected), remarks` | `200 OK` — updated claim |

---

## 4. Cross-Module Dashboard

| FR | Method | Endpoint | Who can call | Request Body | Response |
|---|---|---|---|---|---|
| FR-22 | GET | `/customers/dashboard/` | Customer | — | `200 OK` — combined view: accounts, policies, recent transactions, claim status |

---

## 5. Admin & Reporting

| FR | Method | Endpoint | Who can call | Request Body | Response |
|---|---|---|---|---|---|
| FR-25 | GET | `/admin/reports/summary/` | Admin | Query params: `start_date, end_date` | `200 OK` — total deposits, active accounts, active policies |
| FR-25 | GET | `/admin/reports/branch-wise/` | Admin | — | `200 OK` — transaction summary grouped by branch |

---

## 6. Notifications (Internal — triggered automatically, not called directly by users)

| FR | Trigger | Action |
|---|---|---|
| FR-23 | On deposit/withdraw/transfer | Send email/SMS alert to customer |
| FR-24 | On premium due date approaching (scheduled check) | Send reminder to customer |

These are not user-facing endpoints — they are internal functions/services called from within the deposit, withdraw, transfer, and premium logic, and (later) from a scheduled job.

---

## 7. Standard Response Format

To keep things consistent across the whole API, every response will follow this shape:

**Success:**
```json
{
  "success": true,
  "data": { ... },
  "message": "Deposit successful"
}
```

**Error:**
```json
{
  "success": false,
  "error": "Insufficient balance",
  "code": "INSUFFICIENT_BALANCE"
}
```

---

## 8. Common Status Codes Used

| Code | Meaning | Used when |
|---|---|---|
| 200 | OK | Successful GET, or successful action (deposit, transfer, etc.) |
| 201 | Created | New resource created (account, policy, claim) |
| 400 | Bad Request | Validation error (insufficient balance, invalid amount) |
| 401 | Unauthorized | Missing/invalid JWT token |
| 403 | Forbidden | Logged in, but role doesn't allow this action |
| 404 | Not Found | Resource (account/policy/claim) doesn't exist |
| 500 | Server Error | Unexpected error |

---

## 9. Next Step

With BRD, SRS, ERD, and this API design in place, documentation for Sprint 1 is complete. Next step: **actual Django project setup** — virtual environment, project skeleton, and the `accounts` app with the User model and JWT authentication (FR-01, FR-02, FR-03), built using TDD.
