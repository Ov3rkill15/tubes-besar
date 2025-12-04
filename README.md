# Sistem Layanan Magang (ATS) - MLL Tipe B

![C++](https://img.shields.io/badge/Language-C++-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)

Sistem Layanan Magang adalah aplikasi berbasis konsol (CLI) yang dibangun menggunakan bahasa C++ untuk memfasilitasi proses pelamaran kerja magang mahasiswa. Sistem ini menggunakan struktur data **Multi-Linked List (MLL)** untuk mengelola relasi antara Lowongan (Parent) dan Pelamar (Child).

## 🚀 Fitur Utama

### 1. Multi-Role System
- **Mahasiswa**: Input data diri, melihat lowongan, upload CV, dan menerima notifikasi penerimaan.
- **Dosen**: Memverifikasi lamaran mahasiswa dan melihat rekapitulasi pelamar.
- **Perusahaan**: Membuka lowongan, melihat skor ATS pelamar, review CV, dan memberikan keputusan (Terima/Tolak).
- **Admin**: Mengelola user dan melihat seluruh data sistem.

### 2. Applicant Tracking System (ATS) 🤖
- **CV Scoring**: Sistem otomatis memindai file CV (PDF/TXT) untuk mencari kata kunci relevan (misal: "C++", "Teamwork", "Python").
- **Binary Scanning**: Mendukung pembacaan raw content dari file PDF.
- **Skor**: Setiap kata kunci memberikan poin tambahan pada skor pelamar.

### 3. Manajemen File & CV 📂
- **Upload CV**: Mendukung pemilihan file native Windows (File Picker) untuk format `.pdf` dan `.txt`.
- **File Storage Simulation**: File yang diupload otomatis disalin ke folder lokal `uploads/` dengan penamaan terstruktur.
- **Auto-Cleanup**: Folder `uploads/` otomatis dibersihkan saat aplikasi ditutup untuk menghemat penyimpanan.
- **Integrated Review**: Perusahaan dapat membuka file CV pelamar langsung dari aplikasi sebelum memberikan keputusan.

### 4. Notifikasi Real-time 🔔
- Mahasiswa mendapatkan notifikasi "Pesan" di menu utama jika lamaran mereka diterima oleh perusahaan.

## 🛠️ Teknologi yang Digunakan
- **Bahasa**: C++ (Standard Library)
- **Struktur Data**: Multi-Linked List (MLL) Tipe B
- **OS API**: Windows API (`windows.h`, `commdlg.h`) untuk File Dialog dan File Operations.

## 📦 Cara Menjalankan

### Prasyarat
- Compiler C++ (MinGW / G++)
- Sistem Operasi Windows

### Instalasi & Run
1.  Clone repository ini.
2.  **Cara Mudah (Recommended):**
    Cukup klik dua kali file `run.bat` atau jalankan via terminal:
    ```bash
    ./run.bat
    ```
    Script ini akan otomatis melakukan compile dan menjalankan aplikasi.

3.  **Cara Manual (Alternatif):**
    Jika ingin compile sendiri:
    ```bash
    g++ src/*.cpp -Iinclude -o app.exe -lcomdlg32
    ./app.exe
    ```

## 👥 Akun Demo (Login)

| Role | Username | Password |
| :--- | :--- | :--- |
| **Mahasiswa** | `muhamadalwansuryadi` | `0104` |
| **Dosen** | `dosen1` | `dosen123` |
| **Perusahaan** | `techcorp` | `123` |
| **Admin** | `admin` | `admin123` |

## 📝 Struktur Data (MLL)
- **Parent**: Lowongan Pekerjaan (Double Linked List)
- **Child**: Data Mahasiswa (Single Linked List)
- **Relasi**: Lamaran (Single Linked List yang menghubungkan Parent & Child)

## 📊 Alur Program

```mermaid
graph LR
    %% Setup Styling
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:1px;
    classDef menu fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef term fill:#f9c2ff,stroke:#4a148c,stroke-width:2px;

    %% Main Flow
    Start([Start]) --> Init[Init Data] --> LoginStart{Login Menu}

    subgraph Auth_System [Authentication]
        LoginStart -- "1. Masuk" --> Auth{Cek User}
        LoginStart -- "2. Daftar" --> Register[Register] --> LoginStart
        Auth -- "Gagal" --> LoginStart
    end

    Auth -- "Sukses" --> RoleCheck{Cek Role}

    %% Role Branches (Stacked Vertically in LR mode)
    RoleCheck --> M_Menu
    RoleCheck --> D_Menu
    RoleCheck --> P_Menu
    RoleCheck --> A_Menu

    subgraph R_M [Mahasiswa]
        M_Menu[Menu Mahasiswa] --> M1[1. Input Data]
        M_Menu --> M2[2. Lihat Lowongan]
        M_Menu --> M3[3. Ajukan Lamaran]
        M_Menu --> M4[4. Cek Status]
        M_Menu --> M5[5. Notifikasi]
    end

    subgraph R_D [Dosen]
        D_Menu[Menu Dosen] --> D1[1. Verifikasi]
        D_Menu --> D2[2. Lihat Lowongan]
        D_Menu --> D3[3. Rekap Mhs]
    end

    subgraph R_P [Perusahaan]
        P_Menu[Menu Perusahaan] --> P1[1. Input Lowongan]
        P_Menu --> P2[2. Keputusan]
        P_Menu --> P3[3. Rekap Masuk]
        P_Menu --> P4[4. Cari API]
    end

    subgraph R_A [Admin]
        A_Menu[Menu Admin] --> A1[1. Kelola User]
        A_Menu --> A2[2. Lihat Data]
        A_Menu --> A3[3. Rekap Total]
    end

    %% Logout Routing
    M_Menu -.-> Logout(Logout)
    D_Menu -.-> Logout
    P_Menu -.-> Logout
    A_Menu -.-> Logout
    
    Logout --> LoginStart
    LoginStart -- "0. Keluar" --> End([End])

    %% Apply Styles
    class M_Menu,D_Menu,P_Menu,A_Menu menu;
    class Start,End,Logout term;
```

---
*Dibuat untuk Tugas Besar Struktur Data - Telkom University.*
