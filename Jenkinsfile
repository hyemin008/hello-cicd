pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                git url: 'https://github.com/hyemin008/hello-cicd.git', branch: 'main'
            }
        }

        stage('Build Docker') {
            steps {
                sh "docker build --build-arg GIT_COMMIT=${env.GIT_COMMIT} -t hello-cicd:${env.GIT_COMMIT} ."
            }
        }

        stage('Run Docker') {
            steps {
                sh "docker run -d -p 5000:5000 hello-cicd:${env.GIT_COMMIT}"
            }
        }
    }
}
