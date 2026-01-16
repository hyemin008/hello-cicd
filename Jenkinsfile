pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/hyemin008/hello-cicd.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t hello-cicd .'
            }
        }

        stage('Run Docker') {
            steps {
                sh 'docker run -d -p 5000:5000 hello-cicd'
            }
        }
    }
}
