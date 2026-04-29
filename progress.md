📈 Project Progress: Report2Resolve

This document tracks the development progress, challenges, and work done during the hackathon.

---

🏁 Phase 1: Project Setup (Completed)

- Created GitHub repository and added team members
- Finalized project idea and workflow:
  Citizen → Officer → Worker
- Selected tech stack for development

---

🧱 Phase 2: Core Development (Completed)

Backend & Database

- Developed backend using Python (app.py)
- Used SQLite database (no manual connection required)
- Created tables to store:
  - User details
  - Complaint details (description, category, status, latitude, longitude)

Frontend

- Built separate UI pages for each role:
  - Citizen
  - Officer (Authority)
  - Worker
- Designed complaint reporting form with image upload

---

🎨 Phase 3: UI/UX Design (Completed)

- Implemented a clean light theme UI
- Created simple and user-friendly layouts
- Used card-based design for better readability

---

🛠 Phase 4: Challenges & Fixes (Completed)

- Fixed issues in connecting frontend with backend
- Resolved image upload errors
- Handled database field mismatches
- Debugged routing and page navigation issues

---

🚀 Phase 5: Current Features

- [x] Citizen can report issues with image and description
- [x] Latitude and Longitude captured for location
- [x] Officer can view and assign complaints
- [x] Worker can view tasks and upload "after" image
- [x] Status tracking (Reported → Assigned → Resolved)
- [x] Role-based login system

---

🔄 Phase 6: Work in Progress

- [ ] AI-based complaint classification
- [ ] Duplicate complaint detection

---

📅 Phase 7: Future Scope

- [ ] Map integration using location data
- [ ] Real-time notifications
- [ ] Priority-based complaint handling

---

👥 Team Contributions

- Member 1: UI design for Citizen page
- Member 2: UI design for Officer (Authority) page
- Member 3: UI design for Worker page
- All Members: Backend development (app.py) and database integration

---

✅ Final Status

A working prototype has been successfully developed that demonstrates the complete flow from reporting an issue to resolving it with proper tracking.