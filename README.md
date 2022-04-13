# 주식 예측 AI 모델 개발

주식 예측을 위해 주식 리포트를 크롤링 후 리포트 데이터로 주식 데이터 예측 모델 AI 개발 중..

주식 레포트가 PDF 형식이므로 PDF to Image를 통해 Image화
tssaract OCR을 이용하여 image의 text를 가지고오기
text data를 통해 주식 예측

위 플로우로 진행시 문제점
1. OCR을 통해 PDF를 읽을 시 단이 나눠져 있으면 정확한 Text를 못 가져옴(해결중..)
  > * OCR을 통해 글자의 bounding box를 생성하고 떨어진 거리를 통해 단을 나누는 방법 시도 중
