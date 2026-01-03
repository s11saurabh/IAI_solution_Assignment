# 🎬 VideoStream - Professional Video Streaming Platform

<div align="center">

![VideoStream Logo](https://img.shields.io/badge/VideoStream-Platform-6366f1?style=for-the-badge)
[![Live Demo](https://img.shields.io/badge/Live-Demo-ec4899?style=for-the-badge)](https://streaming-app-sooty.vercel.app)
[![Video Demo](https://img.shields.io/badge/Video-Demo-f59e0b?style=for-the-badge)](https://drive.google.com/file/d/1Vp3-jJEvPtYLF95Z8YWTjtBgOTKNu-nT/view?usp=sharing)

**A full-stack video streaming platform with AI-powered content analysis, real-time processing, and cinematic UI**

[Live Demo](https://streaming-app-sooty.vercel.app) • [Video Walkthrough](https://drive.google.com/file/d/1Vp3-jJEvPtYLF95Z8YWTjtBgOTKNu-nT/view?usp=sharing) • [Report Bug](https://github.com/s11saurabh/Streaming-Application/issues) • [Request Feature](https://github.com/s11saurabh/Streaming-Application/issues)

</div>

---

<img width="1470" height="792" alt="image" src="https://github.com/user-attachments/assets/ac33d04d-3c71-4c33-a48e-76571be245ab" />
<img width="1470" height="798" alt="image" src="https://github.com/user-attachments/assets/47356bc8-00c3-4258-acc9-7e6e92eebdc6" />
<img width="1463" height="797" alt="image" src="https://github.com/user-attachments/assets/7fbaad3c-f9e2-416d-8aa1-ece45aac4cf6" />
<img width="1470" height="793" alt="image" src="https://github.com/user-attachments/assets/38b96cc2-3248-4d57-9c39-c0989c0ef6cd" />
<img width="1470" height="474" alt="image" src="https://github.com/user-attachments/assets/2406fdc4-e08b-47d8-86c9-4c98d1267292" />
<img width="1470" height="803" alt="image" src="https://github.com/user-attachments/assets/5d3224f2-da22-4af4-9881-0a71b767f3a4" />
<img width="1469" height="800" alt="image" src="https://github.com/user-attachments/assets/175ffc0f-25f5-4df2-b71e-5229c0432a74" />



## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [Deployment](#-deployment)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Demo Video](#-demo-video)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🌟 Overview

**VideoStream** is a professional-grade video streaming platform built with the MERN stack, featuring real-time video processing, AI-powered content analysis, and a stunning 3D animated user interface. The platform supports role-based access control, HTTP range streaming, and WebSocket-based real-time updates.

### 🎯 Key Highlights

- **Real-time Video Processing** with FFmpeg
- **AI Content Sensitivity Analysis**
- **HTTP Range Requests** for smooth streaming
- **WebSocket** real-time progress updates
- **Role-Based Access Control** (Viewer, Editor, Admin)
- **Responsive 3D UI** with GSAP animations
- **Multi-tenant Architecture**
- **Production-Ready** deployment on Render & Vercel

---

## ✨ Features

### 🎥 Video Management

- **Upload Videos** - Drag & drop interface with real-time progress tracking
- **Video Processing** - Automatic metadata extraction and thumbnail generation
- **Streaming** - Adaptive quality streaming with HTTP range support
- **Library Management** - Search, filter, and organize videos
- **Video Analytics** - Track views, processing status, and metadata

### 🔐 Authentication & Authorization

- **JWT Authentication** - Secure token-based authentication
- **Role-Based Access Control** - Three user roles (Viewer, Editor, Admin)
- **Protected Routes** - Frontend and backend route protection
- **Session Management** - Persistent login with token refresh

### 🤖 AI-Powered Features

- **Content Sensitivity Analysis** - AI-based flagging of sensitive content
- **Automatic Tagging** - Smart categorization of videos
- **Metadata Extraction** - Duration, format, codec detection
- **Thumbnail Generation** - Automatic preview image creation

### 🎨 User Interface

- **Cinematic Design** - Premium 3D animations with GSAP
- **Responsive Layout** - Mobile, tablet, and desktop optimized
- **Dark Theme** - Modern gradient-based design system
- **Interactive Components** - Smooth transitions and hover effects
- **Real-time Updates** - Live progress bars and status indicators

### 📊 Admin Features

- **User Management** - View and manage all users
- **Content Moderation** - Review flagged videos
- **Analytics Dashboard** - Platform statistics and insights
- **Role Assignment** - Promote/demote user roles

---

## 🛠️ Tech Stack

### Frontend

| Technology | Purpose |
|------------|---------|
| **React 18** | UI framework with hooks and context API |
| **Vite** | Fast build tool and dev server |
| **React Router v6** | Client-side routing |
| **GSAP** | Professional-grade animations |
| **Axios** | HTTP client with interceptors |
| **Socket.io Client** | Real-time WebSocket communication |
| **React Icons** | Icon library |
| **React Toastify** | Toast notifications |

### Backend

| Technology | Purpose |
|------------|---------|
| **Node.js** | JavaScript runtime |
| **Express.js** | Web application framework |
| **MongoDB** | NoSQL database |
| **Mongoose** | ODM for MongoDB |
| **JWT** | Authentication tokens |
| **Socket.io** | WebSocket server |
| **FFmpeg** | Video processing and thumbnails |
| **Multer** | File upload middleware |
| **Bcrypt** | Password hashing |
| **Winston** | Logging framework |
| **Helmet** | Security headers |

### DevOps & Deployment

| Technology | Purpose |
|------------|---------|
| **Docker** | Containerization |
| **Render** | Backend hosting |
| **Vercel** | Frontend hosting |
| **MongoDB Atlas** | Cloud database |
| **GitHub Actions** | CI/CD (optional) |

---

## 🏗️ Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                         Client Layer                         │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   React     │  │  GSAP        │  │  Socket.io   │       │
│  │   Router    │  │  Animations  │  │  Client      │       │
│  └─────────────┘  └──────────────┘  └──────────────┘       │
└─────────────────────────────────────────────────────────────┘
                            ↕ HTTPS/WSS
┌─────────────────────────────────────────────────────────────┐
│                         API Layer                            │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   Express   │  │  JWT Auth    │  │  Socket.io   │       │
│  │   Routes    │  │  Middleware  │  │  Server      │       │
│  └─────────────┘  └──────────────┘  └──────────────┘       │
└─────────────────────────────────────────────────────────────┘
                            ↕
┌─────────────────────────────────────────────────────────────┐
│                      Business Logic Layer                    │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │ Controllers │  │   Services   │  │   FFmpeg     │       │
│  │             │  │              │  │  Processing  │       │
│  └─────────────┘  └──────────────┘  └──────────────┘       │
└─────────────────────────────────────────────────────────────┘
                            ↕
┌─────────────────────────────────────────────────────────────┐
│                       Data Layer                             │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │  MongoDB    │  │  Mongoose    │  │  File        │       │
│  │  Atlas      │  │  Models      │  │  Storage     │       │
│  └─────────────┘  └──────────────┘  └──────────────┘       │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Upload**: User uploads video → Multer saves to disk → Video document created in MongoDB
2. **Processing**: Background job extracts metadata with FFmpeg → Generates thumbnail → AI analysis
3. **Streaming**: Client requests video → Backend serves with HTTP range support → Smooth playback
4. **Real-time Updates**: Socket.io emits progress events → Client updates UI dynamically

---

## 🚀 Getting Started

### Prerequisites

- **Node.js** >= 18.0.0
- **npm** or **yarn**
- **MongoDB** (local or Atlas)
- **FFmpeg** (for video processing)
- **Git**

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/s11saurabh/Streaming-Application.git
cd Streaming-Application
```

#### 2. Backend Setup
```bash
cd backend

# Install dependencies
npm install

# Install FFmpeg (macOS)
brew install ffmpeg

# Install FFmpeg (Ubuntu/Linux)
sudo apt update
sudo apt install ffmpeg

# Install FFmpeg (Windows)
# Download from https://ffmpeg.org/download.html

# Create .env file
cp .env.example .env

# Edit .env with your configuration
nano .env
```

**Backend `.env` Configuration:**
```env
NODE_ENV=development
PORT=5001

# MongoDB (local)
MONGODB_URI=mongodb://localhost:27017/video-platform

# Or MongoDB Atlas
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/video-platform

# JWT Secret (generate with: node -e "console.log(require('crypto').randomBytes(64).toString('hex'))")
JWT_SECRET=your-super-secret-jwt-key-min-64-characters-long
JWT_EXPIRE=7d

# File Upload
UPLOAD_PATH=./uploads
MAX_FILE_SIZE=524288000
ALLOWED_VIDEO_TYPES=video/mp4,video/avi,video/mkv,video/mov

# Frontend URL
FRONTEND_URL=http://localhost:5173
```

#### 3. Frontend Setup
```bash
cd ../frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Edit .env
nano .env
```

**Frontend `.env` Configuration:**
```env
VITE_API_URL=http://localhost:5001/api
VITE_SOCKET_URL=http://localhost:5001
```

#### 4. Start Development Servers

**Terminal 1 - Backend:**
```bash
cd backend
npm run dev
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

#### 5. Access the Application

- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:5001
- **Health Check:** http://localhost:5001/health

---

## 🔧 Environment Variables

### Backend Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `NODE_ENV` | Environment mode | `development` / `production` |
| `PORT` | Server port | `5001` |
| `MONGODB_URI` | MongoDB connection string | `mongodb://localhost:27017/video-platform` |
| `JWT_SECRET` | Secret for JWT signing | 64+ character random string |
| `JWT_EXPIRE` | Token expiration time | `7d` |
| `UPLOAD_PATH` | Video upload directory | `./uploads` |
| `MAX_FILE_SIZE` | Max upload size in bytes | `524288000` (500MB) |
| `ALLOWED_VIDEO_TYPES` | Allowed MIME types | `video/mp4,video/avi` |
| `FRONTEND_URL` | Frontend URL for CORS | `http://localhost:5173` |

### Frontend Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `VITE_API_URL` | Backend API base URL | `http://localhost:5001/api` |
| `VITE_SOCKET_URL` | WebSocket server URL | `http://localhost:5001` |

---

## 🌐 Deployment

### Backend Deployment (Render)

#### 1. Push to GitHub
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

#### 2. Create Render Account

Go to [Render](https://render.com) and sign up

#### 3. Create Web Service

- **Environment:** Docker
- **Repository:** Your GitHub repo
- **Root Directory:** `backend`
- **Dockerfile Path:** `Dockerfile`
- **Docker Build Context:** `.`

#### 4. Environment Variables (Render)

Add all backend environment variables (see table above)

**Important:**
- `NODE_ENV=production`
- `PORT=10000`
- `FRONTEND_URL=https://your-app.vercel.app` (no trailing slash!)
- `MONGODB_URI=mongodb+srv://...` (MongoDB Atlas)

#### 5. Deploy

Click **Create Web Service** and wait for deployment

**Backend URL:** `https://your-app.onrender.com`

---

### Frontend Deployment (Vercel)

#### 1. Install Vercel CLI
```bash
npm install -g vercel
```

#### 2. Deploy
```bash
cd frontend
vercel login
vercel
```

Follow prompts and set environment variables:
- `VITE_API_URL=https://your-backend.onrender.com/api`
- `VITE_SOCKET_URL=https://your-backend.onrender.com`

#### 3. Production Deployment
```bash
vercel --prod
```

**Frontend URL:** `https://your-app.vercel.app`

---

### MongoDB Atlas Setup

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create free M0 cluster
3. **Database Access:** Create user with password
4. **Network Access:** Add IP `0.0.0.0/0` (allow all)
5. Get connection string
6. Update `MONGODB_URI` in Render

---

## 📚 API Documentation

### Authentication

#### Register User
```http
POST /api/auth/register
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123",
  "role": "viewer",
  "organization": "MyOrg"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIs...",
    "user": {
      "_id": "...",
      "name": "John Doe",
      "email": "john@example.com",
      "role": "viewer"
    }
  }
}
```

#### Login
```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "password123"
}
```

### Videos

#### Upload Video
```http
POST /api/videos
Authorization: Bearer <token>
Content-Type: multipart/form-data

{
  "title": "My Video",
  "description": "Video description",
  "file": <video file>
}
```

#### Get All Videos
```http
GET /api/videos?page=1&limit=12
Authorization: Bearer <token>
```

#### Get Video by ID
```http
GET /api/videos/:id
Authorization: Bearer <token>
```

#### Stream Video
```http
GET /api/stream/:id
Range: bytes=0-
```

#### Get Thumbnail
```http
GET /api/stream/:id/thumbnail
```

#### Analyze Video
```http
POST /api/videos/:id/analyze
Authorization: Bearer <token>
```

### Users (Admin Only)

#### Get All Users
```http
GET /api/users
Authorization: Bearer <token>
```

#### Update User Role
```http
PUT /api/users/:id/role
Authorization: Bearer <token>
Content-Type: application/json

{
  "role": "editor"
}
```

---

## 📁 Project Structure
```
Streaming-Application/
├── backend/
│   ├── config/
│   │   ├── database.js          # MongoDB connection
│   │   └── socket.js            # Socket.io setup
│   ├── controllers/
│   │   ├── authController.js    # Auth logic
│   │   ├── userController.js    # User management
│   │   ├── videoController.js   # Video CRUD
│   │   └── streamController.js  # Video streaming
│   ├── middleware/
│   │   ├── authMiddleware.js    # JWT verification
│   │   ├── roleMiddleware.js    # RBAC
│   │   ├── uploadMiddleware.js  # Multer config
│   │   ├── errorHandler.js      # Error handling
│   │   └── validationMiddleware.js
│   ├── models/
│   │   ├── User.js              # User schema
│   │   └── Video.js             # Video schema
│   ├── routes/
│   │   ├── authRoutes.js
│   │   ├── userRoutes.js
│   │   ├── videoRoutes.js
│   │   └── streamRoutes.js
│   ├── services/
│   │   ├── videoProcessingService.js  # FFmpeg processing
│   │   ├── sensitivityAnalysisService.js
│   │   ├── socketService.js
│   │   └── storageService.js
│   ├── utils/
│   │   ├── logger.js
│   │   ├── constants.js
│   │   ├── helpers.js
│   │   └── responseHandler.js
│   ├── uploads/                 # Video storage
│   ├── .dockerignore
│   ├── .env.example
│   ├── .gitignore
│   ├── Dockerfile
│   ├── package.json
│   └── server.js
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Auth/
│   │   │   │   ├── Login.jsx
│   │   │   │   ├── Register.jsx
│   │   │   │   └── Auth.css
│   │   │   ├── Dashboard/
│   │   │   │   ├── Dashboard.jsx
│   │   │   │   ├── VideoCard.jsx
│   │   │   │   ├── StatusIndicator.jsx
│   │   │   │   └── Dashboard.css
│   │   │   ├── VideoPlayer/
│   │   │   │   ├── VideoPlayer.jsx
│   │   │   │   ├── PlayerControls.jsx
│   │   │   │   └── VideoPlayer.css
│   │   │   ├── VideoUpload/
│   │   │   │   ├── VideoUpload.jsx
│   │   │   │   └── VideoUpload.css
│   │   │   ├── Shared/
│   │   │   │   ├── Navbar.jsx
│   │   │   │   ├── Sidebar.jsx
│   │   │   │   ├── Footer.jsx
│   │   │   │   ├── Loader.jsx
│   │   │   │   ├── Modal.jsx
│   │   │   │   └── ProtectedRoute.jsx
│   │   │   └── AdminPanel/
│   │   │       ├── AdminPanel.jsx
│   │   │       └── UserManagement.jsx
│   │   ├── contexts/
│   │   │   ├── AuthContext.jsx
│   │   │   ├── VideoContext.jsx
│   │   │   └── SocketContext.jsx
│   │   ├── hooks/
│   │   │   ├── useAuth.js
│   │   │   └── useSocket.js
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── DashboardPage.jsx
│   │   │   ├── VideoLibrary.jsx
│   │   │   ├── VideoDetail.jsx
│   │   │   ├── UploadPage.jsx
│   │   │   └── AdminPanelPage.jsx
│   │   ├── services/
│   │   │   ├── api.js
│   │   │   ├── authService.js
│   │   │   └── videoService.js
│   │   ├── styles/
│   │   │   ├── global.css
│   │   │   └── variables.css
│   │   ├── utils/
│   │   │   ├── helpers.js
│   │   │   └── validators.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── App.css
│   ├── .env.example
│   ├── .gitignore
│   ├── index.html
│   ├── package.json
│   ├── vercel.json
│   └── vite.config.js
│
├── .gitignore
├── README.md
└── LICENSE
```

---

## 📸 Screenshots

### Home Page
![Home Page](https://via.placeholder.com/800x400?text=Home+Page+Screenshot)

### Dashboard
![Dashboard](https://via.placeholder.com/800x400?text=Dashboard+Screenshot)

### Video Upload
![Upload](https://via.placeholder.com/800x400?text=Upload+Page+Screenshot)

### Video Player
![Player](https://via.placeholder.com/800x400?text=Video+Player+Screenshot)

### Admin Panel
![Admin](https://via.placeholder.com/800x400?text=Admin+Panel+Screenshot)

---

## 🎥 Demo Video

Watch the full demo walkthrough: [Google Drive Video](https://drive.google.com/file/d/1Vp3-jJEvPtYLF95Z8YWTjtBgOTKNu-nT/view?usp=sharing)

**Demo Highlights:**
- User registration and authentication
- Video upload with progress tracking
- Real-time video processing
- Smooth video streaming
- Admin panel features
- Mobile responsiveness

---

## 🔑 Key Features Explained

### Video Processing Pipeline

1. **Upload**: User selects video file
2. **Validation**: Check file type and size
3. **Storage**: Save to disk with unique filename
4. **Database**: Create video document with status "processing"
5. **Background Job**: 
   - Extract metadata (duration, codec, format)
   - Generate thumbnail at 2-second mark
   - Run AI sensitivity analysis
   - Update database with results
6. **WebSocket**: Emit progress updates to client
7. **Completion**: Mark video as "completed" and ready for streaming

### Streaming Architecture

- **HTTP Range Requests**: Support for seeking and partial content
- **Adaptive Streaming**: Client requests chunks based on playback position
- **CORS Enabled**: Cross-origin video access
- **Base64 Thumbnails**: Embedded in database for fast loading

### Role-Based Access Control

| Role | Permissions |
|------|-------------|
| **Viewer** | View videos, stream content |
| **Editor** | Upload, edit, delete own videos |
| **Admin** | Full access, user management, content moderation |

---

## 🧪 Testing

### Backend Tests
```bash
cd backend
npm test
```

### Frontend Tests
```bash
cd frontend
npm test
```

### E2E Tests
```bash
npm run test:e2e
```

---

## 🐛 Known Issues

- [ ] Large video files (>500MB) may timeout on free-tier deployments
- [ ] Thumbnail generation fails for some video codecs
- [ ] Safari browser may have playback issues with certain formats

---

## 🗺️ Roadmap

- [ ] **Video Transcoding** - Convert videos to multiple formats
- [ ] **Cloudinary Integration** - Cloud-based storage
- [ ] **Advanced Analytics** - View counts, watch time, engagement
- [ ] **Comments System** - User comments and replies
- [ ] **Playlists** - Create and manage video playlists
- [ ] **Live Streaming** - RTMP live streaming support
- [ ] **Subtitles** - SRT/VTT subtitle support
- [ ] **Download** - Allow video downloads
- [ ] **Sharing** - Social media integration
- [ ] **Mobile App** - React Native mobile application

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
```bash
   git checkout -b feature/AmazingFeature
```
3. **Commit your changes**
```bash
   git commit -m 'Add some AmazingFeature'
```
4. **Push to the branch**
```bash
   git push origin feature/AmazingFeature
```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow existing code style
- Write meaningful commit messages
- Add tests for new features
- Update documentation
- Ensure all tests pass

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Developer

**Saurabh Singhania**

- GitHub: [@s11saurabh](https://github.com/s11saurabh)
- Email: saurabhsinghania111@gmail.com


---

## 🙏 Acknowledgments

- **MongoDB** - Database platform
- **Render** - Backend hosting
- **Vercel** - Frontend hosting
- **FFmpeg** - Video processing
- **GSAP** - Animation library
- **React** - UI framework
- **Express** - Backend framework

---

## 📞 Support

If you have any questions or need help, please:

1. **Check existing issues**: [GitHub Issues](https://github.com/s11saurabh/Streaming-Application/issues)
2. **Create a new issue**: [New Issue](https://github.com/s11saurabh/Streaming-Application/issues/new)
3. **Email**: saurabhsinghania111@gmail.com

---

## ⭐ Star History

If you find this project useful, please consider giving it a star!

[![Star History Chart](https://api.star-history.com/svg?repos=s11saurabh/Streaming-Application&type=Date)](https://star-history.com/#s11saurabh/Streaming-Application&Date)

---

<div align="center">

**Made with ❤️ by Saurabh**

[⬆ Back to Top](#-videostream---professional-video-streaming-platform)

</div>
