pipeline {
    agent any

    environment {
        IMAGE_NAME = "hello-cicd"
        IMAGE_TAG = "${GIT_COMMIT}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                pip install -r requirements.txt
                pytest
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f hello-cicd || true
                docker run -d -p 5000:5000 --name hello-cicd -e GIT_COMMIT=$IMAGE_TAG $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
    }
}
