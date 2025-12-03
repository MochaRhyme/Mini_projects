#!/bin/bash

# Gemini 2.5의 Pro모드와 Gemini 3 Pro로 생성한 GitHub 커밋 자동화 툴입니다.
# Windows에서는 Git Bash 셸로 실행 가능합니다.
# 1을 누르면 같은 디렉터리 내의 모든 git 저장소에 대해 pull,
# 2를 누르면 같은 디렉터리 내의 모든 git 저장소에 대해 push가 진행되며,
# .gitignore에 의해 걸러진 파일이 있다면 같은 폴더 내의 백업 git 저장소에 넣고 커밋푸시합니다.
# (백업 git 저장소 이름은 BACKUP_REPO_NAME의 값입니다. 수정 가능합니다.)
# 백업 git 저장소가 없어도 pull과 push는 가능합니다.

# 실행 전, 이 스크립트를 실행하는 폴더의 구성은 이런 식으로 하여 주십시오:
# git저장소a/
# git저장소b/
# git저장소c/
# ...

# =========================================================
# 설정 (Configuration) - 이 값을 마음대로 변경해주세요.
# =========================================================
COMMIT_MESSAGE="Automate commiting..."
BACKUP_REPO_NAME="ignored_files"
BACKUP_REPO_PATH="./$BACKUP_REPO_NAME"
LOG_FILE="log.txt"       # 최종 저장될 로그 파일
TEMP_LOG="temp_log.txt"  # 실행 중 임시로 저장할 파일

# =========================================================
# 기능 1: Pull All
# =========================================================
execute_pull() {
    echo ""
    echo ">>> Starting PULL Process..."
    echo ""

    # 1. ignored_files 저장소 우선 Pull
    if [ -d "$BACKUP_REPO_PATH/.git" ]; then
        echo "========================================="
        echo "⏫ Pulling Backup Repository: $BACKUP_REPO_NAME"
        echo "========================================="
        (
            cd "$BACKUP_REPO_PATH" || exit
            echo "🛬 Pulling backup..."
            git pull
        )
    else
        echo "🚨 Warning: '$BACKUP_REPO_NAME' repository not found or not a git repo. Skipping backup pull."
    fi

    # 2. 개별 저장소 순회
    for dir in */ ; do
        if [ "${dir%/}" == "$BACKUP_REPO_NAME" ]; then continue; fi

        if [ -d "${dir}.git" ]; then
            echo ""
            echo "========================================="
            echo "📁 Pulling repository: ${dir}"
            echo "========================================="
            DIR_NAME=${dir%/}
            (
                cd "${dir}" || exit
                echo "🛬 Pulling changes..."
                git pull
                
                SOURCE_DIR="../$BACKUP_REPO_NAME/$DIR_NAME"
                if [ -d "$SOURCE_DIR" ]; then
                    echo "--- Restoring ignored files from backup ---"
                    cp -r "$SOURCE_DIR/"* . 2>/dev/null
                    echo "✅ Restored files from $SOURCE_DIR"
                else
                    echo "🤷 No backup files found for this repository."
                fi
            )
        else
            echo "🐇 Skipping ${dir} (Not a git repository)"
        fi
    done
    echo ""
    echo "✅ All repositories processed (PULL complete)."
}

# =========================================================
# 기능 2: Push All
# =========================================================
execute_push() {
    echo ""
    echo ">>> Starting PUSH Process..."
    echo ""

    if [ ! -d "$BACKUP_REPO_PATH" ]; then
        echo "🚨 Warning: '$BACKUP_REPO_NAME' directory not found."
        echo "   Ignored files will NOT be backed up, but repository changes will still be pushed."
    fi

    for dir in */ ; do
        if [ "${dir%/}" == "$BACKUP_REPO_NAME" ]; then continue; fi

        if [ -d "${dir}.git" ]; then
            echo ""
            echo "========================================="
            echo "📁 Processing repository: ${dir}"
            echo "========================================="
            DIR_NAME=${dir%/}
            cd "${dir}" || continue
            
            # --- 1. 백업 처리 (백업 폴더가 존재할 때만 실행) ---
            if [ -d "../$BACKUP_REPO_NAME" ]; then
                DEST_DIR="../$BACKUP_REPO_NAME/$DIR_NAME"
                if [ -d "$DEST_DIR" ]; then
                    rm -rf "$DEST_DIR"
                fi
                mkdir -p "$DEST_DIR"

                IGNORED_FILES=$(git ls-files --others --ignored --exclude-standard)
                if [ -n "$IGNORED_FILES" ]; then
                    echo "--- Backing up ignored files ---"
                    echo "$IGNORED_FILES" | while read -r file; do
                        cp --parents "$file" "$DEST_DIR" 2>/dev/null || cp "$file" "$DEST_DIR"
                    done
                    echo "✅ Ignored files backup complete."
                else
                    echo "🤷 No ignored files found to backup."
                fi
            else
                echo "⚠️ Backup repo missing. Skipping file backup."
            fi

            # --- 2. Git 커밋 & 푸시 최적화 ---
            echo "--- Checking for changes ---"
            git add .
            
            if ! git diff --cached --quiet; then
                echo "📝 Changes detected. Committing..."
                git commit -m "$COMMIT_MESSAGE"
                
                echo "🛫 Pushing changes..."
                git push
            else
                echo "🐇 No changes detected. Skipping commit & push."
            fi
            
            cd ..
        else
            echo "🐇 Skipping ${dir} (Not a git repository)"
        fi
    done

    # --- 3. ignored_files 저장소 처리 (백업 폴더가 존재할 때만 실행) ---
    if [ -d "$BACKUP_REPO_PATH" ]; then
        echo ""
        echo "========================================="
        echo "⏫ Processing Backup Repository: $BACKUP_REPO_NAME"
        echo "========================================="
        cd "$BACKUP_REPO_PATH" || exit
        
        echo "--- Checking for changes (Backup Repo) ---"
        git add .
        
        if ! git diff --cached --quiet; then
            echo "📝 Changes detected in backup. Committing..."
            git commit -m "Backup ignored files: $COMMIT_MESSAGE"
            
            echo "🛫 Pushing backup..."
            git push
        else
            echo "🐇 No changes in backup. Skipping commit & push."
        fi

        cd ..
    else
        echo ""
        echo "⚠️ Skipping Backup Repository Push ('$BACKUP_REPO_NAME' not found)."
    fi

    echo ""
    echo "✅ All repositories and backup processed (PUSH complete)."
}

# =========================================================
# 로그 분석 및 처리 함수
# =========================================================
process_log() {
    if grep -iqE "error|fatal|conflict|failed|exception" "$TEMP_LOG"; then
        echo ""
        echo "⚠️ ERRORS DETECTED! Saving log to $LOG_FILE..."
        
        {
            echo "---------------------------------------------------"
            echo "[$TIMESTAMP] Error Log Detected"
            echo "---------------------------------------------------"
            cat "$TEMP_LOG"
            echo "" 
        } >> "$LOG_FILE"
        
        echo "✅ Log saved."
    else
        echo ""
        echo "✨ Operation Successful (No errors found). Log discarded."
    fi
    
    rm -f "$TEMP_LOG"
}

# =========================================================
# 메인 메뉴
# =========================================================
echo "========================================="
echo " Git Multi-Repo Automation Tool"
echo "========================================="
echo " 1️⃣ PULL ALL (Restore ignored files)"
echo " 2️⃣ PUSH ALL (Backup ignored files)"
echo "========================================="
read -n 1 -s -r -p "Select Mode (1 or 2): " selection

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# 임시 파일 초기화
: > "$TEMP_LOG"

case "$selection" in
    1)
        execute_pull 2>&1 | tee "$TEMP_LOG"
        process_log
        ;;
    2)
        execute_push 2>&1 | tee "$TEMP_LOG"
        process_log
        ;;
    *)
        echo ""
        echo "❌ Invalid selection. Exiting."
        rm -f "$TEMP_LOG"
        exit 1
        ;;
esac