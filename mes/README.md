# ⚡ 번개톡 (Lightning Talk)
> **GitHub Pages + Firebase + PWA** 기반의 초경량 실시간 알림 메신저

본 프로젝트는 복잡한 서버 구축 없이, URL 접속만으로 즉시 사용 가능한 **설치형 웹 앱(PWA)** 기반 메신저입니다.

## ✨ 핵심 기능
- **실시간 채팅:** Firebase Realtime Database를 이용한 지연 없는 메시지 전송.
- **PWA 지원:** 안드로이드/iOS에서 '홈 화면에 추가' 시 실제 앱처럼 동작 (주소창 제거).
- **푸시 알림:** 앱을 보고 있지 않아도 브라우저 알림 API를 통해 실시간 메시지 수신 알림.
- **카카오톡 스타일 UI:** 모바일 환경에 최적화된 직관적인 채팅 화면.
- **자동 배포:** GitHub Actions를 통해 코드 수정 시 자동으로 웹사이트 업데이트.

## 🛠 기술 스택
- **Frontend:** HTML5, Tailwind CSS, JavaScript (Vanilla JS)
- **Backend/DB:** Firebase Realtime Database
- **Hosting:** GitHub Pages
- **Automation:** GitHub Actions
- **App Feature:** Service Worker, Manifest.json (PWA)

## 📂 파일 구조
- `index.html`: 메인 UI 구조 및 앱 레이아웃
- `style.css`: 카카오톡 느낌의 사용자 정의 스타일
- `app.js`: Firebase 연결 및 채팅 비즈니스 로직
- `sw.js`: 백그라운드 알림 및 오프라인 캐싱 처리 (Service Worker)
- `manifest.json`: 앱 이름, 아이콘, 설치 환경 설정
- `.github/workflows/deploy.yml`: 자동 배포 스크립트

## 🚀 시작하기 (설치 및 실행)
1. 본 저장소를 `Fork` 또는 `Clone` 합니다.
2. `Firebase` 콘솔에서 프로젝트를 생성하고 발급받은 API 키를 `app.js`에 입력합니다.
3. GitHub 저장소의 `Settings > Pages`에서 배포 브랜치를 설정합니다.
4. 스마트폰 크롬 브라우저로 해당 URL에 접속한 뒤 **'홈 화면에 추가'**를 누릅니다.

## ⚠️ 주의사항
- 본 앱은 개인/연습용으로 설계되었습니다.
- 보안을 위해 추후 Firebase Security Rules 설정을 권장합니다.
- 데이터 사용량은 텍스트 위주이므로 매우 적습니다.
