pipeline {
    agent any

    options {
        // 防止構建卡死，超過10分鐘自動停止
        timeout(time: 10, unit: 'MINUTES')
        // 解決 Windows 控制台中文亂碼問題
        encoding('UTF-8')
    }

    stages {
        stage('拉取代碼') {
            steps {
                echo '正在從 GitHub 拉取最新代碼...'
                checkout scm
            }
        }

        stage('環境準備') {
            steps {
                echo '正在安裝依賴...'
                // 安裝 selenium 和 behave
                bat 'pip install -r requirements.txt'
            }
        }

        stage('執行 BDD 測試') {
            steps {
                echo '🚀 啟動自動化測試...'
                // chcp 65001 是為了解決 Windows 命令行顯示中文的問題
                // --no-capture 是為了讓 behave 的打印內容實時顯示在 Jenkins 裡
                bat 'chcp 65001 && behave --no-capture'
            }
        }
    }

    post {
        always {
            echo '測試結束！'
        }
        success {
            echo '🎉 恭喜！所有測試場景通過！'
        }
        failure {
            echo '😢 哎呀，測試失敗了，請檢查日誌。'
        }
    }
}
