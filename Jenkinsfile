pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/vatsal-dhama/se_ass6.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x code.py"
                sh "python3 code.py"
            }
        }
    stage('Test Code') {
            steps {
                sh "chmod u+x tests.py"
                sh "./tests.py"
            }
        }
    } 
}
