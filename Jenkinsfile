pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                git url: 'https://github.com/너의-레포.git', branch: 'main'
            }
        }

        stage('Build Docker') {
            steps {
                script {
                    sh "docker build --build-arg GIT_COMMIT=${env.GIT_COMMIT} -t hello-cicd:${env.GIT_COMMIT} ."
                }
            }
        }

        stage('Run Docker') {
            steps {
                script {
                    sh "docker run -d -p 5000:5000 hello-cicd:${env.GIT_COMMIT}"
                }
            }
        }
    }
}
