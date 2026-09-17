# TrustShare - Area 4: Authentication & User Management

**Developer:** Alan Shiju
**Module:** Area 4 (Frontend)
**Tech Stack:** Next.js, React, Tailwind CSS, Axios, Lucide Icons

## Overview

This branch contains the completed Area 4 frontend requirements for the TrustShare Secure File-Sharing System. It implements the secure client-side authentication shell, user profile management, and global API request interception required to communicate with the FastAPI backend.

## Key Features Implemented

- **Global JWT Interceptor (`lib/api.js`):**
  Engineered a custom Axios instance with request/response interceptors. It securely retrieves the `trustshare_access_token` from `localStorage` and automatically injects it as a Bearer token into the `Authorization` header of every outgoing API request.
- **Authentication UI (`app/login/page.js`):**
  Built a responsive, glassmorphism-styled combined Login and Registration interface. Includes form validation, dynamic state toggling, error handling, and a conditional UI for TOTP Multi-Factor Authentication (MFA) codes.
- **User Profile Dashboard (`app/profile/page.js`):**
  Created a protected route that retrieves and displays the active user's session data (username, email, role) and includes the frontend state toggle for enabling/disabling MFA.
- **Security Settings (`app/settings/page.js`):**
  Developed the account settings interface allowing users to securely update their passwords with client-side matching validation and simulated network loading states.
- **Navigation Integration (`components/Navbar.jsx`):**
  Upgraded the global navigation bar to include a dynamic, state-driven user dropdown menu linking directly to the new Profile and Settings routes.

## Client-Side Security Architecture

- **State Management:** Utilizes React `useState` and `useEffect` alongside Next.js `'use client'` directives for secure browser-side rendering.
- **Route Protection:** Implemented checks on the Profile and Settings pages that immediately redirect unauthenticated users back to `/login` if a valid session is not found in local storage.

## How to Run Locally

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
