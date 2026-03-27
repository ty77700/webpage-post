self.addEventListener('install', (e) => {
  console.log('서비스 워커 설치 완료');
});

self.addEventListener('fetch', (e) => {
  // 오프라인 지원을 위한 로직이 들어가는 곳 (현재는 패스)
});
