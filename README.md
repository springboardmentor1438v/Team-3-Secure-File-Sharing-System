# TrustShare–Authentication Module

## Overview

This branch focuses on the **Authentication Module** of TrustShare, a secure file-sharing system. The authentication functionality provides secure user access, identity verification, password recovery, multi-factor authentication, token management, and session management.

## Authentication Features

### 1. User Registration

* User registration through the authentication API.
* User credentials are securely handled.
* Email verification is supported through OTP.

### 2. User Login

* Secure login endpoint.
* Login verification for registered users.
* Unverified users are prevented from accessing protected functionality.

### 3. JWT Authentication

* JWT-based authentication is used for authenticated requests.
* Token refresh functionality is provided.
* Authentication state can be accessed through the current-user endpoint.

### 4. Email OTP Verification

* Six-digit OTP generation.
* OTP verification for email verification.
* OTP expiration handling.
* OTP resend functionality.
* Invalid OTPs are rejected.

### 5. Multi-Factor Authentication (MFA)

* MFA setup functionality.
* MFA verification endpoint.
* Additional verification provides an extra layer of account security.

### 6. Password Recovery

* Forgot-password functionality.
* Password reset using verification mechanisms.
* Change-password functionality for authenticated users.

### 7. Session Management

* Active user sessions can be retrieved.
* Individual sessions can be deleted.
* Session management helps users control authenticated access.

### 8. Google OAuth2

* Google authentication endpoint is included for OAuth-based login.

## Testing

Authentication functionality was tested using the project's automated test suite.

**Latest test result:**

`25 passed`

Additional authentication-focused tests were added to verify:

* OTP contains exactly six digits.
* OTP contains only numeric characters.
* OTP generation produces different codes.

## Technology

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* JWT
* OTP-based verification
* MFA
* OAuth2

## Branch

**Branch:** `Reshma_challa-Authentication-Module`

This branch contains authentication-module testing work for the TrustShare project.
