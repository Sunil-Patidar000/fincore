# Business Requirement Document (BRD)



## Project: FinCore — Integrated Banking & Insurance Backend System



**Version:** 1.0

**Status:** Draft

**Author:** Sunil Patidar

**Date:** 07/08/2026

---

## 1. Project Overview



FinCore is a backend system that integrates **two core businesses of a financial institution — Banking and Insurance — onto a single platform**. The system enables customers to manage bank accounts, perform transactions, take loans, purchase insurance policies, pay premiums, and file claims — all through a unified backend.

This project simulates the core operations of real-world fintech systems to gain practical exposure to complex business logic, secure transactions, and multi-module integration.

---

## 2. Business Objective / Purpose



* Build a system that demonstrates the core functionality of both banking and insurance domains.


* Provide a single customer profile through which users can manage both their bank accounts and insurance policies.


* Design a financial system with secure, auditable, and role-based access.


* Demonstrate end-to-end workflows through real API integrations (notifications, verification).



---

## 3. Stakeholders



| Role | Description |
| --- | --- |
| **Customer** | End user — account holder, policy holder

 |
| **Bank Employee** | Manages banking operations (account approval, loan review)

 |
| **Insurance Agent** | Manages policies and claims

 |
| **Admin** | Superuser of the entire system — can access/manage everything

 |
| **System (automated)** | Automated processes such as interest calculation, EMI deduction, and notification triggers

 |

---

## 4. High-Level Feature List (Scope)



### Banking Module



* Customer registration & KYC


* Bank account opening (savings/current)


* Deposit, withdrawal, fund transfer


* Transaction history / statement


* Loan application, viewing EMI schedule


* Account freeze/unfreeze (admin action)



### Insurance Module



* Browsing & applying for insurance policies (life/health/vehicle)


* Premium payment (one-time/recurring)


* Filing a claim


* Tracking claim status



### Cross-Module



* Unified customer dashboard (bank accounts + policies + recent activity in one place)


* Checking insurance policy as collateral during loan application (optional advanced feature)



### System-wide



* Role-based authentication (JWT)


* Email/SMS notifications (transaction alerts, premium due reminders, claim updates)


* Admin reporting (total deposits, active policies, branch-wise summary)



---

## 5. Out of Scope (Will not be built in this version)



* Mobile application (only backend API will be built; frontend/mobile is out of scope)


* Real payment gateway integration (only mock/test mode will be used)


* Multi-currency support


* Physical document upload/OCR verification (mock verification API will be used)


* Investment/mutual fund module



---

## 6. Assumptions



* The system will operate in a single currency (INR) only.


* External APIs (email, verification, credit score) will initially be in **mocked/sandbox mode**; production keys can be added later.


* A single customer can hold multiple bank accounts and multiple insurance policies.


* The system is single-tenant (for a single bank/insurance company; multi-bank support is not included).



---

## 7. Constraints



* Development will be done solo/at an individual pace — timeline ~3 weeks (20–25 days), 3–4 hrs/day.


* Fixed tech stack: Django + Django REST Framework + JWT (SimpleJWT).


* Database: PostgreSQL (production-style) / SQLite (local dev, optional).


* Deployment: Cloud-based free/low-cost hosting (Render/Railway) — enterprise-grade infrastructure is out of scope.



---

## 8. Success Criteria



* Smooth end-to-end customer journey: register → KYC → open account → deposit → transfer → apply for loan.


* Smooth insurance customer journey: apply for policy → pay premium → file claim → update claim status.


* All core APIs tested (unit + integration) with reasonable coverage.


* Complete API documentation available (Swagger/Postman).


* Project properly documented on GitHub and in a deployable state.



---

## 9. Next Document



Following the approval/finalization of this BRD, an **SRS (Software Requirement Specification)** will be created, breaking down each feature into technical Functional Requirements (FR) and Non-Functional Requirements (NFR).