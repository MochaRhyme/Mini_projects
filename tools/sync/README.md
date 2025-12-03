# sync_made_by_gemini_3_pro.sh
Gemini 2.5의 Pro모드와 Gemini 3 Pro로 생성한 GitHub 커밋 자동화 툴입니다.  
Windows에서는 Git Bash 셸로 실행 가능합니다.  
1을 누르면 같은 디렉터리 내의 모든 git 저장소에 대해 pull,  
2를 누르면 같은 디렉터리 내의 모든 git 저장소에 대해 push가 진행되며,  
.gitignore에 의해 걸러진 파일이 있다면 같은 폴더 내의 백업 git 저장소에 넣고 커밋푸시합니다.  
(백업 git 저장소 이름은 BACKUP_REPO_NAME의 값입니다. 수정 가능합니다.)  
백업 git 저장소가 없어도 pull과 push는 가능합니다.

실행 전, 이 스크립트를 실행하는 폴더의 구성은 이런 식으로 하여 주십시오:  
git저장소a/  
git저장소b/  
git저장소c/  
...