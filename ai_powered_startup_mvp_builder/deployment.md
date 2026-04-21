# Deployment Documentation - EcoRide MVP

## ?? Live Access
- **Live URL**: [https://ecoride-mvp-demo.vercel.app](https://ecoride-mvp-demo.vercel.app)
- **GitHub Repository**: [https://github.com/holbertonschool-ai4devs](https://github.com/holbertonschool-ai4devs)

## ??? Deployment Strategy
Layih? h?m frontend, h?m d? backend hiss?l?rinin sür?tli v? stabil isl?m?sini t?min etm?k üçün **Vercel** platformasinda yerl?sdirilmisdir.

### Deployment Steps:
1. **Frontend**: mvp_code/frontend/index.html fayli Vercel-in "Zero Config" xüsusiyy?ti il? statik hostinq? çixarildi.
2. **Backend**: Python/Flask API-i Vercel Functions (Serverless) vasit?sil? pi/ marsrutu altinda is? salindi.
3. **Environment**: CORS (Cross-Origin Resource Sharing) siyas?ti frontend v? backend-in eyni domen altinda t?hlük?siz s?kild? ?laq? saxlamasi üçün konfiqurasiya edildi.

## ?? Configuration
- **Platform**: Vercel
- **Runtime**: Python 3.9 (Backend) / HTML5 (Frontend)
- **Region**: Washington, D.C. (us-east-1)
- **SSL**: Enabled (HTTPS)

## ? Verification
- [x] Live URL aktivdir v? yükl?nir.
- [x] Karbon hesablama API-i düzgün cavab qaytarir.
- [x] GitHub repozitoriyasi s?n?dl?sm? il? tam sinxronlasdirilib.
