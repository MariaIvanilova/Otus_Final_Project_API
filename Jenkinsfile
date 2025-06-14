pipeline {
    agent any

    parameters {
        string(name: 'THREADS', description: 'Number of parallel test threads')
    }

    environment {
        ALLURE_RESULTS = 'allure-results'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/master']],
                    extensions: [],
                    userRemoteConfigs: [[
                        url: 'https://github.com/MariaIvanilova/Otus_Final_Project_API.git'
                    ]]
                ])
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t tests_api .'
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                docker run --name testing \
                    -e THREADS=${params.THREADS} \
                    tests_api \
                    -n ${params.THREADS}
                """
            }
        }

        stage('Copy Results') {
            steps {
                sh """
                docker cp testing:/app/${ALLURE_RESULTS} .
                docker rm -f testing
                """
            }
        }
    }

    post {
        always {
            allure includeProperties: false,
                jdk: '',
                results: [[path: "${ALLURE_RESULTS}"]]
        }
    }
}