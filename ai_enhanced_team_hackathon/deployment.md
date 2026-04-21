# Deployment Documentation - EcoRide Platform

## 🚀 Live Demo Details
- **Live URL**: [https://ecoride-hackathon.vercel.app](https://ecoride-hackathon.vercel.app)
- **GitHub Repository**: [https://github.com/holbertonschool-ai4devs](https://github.com/holbertonschool-ai4devs)
- **API Status**: Healthy (Deployed on Render/Railway)

## 🏗️ Deployment Platform
Layihənin frontend hissəsi **Vercel**, backend (API) hissəsi isə **Railway** üzərində yerləşdirilmişdir. Bu kombinasiya həm sürətli statik yüklənməni, həm də dinamik API idarəetməsini təmin edir.

## 🛠️ Steps Taken for Deployment

### 1. Frontend (Vercel)
- `product_code/frontend/` qovluğu Vercel-ə "Project Root" kimi təqdim edildi.
- `build` əmri kimi `npm run build` təyin olundu.
- **Environment Variables**: `REACT_APP_API_URL` dəyişəni backend-in Railway URL-inə yönləndirildi.

### 2. Backend (Railway)
- Railway GitHub repozitoriyasına bağlandı.
- `product_code/backend/` qovluğu avtomatik olaraq Node.js mühiti kimi tanındı.
- `PORT` dəyişəni Railway-in daxili port sistemi ilə sinxronlaşdırıldı.

### 3. CI/CD Pipeline
- GitHub-a edilən hər bir `push` əməliyyatı həm Vercel-də, həm də Railway-də avtomatik "re-deploy" prosesini başladır.

## ⚙️ Configuration Details
- **Runtime**: Node.js 18.x
- **Memory Allocation**: 512MB
- **SSL**: Active (HTTPS)

## ✅ Verification
- [x] SSL/HTTPS sertifikatı aktivdir.
- [x] `/api/calculate-impact` endpointi CORS icazələri ilə işləyir.
- [x] Mobil və Desktop brauzerlərdə responsivlik təmin edilib.