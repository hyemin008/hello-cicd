pipeline {
    agent any

    environment {
        IMAGE_NAME = "hello-cicd"
        GIT_COMMIT = ""  // 나중에 checkout 후 채움
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/hyemin008/hello-cicd.git'
                script {
                    // 현재 커밋 해시 가져오기
                    GIT_COMMIT = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                }
            }
        }

        stage('Build Docker') {
            steps {
                sh "docker build --build-arg GIT_COMMIT=${GIT_COMMIT} -t ${IMAGE_NAME}:${GIT_COMMIT} ."
            }
        }

        stage('Run Docker') {
            steps {
                sh """
                docker rm -f ${IMAGE_NAME} || true
                docker run -d -p 5000:5000 --name ${IMAGE_NAME} -e GIT_COMMIT=${GIT_COMMIT} ${IMAGE_NAME}:${GIT_COMMIT}
                """
            }
        }
    }
}
