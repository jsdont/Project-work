# 📸 Photo Quest

## 📌 Project Overview
Photo Quest is an interactive platform where users participate in photo quests, complete tasks and upload photos.
Tasks may include taking pictures of objects, scenic or thematic shots in specific locations.
Administrators can create new quests, moderate content and track user activity.

## 👥 Team Members
- Aibek Sayat – Frontend Developer  
- Kenzhiyeva Nazerke – Backend Developer  
- Zhumabek Daniyal – UI/UX Designer / Fullstack Developer  

## 🛠️ Stack Technologies
### Backend:
- Django / FastAPI  
- Python  
- PostgreSQL  

### Frontend:
- Angular  
- TypeScript  

## 🎯 Features
### Front-End:
- 📜 **Page with a list of quests** with filtering by category and difficulty.
- 🔍 **Detailed quest page** with description, conditions and examples of completed work.
- 📝 **User registration and authentication** (JWT-based login).
- 📤 **Uploading completed tasks** with the ability to comment and rate.
- 🚀 **Routing between pages** (list of quests, profile, uploaded photos).

### Back-End:
- 🏆 **Models:** `User`, `Quest`, `Submission`, `Category`.
- 🔗 **Associations:** `Quest` is associated with `Category`, `Submission` is associated with `User` and `Quest`.
- 🎛️ **API for working with tasks:** adding new quests, moderating completed tasks.
- 🔐 **Tokenized authentication** (JWT) for users and admins.
