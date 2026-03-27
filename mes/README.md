# ⚡ 번개톡 (Lightning Talk)
> **GitHub Pages + Firebase + PWA** 기반의 초경량 실시간 메신저

이 프로젝트는 서버 구축 없이 **GitHub Actions**와 **Firebase**만으로 동작하는 실시간 웹 앱입니다. 2026년 환경에 맞춰 PWA 기술을 적용하여 모바일 앱처럼 설치 가능합니다.
<url>
https://ty77700.github.io/webpage-post/mes/

---

## 🚀 1. 빠른 시작 (Setup Guide)

### Step 1: Firebase 프로젝트 설정
1. [Firebase Console](https://console.firebase.google.com/) 접속 (구글 로그인)
2. **프로젝트 생성**: 이름 설정 후 생성 (익명성 유지를 위해 본명 제외 권장)
3. **웹 앱 등록**: `</>` 아이콘 클릭 -> 앱 등록 -> `firebaseConfig` 코드 복사
4. **Realtime Database 생성**: (중요!) 
   - [Build] -> [Realtime Database] -> [데이터베이스 만들기]
   - **보안 규칙**: 반드시 `Start in test mode` 선택 또는 규칙 탭에서 `.read: true`, `.write: true`로 수정 후 [게시]

### Step 2: 코드 적용
1. `index.html` 내의 `firebaseConfig` 부분에 본인의 키값을 붙여넣습니다.
2. 깃허브 레포지토리에 `index.html`, `manifest.json`, `sw.js`, `.github/workflows/deploy.yml`을 업로드합니다.

---

## 🛠 2. 겪었던 이슈 및 해결 (Troubleshooting Log)

나중에 다시 개발할 때 헤매지 않기 위해 정리한 실전 이슈들입니다.

### Q1. 데이터베이스를 만들었는데 왜 채팅이 안 가나요?
- **원인**: 단순히 Firebase 프로젝트만 만들고 **[Realtime Database]를 생성**하지 않았거나, **[Rules(규칙)]**에서 읽기/쓰기 허용(`true`)을 안 해줬기 때문입니다.
- **해결**: Database 메뉴에 들어가서 '데이터베이스 만들기'를 완료하고 규칙을 게시해야 통신이 시작됩니다.

### Q2. 2026년인데 메뉴 위치가 설명과 달라요.
- **해결**: Firebase 상단 **통합 검색창**을 활용하세요. `Project Settings`나 `Realtime Database`를 검색하면 메뉴 깊숙이 들어가지 않아도 바로 이동 가능합니다.

### Q3. 공개 레포지토리인데 내 개인정보(구글 아이디)가 노출되나요?
- **안심**: `firebaseConfig`에 포함된 키값들은 통로 번호일 뿐, **당신의 이메일이나 실명은 포함되지 않습니다.** 프로젝트 이름만 익명으로 지으면 완벽하게 숨겨집니다.

### Q4. 데이터 사용량이 많아져서 돈이 청구되면 어쩌죠?
- **해결**: Firebase 무료 요금제(Spark)는 카드 등록을 하지 않으면 결제가 불가능합니다. 사용량을 초과하면 자동으로 **서비스가 일시 중단**될 뿐, 요금이 청구되지 않으니 안심하고 테스트해도 됩니다.

---

## 📱 3. 모바일 앱 설치 방법
1. 모바일 크롬(Chrome) 브라우저로 접속
2. 우측 상단 **[점 3개 메뉴]** 클릭
3. **[앱 설치]** 또는 **[홈 화면에 추가]** 클릭
4. 바탕화면의 '번개톡' 아이콘을 누르면 주소창 없는 앱 모드로 실행됨

---

## ⚙️ 4. 동작 원리
- **Frontend**: GitHub Pages (자동 배포)
- **Database**: Firebase Realtime Database (JSON 형식 실시간 저장)
- **Deployment**: GitHub Actions (코드 Push 시 자동 반영)
- **App Feature**: PWA (Service Worker + Manifest)
